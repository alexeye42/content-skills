---
trigger: always_on
---

# Metadata Rules
Requirements for an article's title and subtitle (or the post text) and the
notation for offering alternatives inside the intro file. Reused by the `*4content`
skills that judge or generate titles. (The outline's own copy of the title
guidelines stays in `outline_rules.md`.)

## Where the metadata lives
- The **title** is the intro file's top heading; the **subtitle** is the intro's
  `<!-- comment -->` under it.
- Fallback: the outline's frontmatter (`title:` / `subtitle:`), used only when the
  intro has neither. The outline is read-only for the skills using this file and may
  be absent; if both exist and disagree, the intro's version is the current one —
  note the mismatch in chat.
- **Post-text channels** (the channel's `Metadata` field in `profile/audience.md`
  says "post text") have no subtitle: the `<!-- comment -->` holds a short post text
  that accompanies the article link.

## Requirements
Length and case limits for all three items are in `profile/editorial.md`
(*Metadata limits*).
- **Title:** promises what the article actually delivers — no over-promising, no
  clickbait; appealing to the channel's audience (`audience_rules.md`).
- **Subtitle:** concrete terms, straight to the point, not wordy; adds to the title
  rather than repeating it.
- **Post text:** judged for appeal and accuracy to the article only.
- **Score:** a single 1–10 number per item combining promise-accuracy, appeal, and
  compliance with the limits — not the three-criteria section rubric.

## Options notation
When a skill offers alternatives, it writes a callout block at the very top of the
intro file (above the heading), three options per item, one marked recommended,
character counts in brackets (none for post text):

```
> 🏷️ **Title options** (current: 7/10 — <why>):
> 1. <option> [58] (recommended)
> 2. <option> [52]
> 3. <option> [61]

> 🏷️ **Subtitle options** (current: 6/10 — <why>):
> 1. <option> [112] (recommended)
> 2. …
```
Use `**Post options**` instead of subtitle options for post-text channels.

## Selection
The human either edits the heading/comment by hand or says "title 2" /
"subtitle 1" / "post 1": the skill puts the chosen text where the item lives in the
intro file and deletes the callout block. If the title lives only in the outline,
the skill says so in chat and leaves the outline to the human.
