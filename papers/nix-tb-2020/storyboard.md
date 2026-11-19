# Storyboard: Nix-TB (2020)
Format: 1920x1080 · 30 fps · 33 s · style: site palette, Pixelify Sans numbers, window-frame "pop-up" transitions.

| # | Time | Visual (deterministic) | On-screen numbers (number ids) | Voiceover / caption |
|---|------|------------------------|--------------------------------|-----------|
| 1 | 0-4s | Title window pops open on the teal desktop | - | "Extensively drug-resistant TB: can three pills for six months cure it?" |
| 2 | 4-9s | Who was studied: enrollment counter | n_total | "Nix-TB treated 109 patients patients with highly resistant TB in South Africa." |
| 3 | 9-15s | Hero finding 1: counter ticks up with animated comparison bars | fav, xdr, mdr | "Favourable outcome: 90% of patients." |
| 4 | 15-21s | Hero finding 2: counter ticks up with animated comparison bars | xdr, xdr, hist | "For XDR-TB: 89%, against a historical average of 14% in South Africa." |
| 5 | 21-27s | Hero finding 3: counter ticks up | neuro | "The cost: peripheral neuropathy in 81%, myelosuppression in 48%." |
| 6 | 27-33s | "What changed" card + citation | - | "BPaL gave a favourable outcome in 90%. N Engl J Med, 2020. Scroll for the full breakdown." |

Rules: every number = paper.json value; primary vs secondary end points labeled as in the paper.

## B-roll prompts (optional, AI generator; NO text, numbers, or charts)
- "Chest X-ray on a light box in a dim clinic room, no text"
- "Pill cups with three tablets on a clinic counter in soft light, no text"
- No AI b-roll was used in the rendered video; all scenes are deterministic data visuals.

## Render notes
- Rendered with Remotion 4 (`PaperVideo` composition, 1920x1080, 30 fps, 1005 frames) from `paper.json`; hero findings come from `paper.json.hero_findings`.
- Captions in `video.vtt` follow the lines above; no voiceover audio (video ships muted/autoplay-safe).
- Poster: frame 60 (title scene).
