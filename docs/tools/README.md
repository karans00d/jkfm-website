# Site check scripts

Python only, no node tooling. Run from the repo root. Needs `pip install pillow playwright`;
the rendered checks use the sandbox Chromium at `/opt/pw-browsers` (edit `CHROMIUM` in
`render_check.py` to point elsewhere, or drop it to use Playwright's own browser).

| Script | What it checks |
|---|---|
| `a11y_audit.py` | Static: one h1, no skipped levels, img alt + real width/height, lazy loading, form labels, Netlify form attributes, link text, new tab links, skip link, FAQ aria, `lang="en-AU"`, focus/skip/reduced motion rules in style.css |
| `render_check.py` | Headless Chromium at 1440x900 and 390x844: first screen vs below fold per image, CLS, skip link, focus ring, FAQ toggle, reduced motion, console errors. `--shots DIR` saves full page PNGs; `--compare A B` pixel diffs two shot folders |
| `contrast.py` | WCAG AA ratios for the style.css tokens; `--rendered` sweeps every visible text node |
| `image_weight.py` | Byte size of every file in Images/ with its largest rendered width; `--resample` shrinks JPEG/PNG over 300 KB displayed below their pixel size (never logos) |

All exit non zero on failure except `image_weight.py`, which only reports.
