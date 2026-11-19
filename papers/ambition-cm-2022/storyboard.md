# Storyboard: AMBITION-cm (2022)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Cryptococcal meningitis: can one dose of AmBisome replace a week of toxic infusions?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_rand | "AMBITION-cm randomized 844 participants adults with HIV-associated cryptococcal meningitis." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | mort_amb, mort_amb, mort_ctl | "Ten-week mortality: 24.8% with one dose of AmBisome versus 28.7% with the WHO standard." |
| 4 | 15-21s | Hero finding 2: counter ticks up | diff | "Difference −3.9%, with the upper confidence limit far inside the 10% margin. Noninferior." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | anemia_amb, anemia_amb, anemia_ctl | "Severe anemia: 13.3% versus 39.1%." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | tx_amb, tx_amb, tx_ctl | "Blood transfusions: 7.6% versus 18.0%." |
| 7 | 33-39s | "What changed" card + citation | - | "Single-dose AmBisome was noninferior and safer. N Engl J Med, 2022. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Slow push-in on an IV infusion bag with yellow liquid in a clinic in soft light, no text"
- "Microscope eyepiece on a lab bench in teal light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
