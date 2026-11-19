# Storyboard: MOVe-OUT (2022)
Format: 1920x1080 · 30 fps · 33 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Molnupiravir: an oral antiviral for at-risk Covid-19 outpatients." |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "MOVe-OUT randomized 1433 participants unvaccinated, at-risk outpatients." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | all_mol, all_mol, all_pbo | "In all randomized participants: 6.8% with molnupiravir versus 9.7% with placebo." |
| 4 | 15-21s | Hero finding 2: counter ticks up | all_diff | "A difference of −3.0 percentage points, down from −6.8 percentage points at the interim analysis." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | death_pbo, death_mol, death_pbo | "Deaths through day 29: 1 with molnupiravir, 9 with placebo." |
| 6 | 27-33s | "What changed" card + citation | - | "Molnupiravir reduced hospitalization or death, modestly. N Engl J Med, 2022. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Pharmacy counter with a paper bag being handed over, shallow depth of field, no text"
- "Thermometer and a glass of water on a bedside table, soft light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1005 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
