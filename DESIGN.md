# Design System — JK Facilities Management

## Product Context
- **What this is:** Marketing website for a facilities management and cleaning services company
- **Who it's for:** Strata/body corporate committees, property developers, builders looking for building managers or cleaning services
- **Space/industry:** Facilities management, strata management, Melbourne Australia
- **Project type:** Marketing site (multi-page, static HTML/CSS/JS on Netlify)

## Aesthetic Direction
- **Direction:** Luxury/Refined meets Industrial/Utilitarian — premium but grounded
- **Decoration level:** Intentional — subtle texture and depth, not flat corporate
- **Mood:** Professional, trustworthy, premium. Not a law firm (too stuffy) or a startup (too playful). A trusted professional who gets their hands dirty.

## Typography
- **Display/Hero:** Montserrat 900 (Black) — bold, commanding headlines
- **Headings:** Montserrat 800/700 — section headers, card titles
- **Body:** Open Sans 400 — clean, highly readable
- **UI/Labels:** Montserrat 600/700 — navigation, buttons, form labels
- **Loading:** Google Fonts CDN with preconnect hints
- **Scale:**
  - Hero: clamp(2.8rem, 6vw, 4.5rem)
  - H2: clamp(1.8rem, 3.5vw, 2.6rem)
  - H3: 1.05-1.15rem
  - Body: 1rem (16px)
  - Small/Meta: 0.8-0.85rem
  - Eyebrow: 0.75rem, uppercase, letter-spacing 0.15em

## Color
- **Approach:** Restrained — green + gold, no blue
- **Primary:** #1A3C2E — headers, nav, footer, strong text
- **Primary Light:** #2D6A4F — hover states, secondary surfaces
- **Accent (Gold):** #C6A24E — CTAs, highlights, emphasis
- **Accent Light:** #E2C97D — hover on gold, subtle emphasis
- **Surface Dark:** #0F1F17 — hero section, dark panels, nav background
- **Surface Light:** #F7F5F0 — page background (warm off-white)
- **White:** #FFFFFF — cards, content blocks, alternating sections
- **Text Primary:** #1C1C1C — body text
- **Text Secondary:** #5C6B5C — supporting text, muted content
- **Text on Dark:** #D4CFC4 — body text on dark backgrounds
- **Border:** #D8D3C8 — card borders, dividers
- **Semantic:** Success #2D7D46, Warning #D4A017, Error #C0392B, Info #2D6A4F

## Spacing
- **Base unit:** 8px
- **Density:** Comfortable — marketing site, not a dashboard
- **Scale:** 2xs(2) xs(4) sm(8) md(16) lg(24) xl(32) 2xl(48) 3xl(64) 4xl(96)
- **Section padding:** 96px vertical
- **Card padding:** 28-36px
- **Container max-width:** 1120px

## Layout
- **Approach:** Grid-disciplined — clean, predictable columns
- **Grid:** 3 columns for services, 4 for process steps, 2 for testimonials/contact
- **Max content width:** 1120px
- **Border radius:** 6px (consistent across all elements)
- **Nav:** Fixed top, dark with backdrop blur

## Motion
- **Approach:** Minimal-functional — subtle, professional
- **Hover:** translateY(-1px to -3px) on cards/buttons, 0.2s transitions
- **Easing:** ease for general, ease-out for entrances
- **Duration:** 0.2s for interactions, 0.3s for transitions

## Icons
- **Style:** SVG line icons, stroke-width 2, no fill
- **Color:** var(--primary) on light backgrounds
- **Size:** 24px in service cards, 14px inline
- **NO emoji icons** — all icons must be SVG

## Logo
- **Primary:** Shield monogram (JKFM Monogram - Final.png) — nav, favicon, social avatars
- **Full:** Shield + "JK Facilities Management" text — footer, about page
- **Needs:** SVG conversion of monogram for crisp rendering

## Key Design Rules
1. Drop all blue from the palette — green + gold only
2. No emoji icons anywhere — SVG line icons or let typography do the work
3. Warm off-white (#F7F5F0) backgrounds, not cold grey or pure white
4. Gold accent used sparingly for CTAs and emphasis, not decoration
5. Dark sections (hero, CTA banner, footer) use Surface Dark (#0F1F17)
6. All nav links must work from any page (use absolute paths)

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-06 | Keep Montserrat + Open Sans | User preference — familiar fonts that work for the audience |
| 2026-04-06 | Drop blue from palette | Dilutes the brand — green + gold is the differentiator |
| 2026-04-06 | Warm off-white backgrounds | Premium feel, pairs with gold, stands out from cold corporate competitors |
| 2026-04-06 | SVG icons only, no emoji | Professional polish — emoji looks cheap |
| 2026-04-06 | 6px border-radius everywhere | Consistent, subtle rounding — not too sharp, not too bubbly |
