#!/usr/bin/env python3
"""Byte size report for Images/, with an optional Pillow resample.

Run from the repo root:
    python3 docs/tools/image_weight.py              # sizes + largest rendered width
    python3 docs/tools/image_weight.py --resample   # also resample candidates in place

A candidate is a JPEG or PNG over 300 KB that is displayed smaller than its
pixel width. It is resampled (same filename, same format) to twice the
largest CSS width any page renders it at, across 1440x900 and 390x844.
Logo and monogram files are never touched. Rendered widths are measured in
headless Chromium via render_check.py, so the site is served locally.
"""
import glob
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from render_check import CHROMIUM, PAGES, ROOT, VIEWPORTS, serve  # noqa: E402

LIMIT = 300 * 1024
PROTECTED = ("logo", "monogram", "initials", "apple-touch-icon", "og-share")


def rendered_widths():
    from playwright.sync_api import sync_playwright
    widest = {}
    srv, base = serve()
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
        for w, h in VIEWPORTS.values():
            for path in PAGES:
                pg = b.new_page(viewport={"width": w, "height": h})
                pg.goto(f"{base}/{path}")
                for src, cw in pg.evaluate("""() => [...document.images].map(i =>
                        [new URL(i.src).pathname, i.getBoundingClientRect().width])"""):
                    name = os.path.basename(src)
                    widest[name] = max(widest.get(name, 0), round(cw))
                pg.close()
        b.close()
    srv.shutdown()
    return widest


def main():
    resample = "--resample" in sys.argv
    widest = rendered_widths()
    print(f"{'file':<40}{'bytes':>9}{'KB':>8}  {'pixels':<11}{'fmt':<5}{'max css w':>10}  note")
    total = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "Images", "*"))):
        name = os.path.basename(f)
        size = os.path.getsize(f)
        total += size
        im = Image.open(f)
        cw = widest.get(name)
        note = ""
        protected = any(p in name.lower() for p in PROTECTED)
        if cw is None:
            note = "not rendered by any page (meta/icon/unused)"
        if size > LIMIT and im.format in ("JPEG", "PNG"):
            if protected:
                note += "; over 300 KB but a logo/monogram file: left alone"
            elif cw and cw * 2 < im.width:
                target = cw * 2
                note += f"; CANDIDATE: resample to {target}px wide"
                if resample:
                    h = round(im.height * target / im.width)
                    out = im.resize((target, h), Image.LANCZOS)
                    kw = {"quality": 82, "optimize": True, "progressive": True} if im.format == "JPEG" else {"optimize": True}
                    out.save(f, im.format, **kw)
                    note += f" -> {os.path.getsize(f)} bytes"
            else:
                note += "; over 300 KB but not displayed smaller than its pixels"
        print(f"{name:<40}{size:>9}{size / 1024:>8.1f}  {im.width}x{im.height:<6}{im.format:<5}"
              f"{cw if cw is not None else '-':>10}  {note.lstrip('; ')}")
    print(f"\nImages/ total: {total} bytes ({total / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
