---
trigger: model_decision
description: Per-type rules for long-form articles. Use when writing or editing an article or its section *.md files.
globs: ["**/*.md"]
---

# Article Rules

Per-type rules for long-form articles. They sit on top of the general rules:
- `writing_rules.md` — prose quality and content requirements (+ `writing_antipatterns.md`).
- `format_rules.md` — markdown formatting and placeholders.
- `audience_rules.md` — audience and per-channel voice.

## Usage
Whatever the action on the file (enhancing, drafting, writing sections), you must:
- meet the Content Requirements from `writing_rules.md`;
- meet the formatting in `format_rules.md`, with the heading override below;
- match the audience and channel voice from `audience_rules.md` (channel by suffix).

## Heading levels (override of format_rules defaults)
Per channel: the `Headings` field of the channel's section in `profile/audience.md`
(channel by the folder-name suffix, `audience_rules.md`). A channel without the
field, or a folder without a suffix, keeps the defaults — top-level `##`,
subsections `###`.

## Introduction and Conclusion
Determine whether the `*.md` file is an introduction ("intro" in the file name) or a
conclusion ("end" or "conclusion" in the file name).

- If this is an introduction:
  - The `###` heading is optional.
  - The first 2 paragraphs must be a) short and b) as engaging and intriguing as possible.
  - If TLDR is mentioned in the source, generate a `#### TL;DR` subsection: a few short
    paragraphs or numbered list items, each summarizing the essence of the corresponding
    section. At least two paragraphs/items must include internal links to the sections.
- If this is a conclusion:
  - Add a heading like `## Conclusion` (or `## What's next?` if this is not the final
    article of the series).
  - Summarize the whole article from a different perspective than the introduction and
    other sections.
  - If this is the final article of the series, add a final note as an important
    paragraph. Use a `<placeholder>` if you're unsure about it.
  - After a horizontal rule:
    - Either write about related things outside the scope of this article, followed by a
      paragraph about the next article on this topic with a "Stay tuned" or similar call.
    - Or write something appealing that provokes the reader's thoughts or actions.
