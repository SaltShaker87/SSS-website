# Storyboard: AReSVi-006 (2023)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "RSV in older adults: could one shot prevent it?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "AReSVi-006 vaccinated 24,966 participants adults aged 60 and older." |
| 3 | 9-15s | Hero finding 1: counter ticks up | ve | "Vaccine efficacy against RSV lower respiratory tract disease: 82.6%." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | cases_pbo, cases_vax, cases_pbo | "40 cases with placebo. 7 with the vaccine." |
| 5 | 21-27s | Hero finding 3: counter ticks up | ve_sev | "Against severe disease: 94.1%." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | pain_vax, pain_vax, pain_pbo | "The trade-off: a sore arm in 60.9%, mostly mild and brief." |
| 7 | 33-39s | "What changed" card + citation | - | "The vaccine was 82.6% effective. N Engl J Med, 2023. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Older adult rolling up a sleeve in a bright pharmacy, faces out of focus, no text"
- "Autumn leaves outside a window in soft light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
