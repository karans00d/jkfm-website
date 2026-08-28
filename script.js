/* ============================================================
   JKFM website: 01 Swiss institutional
   One shared script. Vanilla JS only.
   1. FAQ clause toggles (accessible accordion)
   2. Enquiry form: Netlify Forms AJAX submit
   ============================================================ */

(function () {
  "use strict";

  /* ---------- 1. FAQ clause toggles ---------- */
  /* Answers ship visible in the markup so the content survives
     without JavaScript; collapsing is progressive enhancement. */

  var faqButtons = document.querySelectorAll(".faq-q");
  faqButtons.forEach(function (btn) {
    var target = document.getElementById(btn.getAttribute("aria-controls"));
    if (target) {
      target.hidden = true;
    }
    btn.setAttribute("aria-expanded", "false");
  });
  faqButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var answer = document.getElementById(btn.getAttribute("aria-controls"));
      btn.setAttribute("aria-expanded", expanded ? "false" : "true");
      if (answer) {
        answer.hidden = expanded;
      }
    });
  });

  /* ---------- 2. Enquiry form: Netlify Forms ---------- */

  var form = document.querySelector('form[name="contact"]');
  var formStatus = document.getElementById("formStatus");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var btn = form.querySelector('button[type="submit"]');
      var originalText = btn.textContent;
      btn.textContent = "Sending...";
      btn.disabled = true;

      var formData = new FormData(form);

      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(formData).toString()
      })
        .then(function (response) {
          if (response.ok) {
            formStatus.textContent =
              "Thank you. Your request has been sent and we will be in touch shortly.";
            formStatus.className = "form-status form-status--success";
            form.reset();
          } else {
            throw new Error("Form submission failed");
          }
        })
        .catch(function () {
          formStatus.textContent =
            "Something went wrong. Please call 0459 361 650 or email enquiries@jkfacilitiesmanagement.com.au.";
          formStatus.className = "form-status form-status--error";
        })
        .finally(function () {
          btn.textContent = originalText;
          btn.disabled = false;
        });
    });
  }
})();
