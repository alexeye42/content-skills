---
trigger: manual
description: User profile — editorial calibrations for feedback and review (strictness, what never to flag, score anchors, review part size, title/subtitle limits). Read by feedback-4content, review4content, and metadata_rules.md; edit it to your own taste.
---

# Editorial Profile

Edit this file to your own editorial taste. `feedback-4content` and `review4content`
read it directly; `metadata_rules.md` and `outline_rules.md` take the metadata
limits from it.

## Strictness
- Default (middle sections): flag only what makes reading fail; skip polish.
- `strict` (the caller sets it — normally for the introduction and conclusion):
  flag polish-level issues too.

## Never flag
- Markdown formatting, quote style, number formatting, brand spelling.
- Links and cross-references.
- The author's voice — see `profile/audience.md`, *Author*.
- Missing facts or numbers "for rigor" — unless the passage is unusable without
  them.

## Score anchors
The scale is 1–10 per criterion. Do not be harsher than this — the articles are
not entering a contest:
- **10** — nothing to fix.
- **9** — only minor remarks, however many (typos, punctuation, small word swaps).
- **8** — 1–2 places where the reader stumbles: an unclear paragraph, a missing
  step (a `Should add`).
- **7** — more than two such places, and/or the section drags a little.
- **5–6** — the section drags badly or its point does not land; a chunk needs
  rework.
- **≤4** — better to rewrite the section.

## Review parts
- A part is 1–3 section files, ~600–1800 words, cut by meaning rather than by
  length; the introduction and the conclusion form the last part together.
- A re-run of a part ("redo part N") defaults to 1–2 remarks per section.

## Metadata limits
- Title: 45–65 characters, Title Case.
- Subtitle: 70–140 characters, Sentence case, no trailing period.
- Post text (channels like LinkedIn): 100–150 words, 3–5 short paragraphs.