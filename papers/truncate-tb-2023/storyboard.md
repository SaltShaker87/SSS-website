# Storyboard: TRUNCATE-TB (2023)
Format: 1920x1080 · 30 fps · 33 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Tuberculosis: does everyone really need 6 months of treatment?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "TRUNCATE-TB randomized 674 participants adults with drug-susceptible TB." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | bdq, bdq, std | "Week-96 primary outcome: 5.8% with the bedaquiline-linezolid strategy versus 3.9% with standard treatment." |
| 4 | 15-21s | Hero finding 2: counter ticks up | bdq_diff | "Difference 0.8 percentage points, inside the 12 percentage points margin. Noninferior." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | dur_bdq, dur_bdq, dur_std | "Total treatment time: 85 days versus 180 days." |
| 6 | 27-33s | "What changed" card + citation | - | "The 8-week bedaquiline-linezolid strategy was noninferior. N Engl J Med, 2023. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Calendar pages turning slowly on a clinic desk, soft light, no text"
- "Sputum sample tube on a laboratory rack, teal light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1005 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
