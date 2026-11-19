# Storyboard: Yahav 7 vs 14 (2019)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Gram-negative bacteremia: is 7 days of antibiotics as good as 14?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "The trial randomized 604 patients stable inpatients at 3 centers in Israel and Italy." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | prim_short, prim_short, prim_long | "Primary outcome at 90 days: 45.8% with 7 days versus 48.3% with 14 days." |
| 4 | 15-21s | Hero finding 2: counter ticks up | rd | "Risk difference −2.6%, with the upper confidence limit below the 10% margin. Noninferior." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | abx_short, abx_short, abx_long | "Total antibiotic days by day 90: a median of 10 days versus 16 days." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | func_short, func_short, func_long | "Patients on the short course got back to baseline activity sooner: 2 weeks versus 3 weeks." |
| 7 | 33-39s | "What changed" card + citation | - | "Seven days was noninferior to 14 days. Clinical Infectious Diseases, 2019. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Slow push-in on a blood culture bottle on a lab bench, soft teal light, no text"
- "Pill organizer with a week of compartments on a hospital tray table, shallow depth of field, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
