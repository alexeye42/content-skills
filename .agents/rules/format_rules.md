---
trigger: model_decision
description: Markdown formatting and placeholder conventions for all content types. Per-type files may override defaults (e.g. heading levels). Applies only to final artifacts (sections or whole pieces) — does not apply to intermediate markdown files like outlines or drafts (they're usually named *.mkd rather than *.md)
globs: ["**/*.md"]
---

# Format Rules

Default markdown conventions for any content type. Per-type files (e.g.
`article_rules.md`) may override defaults — the heading levels in particular.

## Headings (default)
- Top-level sections use `##`.
- Subsections use `###`.
- Per-type files override these by file-name suffix (see `article_rules.md`).

## Lists
- Use hyphens (`-`) for bulleted items and `1.`, `2.`, … for numbered items.
- Indent nested list items with 2 spaces.

## Emphasis
- Use **double asterisks** for bold. Bold marks the most important words or
  phrases; no more than 5 bold words/phrases per section. Whole bold sentences may
  serve as sub-subsection "headings".
- Use _single underscore_ for italic. Only single words to pay attention to may be
  italicized.
- Enclose a whole paragraph in *single asterisks* to mark it as important.

## Horizontal rule
- Use `---` on its own line, separated by blank lines.

## Placeholders for media and links
- Use an image placeholder `![phrase](.png)` if you encounter `![phrase]` in the
  source. Do NOT change existing images `![*](*.png)`.
- Use a hyperlink placeholder `[phrase](url)` if you encounter a url (`https://*`).
  - Example: `in my [previous article](https://example.com/...)` for the source
    `in my previous article https://example.com/...`.
  - Exception: if the paragraph contains nothing but the url, leave it unchanged.
- Use an internal hyperlink placeholder `[phrase](#xxxx)` if you encounter a
  hashtag (`#phrase`) in the source.
  - Example: `in [Section 3](#xxxx).` for the source `in #section 3`.
  - Do NOT generate the substitute for `xxxx` — it's a mark for the author.

## Angle-bracket tags
If generating from uncertain inputs, you may add `<placeholder>` to indicate an
uncertain part to be edited by the user. There are also special tags:
- `<TBD>` — a signal for you to generate text here.
- `<image>`, `<subscribe>` — keep AS IS.
- `<TODO>` in a source — turn it into a `➕ **Must add:**` callout when generating
  (see *Agent callouts* below); never keep it as a tag.
- `<DELETE>`, `<note>`, `<ai>` — these tags and the content between them must be
  removed when generating a file.

## Agent callouts
Generated and reviewed files carry the agent's notes as callouts readable in any
markdown preview: a `> emoji **Label:**` line before the paragraph, a blank line, and
`==double equals==` around the fragment concerned. Labels are always in English. The
full set and the commands that act on them live in `feedback-4content`; the two
that generation skills write:
- `> 🤖 **AI wrote:**` + `==fragment==` — text the agent wrote because the source had
  nothing for it (a lead-in, a transition, a short explanation). The human removes
  the callout and the `==` after checking. Until then, editing and feedback skills
  leave the paragraph alone.
- `> ➕ **Must add:**` — a standalone paragraph where only the author can supply the
  material (numbers, checklists, internal examples, an open decision), with a
  one-line note of what is needed. Never filled in by the agent.
