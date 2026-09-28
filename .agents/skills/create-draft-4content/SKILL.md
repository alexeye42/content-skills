---
name: create-draft-4content
description: Write a full draft (n_draft.mkd) of an article from its content plan (n_plan.mkd). Use when the prompt says "write the draft" / "draft from plan".
---

# Create Draft (4content)

Write a full draft from the content plan. Output goes to `n_draft.mkd` in the piece
folder.

Work in the main context (no subagents). The draft is written in the piece's target
language (`audience_rules.md`, *Resolving the language*).

## Steps

1. **Plan status** (`plan_rules.md`):
   - `checked` — go on;
   - `structured` or `reviewed` — the plan has not been checked: offer to run
     `check-plan-4content` first (and, for `structured`, to let the human read the
     plan before that); if the human declines, go on;
   - `preliminary` or no plan — offer to run `create-plan-4content` first; stop until
     there is a structured plan.
2. Read `n_plan.mkd` in full: the Thesis, the Structure, the Source & facts, and the
   sources it lists (the more recent source wins on a conflict). The Ideas section,
   if any, is context only: ideas marked `[Parked]` or `[Rejected]` do not go into
   the draft.
3. Load `article_rules.md` + `writing_rules.md` + `writing_antipatterns.md` +
   `format_rules.md` + `audience_rules.md` (audience and channel).
4. Start the draft with the plan's `title` as the top `#` heading and its
   `subtitle` as a `<!-- comment -->` under it (on a post-text channel, a draft post
   instead — `metadata_rules.md`); on the split they become the intro's metadata.
   Then write the draft block by block following the Structure, applying
   `writing_rules.md`: each block — or group of blocks — becomes one top-level
   section with its heading (levels per `article_rules.md`); the text before the
   first heading is the intro. Keep every artifact and fact tied to its block,
   matching the plan's boundaries; let every block serve the Thesis. Write the
   conclusion per the plan's `series` (`article_rules.md`).
5. Do **not** polish to final quality — that is the improve step. Leave `[Insert …]`
   placeholders for material that is still missing; mark text you had to write
   without source material with an `🤖 **AI wrote:**` callout and author-only
   material with `➕ **Must add:**` (*Agent callouts*, `format_rules.md`).
6. Write `n_draft.mkd`.

## Notes
- The draft is split into section files by its top-level headings as is
  (`create-sections-4content`); write it as one file with continuous prose per
  section, not as section files. Leave the plan's `title`/`subtitle` untouched — they
  stay there as the first version.
- Don't add image references in the draft.
