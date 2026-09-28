---
name: create-outline-4content
description: Build the outline (n_outline.mkd) of an article from a braindump (n_dump.mkd) or a rough draft of notes, and get the human's approval at the outline gate before sections are written. Use when the prompt says "build the outline" / "outline the dump" / "outline the draft"; also invoked by go4content. Not for book chapters (create-outline-4book).
---

# Create Outline (4content)

Build `n_outline.mkd`, the pre-draft of an article whose sections will be generated:
from a braindump (`n_dump.mkd`) or a rough draft (`n_draft.mkd` that is notes to
expand). A plan-based or final draft is split by `create-sections-4content` instead —
unless the human chose to improve a final draft through an outline (`go4content`
round 0, or the split question of `create-sections-4content`). Outline structure and
content rules are in `outline_rules.md`. Mainly invoked from `go4content`.

## Steps

1. **Source.** Verify `n_dump.mkd` or `n_draft.mkd` is referenced; if neither, say
   so and stop. A draft that passes the final-draft check of
   `create-sections-4content` (step 2.1) is outlined only if the human asked to
   improve it; otherwise offer the split and stop. Resolve the audience per
   `audience_rules.md` (*Resolving the audience*); if it is unresolved, report
   "audience unresolved" and stop.

2. **Gap questions (a braindump, or a rough draft with `<TBD>` / `<TODO>` gaps).**
   Ask through `qna-manager` — as the next round of `n_qna.md` — about the main
   thesis, the reader's takeaway, missing facts, placeholders, and which parts the
   author will write themselves. Wait for the answers: the outline is built from
   them, so the human does not review a structure the answers would still change.

3. **Write `n_outline.mkd`** per `outline_rules.md`.
   - If it already exists: when section files are already in the folder, stop — the
     outline is past its gate (`outline_rules.md`, *Lifecycle*); point to
     `create-sections-4content` (step 4). Otherwise treat it as the human's start:
     keep its headings, points, and marks, and add only what is missing.
   - Sections: take the source's headings; where the source has none, add a heading
     for any chunk over 400 words or one that mixes weakly related topics, in natural
     language.
   - A `@section-code` line under each top-level heading (and at the top for a
     headingless intro), the code starting with the section's position: `0` for the
     intro, then `1`, `2`… in order, the conclusion last — even when the heading has
     no number (`@0-intro`, `@3-final-steps`).
   - Under each heading, the points in order with their origin marks — unmarked,
     `(AI)`, `(Must add)`. Mark honestly: every thought that neither the source nor
     the Q&A answers contain is `(AI)` or `(Must add)`, never unmarked.
   - Source tags (`format_rules.md`, *Angle-bracket tags*): `<TBD>` → an `(AI)`
     point; `<TODO>` → a `(Must add)` point; drop the content of `<DELETE>`, `<note>`,
     `<ai>`.
   - Example: `references/example_outline.mkd` in this skill's folder.

4. **Outline gate.** Leave the outline UNCOMMITTED and ask the human, in the language
   of the user's prompt: "The outline is in `n_outline.mkd`: sections in order, and
   under each the points I'll write — unmarked from your text, `(AI)` what I'll add
   myself, `(Must add)` what only you can give. Edit it in the file or tell me here,
   then say ok." Apply remarks given in chat and ask again. On "ok", commit the outline
   via `git-commit-flow` — author `human` if they only edited the file, `human/ai` if
   you applied their remarks (with or without their own edits), otherwise `ai` — and
   return.

## Notes
- NEVER drop or merge away a source thought to tidy the structure: every idea of the
  source lands in a point, or is listed in chat at the gate as left out — the outline
  is the human's only coverage check before text exists.
- NEVER polish unmarked points: a point names the source's thought; polished wording
  leaks into the sections.
- NEVER put a fact, number, example, or tool name in an `(AI)` point — that is
  `(Must add)`; `(AI)` covers connective text only (lead-ins, transitions, short
  explanations).
- The outline is written once: after the gate, never update it (`outline_rules.md`,
  *Lifecycle*).
- No title in the outline: `create-sections-4content` writes the first version into
  the intro.
