# Batch build (Nov 2026): 15 papers from local PDFs

Tooling used to add the 15 papers in one pass. Each `specs/<slug>.py` is the hand-written
source for one page (numbers with verbatim quotes, figures, prose with `{{n:id}}` tokens).

- `build.py specs/<slug>.py` writes `papers/<slug>/{paper.json,index.html,storyboard.md,video.vtt}`
  and refuses to build if any quote, caption, MUST-INCLUDE excerpt, or literal number in the
  prose is missing from the PDF text. It expects `pdftotext -enc UTF-8` output in a `txt/`
  folder next to `build/` (edit the `TXT`/`SITE` paths at the top).
- `remotion/` is the video composition (title, who-was-studied, findings with animated
  comparison bars, what-changed). `render.sh <slug>` renders `video.mp4` + `poster.jpg`.
- `shot.js <slug> [<slug>@m]` loads pages in headless Chrome, scrolls them, and reports
  revealed sections, chart count, JS errors, and horizontal overflow.

Still run `scripts/verify-paper.js` on every `paper.json` afterwards.
