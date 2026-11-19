# Storyboard: EPIC-HR (2022)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Can a 5-day oral pill keep high-risk Covid-19 patients out of hospital?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "EPIC-HR randomized 2246 patients unvaccinated, high-risk outpatients." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | fin_nmv, fin_nmv, fin_pbo | "Hospitalization or death by day 28: 0.72% with nirmatrelvir plus ritonavir versus 6.45% with placebo." |
| 4 | 15-21s | Hero finding 2: counter ticks up | rrr | "That is a relative risk reduction of 88.9%." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | death_pbo, death_nmv, death_pbo | "Deaths: 13 with placebo. None with nirmatrelvir plus ritonavir." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | dys_nmv, dys_nmv, dys_pbo | "The trade-off: dysgeusia in 5.6% versus 0.3%." |
| 7 | 33-39s | "What changed" card + citation | - | "Nirmatrelvir plus ritonavir cut hospitalization or death by about 89%. N Engl J Med, 2022. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Blister pack of tablets on a kitchen table in morning light, shallow depth of field, no text"
- "Person resting on a couch with a cup of tea, soft window light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
