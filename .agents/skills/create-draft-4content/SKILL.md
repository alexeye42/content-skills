---
name: create-draft-4content
description: Write a full draft (n_draft.mkd) of an article from an approved plan. Use when the prompt says "write the draft" / "draft from plan".
---

# Create Draft (4content)

Write a full draft from an approved plan. Output goes to `n_draft.mkd` in the piece
folder.

Work in the main context (no subagents). The draft is written in the piece's target
language (`audience_rules.md`, *Resolving the language*).

## Steps

1. Read the approved `n_plan.mkd` in full. Read the source + `n_findings.mkd`
   (findings override the source on conflicts).
2. Load `article_rules.md` + `writing_rules.md` + `writing_antipatterns.md` +
   `format_rules.md` + `audience_rules.md` (audience and channel).
3. Write the draft block by block following the plan, applying `writing_rules.md`.
   Keep every artifact and fact tied to its block, matching the plan's boundaries.
4. Do **not** polish to final quality — that is the improve step. Leave `[Insert …]`
   placeholders for material that was missing at plan approval; mark text you had
   to write without source material with an `🤖 **AI wrote:**` callout and
   author-only material with `➕ **Must add:**` (*Agent callouts*, `format_rules.md`).
5. Write `n_draft.mkd`.

## Notes
- The draft is the input for the outline → sections steps; write it as continuous
  prose per block, not as section files.
- Don't add image references in the draft.
