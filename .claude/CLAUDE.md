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
