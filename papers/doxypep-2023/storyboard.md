# Storyboard: DoxyPEP (2023)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Can one dose of doxycycline after sex prevent STIs?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "DoxyPEP enrolled 501 participants people with a recent bacterial STI." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | prep_doxy, prep_doxy, prep_sc | "In the PrEP cohort, STIs at 10.7% of visits with doxy-PEP versus 31.9% with standard care." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | plwh_doxy, plwh_doxy, plwh_sc | "In people living with HIV: 11.8% versus 30.5%." |
| 5 | 21-27s | Hero finding 3: counter ticks up | ct_prep | "Chlamydia relative risk 0.12. Gonorrhea fell less, 0.45." |
| 6 | 27-33s | Hero finding 4: counter ticks up | nnt | "Number needed to treat: about 5." |
| 7 | 33-39s | "What changed" card + citation | - | "Doxy-PEP cut bacterial STIs by about two thirds. N Engl J Med, 2023. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Close-up of a single capsule on a bedside table in warm evening light, no text"
- "City street at dusk in soft focus, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
