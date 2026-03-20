// ================================================================
// JKFM WEBSITE — JAVASCRIPT
// ================================================================

// ── 1. ANIMATE STAT NUMBERS ON SCROLL ──
function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');
  counters.forEach(counter => {
    const target = parseInt(counter.dataset.target, 10);
    const duration = 1800;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        counter.textContent = target;
        clearInterval(timer);
      } else {
        counter.textContent = Math.floor(current);
      }
    }, 16);
  });
}

// ── 2. INTERSECTION OBSERVER — animate service cards + trigger counters ──
const observerOptions = { threshold: 0.15 };

const cardObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger each card slightly
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, i * 80);
      cardObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('[data-animate]').forEach(el => {
  cardObserver.observe(el);
});

// Trigger counter animation when hero stats come into view
const heroStats = document.querySelector('.hero-stats');
let countersTriggered = false;
if (heroStats) {
  const statsObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting && !countersTriggered) {
      countersTriggered = true;
      animateCounters();
      statsObserver.disconnect();
    }
  }, { threshold: 0.5 });
  statsObserver.observe(heroStats);
}

// ── 3. MOBILE NAV TOGGLE ──
const navToggle = document.querySelector('.nav-toggle');
const navLinks  = document.querySelector('.nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.style.display === 'flex';
    navLinks.style.cssText = isOpen
      ? ''
      : 'display:flex;flex-direction:column;position:absolute;top:68px;left:0;right:0;background:rgba(13,31,22,0.98);padding:1.5rem 2rem;gap:1.2rem;border-bottom:1px solid rgba(201,168,76,0.2)';
  });
}

// Close mobile nav when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 900) navLinks.style.cssText = '';
  });
});

// ── 4. STICKY NAV — add shadow on scroll ──
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.nav-wrapper');
  if (window.scrollY > 30) {
    nav.style.boxShadow = '0 4px 30px rgba(0,0,0,0.3)';
  } else {
    nav.style.boxShadow = 'none';
  }
});

// ── 5. ACTIVE NAV LINK ON SCROLL ──
const sections  = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navAnchors.forEach(a => {
        a.style.color = a.getAttribute('href') === `#${id}`
          ? 'var(--gold)'
          : '';
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));

// ── 6. FAQ ACCORDION ──
function toggleFaq(btn) {
  const answer = btn.nextElementSibling;
  const isOpen = btn.classList.contains('open');

  // Close all
  document.querySelectorAll('.faq-q').forEach(q => {
    q.classList.remove('open');
    q.nextElementSibling.classList.remove('open');
  });

  // Open this one if it wasn't already open
  if (!isOpen) {
    btn.classList.add('open');
    answer.classList.add('open');
  }
}

// ── 7. CONTACT FORM HANDLER ──
function handleSubmit(e) {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  btn.textContent = 'Sending…';
  btn.disabled = true;

  // Simulate send (replace with real form submission endpoint)
  setTimeout(() => {
    btn.textContent = '✔ Request Sent!';
    btn.style.background = 'var(--green-mid)';
    setTimeout(() => {
      btn.textContent = 'Send Request →';
      btn.style.background = '';
      btn.disabled = false;
      e.target.reset();
    }, 3000);
  }, 1200);
}
