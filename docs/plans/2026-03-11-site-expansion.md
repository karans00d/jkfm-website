# JKFM Site Expansion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add dedicated services.html and cleaning.html pages, update index.html nav/footer/font, and link everything together.

**Architecture:** Option C — index.html stays as teaser landing page; services.html and cleaning.html are full standalone pages sharing the same nav, footer, and style.css. No backend, no build system — plain HTML/CSS/JS files opened directly in a browser.

**Tech Stack:** HTML5, CSS3 (style.css), vanilla JS (script.js), Google Fonts (Montserrat + Open Sans + Playfair Display)

---

## Task 1: Update index.html — Nav & Footer

**Files:**
- Modify: `index.html`

**Step 1: Remove the tagline from nav**

Find and delete this line in index.html (line 21):
```html
<span class="logo-tagline">Risk-Led Oversight</span>
```

**Step 2: Update nav links to point to new pages**

Replace anchor links in the `<ul class="nav-links">`:
```html
<ul class="nav-links">
  <li><a href="index.html#problem">The Problem</a></li>
  <li><a href="services.html">Services</a></li>
  <li><a href="index.html#process">Our Process</a></li>
  <li><a href="cleaning.html">Cleaning</a></li>
  <li><a href="index.html#contact">Contact</a></li>
</ul>
```

**Step 3: Replace footer SVG with JKFM Initials.png**

Find the `<div class="footer-logo">` block (lines 792–811) and replace the entire `<svg>` element with:
```html
<img src="Images/JKFM Initials.png" alt="JKFM" class="footer-logo-img" />
```

**Step 4: Add teaser CTAs to Services and Cleaning sections**

In the services section (after the closing `</div>` of `.services-grid`, before `</section>`), add:
```html
<div class="section-cta-center">
  <a href="services.html" class="btn-primary">See All Services →</a>
</div>
```

In the cleaning section (after `<a href="#contact" class="btn-primary">Book a Clean</a>`), add:
```html
<a href="cleaning.html" class="btn-outline" style="margin-left:1rem;">See All Cleaning →</a>
```

**Step 5: Verify in browser**
Open index.html — check:
- No tagline under company name in nav
- Services and Cleaning nav links don't jump to anchors (they'll 404 until pages are created — that's OK for now)
- Footer shows the Initials PNG
- Two new CTA buttons visible

---

## Task 2: Update style.css — Font & Footer Logo

**Files:**
- Modify: `style.css`
- Modify: `index.html` (Google Fonts import only)

**Step 1: Add Playfair Display to Google Fonts import in index.html**

Replace line 8:
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@300;400;600&display=swap" rel="stylesheet" />
```
With:
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@300;400;600&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet" />
```

**Step 2: Update .logo-name font in style.css**

Find `.logo-name` (around line 1141) and change `font-family`:
```css
.logo-name {
  font-family: 'Playfair Display', Georgia, serif;
  font-weight: 700;
  font-size: 1rem;
  color: var(--white);
  line-height: 1.2;
}
```

**Step 3: Add footer logo image style to style.css**

After `.footer-logo { display: flex; gap: 1rem; align-items: center; }` (line 1122), add:
```css
.footer-logo-img { height: 38px; width: auto; flex-shrink: 0; }
```

**Step 4: Verify in browser**
Open index.html — check:
- "JK Facilities Management" in nav uses a serif font (Playfair Display)
- Footer Initials logo is ~38px tall, not huge

---

## Task 3: Create services.html

**Files:**
- Create: `services.html`

**Step 1: Create the file**

Create `services.html` with this full content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Facilities Management Services | JK Facilities Management</title>
  <link rel="stylesheet" href="style.css" />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@300;400;600&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet" />
</head>
<body>

  <!-- NAVIGATION -->
  <header class="nav-wrapper">
    <nav class="nav-container">
      <a href="index.html" class="nav-logo">
        <img src="Images/JKFM Monogram - Final.png" alt="JKFM Logo" class="nav-logo-icon" />
        <div class="nav-logo-text">
          <span class="logo-name">JK Facilities Management</span>
        </div>
      </a>
      <ul class="nav-links">
        <li><a href="index.html#problem">The Problem</a></li>
        <li><a href="services.html" class="nav-active">Services</a></li>
        <li><a href="index.html#process">Our Process</a></li>
        <li><a href="cleaning.html">Cleaning</a></li>
        <li><a href="index.html#contact">Contact</a></li>
      </ul>
      <a href="index.html#contact" class="btn-nav">Get a Quote</a>
      <button class="nav-toggle" aria-label="Open menu">&#9776;</button>
    </nav>
  </header>

  <!-- HERO -->
  <section class="hero hero-subpage">
    <div class="hero-bg-overlay"></div>
    <div class="hero-content">
      <p class="hero-eyebrow">Facilities Management for Residential Owners Corporations</p>
      <h1 class="hero-headline">
        Facilities Management That Puts Your<br /><span class="gold">Committee in Control</span>
      </h1>
      <p class="hero-sub">
        We take on the operational work — oversight, contractor management, compliance, and reporting —
        so your committee can focus on decision-making, not day-to-day firefighting.
      </p>
      <div class="hero-cta-group">
        <a href="index.html#contact" class="btn-primary">Request a Quote</a>
        <a href="#services-detail" class="btn-outline">See Our Services</a>
      </div>
    </div>
  </section>

  <!-- SERVICES DETAIL -->
  <section class="services-section services-detail-section" id="services-detail">
    <div class="section-container">
      <div class="section-tag tag-center">What We Do</div>
      <h2 class="section-title text-center">Comprehensive <span class="gold">Facilities Management</span></h2>
      <p class="section-subtitle">Everything your building needs — planned, managed, and reported on with full transparency.</p>
      <div class="services-grid services-grid-detail">

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🏗️</div>
          <h3>Building Operations</h3>
          <p>Day-to-day management of all building systems and common property.</p>
          <ul class="service-detail-list">
            <li>HVAC, lift, and essential services coordination</li>
            <li>Preventative and reactive maintenance scheduling</li>
            <li>Utilities and service contract management</li>
            <li>Building access and key management</li>
            <li>Incident response and emergency coordination</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">📋</div>
          <h3>Compliance &amp; Safety</h3>
          <p>Proactive management of all safety and regulatory obligations.</p>
          <ul class="service-detail-list">
            <li>Fire safety system inspections and certifications</li>
            <li>Essential services compliance scheduling</li>
            <li>OHS obligations and hazard identification</li>
            <li>Certification renewal tracking and alerts</li>
            <li>Audit-ready documentation maintained at all times</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🔧</div>
          <h3>Contractor Management</h3>
          <p>Full accountability from scope to sign-off — no more chasing contractors.</p>
          <ul class="service-detail-list">
            <li>Defined scope of works before any job commences</li>
            <li>Contractor vetting, licensing, and insurance checks</li>
            <li>On-site supervision and progress monitoring</li>
            <li>Quality and completion checks before sign-off</li>
            <li>Single accountable point of contact for the committee</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">📊</div>
          <h3>Financial Stewardship</h3>
          <p>Transparent budgeting and reporting to support informed committee decisions.</p>
          <ul class="service-detail-list">
            <li>Maintenance budget planning and cost forecasting</li>
            <li>Capital works planning and fund management support</li>
            <li>Itemised spend reporting per building system</li>
            <li>Quote comparison and value-for-money assessment</li>
            <li>End-of-period financial summaries for AGM preparation</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🏛️</div>
          <h3>Committee Support</h3>
          <p>Everything the committee needs to stay informed and in control.</p>
          <ul class="service-detail-list">
            <li>Regular written building updates and status reports</li>
            <li>Open item tracking with clear owner and deadline</li>
            <li>Escalation of items requiring committee decision</li>
            <li>Meeting preparation support and agenda input</li>
            <li>Resident communication management on common area matters</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🔮</div>
          <h3>Innovation &amp; Future-Proofing</h3>
          <p>Long-term building strategy, sustainability, and smart tools.</p>
          <ul class="service-detail-list">
            <li>10-year capital works planning and lifecycle assessment</li>
            <li>Energy efficiency audits and sustainability initiatives</li>
            <li>Smart building technology integration</li>
            <li>AI-assisted reporting and maintenance insights</li>
            <li>Future-proofing recommendations for ageing infrastructure</li>
          </ul>
        </div>

      </div>
    </div>
  </section>

  <!-- 4-STEP PROCESS -->
  <section class="process-section" id="process">
    <div class="section-container">
      <div class="section-tag tag-center">A Defined Management Lifecycle</div>
      <h2 class="section-title text-center">We follow a <span class="gold">clear, repeatable process</span></h2>
      <p class="section-subtitle">No guesswork. No reactive scrambles. A structured approach every time.</p>
      <div class="process-grid">
        <div class="process-step" data-animate>
          <div class="process-num">01</div>
          <div class="process-icon">🔍</div>
          <h3>Understand the Building</h3>
          <p>Site familiarisation, documentation review, and building risk profile assessment.</p>
        </div>
        <div class="process-connector">→</div>
        <div class="process-step" data-animate>
          <div class="process-num">02</div>
          <div class="process-icon">📋</div>
          <h3>Plan Proactively</h3>
          <p>Maintenance schedules developed based on risk priority, not just urgency.</p>
        </div>
        <div class="process-connector">→</div>
        <div class="process-step" data-animate>
          <div class="process-num">03</div>
          <div class="process-icon">⚙️</div>
          <h3>Manage Execution</h3>
          <p>Contractor coordination, site access, quality checks, and follow-up — all managed by JKFM.</p>
        </div>
        <div class="process-connector">→</div>
        <div class="process-step" data-animate>
          <div class="process-num">04</div>
          <div class="process-icon">📊</div>
          <h3>Report Clearly</h3>
          <p>Written updates on issues, actions, risk status, and recommendations. Committee always informed.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- WHY JKFM -->
  <section class="why-section">
    <div class="section-container">
      <div class="section-tag tag-center">Why Choose JKFM</div>
      <h2 class="section-title text-center">The <span class="gold">JKFM Difference</span></h2>
      <div class="why-grid">
        <div class="why-card" data-animate>
          <div class="why-icon">🎯</div>
          <h3>Risk-Led</h3>
          <p>We prioritise maintenance based on risk level — not the most recent complaint. High-risk items get addressed first, every time.</p>
        </div>
        <div class="why-card" data-animate>
          <div class="why-icon">✅</div>
          <h3>Accountable</h3>
          <p>One point of contact. Defined scopes. Quality checks before sign-off. You always know what's happening and who's responsible.</p>
        </div>
        <div class="why-card" data-animate>
          <div class="why-icon">📄</div>
          <h3>Transparent</h3>
          <p>Audit-ready documentation. Clear financial reporting. Written updates on everything. The committee is always informed, never surprised.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT CTA STRIP -->
  <section class="cta-strip">
    <div class="section-container cta-strip-inner">
      <h2>Ready to take control of your building?</h2>
      <p>Get a tailored proposal within 24 hours.</p>
      <a href="index.html#contact" class="btn-primary">Request a Quote →</a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <div class="footer-logo">
          <img src="Images/JKFM Initials.png" alt="JKFM" class="footer-logo-img" />
          <div>
            <span class="footer-brand-name">JK Facilities Management</span>
            <span class="footer-brand-sub">Enhancing communities, one property at a time.</span>
          </div>
        </div>
      </div>
      <div class="footer-links">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html">Facilities Management</a></li>
          <li><a href="cleaning.html">Cleaning Services</a></li>
          <li><a href="index.html#process">Our Process</a></li>
          <li><a href="index.html#contact">Request a Quote</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Company</h4>
        <ul>
          <li><a href="index.html#problem">The Problem We Solve</a></li>
          <li><a href="services.html">How We Work</a></li>
          <li><a href="index.html#contact">Contact</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Contact</h4>
        <ul>
          <li>Karan@jkfm.co</li>
          <li>0459 361 650</li>
          <li>www.jkfm.co</li>
          <li>Available 24/7</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 JK Facilities Management. All rights reserved. | Risk-Led Oversight | Contractor Accountability | Clear Reporting</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

**Step 2: Verify in browser**
Open services.html — check:
- Nav loads with Playfair Display company name, no tagline
- 6 service cards each with bullet point detail
- 4-step process section visible
- Why JKFM 3-column section visible
- CTA strip at bottom links back to index.html#contact
- Footer shows Initials PNG logo

---

## Task 4: Create cleaning.html

**Files:**
- Create: `cleaning.html`

**Step 1: Create the file**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cleaning Services | JK Facilities Management</title>
  <link rel="stylesheet" href="style.css" />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@300;400;600&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet" />
</head>
<body>

  <!-- NAVIGATION -->
  <header class="nav-wrapper">
    <nav class="nav-container">
      <a href="index.html" class="nav-logo">
        <img src="Images/JKFM Monogram - Final.png" alt="JKFM Logo" class="nav-logo-icon" />
        <div class="nav-logo-text">
          <span class="logo-name">JK Facilities Management</span>
        </div>
      </a>
      <ul class="nav-links">
        <li><a href="index.html#problem">The Problem</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="index.html#process">Our Process</a></li>
        <li><a href="cleaning.html" class="nav-active">Cleaning</a></li>
        <li><a href="index.html#contact">Contact</a></li>
      </ul>
      <a href="index.html#contact" class="btn-nav">Get a Quote</a>
      <button class="nav-toggle" aria-label="Open menu">&#9776;</button>
    </nav>
  </header>

  <!-- HERO -->
  <section class="hero hero-subpage">
    <div class="hero-bg-overlay"></div>
    <div class="hero-content">
      <p class="hero-eyebrow">Commercial &amp; Residential Cleaning</p>
      <h1 class="hero-headline">
        Professional Cleaning<br /><span class="gold">Across Australia</span>
      </h1>
      <p class="hero-sub">
        From steam cleaning and pressure washing to end of lease and strata common areas —
        the same trusted team that manages your building keeps it spotless.
      </p>
      <div class="hero-cta-group">
        <a href="index.html#contact" class="btn-primary">Book a Clean</a>
        <a href="#cleaning-services" class="btn-outline">Our Services</a>
      </div>
    </div>
  </section>

  <!-- CLEANING SERVICES GRID -->
  <section class="services-section services-detail-section" id="cleaning-services">
    <div class="section-container">
      <div class="section-tag tag-center">What We Clean</div>
      <h2 class="section-title text-center">Professional <span class="gold">Cleaning Services</span></h2>
      <p class="section-subtitle">Comprehensive cleaning for commercial, residential, and strata properties across Australia.</p>
      <div class="services-grid services-grid-detail">

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">♨️</div>
          <h3>Steam Cleaning</h3>
          <p>High-temperature steam cleaning for deep sanitisation without harsh chemicals.</p>
          <ul class="service-detail-list">
            <li>Carpet and upholstery steam cleaning</li>
            <li>Hard floor steam sanitisation (tiles, grout, vinyl)</li>
            <li>Kitchen and commercial kitchen deep steam clean</li>
            <li>Mattress and soft furnishing sanitisation</li>
            <li>Ideal for allergen removal and hygiene-critical areas</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">💧</div>
          <h3>Pressure Washing</h3>
          <p>External surface cleaning for driveways, facades, and outdoor areas.</p>
          <ul class="service-detail-list">
            <li>Driveway and car park pressure washing</li>
            <li>Building facade and exterior wall cleaning</li>
            <li>Footpath and common walkway cleaning</li>
            <li>Pool surrounds and outdoor entertaining areas</li>
            <li>Removal of graffiti, mould, and built-up grime</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🔑</div>
          <h3>End of Lease Cleaning</h3>
          <p>Bond-back quality cleaning that meets real estate agent inspection standards.</p>
          <ul class="service-detail-list">
            <li>Full property deep clean — every room, every surface</li>
            <li>Oven, stovetop, and kitchen appliance cleaning</li>
            <li>Bathroom and toilet deep scrub and sanitisation</li>
            <li>Wall marks, light switches, and skirting boards</li>
            <li>Carpet steam clean included on request</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🏢</div>
          <h3>Strata &amp; Common Area Cleaning</h3>
          <p>Consistent, scheduled cleaning for all common property areas.</p>
          <ul class="service-detail-list">
            <li>Lobby, foyer, and entrance cleaning</li>
            <li>Lift car and lift lobby cleaning</li>
            <li>Stairwell and hallway cleaning</li>
            <li>Car park sweeping and pressure washing</li>
            <li>Garden and outdoor common area maintenance</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🪟</div>
          <h3>Window Cleaning</h3>
          <p>Streak-free window cleaning for commercial and residential properties.</p>
          <ul class="service-detail-list">
            <li>Interior and exterior window cleaning</li>
            <li>High-rise and multi-storey window cleaning</li>
            <li>Shopfront and commercial facade glass</li>
            <li>Frame, sill, and track cleaning included</li>
            <li>Regular scheduled or one-off service available</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🏠</div>
          <h3>Residential Cleaning</h3>
          <p>Regular and one-off cleaning for apartments and houses.</p>
          <ul class="service-detail-list">
            <li>Weekly, fortnightly, or monthly scheduled cleans</li>
            <li>One-off deep clean for spring cleaning or special occasions</li>
            <li>Kitchen and bathroom focus cleans</li>
            <li>Dusting, vacuuming, mopping all areas</li>
            <li>Flexible scheduling around your routine</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🏭</div>
          <h3>Commercial Cleaning</h3>
          <p>Professional cleaning for offices, retail, and commercial buildings.</p>
          <ul class="service-detail-list">
            <li>After-hours office cleaning (no disruption to business)</li>
            <li>Retail and showroom cleaning</li>
            <li>Gym, medical, and childcare facility cleaning</li>
            <li>Warehouse and industrial space cleaning</li>
            <li>Periodic deep cleans and scheduled maintenance cleans</li>
          </ul>
        </div>

        <div class="service-card service-card-detail" data-animate>
          <div class="service-icon">🧹</div>
          <h3>Carpet Cleaning</h3>
          <p>Professional carpet cleaning for residential and commercial properties.</p>
          <ul class="service-detail-list">
            <li>Hot water extraction (steam cleaning method)</li>
            <li>Stain and spot treatment</li>
            <li>Deodorising and sanitising treatment</li>
            <li>Suitable for all carpet types including wool and commercial grade</li>
            <li>Fast dry times — back to normal within hours</li>
          </ul>
        </div>

      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="process-section">
    <div class="section-container">
      <div class="section-tag tag-center">Simple Process</div>
      <h2 class="section-title text-center">How It <span class="gold">Works</span></h2>
      <p class="section-subtitle">Three easy steps from booking to a spotless result.</p>
      <div class="process-grid process-grid-3">
        <div class="process-step" data-animate>
          <div class="process-num">01</div>
          <div class="process-icon">📞</div>
          <h3>Book &amp; Brief</h3>
          <p>Tell us about your property — type, size, and what needs cleaning. We'll confirm scope, pricing, and timing within 24 hours.</p>
        </div>
        <div class="process-connector">→</div>
        <div class="process-step" data-animate>
          <div class="process-num">02</div>
          <div class="process-icon">🧽</div>
          <h3>We Clean</h3>
          <p>Our professional team arrives on time, works to the agreed scope, and uses industry-grade equipment and products throughout.</p>
        </div>
        <div class="process-connector">→</div>
        <div class="process-step" data-animate>
          <div class="process-num">03</div>
          <div class="process-icon">✅</div>
          <h3>You Approve</h3>
          <p>We do a final walkthrough with you before we leave. Not satisfied? We'll fix it — no questions asked.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- QUALITY PROMISE -->
  <section class="audit-section">
    <div class="section-container">
      <div class="audit-grid">
        <div class="audit-text">
          <div class="section-tag">Our Standard</div>
          <h2 class="section-title">The Quality <span class="gold">Promise</span></h2>
          <ul class="audit-list">
            <li><span class="audit-diamond">◆</span> Industry-grade equipment and commercial-strength products</li>
            <li><span class="audit-diamond">◆</span> Fully insured team — public liability and workers compensation</li>
            <li><span class="audit-diamond">◆</span> Same team, consistent standard — no rotating agency staff</li>
          </ul>
        </div>
        <div class="audit-receives">
          <h3>Every Clean Includes:</h3>
          <ul>
            <li>✔ Pre-clean brief and scope confirmation</li>
            <li>✔ Trained, vetted, and insured cleaners</li>
            <li>✔ Before-and-after walkthrough on request</li>
            <li>✔ Re-clean guarantee if not satisfied</li>
            <li>✔ Integrated with building FM if required</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT CTA STRIP -->
  <section class="cta-strip">
    <div class="section-container cta-strip-inner">
      <h2>Ready to book a clean?</h2>
      <p>Get a quote within 24 hours. No obligation.</p>
      <a href="index.html#contact" class="btn-primary">Book a Clean →</a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <div class="footer-logo">
          <img src="Images/JKFM Initials.png" alt="JKFM" class="footer-logo-img" />
          <div>
            <span class="footer-brand-name">JK Facilities Management</span>
            <span class="footer-brand-sub">Enhancing communities, one property at a time.</span>
          </div>
        </div>
      </div>
      <div class="footer-links">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html">Facilities Management</a></li>
          <li><a href="cleaning.html">Cleaning Services</a></li>
          <li><a href="index.html#process">Our Process</a></li>
          <li><a href="index.html#contact">Request a Quote</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Company</h4>
        <ul>
          <li><a href="index.html#problem">The Problem We Solve</a></li>
          <li><a href="services.html">How We Work</a></li>
          <li><a href="index.html#contact">Contact</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Contact</h4>
        <ul>
          <li>Karan@jkfm.co</li>
          <li>0459 361 650</li>
          <li>www.jkfm.co</li>
          <li>Available 24/7</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 JK Facilities Management. All rights reserved. | Risk-Led Oversight | Contractor Accountability | Clear Reporting</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

**Step 2: Verify in browser**
Open cleaning.html — check:
- Nav loads correctly, Cleaning link is active
- 8 cleaning service cards with bullet point detail
- 3-step process visible
- Quality Promise section visible
- CTA strip links to index.html#contact
- Footer shows Initials PNG

---

## Task 5: Add CSS for new components

**Files:**
- Modify: `style.css`

**Step 1: Add styles for new elements**

Append to the end of `style.css`:

```css
/* ============================================================
   SUBPAGE STYLES
============================================================ */

/* Hero variant for subpages — slightly shorter than homepage hero */
.hero-subpage { min-height: 60vh; padding: 8rem 2rem 4rem; }

/* Nav active link */
.nav-active { color: var(--gold) !important; }

/* Services detail cards */
.service-card-detail { text-align: left; }
.service-detail-list {
  margin-top: 0.75rem;
  padding-left: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.service-detail-list li {
  font-size: 0.85rem;
  color: var(--text-muted, #555);
  padding-left: 1rem;
  position: relative;
}
.service-detail-list li::before {
  content: '—';
  position: absolute;
  left: 0;
  color: var(--gold);
}

/* Why JKFM section */
.why-section { padding: 5rem 2rem; background: #f8f8f6; }
.why-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
}
.why-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
}
.why-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.why-card h3 { font-family: 'Montserrat', sans-serif; font-weight: 700; margin-bottom: 0.75rem; }
@media (max-width: 768px) {
  .why-grid { grid-template-columns: 1fr; }
}

/* CTA Strip */
.cta-strip {
  background: var(--dark-green, #1B4332);
  padding: 4rem 2rem;
  text-align: center;
}
.cta-strip-inner h2 {
  color: white;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.cta-strip-inner p {
  color: rgba(255,255,255,0.75);
  margin-bottom: 1.5rem;
}

/* 3-step process grid variant */
.process-grid-3 { grid-template-columns: 1fr auto 1fr auto 1fr; }

/* Section CTA center */
.section-cta-center { text-align: center; margin-top: 2.5rem; }
```

**Step 2: Verify in browser**
- Open services.html and cleaning.html
- Check cards have bullet lists with gold dash
- Why JKFM cards display in 3 columns
- CTA strip shows dark green background with white text
- Mobile: why-grid stacks to 1 column

---

## Done Checklist

- [ ] index.html — tagline removed from nav
- [ ] index.html — nav links updated to services.html and cleaning.html
- [ ] index.html — footer SVG replaced with JKFM Initials.png
- [ ] index.html — teaser CTA buttons added to services and cleaning sections
- [ ] style.css — Playfair Display applied to .logo-name
- [ ] style.css — footer-logo-img sized correctly
- [ ] style.css — subpage styles appended
- [ ] services.html — created and verified in browser
- [ ] cleaning.html — created and verified in browser
- [ ] All nav links work correctly across all 3 pages
