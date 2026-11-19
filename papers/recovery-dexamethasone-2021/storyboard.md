# Storyboard: RECOVERY (2021)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Could a cheap steroid save lives in hospitalized Covid-19?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "RECOVERY randomized 6425 patients patients to dexamethasone or usual care." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | mort_dex, mort_dex, mort_uc | "28-day mortality: 22.9% with dexamethasone versus 25.7% with usual care." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | imv_dex, imv_dex, imv_uc | "On invasive ventilation: 29.3% versus 41.4%. Rate ratio 0.64." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | o2_dex, o2_dex, o2_uc | "On oxygen alone: 23.3% versus 26.2%. Rate ratio 0.82." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | none_dex, none_dex, none_uc | "No respiratory support: 17.8% versus 14.0%. No benefit." |
| 7 | 33-39s | "What changed" card + citation | - | "Dexamethasone lowered deaths in patients on oxygen or ventilation. N Engl J Med, 2021. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Oxygen flowmeter bubbling on a hospital wall panel, soft teal light, no text"
- "Close-up of a small white tablet on a steel tray, shallow depth of field, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
