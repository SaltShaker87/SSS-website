/* Draws the fellowship page from course.js. Edit course.js, not this file. */
(function () {
  "use strict";

  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var MONTHS_SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  function parseISODate(iso) {
    var match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || "").trim());
    if (!match) return null;
    var year = Number(match[1]);
    var month = Number(match[2]);
    var day = Number(match[3]);
    var date = new Date(year, month - 1, day);
    if (date.getFullYear() !== year || date.getMonth() !== month - 1 || date.getDate() !== day) return null;
    return date;
  }

  function startOfDay(date) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate());
  }

  function sameDay(a, b) {
    return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
  }

  function esc(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function safeUrl(url) {
    var cleaned = String(url || "").trim();
    if (/^https?:\/\/[^\s"'<>\\]+$/i.test(cleaned)) return cleaned;
    if (/^(?:\.\/)?files\/[A-Za-z0-9._~/-]+$/.test(cleaned) && cleaned.indexOf("..") === -1) return cleaned;
    return "";
  }

  function isExternal(url) {
    return /^https?:\/\//i.test(url);
  }

  function list(value) {
    if (value == null || value === "") return [];
    var source = Array.isArray(value) ? value : [value];
    var out = [];
    for (var i = 0; i < source.length; i++) {
      if (source[i] != null && source[i] !== "") out.push(source[i]);
    }
    return out;
  }

  function linkify(text) {
    var source = String(text == null ? "" : text);
    var pattern = /https?:\/\/[^\s<]+/g;
    var html = "";
    var last = 0;
    var match;
    while ((match = pattern.exec(source))) {
      html += esc(source.slice(last, match.index));
      var raw = match[0];
      var url = raw.replace(/[),.;:]+$/, "");
      var tail = raw.slice(url.length);
      var safe = safeUrl(url);
      if (safe && isExternal(safe)) {
        html += '<a href="' + esc(safe) + '" target="_blank" rel="noopener noreferrer">' + esc(safe) + '<span class="sr-only"> (opens in a new tab)</span></a>';
      } else {
        html += esc(raw);
        tail = "";
      }
      html += esc(tail);
      last = match.index + raw.length;
    }
    html += esc(source.slice(last));
    return html;
  }

  function paragraphs(text) {
    var blocks = String(text).split(/\n\s*\n/);
    var html = "";
    for (var i = 0; i < blocks.length; i++) {
      var trimmed = blocks[i].trim();
      if (!trimmed) continue;
      html += "<p>" + linkify(trimmed).replace(/\n/g, "<br>") + "</p>";
    }
    return html;
  }

  function linkedTitle(item, fallback) {
    if (typeof item === "string") return "<p>" + linkify(item) + "</p>";
    var title = item.title || item.label || fallback || "Link";
    var url = item.url || "";
    var note = item.note || "";
    var safe = url ? safeUrl(url) : "";
    var head;
    if (!url) {
      head = esc(title);
    } else if (!safe) {
      head = esc(title) + ' <span class="note">Link not shown. It should start with https://</span>';
    } else if (isExternal(safe)) {
      head = '<a href="' + esc(safe) + '" target="_blank" rel="noopener noreferrer">' + esc(title) + '<span class="sr-only"> (opens in a new tab)</span></a>';
    } else {
      head = '<a href="' + esc(safe) + '" target="_blank" rel="noopener noreferrer">' + esc(title) + "</a>";
    }
    return "<p>" + head + "</p>" + (note ? '<p class="note">' + linkify(note) + "</p>" : "");
  }

  function readingList(items) {
    var html = '<ul class="reading-list">';
    for (var i = 0; i < items.length; i++) html += "<li class=\"reading\">" + linkedTitle(items[i], "Reading") + "</li>";
    return html + "</ul>";
  }

  function fileList(items) {
    var html = '<ul class="file-list">';
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var file = typeof item === "string" ? item : (item.file || item.url || "");
      var label = typeof item === "string"
        ? (String(item).split("/").pop() || "File")
        : (item.label || item.title || String(file).split("/").pop() || "File");
      var safe = safeUrl(file);
      if (!safe) {
        html += '<li><span class="note">' + esc(label) + " — add a file in the files folder, or a link that starts with https://</span></li>";
        continue;
      }
      html += '<li><a class="btn btn-sm" href="' + esc(safe) + '" target="_blank" rel="noopener noreferrer"><span class="pix" data-pix="floppy"></span>' + esc(label) + '<span class="sr-only"> (opens in a new tab)</span></a></li>';
    }
    return html + "</ul>";
  }

  function assignmentList(items) {
    var html = "";
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var fellow = "Fellow";
      var questions = [];
      if (typeof item === "string") {
        questions = [item];
      } else {
        fellow = item.fellow || item.name || "Fellow";
        questions = list(item.questions != null ? item.questions : item.question);
      }
      html += '<div class="assign"><h4 class="fellow-name">' + esc(fellow) + "</h4>";
      if (questions.length) {
        html += "<ol>";
        for (var q = 0; q < questions.length; q++) html += "<li>" + linkify(questions[q]) + "</li>";
        html += "</ol>";
      }
      html += "</div>";
    }
    return html;
  }

  function section(heading, body) {
    if (!body) return "";
    return '<section class="part"><h3>' + heading + "</h3>" + body + "</section>";
  }

  function plural(count, singular, pluralLabel) {
    return count === 1 ? singular : pluralLabel;
  }

  function hasDetails(session) {
    if (!session || session.break) return false;
    return !!(
      (session.overview && String(session.overview).trim()) ||
      list(session.readings).length ||
      list(session.optional).length ||
      list(session.supplemental).length ||
      list(session.assignments).length ||
      (session.wrapUp && String(session.wrapUp).trim()) ||
      list(session.references).length ||
      list(session.files).length
    );
  }

  function whenOf(session) {
    var date = parseISODate(session.date);
    if (!date) {
      if (/^\s*tbd\s*$/i.test(String(session.date || ""))) {
        return { dow: "Date", md: "TBD", long: "Date to be announced" };
      }
      var raw = session.date ? String(session.date) : "Date needed";
      return { dow: "Date", md: raw, long: raw };
    }
    return {
      dow: DAYS[date.getDay()],
      md: MONTHS_SHORT[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear(),
      long: DAYS[date.getDay()] + ", " + MONTHS[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear()
    };
  }

  // Dated sessions go in date order. A session without a real date ("TBD")
  // stays right after the session above it in course.js.
  function sortSessions(sessions) {
    var keyed = [];
    var lastTime = -8640000000000000;
    for (var i = 0; i < sessions.length; i++) {
      var date = parseISODate(sessions[i].date);
      if (date) lastTime = date.getTime();
      keyed.push({ session: sessions[i], time: lastTime, undated: date ? 0 : 1, index: i });
    }
    keyed.sort(function (a, b) {
      return (a.time - b.time) || (a.undated - b.undated) || (a.index - b.index);
    });
    var out = [];
    for (var k = 0; k < keyed.length; k++) out.push(keyed[k].session);
    return out;
  }

  function withIds(sessions) {
    var sorted = sortSessions(sessions);
    var counts = {};
    var items = [];
    for (var i = 0; i < sorted.length; i++) {
      var session = sorted[i];
      var base = "s-" + (session.date ? String(session.date).trim() : "undated");
      var id = counts[base] ? base + "-" + counts[base] : base;
      counts[base] = (counts[base] || 0) + 1;
      items.push({ session: session, id: id, when: whenOf(session), date: parseISODate(session.date) });
    }
    return items;
  }

  function findNext(items, today) {
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      if (item.session.break || !item.date) continue;
      if (item.date < today) continue;
      return item;
    }
    return null;
  }

  function pill(label) {
    return '<span class="pill">' + esc(label) + "</span>";
  }

  function renderSchedule(items, today, nextItem) {
    var html = "";
    if (nextItem) {
      var jump = sameDay(nextItem.date, today) ? "Jump to today’s session" : "Jump to the next session";
      html += '<p class="now-link"><a href="#' + esc(nextItem.id) + '">' + jump + "</a></p>";
    }
    html += '<ol class="sched">';
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var session = item.session;
      var isBreak = !!session.break;
      var isPast = !isBreak && item.date && item.date < today;
      var isNext = nextItem && item.id === nextItem.id;
      var isToday = item.date && sameDay(item.date, today);
      var classes = isBreak ? "is-break" : (isPast ? "is-past" : (isNext ? "is-next" : "is-upcoming"));
      if (isToday) classes += " is-today";
      var name = session.title ? String(session.title) : "Session";
      var badge = "";
      if (isNext) badge = pill(isToday ? "Today" : "Up next");
      else if (isPast) badge = '<span class="pill past">Past</span>';
      else if (isBreak && isToday) badge = pill("Today");
      var speaker = !isBreak && session.speaker ? '<span class="sched-speaker">' + esc(session.speaker) + "</span>" : "";
      html += '<li><a class="' + classes + '" href="#' + esc(item.id) + '">' +
        '<span class="sched-when"><span class="dow">' + esc(item.when.dow) + '</span><span class="md">' + esc(item.when.md) + "</span></span>" +
        '<span class="sched-main"><span class="sched-title">' + badge + '<span class="sched-name">' + esc(name) + "</span></span>" +
        speaker +
        "</span></a></li>";
    }
    html += "</ol>";
    return html;
  }

  function renderSessions(items, today, nextItem) {
    var html = "";
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var session = item.session;
      if (session.break) {
        var breakToday = item.date && sameDay(item.date, today);
        html += '<aside class="break-banner' + (breakToday ? " is-today" : "") + '" id="' + esc(item.id) + '" tabindex="-1">' +
          '<p class="break-date">' + (breakToday ? pill("Today") : "") + esc(item.when.long) + "</p>" +
          '<p class="break-title">' + esc(session.title || "No session") + "</p>" +
          "</aside>";
        continue;
      }

      var isPast = item.date && item.date < today;
      var isNext = nextItem && item.id === nextItem.id;
      var isToday = item.date && sameDay(item.date, today);
      var classes = "window session " + (isPast ? "is-past" : (isNext ? "is-next" : "is-upcoming"));
      var name = session.title ? String(session.title) : "Session";
      var speaker = session.speaker ? '<p class="session-speaker">' + esc(session.speaker) + "</p>" : "";
      var badge = isNext ? pill(isToday ? "Today" : "Up next") : (isPast ? '<span class="pill past">Past</span>' : "");
      var optional = list(session.optional).concat(list(session.supplemental));
      var readings = list(session.readings);
      var references = list(session.references);
      var files = list(session.files);
      var assignments = list(session.assignments);
      var body = "";

      if (session.overview && String(session.overview).trim()) {
        body += section("Overview", '<div class="overview">' + paragraphs(session.overview) + "</div>");
      }
      if (readings.length) body += section(plural(readings.length, "Main reading", "Main readings"), readingList(readings));
      if (optional.length) body += section(plural(optional.length, "Optional reading", "Optional readings"), readingList(optional));
      if (assignments.length) body += section(plural(assignments.length, "Assignment", "Assignments"), assignmentList(assignments));
      if (session.wrapUp && String(session.wrapUp).trim()) {
        body += section("Wrap-up question", '<div class="wrapup"><p>' + linkify(String(session.wrapUp).trim()) + "</p></div>");
      }
      if (references.length) {
        body += section(plural(references.length, "Other article referenced", "Other articles referenced"), readingList(references));
      }
      if (files.length) body += section(plural(files.length, "File", "Files"), fileList(files));
      if (!hasDetails(session)) body += '<p class="notice soon">Details coming soon.</p>';

      html += '<article class="' + classes + '" id="' + esc(item.id) + '" tabindex="-1">' +
        '<div class="titlebar' + (isPast ? " inactive" : "") + '">' +
        '<span class="pix t-icon" data-pix="notepad"></span>' +
        '<span class="t-text">' + esc(item.when.md) + "</span>" +
        '<span class="t-btns" aria-hidden="true"><span class="t-btn t-min"></span><span class="t-btn t-max"></span></span>' +
        "</div>" +
        '<details class="win-body session-toggle">' +
        '<summary class="session-summary">' +
        '<p class="session-when">' + badge + esc(item.when.long) + "</p>" +
        "<h2>" + esc(name) + "</h2>" +
        speaker +
        '<span class="toggle-hint" aria-hidden="true"></span>' +
        "</summary>" +
        '<div class="session-body">' +
        body +
        '<p class="jump-back"><a href="#schedule">Back to schedule</a></p>' +
        "</div></details></article>";
    }
    return html;
  }

  function renderCourse(course, today) {
    var day = startOfDay(today || new Date());
    var sessions = course && Array.isArray(course.sessions) ? course.sessions : [];
    var items = withIds(sessions);
    var nextItem = findNext(items, day);
    return {
      nextId: nextItem ? nextItem.id : null,
      scheduleHtml: sessions.length ? renderSchedule(items, day, nextItem) : '<p class="notice soon">No sessions yet. Add one in course.js.</p>',
      sessionsHtml: renderSessions(items, day, nextItem)
    };
  }

  function showProblem() {
    var schedule = document.getElementById("schedule-list");
    var sessions = document.getElementById("session-list");
    var message = '<p class="notice soon">This page could not read course.js. Open that file and check for a missing comma or a curly quote, then save and refresh.</p>';
    if (schedule) schedule.innerHTML = message;
    if (sessions) sessions.innerHTML = "";
  }

  function mount() {
    var schedule = document.getElementById("schedule-list");
    var sessions = document.getElementById("session-list");
    if (!schedule || !sessions) return;
    if (typeof HPEF_COURSE === "undefined" || !HPEF_COURSE || !Array.isArray(HPEF_COURSE.sessions)) {
      showProblem();
      return;
    }
    var course = HPEF_COURSE;
    if (course.title) {
      var heading = document.getElementById("course-title");
      if (heading) heading.textContent = course.title;
      document.title = course.title;
    }
    if (course.subtitle) {
      var sub = document.getElementById("course-subtitle");
      if (sub) sub.textContent = course.subtitle;
    }
    var rendered;
    try {
      rendered = renderCourse(course, new Date());
    } catch (err) {
      showProblem();
      return;
    }
    schedule.innerHTML = rendered.scheduleHtml;
    sessions.innerHTML = rendered.sessionsHtml;
    if (window.SSS && window.SSS.paintIcons) {
      window.SSS.paintIcons(schedule);
      window.SSS.paintIcons(sessions);
    }

    // Open the session a link points to (schedule links, "Jump to the next session", shared URLs).
    function openSession(id) {
      if (!id) return;
      var target = document.getElementById(id);
      if (!target || !sessions.contains(target)) return;
      var details = target.querySelector("details.session-toggle");
      if (details) details.open = true;
      target.scrollIntoView();
    }
    schedule.addEventListener("click", function (event) {
      var link = event.target.closest ? event.target.closest('a[href^="#"]') : null;
      if (link) openSession(link.getAttribute("href").slice(1));
    });
    window.addEventListener("hashchange", function () {
      openSession(decodeURIComponent(location.hash.slice(1)));
    });
    if (location.hash) openSession(decodeURIComponent(location.hash.slice(1)));
  }

  if (typeof document !== "undefined") {
    if (document.getElementById("schedule-list")) mount();
    else document.addEventListener("DOMContentLoaded", mount);
  }

  var api = { parseISODate: parseISODate, renderCourse: renderCourse };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  if (typeof window !== "undefined") window.HPEF_PAGE = api;
})();
