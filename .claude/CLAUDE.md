# JKFM Website

Static company website for JK Facilities Management.

- **Hosting:** Netlify (auto-deploy from GitHub karans00d/jkfm-website)
- **Domain:** jkfm.co
- **Stack:** HTML, CSS, vanilla JS — no framework, no build step
- **Language:** Australian English, strata/FM terminology

## Structure

- `index.html` — homepage
- `services.html`, `cleaning.html`, `privacy.html` — content pages
- `blog/` — blog posts (static HTML)
- `style.css` — single stylesheet
- `script.js` — single script file
- `Images/` — site images
- `docs/` — design/planning docs (not deployed)

## Rules

1. Keep it simple — no frameworks, no bundlers, no npm
2. All pages share the same `style.css` and `script.js`
3. Test changes by opening the HTML file locally before pushing
4. Images go in `Images/` — use descriptive filenames
5. Blog posts go in `blog/` as standalone HTML files
6. A redesign plan exists at `docs/WEBSITE_REDESIGN_PLAN.md` — check it before major changes

---

## Active Initiative: 9-Phase Redesign

Plan at `docs/WEBSITE_REDESIGN_PLAN.md`. Phases: (1) design system, (2) SEO infra, (3) site architecture, (4) visual redesign, (5) contact form fix, (6) social media, (7) content/blog, (8) performance, (9) QA/launch.

**Highest-impact quick win: Phase 5 (contact form fix)** — current form is fake and losing leads.

Work in phases — get sign-off after Phase 1 before building.

## Brand

- Colours: Dark green `#1B4332`, mid green `#2D6A4F`, gold `#C9A84C`, blue `#1E6091`
- Fonts: Montserrat (headings), Open Sans (body)
- Logo assets: `Images/JKFM Monogram - Final.png`, `JKFM Logo with White BG.png`
- New brand assets: `C:\Users\kayso\Desktop\JKFM Brand\JKFM - New\` (logo needs SVG conversion)
- Work email for contact form: `karan@jkfm.co`

## Read on Entry

- `docs/WEBSITE_REDESIGN_PLAN.md` — 9-phase plan, source of truth
- Memory: `project_website_redesign.md`, `reference_jkfm_website.md`

## Relevant Skills

| Skill | When |
|-------|------|
| `browse` / `gstack` | Test site at desktop + mobile viewports before pushing |
| `qa` | Full QA pass before each Netlify deploy — catches broken links, console errors |
| `design-review` | Visual polish on rendered pages — finds AI-slop patterns, hierarchy issues |
| `plan-design-review` | Before implementing Phase 1/4 visual changes — review plan first |
| `benchmark` | Phase 8 (performance) — establish baselines, track Core Web Vitals |
| `canary` | Post-Netlify-deploy verification |
| `pdf` | If brochures/flyers ship alongside the website |

## Project-Specific Cautions

- **Static site, no build tools.** No npm, no bundlers, no React. Vanilla HTML/CSS/JS.
- **One stylesheet, one script** — shared across all pages.
- **Netlify auto-deploys from main** — every push to GitHub goes live. Verify on a branch first.
- **Australian English** in all user-facing copy. Strata/FM context.
- **SEO infra (Phase 2)** must include sitemap.xml, robots.txt, structured data — current site has none.
- **Footer links break on subpages** — known bug to fix in Phase 3.
