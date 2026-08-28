# Swiss Institutional Restyle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle all pages of jkfm-website to the 01 swiss institutional skin, claims-swept against jkfm-profile.md, keeping the Netlify form and SEO infrastructure.

**Architecture:** Port the shared stylesheet/script and five page shells from `~/Projects/company-resources/campaigns/oc-outreach-2026/full-sites/01-swiss-institutional/` (SRC below), merge each repo page's head metadata and working form into the ported shell, rewrite copy per the claims table in the design spec, and newly apply the skin to blog (7 files) and 404. All work on branch `swiss-restyle`; main never touched until Karan approves the preview.

**Tech Stack:** Vanilla HTML/CSS/JS. No frameworks, no build step. One shared style.css, one shared script.js.

## Global Constraints

- Claims: every factual statement traces to `~/Projects/company-resources/jkfm-profile.md`; 24 level override applies: "24 levels (B2, B1, ground plus 21 residential levels)".
- Banned phrases (grep must return nothing when done, all pages + meta + JSON-LD): `photo evidence`, `photo-evidence`, `photos`, `testimonial`, `every building we manage`, `our buildings`, `no obligations`, `no lock`, `21 residential storeys`, `13 level`.
  Exception: "photographed where an issue warrants it" is the ONLY permitted photo wording.
- No hyphens or em dashes in visible copy (`4 step`, `day to day`, `high use`, `built in`, `sign off`); numeric street ranges (42-48) stay; HTML attributes/CSS unaffected.
- Australian English. Dates DD/MM/YYYY.
- Keep per page: canonical, og/twitter tags, JSON-LD (descriptions updated where copy changes), URLs unchanged.
- SRC = `/Users/karans00d/Projects/company-resources/campaigns/oc-outreach-2026/full-sites/01-swiss-institutional`
- Commit after each task. Codex gate reviews commits automatically.

---

### Task 1: Shared stylesheet and script

**Files:**
- Modify: `style.css` (replace with SRC/style.css + blog/404 additions)
- Modify: `script.js` (FAQ toggles from SRC + Netlify form handler from current repo script.js)

**Interfaces:**
- Produces: CSS classes used by all later tasks (`.site-head`, `.section-grid`, `.clauses`, `.row`, `.num`, `.minute`, `.exhibit`, `.faq-*`, `.enquiry`, `.form-*`, `.parts`, `.doc-end`, plus new `.article`, `.article-meta`, `.post-list` for blog).
- Consumes: nothing.

- [ ] **Step 1:** Read current repo `script.js` (identify the Netlify form success/error handling) and SRC/style.css + SRC/script.js in full.
- [ ] **Step 2:** Overwrite repo `style.css` with SRC/style.css, then append a `/* ---------- blog articles ---------- */` block: `.post-list` (numbered list of posts styled like `.clauses` rows with title, date, teaser), `.article` (single column, max width 46rem, clause-numbered h2s via existing `.num` spans), `.article-meta` (date + reading line in `--ink-soft`), `.breadcrumb` (small top link "Register / Document 05 / …"). Reuse existing custom properties only; no new colours.
- [ ] **Step 3:** Rewrite repo `script.js`: keep SRC FAQ toggle block verbatim; replace SRC mailto fallback with the repo's existing Netlify form submit handling (form posts normally; JS only does client validation + status text if that is what the current repo script does — mirror current behaviour exactly).
- [ ] **Step 4:** Verify: `grep -c "data-netlify" script.js` returns 0 (handler keys off form id/class, not attributes); `grep -n "mailto" script.js` returns nothing.
- [ ] **Step 5:** Commit: `git add style.css script.js && git commit -m "Port swiss institutional stylesheet and shared script"`

### Task 2: Homepage (Document 01)

**Files:**
- Modify: `index.html` (SRC/index.html shell + repo head block + rewritten sections)

**Interfaces:**
- Consumes: Task 1 classes.
- Produces: nav markup (7 links: 01 Home, 02 Building management, 03 Cleaning, 04 About, 05 Blog, Get a quote button; head-doc line `Register · Document NN · <Page>`) and Schedule A footer markup — copied verbatim into every other page, with `blog/` pages prefixing `../` on links.

- [ ] **Step 1:** Start from SRC/index.html. Replace its `<head>` with the repo index.html head (title, description, canonical, og/twitter, JSON-LD, favicon links, font preconnects removed if fonts unused — swiss skin uses system Helvetica, so drop Google Fonts links). Keep `<link rel="stylesheet" href="style.css">`.
- [ ] **Step 2:** Cover facts strip becomes: `4 step management lifecycle` / `Founder led and directly accountable` / `24/7 emergency response` / `Melbourne based and operated`.
- [ ] **Step 3:** Replace section 06 "On the record" (testimonials) with **06 Track record**, heading "One building, held to the standard.", clauses:
  - 06.1 The flagship — "JKFM holds both the building management and cleaning contracts at 42-48 Claremont Street, South Yarra: a 24 level residential tower (B2, B1, ground plus 21 residential levels) with 111 apartments."
  - 06.2 Contractor coordination — "25+ specialist contractors coordinated at this single building, across fire systems, lifts, car stackers, electrical, plumbing, waterproofing, waste, pest control, doors, access control, security and glazing."
  - 06.3 Everything on the record — "Every open item is tracked on a live works register, more than 1,000 entries to date, and reported to the committee in writing at every committee meeting."
  - 06.4 One accountable party — "The building manager and the cleaning provider are the same accountable party."
  - Close with **Worked example** (`.minute` styling, ref "Extract 06-A"): "Six months after a routine service passed the system, the fire pump accumulator at our flagship building read zero pressure. The first quote was a one line replacement. JKFM asked what the service had tested, why a pass preceded failure, whether a recharge was an option and what pressure rating the system needs. That questioning produced a properly specified replacement at close to half the quoted cost."
- [ ] **Step 4:** Claims sweep of remaining sections: cleaning clauses 03.2/04.3 and FAQ 08.4 lose photo evidence → "documented per shift checklists and unannounced quality audits"; onboarding outro `"No obligations beyond the agreed engagement."` → `"Every JKFM building management agreement starts with a six month trial period."`; contact lede "free assessment" → "a free building health check: a no obligation walkthrough of your building's common areas by the director, with a short written summary of findings for your committee."; FAQ 08.5 same substitution. Sweep 01.2 intro "every building we manage" → "JKFM brings structure and accountability to the buildings in its care" is NOT allowed either (plural) → use "JKFM brings structure and accountability through written records and direct oversight."
- [ ] **Step 5:** Replace SRC form block with repo's Netlify form fields inside the swiss `.form-ex` wrapper, caption `Form 09-A Enquiry.` Keep `method="POST" data-netlify="true" netlify-honeypot="bot-field" name="contact"`. Remove the "no form backend" note.
- [ ] **Step 6:** Hyphen sweep + JSON-LD FAQ text updated to match visible FAQ answers.
- [ ] **Step 7:** Verify: `grep -inE "photo|testimonial|every building we|no obligation|free assessment|4-step|day-to-day" index.html` → only permitted matches (none expected).
- [ ] **Step 8:** Commit: `git commit -am "Restyle homepage as Document 01 with track record and case note"`

### Task 3: Services page (Document 02)

**Files:** Modify: `services.html` (SRC/services.html shell + repo head)

- [ ] **Step 1:** Port SRC/services.html; swap in repo head block (canonical etc.); insert Task 2 nav/footer with `aria-current` on 02.
- [ ] **Step 2:** Sweep: "every building we manage" → "each building under JKFM management is run to the same written standard" — NOT allowed (plural implication) → use "the same written standard applies wherever JKFM is engaged"; "document outcomes with photo evidence" → "verify completion and document outcomes in writing, photographed where an issue warrants it". Add trial clause using approved wording; add PPSA clause verbatim: "JKFM does not take security interests over owners corporation assets or funds. Some service contracts in the market include PPSR registration rights, break fees and penalty interest; committees should check theirs." Add insurance line: "Public liability insurance of $20 million. Certificate available on request." Hyphen sweep.
- [ ] **Step 3:** Verify grep (Task 2 Step 7 pattern) + commit: `git commit -am "Restyle services page as Document 02"`

### Task 4: Cleaning page (Document 03)

**Files:** Modify: `cleaning.html`

- [ ] **Step 1:** Port SRC/cleaning.html; repo head; nav/footer, `aria-current` on 03.
- [ ] **Step 2:** Heaviest sweep — accountability model rewritten to: documented per shift checklists (the day's actual scheduled tasks ticked on a documented checklist), unannounced quality audits, site specific teams rather than roving crews, committee facing dashboard showing contractor in and out times (SiteCheck), issues photographed where an issue warrants it. Remove ALL "before and after photos" / "photo evidence" / "visual proof" clauses including meta description, og/twitter descriptions and JSON-LD service description — rewrite those to "documented checklists, unannounced quality audits and full accountability". Add: cleaners hold current police checks and complete site specific safety induction.
- [ ] **Step 3:** Verify: `grep -icE "photo" cleaning.html` → only "photographed where an issue warrants it" matches (≤2). Commit: `git commit -am "Restyle cleaning page as Document 03 with corrected accountability claims"`

### Task 5: About page (Document 04)

**Files:** Modify: `about.html`

- [ ] **Step 1:** Port SRC/about.html; repo head; nav/footer, `aria-current` on 04.
- [ ] **Step 2:** Sweep: "every building we manage" (2×) → flagship/singular framing; "photo evidence as standard" → "written records as standard"; founder block limited to profile s6 (director, hands on manager of the flagship, prior career across property and facilities management in Melbourne; founded 2023 exact wording; NO solar background, NO ABMA, NO chairmanship). Add founder led differentiator: "issues escalate directly to the director, not through layers of area managers" (exact wording). Hyphen sweep.
- [ ] **Step 3:** Verify grep + commit: `git commit -am "Restyle about page as Document 04"`

### Task 6: Privacy page (Document 06) and 404

**Files:** Modify: `privacy.html`, `404.html`

- [ ] **Step 1:** Port SRC/privacy.html; repo head; nav/footer (no aria-current). Verify its policy copy matches repo privacy.html substance (form data → Netlify → enquiries mailbox); keep repo wording where they differ on facts.
- [ ] **Step 2:** Rebuild `404.html` in the skin: head-doc line `Register · Unfiled`, h1 "Document not found.", body "The page you requested is not in the register. It may have been moved or renumbered.", links to Documents 01–06, standard nav/footer.
- [ ] **Step 3:** Verify links resolve to real files; commit: `git commit -am "Restyle privacy page and 404 in swiss register skin"`

### Task 7: Blog (Document 05)

**Files:** Modify: `blog/index.html` + 6 post files

**Interfaces:** Consumes Task 1 `.post-list`/`.article`/`.breadcrumb` classes and Task 2 nav/footer (links prefixed `../`, stylesheet `../style.css`, script `../script.js`).

- [ ] **Step 1:** Rebuild `blog/index.html`: head from current repo file (canonical `/blog/`), swiss shell, head-doc `Register · Document 05 · Blog`, posts as a `.post-list` numbered 05.1–05.6 with existing titles, dates and teasers (teasers from current repo blog index, claims-swept — repo blog was already swept in earlier commits, but re-grep anyway).
- [ ] **Step 2:** For each of the 6 posts: keep `<head>` + article text from the repo file; wrap in swiss shell with `.breadcrumb` ("Document 05 · Extract 05.N"), `.article` body, h2s numbered `05.N.1, 05.N.2 …`, nav/footer. Grep each for banned phrases; fix any stragglers.
- [ ] **Step 3:** Verify: every blog page loads `../style.css` and `../script.js`; internal links work. Commit: `git commit -am "Restyle blog index and posts as Document 05"`

### Task 8: OG share image + docs reconciliation

**Files:**
- Create: `Images/og-share.png` (replace, 1200×630, swiss style)
- Modify: `docs/WEBSITE_REDESIGN_PLAN.md` (superseded banner)
- Create: `docs/FOLLOW-UPS.md`
- Modify: `.claude/CLAUDE.md` (brand section → swiss tokens)

- [ ] **Step 1:** Author `scratchpad/og-card.html`: 1200×630 navy `#0f2440` card, paper `#f4f1ea` type, "JKFM" lockup, "JK Facilities Management", rule line, "Moving from reactive chaos to proactive control." Screenshot at exactly 1200×630 in the preview browser; save over `Images/og-share.png`.
- [ ] **Step 2:** Prepend to WEBSITE_REDESIGN_PLAN.md: `> **SUPERSEDED 28/08/2026** by the swiss institutional restyle (docs/superpowers/specs/2026-08-28-swiss-restyle-design.md). Remaining live items moved to docs/FOLLOW-UPS.md.`
- [ ] **Step 3:** Write `docs/FOLLOW-UPS.md`: GA4 setup, Search Console sitemap re-submit after deploy, Google Business Profile (Karan verifies), performance/accessibility pass, social profile links.
- [ ] **Step 4:** Update `.claude/CLAUDE.md`: brand = navy `#0f2440` / paper `#f4f1ea`, Helvetica system stack (no Google Fonts), swiss register conventions, pointer to the spec.
- [ ] **Step 5:** Commit: `git commit -am "New swiss og-share image; supersede 9 phase plan; update project docs"`

### Task 9: Full verification + preview for Karan

- [ ] **Step 1:** Repo-wide grep (all .html): banned phrases list from Global Constraints + `Montserrat|Open Sans|fonts.googleapis` (should be gone) + `jkfm.co` (only in redirects/comments).
- [ ] **Step 2:** Link check: extract all href/src, confirm every relative target exists.
- [ ] **Step 3:** Serve locally, browse every page at desktop and 375px mobile; check nav wrap, FAQ toggles, form renders, footer Schedule A.
- [ ] **Step 4:** Screenshots of all pages; push branch to GitHub for a Netlify branch preview URL.
- [ ] **Step 5:** Present to Karan: preview link + screenshots + claims-sweep summary. **STOP — no merge to main without his go.**
