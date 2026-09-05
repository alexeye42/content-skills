---
name: create-outline-4content
description: Build an outline (n_outline.mkd) from a draft or braindump for an article. Use when the prompt says "build the outline" / "outline from draft".
---

# Create Outline (4content)

Build `n_outline.mkd` from a draft (`n_draft.mkd`) or braindump (`n_dump.mkd`) in the
piece folder. Outline structure and content rules are in `outline_rules.md`; formatting
in `format_rules.md`. Mainly invoked from `go4content`.

## Steps

1. Verify a draft (`n_draft.mkd`) or braindump (`n_dump.mkd`) is referenced. Resolve
   the audience per `audience_rules.md` (*Resolving the audience*).
   **Gap questions (braindump source only).** A braindump is usually incomplete:
   before outlining, ask through `qna-manager` — as the next round of `n_qna.md` —
   about the main thesis, the reader's takeaway, missing facts, placeholders, and
   which parts the author will write themselves. Outline from the answers; do not
   invent content the answers did not give.
   **Other channels (draft source only).** Before outlining a draft, ask through
   `qna-manager` (one question, recorded in `n_qna.md`): "If you plan to publish
   this piece in other channels too, now is the moment to create their folders
   with the same draft — which channels (suffixes)?" For each suffix named, create
   the sibling folder `N.n<suffix>-code` next to this one and put a copy of the
   draft there as `n<suffix>_draft.mkd`; copy nothing else, list the folders
   created, and continue with the current folder only. The other folders are
   run through the pipeline later, each with its own outline and sections.
   Channel versions differ in structure, so branching later — at the section
   files — is too late.
2. Check if `n_outline.mkd` exists:
   - If yes, analyze it to preserve existing content.
   - If no, create it and write the frontmatter.
   If the outline already has frontmatter or content, don't change it — append
   generated content to the end.
3. Under the frontmatter, write the title (the same as in the frontmatter) as a `#`
   heading.
4. Generate sections. A section is either:
   - found in the source (as a heading) — keep existing indices in headings; or
   - generated from the source content — check the headline for natural language and
     improve it if needed. Insert a heading for any headingless chunk over 400 words
     or one that mixes weakly-related topics.
5. Under each top-level section, add a `@section-code` reference (a section file to
   create later). The code starts with the section index, e.g. `@0-intro` or
   `@3-use-cases`. Put the section heading above each `@section-code`.
6. Follow the structure and content rules in `outline_rules.md` (its example outline
   is `references/example_outline.mkd` in this skill's folder), and
   `format_rules.md` for formatting.
