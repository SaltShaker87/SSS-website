/* =====================================================================
   Salt Shaker Studio: shared behaviour for every page.
   Each block checks that its elements exist, so pages load only what they use.
   ===================================================================== */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Pixel icons ----------
     16x16 grids drawn as SVG, so every visitor sees the same icon
     (emoji look different on Windows, Mac, iPhone and Android).
     Use: <span class="pix" data-pix="floppy"></span> */
  var PAL = {
    k: '#000', w: '#fff', g: '#c0c0c0', d: '#808080', y: '#ffd23f', b: '#000080',
    l: '#1084d0', t: '#0d7c7c', r: '#c43a2f', o: '#b86a00', n: '#1ca31c', s: '#f1c27d'
  };
  var E = '................';
  var ICONS = {
    shaker: [E, '.....kkkkkk.....', '....kggwgggk....', '....kgkgkgdk....', '....kgggggdk....', '....kkkkkkkk....',
      '...kwwwwwwwlk...', '...kwlwwwwwlk...', '...kwlwyywwlk...', '...kwwyyyywlk...', '...kwyyyyyylk...',
      '...kwyyyyyylk...', '...kwyyyyyylk...', '...kdyyyyyydk...', '....kkkkkkkk....', E],
    floppy: [E, '.kkkkkkkkkkkkkk.', '.kbbgggggkggbbk.', '.kbbgggggkggbbk.', '.kbbgggggkggbbk.', '.kbbggggggggbbk.',
      '.kbbbbbbbbbbbbk.', '.kbwwwwwwwwwwbk.', '.kbwddddddddwbk.', '.kbwwwwwwwwwwbk.', '.kbwddddddddwbk.',
      '.kbwwwwwwwwwwbk.', '.kbwwwwwwwwwwbk.', '.kbbbbbbbbbbbbk.', '.kkkkkkkkkkkkkk.', E],
    notepad: [E, '..kkkkkkkkkkkk..', '..kllllllllllk..', '..kwwwwwwwwwwk..', '..kwddddddwwwk..', '..kwwwwwwwwwwk..',
      '..kwddddddddwk..', '..kwwwwwwwwwwk..', '..kwddddddddwk..', '..kwwwwwwwwwwk..', '..kwdddddwwwwk..',
      '..kwwwwwwwwwwk..', '..kwwwwwwwwwwk..', '..kkkkkkkkkkkk..', E, E],
    folder: [E, E, E, '..kkkkk.........', '.kyyyyyk........', '.kyyyyyykkkkkkk.', '.kwwwwwwwwwwwwk.',
      '.kyyyyyyyyyyyyk.', '.kyyyyyyyyyyyyk.', '.kyyyyyyyyyyyyk.', '.kyyyyyyyyyyyyk.', '.kyyyyyyyyyyyyk.',
      '.kyyyyyyyyyyyyk.', '.kooooooooooook.', '.kkkkkkkkkkkkkk.', E],
    person: [E, '.....kkkkkk.....', '....kssssssk....', '....kskssksk....', '....kssssssk....', '....ksskkssk....',
      '.....kssssk.....', '......kssk......', '...kkwwllwwkk...', '..kwwwwllwwwwk..', '.kwwwwwllwwwwwk.',
      '.kwwwwwllwwwwwk.', '.kwwwwwllwwwwwk.', '.kkkkkkkkkkkkkk.', E, E],
    chat: [E, '..kkkkkkkkkkkk..', '.kwwwwwwwwwwwwk.', '.kwddddddddddwk.', '.kwwwwwwwwwwwwk.', '.kwddddddwwwwwk.',
      '.kwwwwwwwwwwwwk.', '.kwdddddddddwwk.', '.kwwwwwwwwwwwwk.', '..kkkwwkkkkkkk..', '....kwk.........',
      '....kk..........', E, E, E, E],
    calendar: [E, '.kkkkkkkkkkkkkk.', '.krrrrrrrrrrrrk.', '.krrrrrrrrrrrrk.', '.kwwwwwwwwwwwwk.', '.kwkwkwkwkwkwwk.',
      '.kwwwwwwwwwwwwk.', '.kwkwkwkwkwkwwk.', '.kwwwwwwwwwwwwk.', '.kwkwkwkbbbwwwk.', '.kwwwwwwbbbwwwk.',
      '.kwwwwwwwwwwwwk.', '.kkkkkkkkkkkkkk.', E, E, E],
    computer: ['..kkkkkkkkkkkk..', '..kggggggggggk..', '..kgkkkkkkkkgk..', '..kgkttttttkgk..', '..kgktyytttkgk..',
      '..kgkttttttkgk..', '..kgkkkkkkkkgk..', '..kggggggggggk..', '..kgggggggnggk..', '..kkkkkkkkkkkk..',
      '......kddk......', '....kkkkkkkk....', '...kggggggggk...', '...kkkkkkkkkk...', E, E],
    bulb: [E, '......kkkk......', '.....kyyyyk.....', '....kyywyyyk....', '....kywyyyyk....', '....kyyyyyyk....',
      '....kyyyyyyk....', '.....kyyyyk.....', '......kyyk......', '......kddk......', '......kggk......',
      '......kddk......', '.......kk.......', E, E, E],
    mail: [E, E, E, '.kkkkkkkkkkkkkk.', '.kkwwwwwwwwwwkk.', '.kwkwwwwwwwwkwk.', '.kwwkwwwwwwkwwk.',
      '.kwwwkwwwwkwwwk.', '.kwwwwkkkkwwwwk.', '.kwwwwwwwwwwwwk.', '.kwwwwwwwwwwwwk.', '.kkkkkkkkkkkkkk.', E, E, E, E],
    cup: [E, '......w..w......', '.....w..w.......', '......w..w......', E, '..kkkkkkkkkk....',
      '..kwwwwwwwwkkk..', '..kwoooooowk.k..', '..kwoooooowk.k..', '..kwoooooowkkk..', '..kwwwwwwwwk....',
      '...kwwwwwwk.....', '....kkkkkk......', '.kkkkkkkkkkkk...', E, E],
    globe: [E, '.....kkkkkk.....', '...kkllnnllkk...', '..klllnnnlllk...', '.kllnnnnnllllk..', '.klllnnnlllnlk..',
      'kllllnnllllnnlk.', 'klllllnllllnnlk.', 'kllllllllnnnllk.', 'klllllllnnnnllk.', '.klllllllnnnlk..',
      '.kllllllllnllk..', '..klllllllllk...', '...kklllllkk....', '.....kkkkk......', E],
    play: [E, E, E, '......kk........', '......knk.......', '......knnk......', '......knnnk.....', '......knnnnk....',
      '......knnnnnk...', '......knnnnk....', '......knnnk.....', '......knnk......', '......knk.......',
      '......kk........', E, E]
  };

  function pixSvg(name) {
    var rows = ICONS[name];
    if (!rows) return '';
    var r = '';
    for (var y = 0; y < rows.length; y++) {
      for (var x = 0; x < rows[y].length; x++) {
        var c = rows[y][x];
        if (c !== '.') r += '<rect x="' + x + '" y="' + y + '" width="1" height="1" fill="' + PAL[c] + '"/>';
      }
    }
    return '<svg viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true" focusable="false">' + r + '</svg>';
  }
  function paintIcons(root) {
    var els = (root || document).querySelectorAll('[data-pix]');
    for (var i = 0; i < els.length; i++) els[i].innerHTML = pixSvg(els[i].getAttribute('data-pix'));
  }
  paintIcons();

  /* ---------- Email links ----------
     Assembled here so there is no @ in the HTML: Cloudflare would otherwise
     rewrite it into /cdn-cgi/l/email-protection, a 404 Google kept crawling. */
  var mails = document.querySelectorAll('a[data-email-user][data-email-domain]');
  for (var m = 0; m < mails.length; m++) {
    mails[m].setAttribute('href', 'mailto:' + mails[m].getAttribute('data-email-user') + '@' + mails[m].getAttribute('data-email-domain'));
  }

  /* ---------- Start menu ---------- */
  var startBtn = document.getElementById('startBtn');
  var startMenu = document.getElementById('startMenu');
  function setMenu(open) {
    if (!startMenu) return;
    startMenu.hidden = !open;
    startBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (startBtn && startMenu) {
    startBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      setMenu(startMenu.hidden);
      if (!startMenu.hidden) {
        var first = startMenu.querySelector('a');
        if (first) first.focus();
      }
    });
    document.addEventListener('click', function (e) { if (!startMenu.contains(e.target)) setMenu(false); });
    startMenu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !startMenu.hidden) { setMenu(false); startBtn.focus(); }
    });
  }

  /* ---------- Taskbar clock ---------- */
  var clock = document.getElementById('clock');
  function tickClock() {
    var d = new Date(), h = d.getHours(), mm = d.getMinutes();
    clock.textContent = (h % 12 || 12) + ':' + (mm < 10 ? '0' : '') + mm + ' ' + (h < 12 ? 'AM' : 'PM');
  }
  if (clock) { tickClock(); setInterval(tickClock, 30000); }

  /* ---------- Taskbar: highlight the section being read ---------- */
  var taskLinks = document.querySelectorAll('.task-links a[data-for]');
  if (taskLinks.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        for (var i = 0; i < taskLinks.length; i++) {
          taskLinks[i].classList.toggle('is-active', taskLinks[i].getAttribute('data-for') === entry.target.id);
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    for (var t = 0; t < taskLinks.length; t++) {
      var target = document.getElementById(taskLinks[t].getAttribute('data-for'));
      if (target) spy.observe(target);
    }
  }

  /* ---------- Visitor counter (this browser only) ---------- */
  var counter = document.getElementById('hit-counter');
  if (counter) {
    try {
      var visits = parseInt(localStorage.getItem('sss-visits') || '0', 10);
      if (counter.hasAttribute('data-increment')) {
        visits++;
        localStorage.setItem('sss-visits', String(visits));
      }
      counter.textContent = String(Math.max(visits, 1)).padStart(8, '0');
    } catch (err) {
      counter.textContent = '00000001';   /* private browsing / storage blocked */
    }
  }

  /* ---------- Dialog helper (easter eggs) ---------- */
  function dialog(title, bodyHtml, buttons) {
    var wrap = document.createElement('div');
    wrap.className = 'dialog-backdrop';
    wrap.innerHTML =
      '<div class="window" role="alertdialog" aria-modal="true" aria-label="' + title + '">' +
      '<div class="titlebar"><span class="pix t-icon" data-pix="shaker"></span><span class="t-text">' + title + '</span>' +
      '<span class="t-btns"><button type="button" class="t-btn t-close" aria-label="Close" data-close></button></span></div>' +
      '<div class="win-body">' + bodyHtml + '<div class="btn-row">' +
      buttons.map(function (b, i) {
        return '<button type="button" class="btn' + (i === 0 ? ' btn-primary' : '') + '" data-close>' + b + '</button>';
      }).join('') + '</div></div></div>';
    paintIcons(wrap);
    var previous = document.activeElement;
    function close() { wrap.remove(); if (previous && previous.focus) previous.focus(); }
    wrap.addEventListener('click', function (e) { if (e.target === wrap || e.target.hasAttribute('data-close')) close(); });
    wrap.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.body.appendChild(wrap);
    wrap.querySelector('.btn').focus();
  }

  /* Window close buttons: the program is, of course, not responding */
  var closers = document.querySelectorAll('.titlebar .t-close');
  for (var c = 0; c < closers.length; c++) {
    closers[c].addEventListener('click', function () {
      dialog('Salt Shaker Studio',
        '<p><b>This program is not responding.</b></p><p class="muted">If you close it, you might lose unsaved data.</p>',
        ['End Now', 'Cancel']);
    });
  }

  /* Konami code */
  var konami = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
  var kIndex = 0;
  document.addEventListener('keydown', function (e) {
    kIndex = (e.key === konami[kIndex]) ? kIndex + 1 : (e.key === konami[0] ? 1 : 0);
    if (kIndex === konami.length) {
      kIndex = 0;
      dialog('Secret!', '<p style="font:700 20px/1.3 var(--font-display)">KONAMI CODE ACTIVATED!</p><p>You found the secret. Enjoy the extra retro vibes.</p>', ['OK']);
    }
  });

  /* ---------- Screenshot slider (ABG and Scrubboard pages) ---------- */
  (function () {
    var root = document.getElementById('shotSlider');
    if (!root) return;
    var shots = root.querySelectorAll('.shot');
    var items = root.querySelectorAll('.shot-nav-item');
    var count = document.getElementById('shotCounter');
    var nav = document.getElementById('shotNav');
    if (!shots.length || shots.length !== items.length) return;

    var SLIDE_MS = 5000, TICK = 50, FADE_MS = 350;
    var index = 0, interval = null, elapsed = 0;
    var isPaused = false, isVisible = true, isAnimating = false, lockTimer = null;

    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function setFill(i, pct) {
      var fill = items[i].querySelector('.shot-progress-fill');
      if (fill) fill.style.width = pct + '%';
    }
    function goTo(n, moveFocus) {
      n = (n % shots.length + shots.length) % shots.length;
      if (isAnimating || n === index) return;
      isAnimating = true;
      if (lockTimer) clearTimeout(lockTimer);
      lockTimer = setTimeout(function () { isAnimating = false; }, FADE_MS);

      setFill(index, 0);
      shots[index].classList.remove('is-active');
      items[index].classList.remove('is-active');
      items[index].setAttribute('aria-selected', 'false');
      items[index].tabIndex = -1;

      index = n;
      elapsed = 0;
      shots[index].classList.add('is-active');
      items[index].classList.add('is-active');
      items[index].setAttribute('aria-selected', 'true');
      items[index].tabIndex = 0;
      setFill(index, 0);
      if (count) count.textContent = pad(index + 1) + ' / ' + pad(shots.length);
      if (moveFocus) items[index].focus();
    }
    function tick() {
      if (isPaused) return;
      elapsed += TICK;
      setFill(index, Math.min(100, elapsed / SLIDE_MS * 100));
      if (elapsed >= SLIDE_MS) goTo(index + 1);
    }
    function start() {
      if (reducedMotion || interval !== null) return;   /* never stack intervals */
      interval = setInterval(tick, TICK);
    }
    function stop() {
      if (interval !== null) { clearInterval(interval); interval = null; }
    }

    nav.addEventListener('click', function (e) {
      var btn = e.target.closest('.shot-nav-item');
      if (btn) goTo(parseInt(btn.getAttribute('data-i'), 10), false);
    });
    document.getElementById('shotPrev').addEventListener('click', function () { goTo(index - 1, false); });
    document.getElementById('shotNext').addEventListener('click', function () { goTo(index + 1, false); });
    nav.addEventListener('keydown', function (e) {
      var k = e.key;
      if (k === 'ArrowRight' || k === 'ArrowDown') goTo(index + 1, true);
      else if (k === 'ArrowLeft' || k === 'ArrowUp') goTo(index - 1, true);
      else if (k === 'Home') goTo(0, true);
      else if (k === 'End') goTo(shots.length - 1, true);
      else return;
      e.preventDefault();
    });
    root.addEventListener('mouseenter', function () { isPaused = true; });
    root.addEventListener('mouseleave', function () { isPaused = false; });
    root.addEventListener('focusin', function () { isPaused = true; });
    root.addEventListener('focusout', function () { isPaused = false; });
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop();
      else if (isVisible) start();
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        isVisible = entries[0].isIntersecting;
        if (isVisible) start(); else stop();
      }, { threshold: 0.3 }).observe(root);
    } else {
      start();
    }
  })();

  window.SSS = { paintIcons: paintIcons, reducedMotion: reducedMotion };
})();
