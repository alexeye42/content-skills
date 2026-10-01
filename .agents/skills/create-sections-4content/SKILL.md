---
name: create-sections-4content
description: Create or update section files (n-*.md) of an article - generate them from an approved outline (n_outline.mkd), or split a plan-based or final draft (n_draft.mkd) by its headings as is, translating it if the channel's language differs. Use when the prompt says "create section files" / "split into sections" / "split the draft as is"; also invoked by go4content.
---

# Create Sections (4content)

Create or update the section files (`n-section-code.md`) of a piece folder. Two
inputs, chosen by what the folder has:
- **`n_outline.mkd`** (a braindump or a rough draft, outline approved at the gate) →
  **generate** the sections from the outline (step 3);
- **no outline, `n_draft.mkd`** (a plan-based draft or a final human draft) →
  **split** the draft by its headings (step 2).

Outline rules: `outline_rules.md`; generate content per `article_rules.md` +
`writing_rules.md` + `format_rules.md`, for the audience per `audience_rules.md`
(*Resolving the audience*). Mainly invoked from `go4content`.

## Steps

1. **Pick the input.**
   - Section files already exist: with an outline → step 4 (update); without one →
     list them and ask the human whether to re-split or stop. Re-splitting needs
     `--force`, which overwrites only files of the same name, so delete the old files
     first — only with the human's yes: they may already carry the human's edits.
   - An outline exists → step 3. If it has no `@section-code` lines, warn and stop.
   - No outline, a draft exists → step 2.
   - Neither → error: "Nothing to create sections from — run `create-outline-4content`
     on the braindump first." Stop.

2. **Split the draft.**
   1. **Final or rough?** Skip this check when the draft came from
      `create-draft-4content` (the folder has `n_plan.mkd`): a plan-based draft is
      always split. Otherwise the draft is final when BOTH hold:
      - it is finished prose, not notes to expand;
      - it has no `<TBD>`, `<TODO>`, or `<placeholder>` tags.

      If it is rough, say so, offer to run `create-outline-4content`, and stop. If it
      is final, ask the human through the agent's question tool (in chat if there is
      none): **split the draft as is** (recommended) or **improve it**? "Improve"
      means the outline route: offer `create-outline-4content` and stop. If the
      prompt already says "as is", or `go4content` already asked, skip the question.
   2. **Headings.** A chunk longer than 400 words without a heading, or one that mixes
      weakly related topics, needs a top-level heading of its own. Commit the draft
      first if it has uncommitted changes (`git-commit-flow`, author `human` for the
      human's draft, `ai` for a plan-based one). Insert the missing headings into
      `n_draft.mkd` itself at the draft's existing top-level level (`##` or `###`; in
      a draft with no headings, the channel's level per `article_rules.md`) — the
      script splits on `##` as soon as one `##` exists, so a single `##` in a `###`
      draft swallows every `###` section. Demote `#` section headings (a Google Docs
      export) to that level too; only the title stays `#`. List the headings in chat
      and wait for the human's "ok" — they may fix them in the file first. On "ok",
      commit the draft (`human/ai` if they edited it, otherwise `ai`), so the split
      commit holds only the new files.
   3. **Split** by script, from the project root. The split is verbatim: polishing
      belongs to stage 2 (`improve4content` / `review4content`), and a mixed commit
      hides what changed.
      ```
      python3 <this skill's folder>/scripts/draft-to-sections.py <folder>/n_draft.mkd
      ```
      File names come from the headings, numbered by position (`0-intro`,
      `1-<slug>`, …, `<N>-conclusion`). Check the output lists one file per
      top-level section. If the draft had no `#` title, write the first version of
      the title and subtitle into the intro file as in step 3. Commit via
      `git-commit-flow` (author `ai`).
   4. **Translate** only if the draft is not in the piece's target language
      (`audience_rules.md`, *Resolving the language*): translate each section file in
      place per `writing_rules.md`, rename it after its translated heading (keep the
      number), and commit via `git-commit-flow` (author `ai`) — a separate commit,
      so the translation is a diff against the split. Then return.

3. **Generate from the outline.** For each top-level section with a `@section-code`
   line, create `n-section-code.md` with the section heading(s) from the outline
   (not the `@` line), re-levelled to the channel's headings (`article_rules.md`;
   the outline always uses `###`/`####`), and text built from its points:
   - unmarked point → the source's own wording (from `n_dump.mkd`, `n_draft.mkd`, or
     the human's answer in `n_qna.md`): verbatim with typo fixes for a braindump,
     expanded into prose without new thoughts for a rough draft; translated into the
     target language when the source is in another one;
   - `(AI)` point → brief text under a `🤖 **AI wrote:**` callout with the fragment in
     `==…==`;
   - `(Must add)` point → a `➕ **Must add:**` callout with a one-line note of what is
     needed, never invented.

   Notation: *Agent callouts* in `format_rules.md`. Every `(AI)` and `(Must add)`
   point keeps its callout: the callouts are the human's only map of what to check.
   No image references.
   The intro file starts with the title as its top `#` heading and the subtitle as a
   `<!-- comment -->` under it — the first version, written from the content
   (`metadata_rules.md`; the channel's post-text rule applies).

4. **Add sections** (the human reopened the outline, e.g. added a section): create
   the files for `@section-code` lines that have no file yet, as in step 3. Leave the
   existing files untouched — they are the current text (`outline_rules.md`,
   *Lifecycle*).
