# JKFM Website Redesign & SEO Plan

**Created:** 2026-04-06
**Status:** Planning
**Site:** https://jkfm.co
**Repo:** C:\Users\kayso\Projects\jkfm-website (GitHub: karans00d/jkfm-website)
**Hosting:** Netlify
**Current stack:** Static HTML/CSS/JS

---

## Business Context

**JK Facilities Management (JKFM)** provides two core services:
1. **Building Management** — for strata/body corporate committees, developers, builders
2. **Cleaning Services** — commercial cleaning for residential OCs

**Service area:** Melbourne only (for now)
**Target audience:** Strata/body corporate committees, property developers, builders — anyone looking for building managers or cleaning services.
**Director:** Karan Sood — karan@jkfm.co — 0459 361 650

---

## Brand Assets (current)

### Logo
- **Shield + text** logo: dark green + gold (PNG only — needs SVG conversion)
- **Monogram** (shield only): great for favicon, social avatars
- **Text initials**: "JKFM" wordmark
- Location: `C:\Users\kayso\Desktop\JKFM Brand\JKFM - New\`

### Brand Colours (extracted from logo)
- Primary: Deep forest green (~#1B4332)
- Accent: Gold/champagne (~#C5A55A)
- Text: Dark green/near-black
- Background: White

### Photos
- Karan headshots (2x professional, suit) — for About page
- Email signature design — already branded
- Infographic: "Reactive Chaos to Proactive Control"
- Slide deck (PDF + PPTX) for residential OC pitches
- NOTE: "9 Darling.jpg" is for a separate pitch project, NOT for general JKFM branding

### What's Missing
- SVG version of logo (need to create from PNG)
- Building photography of 42-48 Claremont St or generic Melbourne buildings
- No professional team/work-in-action photos

---

## Current Site Audit (2026-04-06)

### Structure
Single-page marketing site with sections: Hero, Problem, Central Hub, Reactive vs Proactive, 4-Step Process, Services, Cleaning, Onboarding, Audit Trail, Testimonials, Blog (6 posts), FAQ, Contact, Footer.
Additional pages: services.html, cleaning.html, privacy.html, 6 blog posts.

### Critical Issues
1. **Contact form is fake** — handleSubmit() fakes success, data goes nowhere. Losing leads.
2. **No sitemap.xml** (returns 404)
3. **No robots.txt** (returns 404)
4. **No og:image** — social shares have no preview image
5. **No Twitter Card tags**
6. **No structured data (JSON-LD)** — no LocalBusiness schema
7. **No canonical URL tags**
8. **Footer links broken on subpages** — bare anchors only work on homepage
9. **No preconnect hints** for Google Fonts (render-blocking)
10. **Favicon has spaces in filename** and is PNG instead of ICO/SVG
11. **No Google Analytics**
12. **No Google Business Profile**

### Social Presence
- **LinkedIn**: Business page exists
- **Instagram**: Needs creating
- **YouTube**: Needs creating
- **Facebook**: Consider creating (strata/body corp demographics)
- **Google Business Profile**: Needs creating (critical for local SEO)

---

## Phase 1: Design System & Brand Foundation

**Goal:** Establish the visual identity system that all subsequent work builds on.

### Tasks
- [ ] 1.1 Create SVG version of shield logo (trace from high-res PNG)
- [ ] 1.2 Create SVG favicon from monogram
- [ ] 1.3 Run `/design-consultation` — establish full design system:
  - Typography (heading + body font pairing)
  - Colour palette (primary, accent, neutrals, semantic colours)
  - Spacing scale
  - Component styles (buttons, cards, forms, nav)
  - Motion/animation guidelines
- [ ] 1.4 Generate font + colour preview page
- [ ] 1.5 Save design system as DESIGN.md in project root
- [ ] 1.6 Review with Karan — get sign-off before proceeding

### Deliverables
- DESIGN.md (design system source of truth)
- SVG logo files
- Favicon (ICO + SVG)
- Preview page showing palette, typography, components

---

## Phase 2: SEO & Technical Infrastructure

**Goal:** Fix all technical SEO issues so the site is discoverable.

### Tasks
- [ ] 2.1 Create robots.txt with sitemap reference
- [ ] 2.2 Create sitemap.xml covering all pages
- [ ] 2.3 Add JSON-LD structured data (LocalBusiness schema) to all pages
  - Business name, address (42-48 Claremont St, South Yarra VIC 3141)
  - Service area: Melbourne
  - Phone, email, website
  - Services: Building Management, Cleaning
- [ ] 2.4 Add canonical URL tags to every page
- [ ] 2.5 Add Open Graph meta tags to every page (og:title, og:description, og:image, og:url)
- [ ] 2.6 Add Twitter Card meta tags to every page
- [ ] 2.7 Create OG share image (branded card for social sharing)
- [ ] 2.8 Fix favicon — use SVG/ICO from Phase 1, no spaces in path
- [ ] 2.9 Add preconnect hints for Google Fonts
- [ ] 2.10 Set up Google Analytics 4
- [ ] 2.11 Set up Google Search Console — submit sitemap
- [ ] 2.12 Create Google Business Profile (Karan to verify)

### Deliverables
- robots.txt, sitemap.xml
- JSON-LD on all pages
- Full meta tag coverage
- GA4 tracking live
- Google Business Profile created

---

## Phase 3: Site Architecture & Navigation

**Goal:** Restructure from a single-page site to a proper multi-page site.

### Proposed Site Map
```
Home (/)
├── Services (/services/)
│   ├── Building Management (/services/building-management.html)
│   └── Cleaning Services (/services/cleaning.html)
├── About (/about.html)
├── Blog (/blog/)
│   └── [existing 6 posts + new content]
├── Contact (/contact.html)
├── Privacy Policy (/privacy.html)
└── sitemap.xml
```

### Tasks
- [ ] 3.1 Design navigation (header + footer + mobile menu)
- [ ] 3.2 Create About page — Karan's story, approach, why JKFM, headshot
- [ ] 3.3 Split services into dedicated pages with detailed content
- [ ] 3.4 Create standalone Contact page
- [ ] 3.5 Fix all internal links (footer, nav, cross-page references)
- [ ] 3.6 Add breadcrumbs for blog posts
- [ ] 3.7 Ensure all pages have consistent header/footer

---

## Phase 4: Visual Redesign

**Goal:** Full visual refresh using the design system from Phase 1.

### Tasks
- [ ] 4.1 Homepage redesign:
  - Hero with compelling headline + CTA + building imagery
  - Services overview (cards linking to detail pages)
  - Trust signals (years of experience, number of buildings, etc.)
  - Testimonials section
  - CTA section
- [ ] 4.2 Services pages — professional layout with icons, features, process
- [ ] 4.3 About page — personal, trustworthy, with headshot
- [ ] 4.4 Blog redesign — clean grid layout, categories, better readability
- [ ] 4.5 Contact page — form + map + direct contact details
- [ ] 4.6 Responsive design — mobile-first, tested on all breakpoints
- [ ] 4.7 Use `/design-shotgun` to generate variant options for hero section
- [ ] 4.8 Review with Karan — iterate on feedback

---

## Phase 5: Contact Form (Lead Capture)

**Goal:** Make the contact form actually work.

### Tasks
- [ ] 5.1 Integrate Netlify Forms (add `netlify` attribute to form)
- [ ] 5.2 Configure email notifications to karan@jkfm.co
- [ ] 5.3 Add proper form validation (client-side)
- [ ] 5.4 Add real success/error states
- [ ] 5.5 Add honeypot spam protection
- [ ] 5.6 Test form submission end-to-end

---

## Phase 6: Social Media Setup & Integration

**Goal:** Establish social presence and integrate with website.

### Tasks
- [ ] 6.1 Create Instagram Business page for JKFM
- [ ] 6.2 Create YouTube channel for JKFM
- [ ] 6.3 Consider creating Facebook Business Page
- [ ] 6.4 Consider Houzz profile (property/building niche)
- [ ] 6.5 Add social links to website header/footer with icons
- [ ] 6.6 Create branded OG share images for each page
- [ ] 6.7 Set up link-in-bio page (optional — for Instagram)

### Accounts Karan needs to create (manual):
- Instagram (needs phone verification)
- YouTube (needs Google account)
- Google Business Profile (needs postcard/phone verification)

---

## Phase 7: Content & Blog Strategy

**Goal:** Optimise existing content and plan new content for SEO.

### Tasks
- [ ] 7.1 Audit existing 6 blog posts — optimise titles, headings, meta descriptions
- [ ] 7.2 Add internal linking (blog ↔ service pages)
- [ ] 7.3 Plan new blog posts targeting high-intent search queries:
  - "What does a building manager do?"
  - "Strata cleaning standards in Melbourne"
  - "How to choose a facilities manager for your building"
  - "Common maintenance issues in Melbourne apartments"
  - "Body corporate building manager responsibilities"
  - "Cost of facilities management Melbourne"
- [ ] 7.4 Add blog categories/tags
- [ ] 7.5 Add related posts section to each blog post

---

## Phase 8: Performance & Accessibility

**Goal:** Fast, accessible, best-practice site.

### Tasks
- [ ] 8.1 Optimise images — WebP format, lazy loading, proper sizing
- [ ] 8.2 Minify CSS/JS
- [ ] 8.3 Add noscript fallbacks for critical content
- [ ] 8.4 Accessibility audit — alt text, contrast ratios, keyboard navigation, ARIA
- [ ] 8.5 Add skip-to-content link
- [ ] 8.6 Test with screen reader

---

## Phase 9: QA & Launch

**Goal:** Verify everything works before going live.

### Tasks
- [ ] 9.1 Full QA via GStack — visual review, responsive testing, form testing
- [ ] 9.2 Cross-browser testing (Chrome, Safari, Firefox, Edge)
- [ ] 9.3 Lighthouse audit — target 90+ on all four categories
- [ ] 9.4 Test social sharing — verify og:image on LinkedIn, Facebook, Twitter
- [ ] 9.5 Verify Google Analytics tracking
- [ ] 9.6 Submit updated sitemap to Google Search Console
- [ ] 9.7 Final review with Karan
- [ ] 9.8 Deploy to production

---

## Separate Project: 9 Darling Pitch Deck

**NOTE:** The 9 Darling building image and slide deck work is a separate project for pitching a specific building contract. Will be tracked separately.

---

## Progress Log

| Date | Phase | What was done |
|------|-------|---------------|
| 2026-04-06 | Planning | Initial audit, brand review, plan created |
