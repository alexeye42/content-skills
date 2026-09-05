---
name: create-sections-4content
description: Create or update section files (n-*.md) from the outline for an article. Use when the prompt says "create section files" / "split into sections".
---

# Create Sections (4content)

Create or update section files (`n-section-code.md`) from `n_outline.mkd` in the piece
folder. Outline rules are in `outline_rules.md`; generate content per `article_rules.md`
+ `writing_rules.md` + `format_rules.md`. Mainly invoked from `go4content`.

## Steps

1. Check that `n_outline.mkd` exists. If not, output an error and stop.
2. Verify the outline contains `@section-code` references. If none, output a warning
   and stop.
3. **Draft as-is check** (only if the folder contains `n_draft.mkd`). A draft that is
   already final can be split into section files VERBATIM by
   `scripts/draft-to-sections.py` (in this skill's folder) instead of being
   regenerated. Check ALL of the
   conditions below; if one fails, go to step 4:
   - the draft is entirely in the piece's target language (`audience_rules.md`,
     *Resolving the language*);
   - it is finished prose, not notes to expand; no `<TBD>`, `<TODO>`, or
     `<placeholder>` tags;
   - no section files exist yet (otherwise this is an update — step 5).

   If every condition holds, ask the human through the agent's question tool (in
   chat if there is none): **split the draft as is** (recommended) or **generate the
   sections from the draft with improvements**? Their answer decides. If the prompt
   already says "as is", skip the question (the conditions are still checked). 
   To split, run from the project root
   ```
   python3 <this skill's folder>/scripts/draft-to-sections.py <folder>/n_draft.mkd
   ```

   The file names come from the outline's `@` codes in order (the script warns and
   falls back to heading-derived names if the counts differ — treat that as a failed
   condition and fix the outline first). Check the run's output lists one file per
   code, commit via `git-commit-flow` (author `ai`), and stop.

4. For each top-level section that has a `@section-code` reference, create or update
   the section file `n-section-code.md`:

   **If the folder contains `n_draft.mkd`:**
   - Find the part of the draft for this section and use it to fill the section file.
   - Translate the draft content into the piece's target language
     (`audience_rules.md`, *Resolving the language*) if needed, or copy it with
     grammar and style corrections if it is already in that language.
   - If the draft has brief ideas rather than complete text, expand them.
   - Do NOT create any image references.

   **Otherwise (no `n_draft.mkd`):**
   - Fill the section file with the outline's content for this `@section-code`
     (including section heading(s)), except the reference itself, using the
     braindump's own wording verbatim wherever it exists (typo fixes only).
   - Where the outline needs text the braindump does not have (a lead-in, a
     transition, a short explanation), write it briefly under a `🤖 **AI wrote:**`
     callout with the fragment in `==…==`.
   - Where only the author can supply the material (numbers, checklists, internal
     examples, a decision the Q&A left open), put a `➕ **Must add:**` callout with a
     one-line note instead of inventing it. Notation: *Agent callouts* in
     `format_rules.md`.

5. **For existing section files** (folder already has `n-section-code.md` referenced
   as `@section-code`), update rather than recreate:
   - Update the main section heading.
   - Add missing subsections; generate their content from the outline's content for
     that subsection (if any). Preserve existing subsections.

6. Follow `article_rules.md`, `writing_rules.md`, and `format_rules.md`
   when generating section content; the audience per `audience_rules.md`
   (*Resolving the audience*).
