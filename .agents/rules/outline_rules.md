---
trigger: model_decision
description: Use it if asked to do something with the outline of an article (not a book chapter — that is `book_outline_rules.md`); a piece folder `*.*-*` or `*_outline.mkd` file may be referenced to denote the outline.
---

# Outline Rules

The outline `n_outline.mkd` is the pre-draft of an article whose section files are
generated rather than split: it exists only when the source is a braindump
(`n_dump.mkd`) or a rough draft (`n_draft.mkd` that is notes to expand, not finished
prose) — or a final draft the human chose to improve rather than split as is. A
plan-based article and a final draft split as is have no outline — the draft is split
by its headings. The human reads the outline and approves it before any section is
written.

## File Naming
Folder name `N.n-piece-code`, outline file name `n_outline.mkd` and section file names
`n-section-code.md` have the same n.

## Outline Structure
- No frontmatter and no title: the title and subtitle live in the plan and the intro
  (`metadata_rules.md`).
- A list of section headings, each preceded by a blank line. Top-level section
  headings start with `###`, subsection headings with `####`, whatever the channel —
  the section files get the channel's levels (`article_rules.md`).
- The first section is the introduction and may have no heading.
- Under each top-level section heading (and at the top for a headingless intro), a
  `@section-code` line: a reference to the `n-section-code.md` file to create. The
  code starts with the section's position — `0` for the intro, then `1`, `2`… in
  order, the conclusion last — even when the heading has no number: `@0-intro`,
  `@3-final-steps`, `@7-conclusion`.
- Under each heading, the content points (see below).

## Content Rules
- Points in the order the section will present them, one point per thought, a short
  line or two each, in the piece's target language (`audience_rules.md`,
  *Resolving the language*). Not prose — the section files are written from them.
- Each point carries its origin, so the human sees at the gate what the agent will
  invent:
  - no mark — the thought is in the source or in the human's answers in `n_qna.md`
    (its wording is kept, translated into the target language if needed);
  - `(AI)` — the source has nothing for it; the agent will write it (a lead-in, a
    transition, a short explanation) under a `🤖 AI wrote` callout;
  - `(Must add)` — only the author can supply it (numbers, checklists, internal
    examples, an open decision); it will become a `➕ Must add` callout.
- Nothing is invented beyond `(AI)` points, and `(AI)` covers connective text only:
  a fact, number, example, or tool name the source lacks is a `(Must add)` point.
- Example: `references/example_outline.mkd` in the `create-outline-4content` skill
  folder, if another example is not given in the prompt.

## Lifecycle
- The outline is written once. Until the human's "ok" at the gate it is edited on
  their remarks; after that the agent never updates it — once section files exist,
  they are the current text and the outline goes stale.
- The human may reopen it on purpose (e.g. add a section and ask to create it);
  `create-sections-4content` then updates the section files from it.
