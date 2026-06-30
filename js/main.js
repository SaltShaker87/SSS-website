/* === Salt Shaker Studio — Main JavaScript === */
/* Progressive enhancement only — site works without JS */

(function () {
    'use strict';

    /* --- Mobile Nav Toggle --- */
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            const isOpen = navMenu.classList.toggle('nav--open');
            navToggle.setAttribute('aria-expanded', isOpen);
        });

        // Close nav when a link is clicked (mobile)
        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('nav--open');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    /* --- Smooth Scroll for Nav Links --- */
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;
            var target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* --- Active Section Highlighting --- */
    var sections = document.querySelectorAll('section[id]');
    var navLinks = document.querySelectorAll('.nav-links a[href^="#"]');

    if (sections.length && navLinks.length) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var id = entry.target.getAttribute('id');
                    navLinks.forEach(function (link) {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === '#' + id) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, {
            rootMargin: '-20% 0px -70% 0px',
            threshold: 0
        });

        sections.forEach(function (section) {
            observer.observe(section);
        });
    }

    /* --- Faux Hit Counter --- */
    var hitCounter = document.getElementById('hit-counter');
    if (hitCounter) {
        var visits = parseInt(localStorage.getItem('sss-visits') || '0', 10);
        visits++;
        localStorage.setItem('sss-visits', visits.toString());
        hitCounter.textContent = visits.toString().padStart(8, '0');
    }

    /* --- Konami Code Easter Egg --- */
    var konamiCode = [
        'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
        'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
        'b', 'a'
    ];
    var konamiIndex = 0;

    document.addEventListener('keydown', function (e) {
        if (e.key === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                activateKonamiMode();
                konamiIndex = 0;
            }
        } else {
            konamiIndex = 0;
        }
    });

    function activateKonamiMode() {
        document.body.classList.toggle('konami-mode');

        // Show a retro alert
        var overlay = document.createElement('div');
        overlay.className = 'konami-alert';
        overlay.innerHTML =
            '<div class="retro-window" style="max-width:400px;margin:20vh auto;">' +
            '  <div class="retro-window__titlebar">' +
            '    <span class="retro-window__title">Secret!</span>' +
            '    <div class="retro-window__controls">' +
            '      <span class="retro-window__control">&times;</span>' +
            '    </div>' +
            '  </div>' +
            '  <div class="retro-window__body" style="text-align:center;padding:24px;">' +
            '    <p style="font-family:var(--font-pixel);font-size:24px;margin-bottom:16px;">' +
            '      &#127775; KONAMI CODE ACTIVATED! &#127775;' +
            '    </p>' +
            '    <p style="font-size:14px;margin-bottom:16px;">You found the secret! Enjoy the extra retro vibes.</p>' +
            '    <button class="retro-button konami-close">OK</button>' +
            '  </div>' +
            '</div>';

        overlay.style.cssText =
            'position:fixed;top:0;left:0;right:0;bottom:0;' +
            'background:rgba(0,0,0,0.6);z-index:9999;padding:16px;';

        document.body.appendChild(overlay);

        overlay.querySelector('.konami-close').addEventListener('click', function () {
            overlay.remove();
        });

        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) overlay.remove();
        });
    }

    /* --- Window Close Button Fun --- */
    document.querySelectorAll('.retro-window__control').forEach(function (btn) {
        if (btn.textContent.trim() === '×') {
            btn.style.cursor = 'pointer';
            btn.addEventListener('click', function () {
                var win = this.closest('.retro-window');
                if (!win) return;

                // "Not responding" dialog
                var dialog = document.createElement('div');
                dialog.style.cssText =
                    'position:fixed;top:0;left:0;right:0;bottom:0;' +
                    'background:rgba(0,0,0,0.4);z-index:9999;padding:16px;' +
                    'display:flex;align-items:center;justify-content:center;';
                dialog.innerHTML =
                    '<div class="retro-window" style="max-width:340px;width:100%;">' +
                    '  <div class="retro-window__titlebar">' +
                    '    <span class="retro-window__title">Salt Shaker Studio</span>' +
                    '    <div class="retro-window__controls">' +
                    '      <span class="retro-window__control">&times;</span>' +
                    '    </div>' +
                    '  </div>' +
                    '  <div class="retro-window__body" style="text-align:center;padding:20px;">' +
                    '    <p style="margin-bottom:16px;">&#9888; This program is not responding.</p>' +
                    '    <p style="font-size:13px;margin-bottom:16px;color:var(--text-secondary);">If you close it, you might lose unsaved data.</p>' +
                    '    <div style="display:flex;gap:8px;justify-content:center;">' +
                    '      <button class="retro-button dialog-close">End Now</button>' +
                    '      <button class="retro-button dialog-cancel">Cancel</button>' +
                    '    </div>' +
                    '  </div>' +
                    '</div>';

                document.body.appendChild(dialog);

                dialog.querySelector('.dialog-cancel').addEventListener('click', function () {
                    dialog.remove();
                });

                dialog.querySelector('.dialog-close').addEventListener('click', function () {
                    dialog.remove();
                });

                dialog.addEventListener('click', function (e) {
                    if (e.target === dialog) dialog.remove();
                });
            });
        }
    });

/* --- Rotating Taglines --- */
(function () {
    const tagline = document.getElementById('rotating-tagline');
    if (!tagline) return;

    const taglines = [
        "Because learning by osmosis is still a myth",
        "Because your brain doesn't have a save button",
        "Because staring at something isn't the same as understanding it",
        "Because hope is not a study strategy",
        "Because your brain doesn't run on Wi-Fi",
        "Because 'I'll figure it out later' is a bold strategy",
        "Because your brain isn't a hard drive",
        "Because pretending to pay attention doesn't work",
        "Because watching someone else do it doesn't count",
        "Because 'follow along on the slides' is a nightmare",
        "Because real learning doesn't come from a deck",
        "Because your brain doesn't have a download button",
        "Because watching slides isn't learning",
        "Because brains aren't USB ports",
        "Because someone reading slides to you? Not a thing.",
    ];

    let currentIndex = 0;
    let interval;
    let isPaused = false;

    function showNextTagline() {
        tagline.classList.add('fading');

        setTimeout(() => {
            currentIndex = (currentIndex + 1) % taglines.length;
            tagline.textContent = taglines[currentIndex];
            tagline.classList.remove('fading');
        }, 300);
    }

    interval = setInterval(showNextTagline, 10000);

    /* Pause when hero is out of view */
    const heroSection = document.querySelector('.hero');
    if (heroSection && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    if (!isPaused) {
                        tagline.style.opacity = '1';
                        tagline.classList.remove('fading');
                        interval = setInterval(showNextTagline, 10000);
                    }
                } else {
                    isPaused = true;
                    clearInterval(interval);
                    tagline.style.opacity = '1';
                    tagline.classList.remove('fading');
                }
            });
        }, { threshold: 0.3 });

        observer.observe(heroSection);
    }

    /* Pause on hover */
    tagline.addEventListener('mouseenter', () => {
        isPaused = true;
        clearInterval(interval);
        tagline.style.opacity = '1';
        tagline.classList.remove('fading');
    });

    tagline.addEventListener('mouseleave', () => {
        isPaused = false;
        interval = setInterval(showNextTagline, 10000);
    });
})();
