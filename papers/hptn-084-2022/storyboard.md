# Storyboard: HPTN 084 (2022)
Format: 1920x1080 · 30 fps · 33 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "HIV prevention for women: is an injection every 8 weeks better than a daily pill?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "HPTN 084 enrolled 3224 participants women at 20 sites in sub-Saharan Africa." |
| 3 | 9-15s | Hero finding 1: counter ticks up | hr | "Hazard ratio 0.12: cabotegravir was superior." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | inf_tdf, inf_cab, inf_tdf | "Infections: 4 with cabotegravir, 36 with daily pills." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | adh, cov, adh | "The reason: only 42.1% of pill-group samples showed daily use. Injection coverage was 93%." |
| 6 | 27-33s | "What changed" card + citation | - | "Injectable cabotegravir was superior to daily PrEP. The Lancet, 2022. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Clinic waiting room with morning light in sub-Saharan Africa, people out of focus, no text"
- "Nurse preparing an intramuscular injection, gloved hands, shallow depth of field, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1005 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
