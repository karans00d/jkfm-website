# JKFM Website Expansion — Design Doc
**Date:** 2026-03-11
**Approach:** Option C — Separate pages + index as teaser landing page

---

## Files Changed / Created

| File | Action |
|------|--------|
| `index.html` | Update nav, footer, add teaser CTAs |
| `style.css` | Add Playfair Display, footer logo img styles |
| `services.html` | Create new |
| `cleaning.html` | Create new |

---

## index.html Changes

1. Remove `<span class="logo-tagline">Risk-Led Oversight</span>` from nav
2. Add `Playfair Display` to Google Fonts import
3. Change `.logo-name` font to Playfair Display in CSS
4. Footer: replace hand-drawn SVG with `<img src="Images/JKFM Initials.png">`
5. Nav links: `#services` → `services.html`, `#cleaning` → `cleaning.html`
6. Services section: add "See All Services →" button → `services.html`
7. Cleaning section: add "See All Cleaning →" button → `cleaning.html`

---

## services.html Structure

- **Nav** — same as index, logo links back to `index.html`
- **Hero** — dark green bg, headline: "Facilities Management That Puts Your Committee in Control"
- **Services Grid** — 6 cards with expanded detail + bullet points
  - Building Operations
  - Compliance & Safety
  - Contractor Management
  - Financial Stewardship
  - Committee Support
  - Innovation & Future-Proofing
- **4-Step Process** — same as index
- **Why JKFM** — 3 columns: Risk-Led | Accountable | Transparent
- **Contact CTA strip** — links to `index.html#contact`
- **Footer** — same as index

---

## cleaning.html Structure

- **Nav** — same as index
- **Hero** — headline: "Commercial & Residential Cleaning Across Australia"
- **Services Grid** — 8 cards:
  - Steam Cleaning
  - Pressure Washing (external areas, driveways, facades)
  - End of Lease Cleaning (bond-back standard)
  - Strata & Common Area Cleaning
  - Carpet Cleaning
  - Window Cleaning
  - Commercial Cleaning
  - Residential Cleaning
- **How It Works** — 3 steps: Book → We Clean → You Approve
- **Quality Promise** — bullet list
- **Contact CTA strip** — "Book a Clean" → `index.html#contact`
- **Footer** — same as index

---

## Design Tokens (unchanged)

- Dark green: `#1B4332`
- Gold: `#C9A84C`
- Blue accent: `#1E6091`
- Dark BG: `#050e08`
- White background sections: `#ffffff`
- Company name font: **Playfair Display** (new)
- Body font: Montserrat + Open Sans (existing)

---

## Out of Scope

- Backend / form processing
- CMS
- New color palette
- Blog article full pages
