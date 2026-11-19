#!/usr/bin/env python3
"""WCAG 2.x contrast ratios for the JKFM palette.

Run from the repo root:
    python3 docs/tools/contrast.py              # token pairs from style.css :root
    python3 docs/tools/contrast.py --rendered   # also sweep every text node on
                                                # every page in headless Chromium

Reads the colour tokens straight from style.css so the numbers track the
stylesheet. Translucent colours are composited over the ground they sit on.
AA thresholds: 4.5:1 normal text, 3:1 large text (24px, or 18.66px bold)
and non text UI (form field borders, focus rings).
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def parse(c):
    c = c.strip()
    if c.startswith("#"):
        h = c[1:]
        if len(h) == 3:
            h = "".join(x * 2 for x in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (1.0,)
    m = re.match(r"rgba?\(([^)]*)\)", c)
    parts = [p.strip() for p in m.group(1).replace("/", ",").split(",")]
    r, g, b = (float(x) for x in parts[:3])
    a = float(parts[3]) if len(parts) > 3 else 1.0
    return (r, g, b, a)


def over(fg, bg):
    a = fg[3]
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1.0,)


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in c[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    bg = over(bg, (255, 255, 255, 1)) if bg[3] < 1 else bg
    fg = over(fg, bg) if fg[3] < 1 else fg
    a, b = sorted((lum(fg), lum(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def tokens():
    css = open(os.path.join(ROOT, "style.css"), encoding="utf-8").read()
    root = re.search(r":root\{(.*?)\}", css, re.S).group(1)
    t = {k: parse(v) for k, v in re.findall(r"--([\w-]+):\s*([^;]+);", root) if k != "font"}
    ph = re.search(r"\.form-input::placeholder\{color:([^}]+)\}", css)
    if ph:
        t["placeholder"] = parse(ph.group(1))
    return t


def token_report():
    t = tokens()
    paper, navy = t["paper"], t["navy"]
    tint_ground = over(t["tint"], paper)
    pairs = [
        # (label, fg, bg, threshold, where it is used)
        ("navy on paper", navy, paper, 4.5, "body text, headings, links"),
        ("paper on navy", paper, navy, 4.5, "on-navy sections, buttons, nav contact, skip link"),
        ("ink-soft on paper", t["ink-soft"], paper, 4.5, "labels, notes, captions, footer legal"),
        ("ink-soft on tint", t["ink-soft"], tint_ground, 4.5, "specimen table head cells"),
        ("navy on tint", navy, tint_ground, 4.5, "specimen table head strong text"),
        ("soft-on-navy on navy", t["soft-on-navy"], navy, 4.5, "secondary text in on-navy sections"),
        ("placeholder on paper", t["placeholder"], paper, 4.5, "contact form placeholder text"),
        ("hair-strong on paper (UI)", t["hair-strong"], paper, 3.0, "form field underline and textarea border"),
        ("hair on paper (UI, decorative)", t["hair"], paper, 3.0, "row rules, decorative only"),
        ("hair-on-navy on navy (UI, decorative)", t["hair-on-navy"], navy, 3.0, "row rules, decorative only"),
        ("focus ring navy on paper (UI)", navy, paper, 3.0, "3px focus outline"),
        ("focus ring paper on navy (UI)", paper, navy, 3.0, "3px focus outline in on-navy sections"),
    ]
    fails = 0
    print(f"{'pair':<40}{'ratio':>8}  {'need':>5}  result  used for")
    for label, fg, bg, need, use in pairs:
        r = ratio(fg, bg)
        ok = r >= need
        decorative = "decorative" in label
        fails += (not ok and not decorative)
        res = "PASS" if ok else ("n/a " if decorative else "FAIL")
        print(f"{label:<40}{r:>7.2f}:1 {need:>4}:1  {res}    {use}")
    return fails


RENDERED_JS = r"""() => {
  const out = [];
  const bgOf = el => {
    for (let e = el; e; e = e.parentElement) {
      const b = getComputedStyle(e).backgroundColor;
      if (b && b !== 'rgba(0, 0, 0, 0)' && b !== 'transparent') return b;
    }
    return getComputedStyle(document.body).backgroundColor;
  };
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walk.nextNode()) {
    const n = walk.currentNode, el = n.parentElement;
    if (!n.textContent.trim() || !el || seen.has(el)) continue;
    seen.add(el);
    const s = getComputedStyle(el), r = el.getBoundingClientRect();
    if (s.visibility === 'hidden' || s.display === 'none' || r.width === 0 || r.height === 0) continue;
    if (el.closest('.skip,.hidden-field,[hidden]')) continue;
    out.push({text: n.textContent.trim().slice(0, 40), fg: s.color, bg: bgOf(el),
              size: parseFloat(s.fontSize), weight: parseInt(s.fontWeight),
              cls: el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ').join('.') : '')});
  }
  return out;
}"""


def rendered_report():
    sys.path.insert(0, os.path.dirname(__file__))
    from render_check import PAGES, serve, CHROMIUM
    from playwright.sync_api import sync_playwright
    srv, base = serve()
    combos, fails = {}, 0
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
        for path in PAGES:
            pg = b.new_page(viewport={"width": 1440, "height": 900})
            pg.goto(f"{base}/{path}")
            for item in pg.evaluate(RENDERED_JS):
                fg, bg = parse(item["fg"]), parse(item["bg"])
                large = item["size"] >= 24 or (item["size"] >= 18.66 and item["weight"] >= 700)
                need = 3.0 if large else 4.5
                key = (item["fg"], item["bg"], need)
                c = combos.setdefault(key, {"ratio": ratio(fg, bg), "n": 0, "eg": item, "pages": set()})
                c["n"] += 1
                c["pages"].add(path)
            pg.close()
        b.close()
    srv.shutdown()
    print(f"\nRendered sweep: {sum(c['n'] for c in combos.values())} text elements, "
          f"{len(PAGES)} pages, {len(combos)} distinct colour/background/size combinations")
    for (fg, bg, need), c in sorted(combos.items(), key=lambda kv: kv[1]["ratio"]):
        ok = c["ratio"] >= need
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'} {c['ratio']:>5.2f}:1 (need {need}) x{c['n']:<4} "
              f"fg {fg} on {bg}  e.g. {c['eg']['cls'][:40]} \"{c['eg']['text']}\"")
    return fails


def main():
    fails = token_report()
    if "--rendered" in sys.argv:
        fails += rendered_report()
    print(f"\n{fails} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
