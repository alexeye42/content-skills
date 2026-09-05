---
name: review4content
description: Orchestrate a feedback-driven revision of an article — split into parts, inline feedback per part, the human's own edits, diff lessons after each part, framing parts last, final before/after score table. Invoke via "/review4content <article-folder> [audience/personas] [instructions]" (also "review the article" and similar prompts).
argument-hint: <article-folder> [audience] [instructions]
---

# review4content (orchestrator)

Runs the "feedback by parts → the human rewrites → next part" cycle for one article,
in the main context, step by step. The agent marks up; the human edits; the agent
learns from the diff before the next part. Nothing is stored between parts except
in this session — the final table is built from the chat history (write a handoff
note if the session context may be lost, listing per part its initial score lines
and the accumulated patterns).

Delegates to: `feedback-4content` (a part), `feedback-abstracts-4content` (framing),
`qna-manager` (questions and general feedback), `git-commit-flow` (commits).

## Steps

1. **Parse arguments:** the article folder (`N.n-piece-code`), optional audience /
   personas (at most two — they override what is stored), optional instructions
   (remark limit, "strict everywhere", what never to flag). Resolve the audience per
   `audience_rules.md` (*Resolving the audience*); if it is unresolved, the audience
   question joins round 0 as a `qna-manager` audience item. Section files are the `n-*.md` files per `project_rules.md`;
   the outline and other `*.mkd` files are ignored.

2. **Commit check.** `git status --short` for the folder; commit uncommitted changes
   via `git-commit-flow` (author `human` or `human/ai`) BEFORE any markup.

3. **Round 0 (never written to the Q&A file).** Read the intro first — it sets the
   angle for judging every other section — then all sections. Propose the split
   into parts per `profile/editorial.md` (*Review parts*); the intro and the
   conclusion form the LAST part together. Ask through
   `qna-manager` with `record: no`: is the split ok? — plus the audience item when
   needed (that one is always recorded). (`qna-manager` asks its own "file or
   inline" question on this first call — do not ask it here.) Wait for the
   confirmation.

4. **Per part**, in the confirmed order:
   1. `feedback-4content`, review mode: the files of the part, the audience, the
      intro as context, the patterns collected so far, the remark limit and any
      "strict everywhere" / never-flag instructions from step 1. Scores and overall
      suggestions go to chat; the overall suggestions are also handed to
      `qna-manager` for the *General feedback* section (it creates the Q&A file on
      first use, whatever channel the questions go through).
   2. Commit via `git-commit-flow`, author `ai`.
   3. Stop. The human edits the files by hand (or asks to apply the feedback —
      see *Commands*). Wait for the signal ("done", "I edited it").
   4. Commit via `git-commit-flow`, author `human`.
   5. **Diff lessons:** `git diff` of the two commits (without git: compare the files
      with the versions you marked up, still in context). Post 3–5 lines of PATTERNS to
      chat — not individual phrases: which callouts were accepted, which were
      ignored (and what they had in common), where strictness was off, what the
      author does with long sentences, and so on. Keep these patterns for the next
      parts; write nothing to files.
   The last part goes through `feedback-abstracts-4content` instead of
   `feedback-4content`, then the same commit → edit → commit → diff-lessons cycle;
   the human resolves the title/subtitle options ("title N" / "subtitle N") before
   that part's `human` commit, so no options callout stays open.

5. **Final table.** Run `feedback-4content` in score mode over all sections and
   `feedback-abstracts-4content` re-scoring for the title/subtitle; print one table:
   sections × criteria, each cell `initial → new` (e.g. `7 → 9`), with the
   title/subtitle line separately. "Initial" is always the score from the part's
   FIRST review pass — a redo never overwrites it. 
   Under it, list the cross-cutting problems that remain, if any.
   Finally, check if any markup is left in the files; if no, propose to assemble 
   the whole article into one file.

6. **Build.** Once the human confirms, run the assembling script from the project
   root (it lives in the `go4content` skill folder):
   ```
   python3 <go4content skill folder>/scripts/sections-to-markdown.py <folder>
   ```

   The script concatenates the `*.md` section files in file-name order (the Q&A
   file excluded) into `<folder>/dist/<folder-name>.md`. On successful run,
   report the output path; the `dist` file is not committed, as it's gitignored.

## Commands the human may give at any point

- **"redo part N"** (optionally with a limit; the default is in `profile/editorial.md`,
  *Review parts*) —
  step 4 again for that part, on the current text.
- **"apply feedback"** / "apply except …" / "remove markup" / "remove all markup"
  — delegated to `feedback-4content` apply mode for the current
  part.
- **"title 2"**, **"subtitle 1"** — delegated to `feedback-abstracts-4content`.

## Notes

- The resolved audience and personas are passed to every feedback call unchanged;
  never invent personas.
- Never read or modify the outline; it may be stale. Title/subtitle handling is
  inside `feedback-abstracts-4content`.
