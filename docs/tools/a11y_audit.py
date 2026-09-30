#!/usr/bin/env python3
"""Static accessibility and image markup audit for the JKFM site.

Standard library only, apart from Pillow for reading image pixel sizes.
Run from the repo root:  python3 docs/tools/a11y_audit.py
Exits non zero if any check fails.

Checks, per deployed HTML page:
  1. exactly one h1, no skipped heading levels
  2. every img has alt; width and height present and equal to the file's pixels
  3. loading="lazy" on images below the first screen, not on first screen ones
     (the header logo is first screen; content images are classed by
     docs/tools/fold_check.py, whose results are pinned in FIRST_SCREEN below)
  4. every form control has a label or aria-label; Netlify form attributes intact
  5. every link has discernible text, no "click here"; target=_blank links
     announce the new tab
  6. skip link targets #main, FAQ buttons carry aria-expanded + aria-controls
     pointing at a real id
  8. html lang="en-AU"
"""
import glob
import os
import re
import sys
from html.parser import HTMLParser

from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PAGES = sorted(
    ["index.html", "about.html", "services.html", "cleaning.html",
     "oc-managers.html", "privacy.html", "404.html"]
    + [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "blog", "*.html"))]
)

# Images that are visible in the first screen at 1440x900 or 390x844 without
# scrolling (measured by fold_check.py). Everything else must be lazy.
FIRST_SCREEN = {
    "/Images/jkfm-logo-lockup.png#header",   # running head logo, every page
    "/Images/karan-sood.jpg#body",           # about: founder photo, first screen at 1440x900
    "/Images/cleaning-wiping-glass.jpg#body",  # cleaning: first plate, first screen on both
}

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.headings = []
        self.imgs = []
        self.controls = []
        self.label_for = set()
        self.label_depth = 0
        self.links = []
        self.link_stack = []
        self.forms = []
        self.buttons = []
        self.ids = set()
        self.stack = []
        self.in_header = 0
        self.in_hidden = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "header":
            self.in_header += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "img":
            a["_where"] = "header" if self.in_header else "body"
            self.imgs.append(a)
            for l in self.link_stack:
                l["text"] += " " + (a.get("alt") or "")
        if tag == "label":
            self.label_depth += 1
            if a.get("for"):
                self.label_for.add(a["for"])
        if tag in ("input", "textarea", "select"):
            if a.get("type") != "hidden":
                a["_tag"] = tag
                a["_wrapped"] = self.label_depth > 0
                self.controls.append(a)
        if tag == "form":
            self.forms.append(a)
        if tag == "button":
            self.buttons.append(a)
        if tag == "a":
            link = dict(a, text="")
            self.links.append(link)
            self.link_stack.append(link)

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
        if tag == "header":
            self.in_header -= 1
        if tag == "label":
            self.label_depth -= 1
        if tag == "a" and self.link_stack:
            self.link_stack.pop()

    def handle_data(self, data):
        for l in self.link_stack:
            l["text"] += data


def img_file(src, page):
    src = src.split("?")[0]
    if src.startswith("/"):
        return os.path.join(ROOT, src.lstrip("/"))
    return os.path.normpath(os.path.join(ROOT, os.path.dirname(page), src))


def audit(page):
    fails, notes = [], []
    p = Page()
    with open(os.path.join(ROOT, page), encoding="utf-8") as f:
        p.feed(f.read())

    # 8. lang
    if p.lang != "en-AU":
        fails.append(f'html lang is {p.lang!r}, expected "en-AU"')

    # 1. headings
    h1 = p.headings.count(1)
    if h1 != 1:
        fails.append(f"{h1} h1 elements")
    prev = 0
    for lvl in p.headings:
        if prev and lvl > prev + 1:
            fails.append(f"heading skips h{prev} -> h{lvl}")
        prev = lvl
    if p.headings and p.headings[0] != 1:
        fails.append(f"first heading is h{p.headings[0]}")
    notes.append("headings " + " ".join(f"h{l}" for l in p.headings))

    # 2 + 3. images
    for im in p.imgs:
        src = im.get("src", "")
        tag = f"img {src}"
        if "alt" not in im:
            fails.append(f"{tag}: no alt")
        path = img_file(src, page)
        if not os.path.exists(path):
            fails.append(f"{tag}: file missing")
            continue
        w, h = Image.open(path).size
        if im.get("width") != str(w) or im.get("height") != str(h):
            fails.append(f"{tag}: width/height {im.get('width')}x{im.get('height')}, file is {w}x{h}")
        key = f"/{os.path.relpath(path, ROOT)}#{im['_where']}"
        first = key in FIRST_SCREEN
        lazy = im.get("loading") == "lazy"
        if first and lazy:
            fails.append(f"{tag}: first screen image is lazy")
        if not first and not lazy:
            fails.append(f"{tag}: below the fold but not lazy")

    # 4. form controls
    for c in p.controls:
        ok = c["_wrapped"] or c.get("id") in p.label_for or c.get("aria-label") or c.get("aria-labelledby")
        if not ok:
            fails.append(f"{c['_tag']} name={c.get('name')}: no label")
    for fm in p.forms:
        if fm.get("name") == "contact":
            want = {"method": "POST", "data-netlify": "true", "netlify-honeypot": "bot-field"}
            for k, v in want.items():
                if fm.get(k) != v:
                    fails.append(f"contact form {k}={fm.get(k)!r}, expected {v!r}")
            notes.append("contact form Netlify attributes intact")

    # 5. links
    for l in p.links:
        text = " ".join((l["text"] + " " + (l.get("aria-label") or "")).split())
        if not text:
            fails.append(f"link {l.get('href')}: no discernible text")
        if re.search(r"\b(click here|here|read more|more)\b\W*$", l["text"].strip(), re.I) and not l.get("aria-label"):
            fails.append(f"link {l.get('href')}: vague text {l['text'].strip()!r}")
        if l.get("target") == "_blank" and "new tab" not in text.lower():
            fails.append(f"link {l.get('href')}: opens a new tab without saying so")

    # 6. skip link + FAQ
    if not any(l.get("class") == "skip" and l.get("href") == "#main" for l in p.links):
        fails.append("no skip link to #main")
    if "main" not in p.ids:
        fails.append("no element with id=main")
    for b in p.buttons:
        if "faq-q" in (b.get("class") or ""):
            if "aria-expanded" not in b or b.get("aria-controls") not in p.ids:
                fails.append(f"FAQ button aria-controls={b.get('aria-controls')!r} broken")
    faq = sum("faq-q" in (b.get("class") or "") for b in p.buttons)
    if faq:
        notes.append(f"{faq} FAQ buttons wired")
    return fails, notes


def css_checks():
    fails = []
    with open(os.path.join(ROOT, "style.css"), encoding="utf-8") as f:
        css = f.read()
    for needle in (".skip:focus", ":focus-visible", "prefers-reduced-motion: reduce"):
        if needle not in css:
            fails.append(f"style.css missing {needle}")
    return fails


def main():
    total = 0
    for page in PAGES:
        fails, notes = audit(page)
        total += len(fails)
        print(f"{'FAIL' if fails else 'PASS'}  {page}  ({'; '.join(notes)})")
        for f in fails:
            print(f"      - {f}")
    cf = css_checks()
    total += len(cf)
    print(f"{'FAIL' if cf else 'PASS'}  style.css skip/focus/reduced motion rules present")
    for f in cf:
        print(f"      - {f}")
    print(f"\n{total} failure(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
