---
trigger: model_decision
description: Use it if asked to do something with an outline; a piece folder `*.*-*` or `*_outline.mkd` file may be referenced to denote the outline.
---

## File Naming
Folder name `N.n-piece-code`, outline file name `n_outline.mkd` and section file names `n-section-code.md` have the same n. 

## Outline Structure
- The outline must contain YAML frontmatter enclosed by `---` lines. 
  - The frontmatter has three mandatory fields: `layout: article` or `layout: book`, `title: <see the guidelines below>`, `subtitle: <see the guidelines below>`. 
  - If this is part of the series or a book, the frontmatter must contain two more fields: `part: <n>` and `final: <true or false>`.
- The outline must contain a list of section headings.
  - Each section heading must be preceded by a blank line.
  - Each top-level section heading must start with `###`, subsection headings must start with `####`.
- Lines with `@section-code` means references to `*-section-code.md` file .
- Content lines without `#` and `@` are optional. If they exist, they are eligible to %Content Rules%.

## Title and Subtitle Guidelines
- **Title**: must be appealing and promise value.
- **Subtitle**: must use concrete terms and be straight to the point (not wordy).
- Length and case limits: `profile/editorial.md`, *Metadata limits*.

## Content Rules
- **When writing an outline:**
  - Outline content must consist of source section summaries, each of ~3 sentences length, in the piece's target language (`audience_rules.md`, *Resolving the language*).
  - If a source section is no more than 4 sentences, just copy its content instead of summarizing.
  - Use `references/example_outline.mkd` in the `create-outline-4content` skill folder as an example outline, if another example is not given in the prompt.
- **When creating or generating sections,** use `format_rules.md`.