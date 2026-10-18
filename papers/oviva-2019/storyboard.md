# Storyboard: OVIVA (2019)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0–4s | Title window pops open on teal desktop; trial name types out | — | "Could oral antibiotics replace six weeks of intravenous therapy for bone and joint infection?" |
| 2 | 4–10s | The question: who joined the trial | n_total, centers | "OVIVA randomized 1054 adults at 26 U.K. sites." |
| 3 | 10–16s | Hero finding 1: counter ticks to 13.2% | failure_oral (context: failure_iv) | "Definite treatment failure at 1 year: 13.2% with oral therapy." |
| 4 | 16–22s | Hero finding 2: counter ticks to -1.4 pp | risk_diff, rd_ci90_low, rd_ci90_high, margin | "Risk difference minus 1.4 percentage points, 90% CI -4.9 to 2.2, inside the 7.5-point margin." |
| 5 | 22–28s | Hero finding 3: counter ticks to 1.0% | cath_oral (context: cath_iv) | "Catheter complications: 1.0% with oral versus 9.4% with intravenous." |
| 6 | 28–34s | Hero finding 4: counter ticks to 11 days | stay_oral (context: stay_iv) | "Median hospital stay: 11 days oral versus 14 days intravenous." |
| 7 | 34–39s | "What changed" card + citation | — | "Oral therapy was noninferior. N Engl J Med, 2019. Scroll for the full breakdown." |

Rules: every number = paper.json value; label primary vs secondary; "noninferior" spoken as such.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Slow push-in on a blood culture bottle on a lab bench, soft teal light, no text"
- "Hands dabbing an alcohol swab on the hub of an intravenous line, shallow depth of field, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1170 frames) from this file and `paper.json`; hero findings come straight from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the voiceover lines above; no TTS audio was muxed (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
