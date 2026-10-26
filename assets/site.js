(function () {
  // Remember language preference (per browser) and offer mobile nav toggle.
  var lang = document.documentElement.lang === 'he' ? 'he' : 'en';
  try { localStorage.setItem('pakram-lang', lang); } catch (e) {}

  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.mobile-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Keep the section anchor when switching language (e.g. #faculty -> /he/#faculty).
  document.querySelectorAll('.lang-tabs a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (location.hash) { a.href = a.getAttribute('href').split('#')[0] + location.hash; }
    });
  });
})();
