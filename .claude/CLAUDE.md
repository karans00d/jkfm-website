# JKFM Website

Static company website for JK Facilities Management.

- **Hosting:** Netlify (auto-deploy from GitHub karans00d/jkfm-website) — every push to `main` goes live; verify on a branch first
- **Domain:** jkfacilitiesmanagement.com.au (jkfm.co 301s to it during grace window)
- **Stack:** HTML, CSS, vanilla JS — no framework, no build step
- **Language:** Australian English, strata/FM terminology

## Structure

- `index.html` — homepage
- `services.html`, `cleaning.html`, `privacy.html` — content pages
- `blog/` — blog posts (static HTML)
- `style.css` — single stylesheet
- `script.js` — single script file
- `Images/` — site images (descriptive filenames)
- `docs/` — design/planning docs (not deployed)

## Rules

1. No frameworks, no bundlers, no npm
2. All pages share the same `style.css` and `script.js`
3. Test changes by opening the HTML file locally before pushing
4. Blog posts go in `blog/` as standalone HTML files
5. Check `docs/WEBSITE_REDESIGN_PLAN.md` before major changes

## Design: 01 Swiss Institutional (since 28/08/2026)

The whole site uses the swiss institutional skin (Gate 2 winner, matches the
capability statement). Spec: `docs/superpowers/specs/2026-08-28-swiss-restyle-design.md`.
Karan's ruling 28/08/2026 (evening): the register NUMBERING conceit is REMOVED — no
document/clause/plate/schedule numbers anywhere; small caps section labels, hairline
rules and the navy/paper palette stay. Header shows the monogram logo
(`Images/jkfm-monogram-nav.png`, transparent bg) + company name; footer is a compact
particulars block, logo on top. The old 9 phase plan (`docs/WEBSITE_REDESIGN_PLAN.md`)
is SUPERSEDED; leftovers live in `docs/FOLLOW-UPS.md`.

**Claims rule:** every factual statement must trace to
`~/Projects/company-resources/jkfm-profile.md`. One override: the flagship building is
described as 24 levels (B2, B1, ground plus 21 residential levels) — Karan's ruling
28/08/2026. Hard bans include testimonials, photo evidence claims (ceiling:
"photographed where an issue warrants it"), plural client framing, and "no lock in".
No hyphens or em dashes in visible copy (street ranges like 42-48 stay).

## Brand

- Colours: navy `#0f2440` (ink and surface), paper `#f4f1ea` (ground); tokens in style.css `:root`
- Type: Helvetica system stack — no Google Fonts, no webfont requests
- Lockup is typographic ("JKFM" + spaced small caps name); monogram PNG used for favicon/touch icon only
- Contact form target email: `enquiries@jkfacilitiesmanagement.com.au` (Netlify Forms, form name `contact`)

## Read on Entry

- `docs/superpowers/specs/2026-08-28-swiss-restyle-design.md` — design + claims spec, source of truth
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
