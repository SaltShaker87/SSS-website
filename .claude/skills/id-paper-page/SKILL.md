---
name: id-paper-page
description: Turn ONE landmark infectious-diseases paper into a Salt Shaker Studio page (hero video + scrollable summary with recreated charts) and append it to the papers index. Use when Arman pastes a filled input-template.md.
---

# ID Paper → Page pipeline (one paper per run)

## Golden rules (read first, obey always)
1. **Never invent numbers.** Every number on the page, in charts, or in the video must come from Arman's paste or the paper text he supplied. Each one is stored in `paper.json` with a `source_quote`.
2. **If a value is missing, flag it. Don't guess.** Write `"value": null, "status": "MISSING"` and list it in `QUESTIONS.md`. Do not estimate values by reading them off figure images.
3. **Everything in the MUST-INCLUDE block appears on the page**, either quoted or faithfully paraphrased.
4. **Recreate figures from data. Never copy figure images** from the paper (copyright). Always cite and link the source (PubMed + DOI).
5. **Medical accuracy:** keep the authors' framing (noninferior ≠ superior; HR/CI exactly as reported; primary vs secondary endpoint labeled). Add "Educational summary, not medical advice."
6. **One paper per run.** Do not touch other paper pages except the index entry.
7. **Never recreate shared files.** `papers/index.html`, `papers/paper-charts.js` and `sitemap.xml` already exist. Edit them in place (append a card, add a sitemap URL). Do not regenerate them from the templates.
8. **Keep the site wrapper.** Every page keeps the template's `<head>` (canonical, OpenGraph, favicon), skip link, `wrap narrow` container, footer, Start menu, taskbar and `/js/site.js` unchanged. Only the `{{…}}` placeholders and the content windows change.

## Files in this skill
- `templates/input-template.md`: what Arman pastes
- `templates/paper.schema.json`: the intermediate data contract
- `templates/paper-page.html`: page template in the site's style
- `templates/papers-index.html`: index page plus the card snippet to append
- `templates/paper-charts.js`: Chart.js renderer driven by paper.json
- `templates/video-storyboard.md`: scene script and voiceover template
- `templates/remotion/PaperVideo.tsx`: deterministic data-driven video
- `scripts/verify-paper.js`: the Step 3 verify gate

## Output layout (in the site repo; static HTML site, `css/site.css` at root)
Papers live inside the **Seasoning Lab**, the site's ID learning hub: home page `#lab` section → `/seasoning-lab/` → `/papers/` → `/papers/<slug>/`. The hub reads the papers index at runtime and the home section only links to it, so a new paper never requires editing either.
```
seasoning-lab/index.html          # hub (never edit for a new paper)
papers/index.html                 # index (create from template if absent)
papers/<slug>/index.html          # paper page
papers/<slug>/paper.json          # verified data
papers/<slug>/video.mp4           # rendered hero video (+ poster.jpg)
papers/<slug>/storyboard.md
papers/<slug>/QUESTIONS.md        # only if anything is MISSING/UNVERIFIED
```
**Slug** = lowercase trial short name + year, hyphenated, ASCII only: `poet-2019`, `recovery-dexamethasone-2021`. If there's no trial name, use first-author + year: `van-nood-2013`.

## Steps

### Step 1: Parse input
1.1 Read Arman's paste (format: `templates/input-template.md`). Required: title, journal, year, PMID or DOI, MUST-INCLUDE excerpts, KEY NUMBERS.
1.2 If a required field is empty, stop and ask. If optional fields are empty, continue.

### Step 2: Build paper.json
2.1 Fill `templates/paper.schema.json` fields. Sections: background, methods (design, population, n, intervention, comparator, primary endpoint, follow-up), results, conclusions, limitations, practice_impact.
2.2 For every number make a `numbers[]` entry: `id`, `label`, `value`, `unit`, `source_quote` (verbatim ≤ 300 chars), `source` ("paste" | "paper"), `status`. Section text and `one_liner` cite numbers as `{{n:id}}` tokens rather than typing them.
2.3 Build `figures[]`. Each figure only references numbers by `id`. Choose type:
   - two-arm rate comparison → `bar` (grouped)
   - effect sizes / noninferiority margin → `forest` (point + CI + margin line)
   - time-to-event, if curve points are supplied → `km` (step line). If only HR is given, use a `forest` or `bignumber` chart instead. **Never fabricate curve points.**
   - single headline stat → `bignumber`
   - proportions → `donut` / `waffle`
2.4 Pick 2–4 `hero_findings` (the most impactful numbers) for the video.

### Step 3: Verify (mandatory gate)
3.1 For each `numbers[]` entry, check the `value` literally appears in its `source_quote` (allow formatting: 9.0 vs 9.0%, 1,000 vs 1000, 6 vs "Six"). `1` does not match inside `13.2`. Run:
```
node .claude/skills/id-paper-page/scripts/verify-paper.js papers/<slug>/paper.json
```
3.2 Check derived values (differences, relative reductions) are either quoted or marked `"derived": true` with the formula shown.
3.3 Check each MUST-INCLUDE item maps to a section (`must_include_map`).
3.4 Check denominators: n per arm sums to total randomized/analysed as stated.
3.5 If anything FAILs: set status, write `QUESTIONS.md`, and render those items with a visible "⚠ data needed" placeholder. Never fill them with a guess.

### Step 4: Generate the page
4.1 Copy `templates/paper-page.html` to `papers/<slug>/index.html`. Replace every `{{…}}` (including the ones in `<head>` and the taskbar, and each `{{n:id}}` from `paper.json`, which becomes that number's value and unit). Leave everything outside the `.pp` container exactly as the template has it. Order, top to bottom:
   1. title window: full title, citation line, **Source** buttons (PubMed, DOI)
   2. hero video window (`video.mp4`, poster, captions `.vtt`, play/pause controls, `muted playsinline`)
   3. TL;DR big-number strip (hero findings)
   4. Background → Methods (PICO table) → Results (charts) → Conclusions → Limitations → What changed in practice
   5. Citation + "Educational summary, not medical advice"
4.2 Charts: the template already loads Chart.js and the shared `../paper-charts.js`. Each chart sits in `<figure>` with an `<h3>` (the figure title), the `<canvas>` inside `<div class="chart-box">`, a `<figcaption>` (source quote + "Recreated from data reported in …"), `aria-label`, and a `<details>` data table.
   Renderer options (all in `paper.json`, see the schema):
   - `arms` (top level) maps each number's `arm` to `"intervention"` (salt yellow) or `"comparator"` (blue), e.g. `{"oral":"intervention","intravenous":"comparator"}`. Set it for every two-arm trial so the colours mean the same thing on every page.
   - `series_labels`: short axis labels ("Oral", "IV"). Use them whenever the number labels are long.
   - `grouped` type with `groups: [{label, ids:[armA, armB]}]` for per-component comparisons.
   - Forest plots: `margin_id` draws the noninferiority margin line (only if that number is VERIFIED). `margin_direction: -1` draws it on the negative side. `ci_label` sets the table header when the CI isn't 95%. `y_label` titles the x-axis and should say which side favours which arm.
   - `decimals` on a number keeps trailing zeros (9.0, not 9).
   If the renderer genuinely needs a new feature, change `templates/paper-charts.js` and `papers/paper-charts.js` identically, keep existing options working, and re-check that every existing paper page still renders.
4.3 Animations: charts animate when scrolled into view (IntersectionObserver in paper-charts.js). Respect `prefers-reduced-motion`.
4.4 Tone: plain, friendly, a bit playful (like the rest of the site), clinically precise. Short paragraphs, ≤ 68ch.

### Step 5: Video (deterministic, data-driven)
5.1 Fill `templates/video-storyboard.md` → `papers/<slug>/storyboard.md`: 6–8 scenes, 30–60 s, VO text per scene. Every on-screen number references a `numbers[].id`.
5.2 Render with Remotion (preferred):
```
npx create-video@latest paper-video --template blank   # once
cp .claude/skills/id-paper-page/templates/remotion/PaperVideo.tsx paper-video/src/
# register composition id "PaperVideo" in src/Root.tsx with defaultProps from paper.json (1080x1920 or 1920x1080, 30fps)
npx remotion render PaperVideo out/<slug>.mp4 --props=../papers/<slug>/paper.json
```
   `PaperVideo.tsx` renders the title, one scene per hero finding, and "what changed". Add any other storyboard scene (PICO, chart draws) to it before rendering, and set `durationInFrames` to match.
   Fallback if Remotion isn't available: animate the charts page-section at 1920×1080 with Playwright `recordVideo`, then `ffmpeg -i in.webm -c:v libx264 -pix_fmt yuv420p video.mp4`.
5.3 Voiceover (optional): TTS from the storyboard VO lines; mux with ffmpeg. Also write captions `video.vtt` from the VO lines.
5.4 Poster: `ffmpeg -ss 2 -i video.mp4 -frames:v 1 poster.jpg` (also used as index thumbnail).
5.5 Optional AI b-roll (Sora/Veo/Runway etc.): **only** non-data atmosphere shots (microscope, hospital corridor, pills). Never let a generative model draw charts, numbers, or text. Pass it the "B-roll prompts" section of the storyboard.

### Step 6: Update the index
6.1 `papers/index.html` already exists. Only if it's absent, create it from `templates/papers-index.html`.
6.2 Append the card snippet (inside `<!-- PAPER CARDS -->`, after the existing cards) with title, short name, topic, year, one-line finding (must reuse a verified number), and thumbnail `poster.jpg`. Fill **both** `data-topic` and `data-year` on the `<a class="window card">`: the index script groups cards by `data-topic` (A to Z) and sorts by `data-year`, and the hub's "latest papers" list takes the last cards in the file, so always append at the end. `data-topic` must match the `.tag` text exactly. Don't duplicate the slug; if it exists, replace that card in place. Leave the other cards alone.
6.3 Topics: Bacteremia & duration · Endocarditis · Bone & joint · HIV · COVID-19 · Hepatitis · Fungal · C. diff · TB · Vaccines & RSV · STI prevention · Resistance & stewardship. If none fits, ask Arman rather than forcing one.
6.4 Add `https://www.saltshakerstudio.net/papers/<slug>/` to `sitemap.xml` with today's date as `<lastmod>`.

### Step 7: Final checklist (print it with ✅/❌)
- [ ] Verify script prints PASS (or QUESTIONS.md lists every gap and placeholders are visible)
- [ ] Every MUST-INCLUDE item appears on the page
- [ ] No figure images copied; every chart has a caption, source, and data table
- [ ] PubMed + DOI links resolve; citation present
- [ ] Video numbers equal paper.json numbers; no AI-generated data visuals
- [ ] Video has captions, poster, and is muted/autoplay-safe
- [ ] Page uses `/css/site.css` tokens; fonts load; mobile width 360px looks fine
- [ ] Site wrapper intact. This prints nothing when it is:
```
for s in 'rel="canonical"' 'property="og:image"' 'class="skip-link"' 'class="wrap narrow"' 'class="site-footer"' 'id="startMenu"' 'class="taskbar"' '/js/site.js' 'class="t-btns"'; do grep -q "$s" papers/<slug>/index.html || echo "MISSING $s"; done; grep -n '{{\|googletagmanager\|gtag(' papers/<slug>/index.html
```
- [ ] Every other paper page under `papers/` still renders its charts
- [ ] Sitemap entry added
- [ ] Reduced-motion users get static charts
- [ ] Index card added/updated once
- [ ] Nothing deployed or pushed. Report to Arman for review.

## Site style tokens (from saltshakerstudio.net `css/site.css`)
Stack: hand-written static HTML + `css/site.css` + `js/site.js`, Google Fonts, no analytics. No framework detected. Look: retro desktop OS (draggable-looking "windows" with blue gradient titlebars, a taskbar, pixel icons) on a teal desktop.
```
--desk-a:#117178  --desk-b:#0a4650   (page bg gradient + yellow/blue radial glows + 4px dot grid at 6%)
--face:#eef0f3 --face-2:#e2e5ea --paper:#fff   (window body / inner panels)
--ink:#141a24 --ink-2:#39414f --muted:#586173 --hairline:#d5dae2 --edge:#141a24
--title-a:#0b1f8f → --title-b:#1f82e0  (titlebar gradient, white 600 13px text, 34px tall)
--salt:#ffd23f (primary accent/buttons) --salt-hover:#ffdb5c --salt-deep:#c89400
--live:#15994a --dev:#2563eb --beta:#7b3fb5 --proto:#d97706 --danger:#b91c1c --notice:#fffbe6
--r:10px  --lift:6px 6px 0 rgba(3,22,26,.38),0 18px 40px -12px rgba(0,0,0,.35)
Fonts: display "Pixelify Sans" 500/700 · body "IBM Plex Sans" 15px/1.55 · mono "IBM Plex Mono"
Window: 2px solid --edge border, radius 10px, --lift shadow, inner bevel highlight
Button: 2px edge border, radius 8px, 0 3px 0 edge shadow, 600 14px; pressed = translateY(3px); .btn-primary = --salt bg
h2: preceded by 12px yellow square with 2px edge border. Paragraph max 68ch.
```
Chart palette: intervention `#ffd23f` (edge-outlined), comparator `#1f82e0`, neutral `#586173`, harm `#b91c1c`, benefit `#15994a`. Fonts in charts: IBM Plex Sans; big numbers in Pixelify Sans.
The templates carry the real wrapper markup (titlebar icons `.pix.t-icon[data-pix]`, window buttons `.t-btns`, taskbar, Start menu, footer), copied from the live pages. Reuse existing classes (`.window`, `.titlebar`, `.t-text`, `.win-body`, `.btn`, `.btn-primary`, `.btn-row`) rather than inventing new ones.
