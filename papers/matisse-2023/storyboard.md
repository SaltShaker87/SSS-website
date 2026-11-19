# Storyboard: MATISSE (2023)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Can vaccinating mothers in pregnancy protect newborns from RSV?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_vax | "MATISSE vaccinated 3682 pregnant women, and 3676 received placebo." |
| 3 | 9-15s | Hero finding 1: counter ticks up | ve_sev90 | "Efficacy against severe RSV illness in the first 90 days: 81.8%." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | sev_pbo, sev_vax, sev_pbo | "33 severe cases with placebo. 6 after maternal vaccination." |
| 5 | 21-27s | Hero finding 3: counter ticks up | ve_sev180 | "Still 69.4% at 180 days." |
| 6 | 27-33s | Hero finding 4: counter ticks up | ve_lrti90 | "Against illness of any severity: 57.1%, short of the success criterion." |
| 7 | 33-39s | "What changed" card + citation | - | "Maternal RSVpreF vaccine protected infants from severe RSV. N Engl J Med, 2023. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Newborn's hand holding a parent's finger in soft window light, no text"
- "Pregnant person's silhouette by a window at golden hour, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
