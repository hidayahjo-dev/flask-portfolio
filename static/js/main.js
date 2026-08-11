/**
 * Small, dependency-free UI polish. No framework needed for a page this
 * size - keeping it vanilla JS keeps the "modular, easy to extend" story
 * honest: add new behavior as another small function below, or split
 * into separate files under static/js/ as the site grows.
 */
document.addEventListener("DOMContentLoaded", () => {
  highlightActiveNavLink();
  collapseNavOnLinkClick();
});

/**
 * Adds an "active" style to the nav link matching whichever section is
 * currently in view, using IntersectionObserver (cheap, no scroll-event
 * math).
 */
function highlightActiveNavLink() {
  const sections = document.querySelectorAll("main [id]");
  const navLinks = document.querySelectorAll(".ide-tabs .nav-link");
  if (!sections.length || !navLinks.length) return;

  const linkFor = (id) =>
    [...navLinks].find((link) => link.getAttribute("href") === `#${id}`);

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const link = linkFor(entry.target.id);
        if (!link) return;
        link.classList.toggle("active", entry.isIntersecting);
      });
    },
    { rootMargin: "-40% 0px -50% 0px" }
  );

  sections.forEach((section) => observer.observe(section));
}

/** Closes the mobile navbar collapse after tapping an anchor link. */
function collapseNavOnLinkClick() {
  const navCollapse = document.getElementById("navMain");
  if (!navCollapse) return;

  navCollapse.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => {
      if (navCollapse.classList.contains("show") && window.bootstrap) {
        const bsCollapse = window.bootstrap.Collapse.getOrCreateInstance(navCollapse);
        bsCollapse.hide();
      }
    });
  });
}
