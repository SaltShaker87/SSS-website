# Storyboard: C4591001 (2020)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Could a new mRNA vaccine prevent Covid-19?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_rand | "The trial randomized 43,548 participants people aged 16 and older." |
| 3 | 9-15s | Hero finding 1: counter ticks up | ve | "BNT162b2 was 95% effective against Covid-19." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | cases_pbo, cases_vax, cases_pbo | "162 cases with placebo. Just 8 with the vaccine." |
| 5 | 21-27s | Hero finding 3: counter ticks up | ve_d1 | "Protection started early: 52% efficacy between the two doses." |
| 6 | 27-33s | Hero finding 4: counter ticks up with animated comparison bars | sev_pbo, sev_vax, sev_pbo | "Severe Covid-19: 9 cases with placebo, 1 with the vaccine." |
| 7 | 33-39s | "What changed" card + citation | - | "Two doses of BNT162b2 gave 95% protection. N Engl J Med, 2020. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Gloved hands drawing a vaccine dose into a syringe, soft teal light, no text"
- "Row of vials on a lab rack under cool light, shallow depth of field, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
