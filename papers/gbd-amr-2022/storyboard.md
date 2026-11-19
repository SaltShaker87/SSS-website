# Storyboard: GBD AMR 2019 (2022)
Format: 1920x1080 · 30 fps · 39 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "How many people does antimicrobial resistance kill?" |
| 2 | 4-9s | Who was studied: enrollment counter | countries | "The study modelled AMR deaths in 204 countries and territories." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | assoc, attr, assoc | "4.95 million deaths were associated with bacterial resistance in 2019." |
| 4 | 15-21s | Hero finding 2: counter ticks up | attr | "1.27 million deaths were directly attributable to resistance." |
| 5 | 21-27s | Hero finding 3: counter ticks up with animated comparison bars | high, high, low | "Highest burden: western sub-Saharan Africa, 27.3 per 100 000. Lowest: Australasia, 6.5." |
| 6 | 27-33s | Hero finding 4: counter ticks up | six | "Six pathogens caused 73.4% of attributable deaths." |
| 7 | 33-39s | "What changed" card + citation | - | "AMR is a leading cause of death worldwide. The Lancet, 2022. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Petri dishes with bacterial colonies under lab light, slow pan, no text"
- "World map texture on a wall in soft focus, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1185 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
