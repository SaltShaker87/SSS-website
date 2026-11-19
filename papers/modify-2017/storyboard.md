# Storyboard: MODIFY I/II (2017)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "C. difficile keeps coming back. Can an antibody against its toxin stop that?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "MODIFY I and II enrolled 2655 adults adults being treated for C. difficile." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | m1_bez, m1_bez, m1_pbo | "MODIFY I recurrence: 17% with bezlotoxumab versus 28% with placebo." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | m2_bez, m2_bez, m2_pbo | "MODIFY II: 16% versus 26%. The same result twice." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | sus_bez, sus_bez, sus_pbo | "Sustained cure: 64% versus 54%." |
| 6 | 27-33s | Hero finding 4: counter ticks up | nnt_hi | "Number needed to treat: 10 overall, 6 in older patients or after a previous episode." |
| 7 | 33-39s | "What changed" card + citation | - | "Bezlotoxumab lowered recurrence. N Engl J Med, 2017. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Slow push-in on an IV infusion pump in a quiet hospital room, no text"
- "Lab technician placing a culture plate into an anaerobic chamber, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
