#!/usr/bin/env python3
"""Link checker for the JKFM static site.

Checks every href, src and srcset on every deployed page (root *.html and
blog/*.html). Each internal reference must resolve to a file in the repo or
to a route in _redirects; a #fragment must match an id on the target page.
404.html is also resolved as if served from a nested missing path, because
Netlify serves it for any unknown URL and relative links there would break.

Usage (from the repo root, standard library only):
    python3 docs/tools/check_links.py              # internal links
    python3 docs/tools/check_links.py --external   # also request every external URL

Exit status is 1 if any internal link is broken, 0 otherwise. External
failures are reported but do not change the exit status.
"""

import argparse
import posixpath
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE_HOSTS = {"jkfacilitiesmanagement.com.au", "www.jkfacilitiesmanagement.com.au"}
SKIP_SCHEMES = {"mailto", "tel", "javascript", "data"}
NESTED_404_PATH = "/no/such/deep/page.html"


class RefParser(HTMLParser):
    """Collects (line, attribute, value) for every link bearing attribute, plus ids."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []
        self.ids = set()
        self.meta_urls = []

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key) is not None:
                self.refs.append((line, key, a[key].strip()))
        if a.get("srcset"):
            for part in a["srcset"].split(","):
                url = part.strip().split(" ")[0]
                if url:
                    self.refs.append((line, "srcset", url))
        # og:url, og:image, twitter:image carry absolute URLs
        content = (a.get("content") or "").strip()
        if tag == "meta" and re.match(r"https?://", content):
            self.refs.append((line, "content", content))
        self._in_jsonld = tag == "script" and a.get("type") == "application/ld+json"

    def handle_data(self, data):
        # URLs inside JSON-LD structured data
        if getattr(self, "_in_jsonld", False):
            start = self.getpos()[0]
            for m in re.finditer(r'"(https?://[^"\s]+)"', data):
                self.refs.append((start + data.count("\n", 0, m.start()), "json-ld", m.group(1)))

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_jsonld = False

    handle_startendtag = handle_starttag


def site_pages():
    pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "blog").glob("*.html"))
    return [p for p in pages if p.is_file()]


def served_path(page):
    rel = page.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def load_redirects():
    """Return (from_pattern, to) pairs for path rules in _redirects."""
    rules = []
    f = ROOT / "_redirects"
    if not f.exists():
        return rules
    for raw in f.read_text().splitlines():
        line = raw.split("#", 1)[0].strip() if raw.lstrip().startswith("#") else raw.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            rules.append((parts[0], parts[1]))
    return rules


def match_redirect(path, rules):
    for src, dst in rules:
        if "://" in src:
            continue  # host rules only apply to the old or www host
        pattern = "^" + re.escape(src).replace(r"\*", "(.*)") + "$"
        m = re.match(pattern, path)
        if m:
            splat = m.group(1) if m.groups() else ""
            return dst.replace(":splat", splat)
    return None


def file_for(path):
    rel = unquote(path).lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    target = ROOT / rel
    return target if target.is_file() else None


_ids_cache = {}


def ids_of(target):
    if target not in _ids_cache:
        p = RefParser()
        p.feed(target.read_text(encoding="utf-8", errors="replace"))
        _ids_cache[target] = p.ids
    return _ids_cache[target]


def resolve(path, rules, depth=0):
    """Return (file or None, note)."""
    target = file_for(path)
    if target:
        return target, ""
    dst = match_redirect(path, rules)
    if dst and depth < 5:
        parts = urlsplit(dst)
        if parts.netloc and parts.netloc not in SITE_HOSTS:
            return None, "redirects off site to " + dst
        t, note = resolve(parts.path or "/", rules, depth + 1)
        return t, "via _redirects to " + dst + (("; " + note) if note else "")
    return None, ""


def check_ref(value, base_path, rules, page):
    """Return (kind, error) where kind is internal/external/skip."""
    if value == "":
        return "internal", "empty URL"
    parts = urlsplit(value)
    if parts.scheme in SKIP_SCHEMES:
        return "skip", None
    if parts.scheme in ("http", "https") or value.startswith("//"):
        if parts.netloc not in SITE_HOSTS:
            return "external", None
        path = parts.path or "/"
    else:
        path = parts.path
        if path == "":
            # fragment or query only: same document wherever it is served
            frag = unquote(parts.fragment)
            if frag and frag not in ids_of(page):
                return "internal", "no id '%s' on this page" % frag
            return "internal", None
        if not path.startswith("/"):
            path = posixpath.normpath(posixpath.join(posixpath.dirname(base_path), path)) + (
                "/" if path.endswith("/") else ""
            )
            if path.startswith("//"):
                path = path[1:]
    target, note = resolve(path, rules)
    if target is None:
        return "internal", "no file or _redirects route for " + path + ((" (" + note + ")") if note else "")
    frag = unquote(parts.fragment)
    if frag and target.suffix == ".html" and frag not in ids_of(target):
        return "internal", "no id '%s' in %s" % (frag, target.relative_to(ROOT).as_posix())
    return "internal", None


def request_status(url, timeout=20):
    headers = {"User-Agent": "Mozilla/5.0 (JKFM link check)"}
    last = None
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return method, r.status, r.geturl()
        except urllib.error.HTTPError as e:
            last = (method, e.code, url)
            if method == "HEAD" and e.code in (403, 405, 429, 400, 404, 501, 999):
                continue  # some servers refuse HEAD; retry with GET
            return last
        except Exception as e:  # network, TLS, timeout
            last = (method, "ERR " + e.__class__.__name__ + ": " + str(e)[:80], url)
    return last


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--external", action="store_true", help="request every external URL and print its status")
    args = ap.parse_args()

    rules = load_redirects()
    broken = []
    external = {}
    checked = 0
    for page in site_pages():
        p = RefParser()
        p.feed(page.read_text(encoding="utf-8", errors="replace"))
        rel = page.relative_to(ROOT).as_posix()
        bases = [served_path(page)]
        if rel == "404.html":
            bases.append(NESTED_404_PATH)
        for line, attr, value in p.refs:
            relative = not (value.startswith(("/", "#", "?")) or urlsplit(value).scheme)
            for base in bases if relative else bases[:1]:
                kind, err = check_ref(value, base, rules, page)
                if kind == "external":
                    external.setdefault(value, set()).add(rel)
                    break
                if kind == "skip":
                    break
                if base == bases[0]:
                    checked += 1
                if err:
                    where = "" if base == bases[0] else " [when served at %s]" % base
                    broken.append("%s:%d %s=%r -> %s%s" % (rel, line, attr, value, err, where))

    print("Pages scanned: %d" % len(site_pages()))
    print("Internal references checked: %d" % checked)
    print("Broken internal references: %d" % len(broken))
    for b in broken:
        print("  BROKEN " + b)

    print("External URLs: %d" % len(external))
    for url in sorted(external):
        pages = ", ".join(sorted(external[url]))
        if args.external:
            method, status, final = request_status(url)
            moved = "" if final == url else " -> " + final
            print("  %s %s %s%s  [%s]" % (status, method, url, moved, pages))
        else:
            print("  %s  [%s]" % (url, pages))

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
