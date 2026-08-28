# Swiss Institutional Restyle — Design Spec

**Date:** 28/08/2026
**Status:** LOCKED (Karan confirmed all four open calls, 28/08/2026)
**Supersedes:** docs/WEBSITE_REDESIGN_PLAN.md Phases 1 and 4 (see Reconciliation below)

## Goal

Restyle every page of the live JKFM website to the 01 swiss institutional design
direction (OC outreach Gate 2 winner, revised 10/08/2026) so the site matches the
capability statement, while keeping the working Netlify contact form and all
existing SEO infrastructure, and sweeping every factual claim against
`~/Projects/company-resources/jkfm-profile.md`.

## Source material

- **Skin + structure:** `~/Projects/company-resources/campaigns/oc-outreach-2026/full-sites/01-swiss-institutional/`
  (index, services, cleaning, about, privacy + style.css + script.js). This is the
  base. Reference tokens: navy `#0f2440`, paper `#f4f1ea`, Helvetica stack,
  hairline rules, decimal clause numbering, zero imagery.
- **Claims:** `jkfm-profile.md` is the single source of factual claims. Every
  claim on the site must trace to it, with ONE override:
- **24 level ruling (Karan, 28/08/2026):** the flagship building is described as
  **24 levels (B2, B1, ground plus 21 residential levels)** — overrides the
  profile's 21 level wording wherever the building is described.

## Page inventory (all get the swiss skin)

| Page | Register label | Content source |
|---|---|---|
| index.html | Document 01 · Home | full-sites index, claims swept |
| services.html | Document 02 · Building management | full-sites services, claims swept |
| cleaning.html | Document 03 · Cleaning | full-sites cleaning, claims swept |
| about.html | Document 04 · About | full-sites about, claims swept |
| blog/index.html | Document 05 · Blog | NEW skin, existing repo content |
| blog/*.html (6 posts) | Document 05.1–05.6 | NEW skin, existing repo content |
| privacy.html | Document 06 · Privacy | full-sites privacy |
| 404.html | Unnumbered | NEW skin, short "document not found" page |

Full register conceit everywhere (Karan's call): document numbers in nav,
clause numbering, Schedule A footer, End of Document marks.

## Locked decisions (28/08/2026)

1. **Testimonials removed** (claims file bans them; none approved). Replaced on
   the homepage by a **Track record** section on 42-48 Claremont Street, built
   from profile section 3: 24 levels (ruling wording), 111 apartments, 25+
   specialist contractors coordinated at one building, live WIP register (1,000+
   historical entries), written report to every committee meeting (locked
   generic wording — no frequency), BM + cleaning held by the same accountable
   party. "Flagship" framing only — never plural clients.
2. **Accumulator case note widened to the website homepage** (Karan's ruling
   28/08/2026 widens the 10/08 landing-page-only scope). Use the approved
   wording from profile section 10a revision: zero pressure six months after a
   passed service; one line replacement quote; JKFM's four questions; properly
   specified replacement at close to half the quoted cost. No contractor names,
   no dollar figures, no claim works are complete.
3. **WEBSITE_REDESIGN_PLAN.md superseded.** Surviving items move to
   `docs/FOLLOW-UPS.md`: GA4, Google Search Console sitemap re-submit, Google
   Business Profile, performance/accessibility pass, social links.
4. **Full register conceit** carried to the live site, not softened.

## Claims sweep (applies to base build AND current live copy)

| Current claim | Correction | Profile ref |
|---|---|---|
| "photo evidence" on cleaning (all pages + meta + JSON-LD) | Documented per shift checklists, unannounced quality audits, site specific teams. Photo ceiling: "photographed where an issue warrants it" | s2, s4, s9.12 |
| Testimonials (2 quotes) | Removed → Track record section | s9.6 |
| "every building we manage" / "our buildings" | "JKFM works with owners corporations and strata committees" or flagship framing | s5a |
| "No obligations beyond the agreed engagement" | Six month trial approved wording: "every JKFM building management agreement starts with a six month trial period" | s5a |
| "free assessment" | Free building health check: free, no obligation walkthrough of common areas by the director, short written summary of findings. No promised format, turnaround or monitoring | s5 |
| "100% contractor accountability" stat | Not in profile — replace with claimable fact (e.g. 24/7 emergency response stays as exactly those four words) | s5a |
| Any response time/speed framing | "Issues escalate directly to the director, not through layers of area managers" | s5a |

Additions the profile supports and the swiss direction wants: founder led
accountability, no PPSA security interests (exact approved wording), $20m public
liability (certificate available on request, no insurer named), WorkSafe Victoria
registered, police checked cleaners, SiteCheck (live at sitecheck.jkfm.co,
contractor sign in + induction, committee facing dashboard with in/out times —
NO photo claims), founded 2023 (exact wording only).

Hard bans checklist (s9): no clients beyond the flagship, no Watergate, no
Glenarm, no team size/revenue, no pricing, no named contractors/builder/insurer,
no SLAs, no per task photo claims, no 9 Darling photo.

## Style law

- Australian English. No hyphens or em dashes in copy ("4 step lifecycle",
  "day to day"); street ranges like 42-48 stay. Dates DD/MM/YYYY.
- Vanilla HTML/CSS/JS. One shared style.css, one shared script.js. No
  frameworks, no build step.
- stop-slop pass on all rewritten copy.

## Keep intact (from current repo)

- Netlify contact form (`data-netlify="true"`, honeypot, name="contact") —
  restyled as **Form 09-A** but functionally unchanged. The full-sites mailto
  fallback script is NOT ported; keep the real form POST.
- All head metadata per page: canonical (.com.au), og/twitter tags, JSON-LD
  (update descriptions where the claims sweep changes them), robots.txt,
  sitemap.xml, _redirects, favicon, google site verification file.
- URLs unchanged — no page renames, sitemap stays valid.
- New og-share.png in swiss style (navy/paper typographic card) replacing the
  old green/gold one.

## Process

1. Branch `swiss-restyle`; nothing merges to main (Netlify auto-deploys main)
   until Karan approves the preview.
2. Codex plan review (sol, 4 min cap) before implementation.
3. Build: port shared style.css + script.js, then page by page.
4. Verify: local browser preview at desktop + mobile widths, link check,
   form markup check, hyphen sweep grep, claims grep (photo evidence,
   testimonial, banned phrases).
5. Show Karan: browser preview + screenshots + Netlify branch preview link.
   Deploy to main only on his go.

## Scope addition (28/08/2026 evening, relayed from the capability statement session)

- Homepage section 06 is now **The flagship**: 42-48 Claremont Street featured with
  the approved dusk render (Images/claremont-tower.jpg, shown solid in colour with a
  hairline border — no fade treatments), covering building management, maintenance
  and cleaning. New approved claim: "more than 5,000 cleaning hours delivered since
  October 2023" (contract since 23/10/2023, Mon to Sat 6h/day).
- Carried-over capability statement rulings: plain factual headings, no slogans in
  the new section; "quality audits" not "unannounced quality audits" (swept site
  wide); cleaning framed as trained site dedicated teams, never Karan personally.
- NOT changed pending Karan's word: sitewide contact email stays
  enquiries@jkfacilitiesmanagement.com.au (the karan@jkfm.co ruling was for the
  capability statement contact line); homepage tagline stays (profile approved core
  tagline).
