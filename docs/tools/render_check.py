#!/usr/bin/env python3
"""Rendered checks for the JKFM site in headless Chromium (Python Playwright).

Run from the repo root:
    python3 docs/tools/render_check.py                 # fold + behaviour report
    python3 docs/tools/render_check.py --shots DIR     # also save full page PNGs
    python3 docs/tools/render_check.py --compare A B   # pixel diff two shot dirs

Needs `pip install playwright pillow`; uses the sandbox Chromium at
/opt/pw-browsers (no browser download, no node tooling in the repo).

For each page at 1440x900 and 390x844 it reports:
  - every img: top edge in the first screen or not, rendered CSS width,
    loading attribute, and the pixel width needed at 2x
  - layout shift: CLS measured while the page loads
  - skip link: off screen until focused, visible on focus, lands on #main
  - focus ring: computed outline on a focused nav link
  - FAQ (services): buttons collapse on load, toggle aria-expanded and hidden
  - reduced motion: transitions are 0s under prefers-reduced-motion: reduce
  - console errors
"""
import argparse
import functools
import glob
import http.server
import os
import sys
import threading

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PAGES = ["index.html", "about.html", "services.html", "cleaning.html",
         "oc-managers.html", "privacy.html", "404.html"] + sorted(
    os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "blog", "*.html")))
VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

FOLD = {}  # (page, src, where) -> [loading attr, first screen at any viewport]

CLS_INIT = """
window.__cls = 0;
new PerformanceObserver(l => { for (const e of l.getEntries())
  if (!e.hadRecentInput) window.__cls += e.value; })
  .observe({type: 'layout-shift', buffered: true});
"""


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=ROOT)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def scroll_all(page):
    # instant scrolling so screenshots are not taken mid smooth scroll
    page.evaluate("document.documentElement.style.scrollBehavior = 'auto'")
    page.evaluate("""async () => {
      for (let y = 0; y < document.body.scrollHeight; y += 400) {
        window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); }
    }""")
    try:
        page.wait_for_function("[...document.images].every(i => i.complete && i.naturalWidth)",
                               timeout=8000)
    except Exception:
        print("    (timed out waiting for images)")
    page.evaluate("window.scrollTo(0, 0)")


def check_page(ctx, base, path, vp, shots, fails):
    page = ctx.new_page()
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: m.type == "error" and errors.append(m.text))
    page.add_init_script(CLS_INIT)
    url = f"{base}/{path}"
    page.goto(url, wait_until="load")
    # images as laid out on first paint, before any scrolling
    imgs = page.evaluate("""() => [...document.images].map(i => {
      const r = i.getBoundingClientRect();
      return {src: i.getAttribute('src'), top: Math.round(r.top + scrollY),
              w: Math.round(r.width), first: r.top < innerHeight && r.bottom > 0,
              loading: i.getAttribute('loading') || '', nat: i.naturalWidth,
              where: i.closest('header') ? 'header' : i.closest('footer') ? 'footer' : 'body'};
    })""")
    scroll_all(page)
    page.wait_for_timeout(200)
    cls = page.evaluate("window.__cls")
    if shots:
        page.wait_for_timeout(300)
        out = os.path.join(shots, f"{path.replace('/', '__')}.{vp}.png")
        page.screenshot(path=out, full_page=True, animations="disabled")
    for im in imgs:
        # an image counts as first screen if it is visible without scrolling
        # at ANY viewport; lazy is judged across viewports in main()
        FOLD.setdefault((path, im["src"], im["where"]), [im["loading"], False])[1] |= im["first"]
        print(f"    img {im['src']:<40} {im['where']:<6} {'FIRST' if im['first'] else 'below'}"
              f" top={im['top']:>5} css_w={im['w']:>4} 2x={im['w']*2:>4} file_w={im['nat']:>4}"
              f" loading={im['loading'] or '-'}")
    print(f"    CLS {cls:.4f}")
    if cls > 0.001:
        fails.append(f"{path} {vp}: CLS {cls:.4f}")

    # skip link
    page.evaluate("window.scrollTo(0,0)")
    before = page.eval_on_selector(".skip", "e => e.getBoundingClientRect().right")
    page.keyboard.press("Tab")
    focused = page.evaluate("document.activeElement.className")
    after = page.eval_on_selector(".skip", "e => e.getBoundingClientRect().left")
    page.keyboard.press("Enter")
    page.wait_for_timeout(50)
    hash_ = page.evaluate("location.hash")
    ok = before <= 0 and focused == "skip" and after >= 0 and hash_ == "#main"
    print(f"    skip link {'ok' if ok else 'BROKEN'} (hidden right={before:.0f}, focused left={after:.0f}, hash={hash_})")
    if not ok:
        fails.append(f"{path} {vp}: skip link")

    # focus ring on first nav link
    page.focus(".site-nav a")
    page.keyboard.press("Shift+Tab")
    page.keyboard.press("Tab")
    outline = page.evaluate("""() => { const s = getComputedStyle(document.activeElement);
      return s.outlineStyle + ' ' + s.outlineWidth; }""")
    print(f"    focus ring on nav link: {outline}")
    if not outline.startswith("solid 3px"):
        fails.append(f"{path} {vp}: focus ring {outline}")

    # FAQ
    n = page.locator(".faq-q").count()
    if n:
        b = page.locator(".faq-q").first
        tid = b.get_attribute("aria-controls")
        start = (b.get_attribute("aria-expanded"), page.eval_on_selector(f"#{tid}", "e => e.hidden"))
        b.click()
        opened = (b.get_attribute("aria-expanded"), page.eval_on_selector(f"#{tid}", "e => e.hidden"))
        b.click()
        closed = (b.get_attribute("aria-expanded"), page.eval_on_selector(f"#{tid}", "e => e.hidden"))
        ok = start == ("false", True) and opened == ("true", False) and closed == ("false", True)
        print(f"    FAQ x{n} {'ok' if ok else 'BROKEN'}: load {start} click {opened} click {closed}")
        if not ok:
            fails.append(f"{path} {vp}: FAQ toggle")

    if errors:
        fails.append(f"{path} {vp}: console errors {errors}")
    print(f"    console errors: {len(errors)}")

    page.close()


def reduced_motion(browser, base, fails):
    ctx = browser.new_context(reduced_motion="reduce")
    page = ctx.new_page()
    page.goto(f"{base}/index.html")
    t = page.eval_on_selector(".btn", "e => getComputedStyle(e).transitionDuration")
    sb = page.evaluate("getComputedStyle(document.documentElement).scrollBehavior")
    ok = t == "0s" and sb == "auto"
    print(f"reduced motion: .btn transition={t}, scroll-behavior={sb} -> {'ok' if ok else 'BROKEN'}")
    if not ok:
        fails.append("reduced motion rule")
    ctx.close()


def compare(a, b):
    from PIL import Image, ImageChops
    bad = 0
    for fa in sorted(glob.glob(os.path.join(a, "*.png"))):
        fb = os.path.join(b, os.path.basename(fa))
        ia, ib = Image.open(fa).convert("RGB"), Image.open(fb).convert("RGB")
        if ia.size != ib.size:
            print(f"DIFF  {os.path.basename(fa)}  size {ia.size} vs {ib.size}")
            bad += 1
            continue
        box = ImageChops.difference(ia, ib).getbbox()
        print(f"{'DIFF' if box else 'SAME'}  {os.path.basename(fa)}  {ia.size}{'  bbox ' + str(box) if box else ''}")
        bad += bool(box)
    print(f"\n{bad} page(s) differ")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots")
    ap.add_argument("--compare", nargs=2)
    args = ap.parse_args()
    if args.compare:
        return compare(*args.compare)
    from playwright.sync_api import sync_playwright
    if args.shots:
        os.makedirs(args.shots, exist_ok=True)
    srv, base = serve()
    fails = []
    with sync_playwright() as pw:
        exe = CHROMIUM if os.path.exists(CHROMIUM) else None
        browser = pw.chromium.launch(executable_path=exe)
        for vp, (w, h) in VIEWPORTS.items():
            ctx = browser.new_context(viewport={"width": w, "height": h})
            for path in PAGES:
                print(f"{path} @ {vp} {w}x{h}")
                check_page(ctx, base, path, vp, args.shots, fails)
            ctx.close()
        reduced_motion(browser, base, fails)
        print("\nlazy loading, judged across both viewports:")
        for (path, src, where), (loading, first) in FOLD.items():
            lazy = loading == "lazy"
            ok = lazy != first
            if not ok:
                fails.append(f"{path}: {src} ({where}) is {'first screen but lazy' if first else 'below the fold on every viewport but not lazy'}")
            if where != "header":
                print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {src:<36} {where:<6} "
                      f"{'first screen' if first else 'below fold'}, loading={loading or '-'}")
        browser.close()
    srv.shutdown()
    print(f"\n{len(fails)} failure(s)")
    for f in fails:
        print("  - " + f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
