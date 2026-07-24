/* ================================================================
   JKFM Website — JavaScript
   Mobile nav, FAQ accordion, contact form, smooth scroll
================================================================ */

document.addEventListener('DOMContentLoaded', function () {

  // ── Mobile Nav Toggle ──────────────────────────────────────────
  const navToggle = document.getElementById('navToggle');
  const navMobile = document.getElementById('navMobile');

  if (navToggle && navMobile) {
    navToggle.addEventListener('click', function () {
      const isOpen = navMobile.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      navToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
    });

    // Close mobile menu when a link is clicked
    navMobile.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navMobile.classList.remove('open');
        navToggle.classList.remove('open');
      });
    });
  }

  // ── FAQ Accordion ──────────────────────────────────────────────
  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      // Close all other FAQ items
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove('open');
          openItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle current item
      item.classList.toggle('open', !isOpen);
      btn.setAttribute('aria-expanded', String(!isOpen));
    });
  });

  // ── Contact Form (Netlify Forms) ───────────────────────────────
  const form = document.querySelector('form[name="contact"]');
  const formStatus = document.getElementById('formStatus');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const btn = form.querySelector('.form-btn');
      const originalText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      const formData = new FormData(form);

      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(formData).toString()
      })
        .then(function (response) {
          if (response.ok) {
            formStatus.textContent = 'Thank you! Your request has been sent. We\'ll be in touch shortly.';
            formStatus.className = 'form-status form-status--success';
            form.reset();
          } else {
            throw new Error('Form submission failed');
          }
        })
        .catch(function () {
          formStatus.textContent = 'Something went wrong. Please call us on 0459 361 650 or email enquiries@jkfacilitiesmanagement.com.au.';
          formStatus.className = 'form-status form-status--error';
        })
        .finally(function () {
          btn.textContent = originalText;
          btn.disabled = false;
        });
    });
  }

  // ── Smooth Scroll for Anchor Links ─────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var navEl = document.querySelector('.nav');
        var navHeight = navEl ? navEl.offsetHeight : 0;
        var top = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // ── Nav Background on Scroll ───────────────────────────────────
  var nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });
  }

});
