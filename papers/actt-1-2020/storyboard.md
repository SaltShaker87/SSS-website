# Storyboard: ACTT-1 (2020)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Could an antiviral speed recovery in hospitalized Covid-19?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "ACTT-1 randomized 1062 patients hospitalized adults to remdesivir or placebo." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | rec_rdv, rec_rdv, rec_pbo | "Median time to recovery: 10 days with remdesivir versus 15 days with placebo." |
| 4 | 15-21s | Hero finding 2: counter ticks up | rr_os5 | "The clearest benefit was in patients on low-flow oxygen: rate ratio for recovery 1.45." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | m29_rdv, m29_rdv, m29_pbo | "Mortality by day 29: 11.4% versus 15.2%. Hazard ratio 0.73, not statistically significant." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | stay_rdv, stay_rdv, stay_pbo | "Median initial hospital stay: 12 days versus 17 days." |
| 7 | 33-39s | "What changed" card + citation | - | "Remdesivir shortened time to recovery. N Engl J Med, 2020. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "IV infusion bag dripping slowly beside a hospital bed, soft teal light, no text"
- "Hospital corridor at night with soft window light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
