---
name: improve4content
description: Orchestrate the AI edit of a whole article — file by file with the human reviewing each result as an uncommitted diff, lessons carried from the human's corrections to the next file, and title/subtitle options at the end. Invoke via "/improve4content <article-folder>" (also "improve the whole article" and similar prompts).
argument-hint: <article-folder> [instructions]
---

# improve4content (orchestrator)

The AI-editing counterpart of `review4content`: the agent rewrites, the human
corrects. Input is the WHOLE article (a piece folder); the work goes one section
file at a time so the human can review each result in the IDE diff view and the
agent can learn from the corrections before touching the next file. Ends with a
finished article, title and subtitle included.

Delegates to: `improve-article-4content` (one file), `git-commit-flow` (commits),
`metadata_rules.md` (title/subtitle).

## Steps

1. **Parse arguments:** the article folder (`N.n-piece-code`) and optional
   instructions (what to focus on, what never to touch). Resolve the audience per
   `audience_rules.md` (*Resolving the audience*); if unresolved, ask through
   `qna-manager` as an audience item before any edit, and pass the audience to
   every `improve-article-4content` call. Section files are the
   `n-*.md` files per `project_rules.md`, processed in file-name order; the outline
   and other `*.mkd` files are ignored.

2. Read the whole article once — the intro first (it sets the angle), then all
   sections — so every per-file edit keeps the piece consistent.

3. **Per file**, in order:
   1. **Commit check.** `git status --short` for the folder; if uncommitted changes
      exist, commit via `git-commit-flow` (author `human/ai` after a reviewed AI
      edit, `human` otherwise — never `ai`) BEFORE editing. NOT AFTER: the human
      reviews the agent's output as an uncommitted diff (a deliberate exception to
      committing right after generation).
   2. Run `improve-article-4content` on this one file, passing the instructions and
      the **lessons** collected so far.
   3. Stop. Tell the human which file is done and wait for the signal ("next",
      "done", etc.). The human may edit the file meanwhile.
   4. **Lessons.** Re-read the file and compare it with the version you produced
      (still in context): what the human reverted, softened, or rewrote, and what
      they left alone. Post 3–5 lines of PATTERNS to chat (not phrases) and carry
      them into the next file's instructions. Write nothing to files.

4. **Title and subtitle.** After the last file, judge the current title/subtitle (or
   post text) and write the options block at the top of the intro file per
   `metadata_rules.md`. Wait for the human's choice ("title 2" / "subtitle 1" /
   "post 1" or a hand edit); apply it and delete the callout block.

5. **Finish.** Commit check as in 3.1 (author `human/ai`). Report in chat: files
   edited, the patterns learned, and the final title/subtitle. Then, check if 
   any markup is left in the section files. The markup includes `AI wrote`, `Must add`
   and other callouts (>), `<TODO>`, `<TBD>` and similar tags. If no markup is left,
   propose to assemble the whole article into one file.

6. **Build.** Once the human confirms, run the assembling script from the project
   root (it lives in the `go4content` skill folder):
   ```
   python3 <go4content skill folder>/scripts/sections-to-markdown.py <folder>
   ```

   The script concatenates the `*.md` section files in file-name order (the Q&A
   file excluded) into `<folder>/dist/<folder-name>.md`. On successful run,
   report the output path; the `dist` file is not committed, as it's gitignored.

## Commands the human may give at any point

- **"redo this file"** (optionally with instructions) — step 3 again on the current
  file, starting with its commit check.
- **"skip"** — leave the current file as is and move on.

## Notes

- Never edit two files in one pass; the diff view is the human's review surface.
- Never read or modify the outline; it may be stale.
- Paragraphs under `AI wrote` / `Must add` callouts (`format_rules.md`) are left
  untouched; remind the human of the ones still open in the final report.
- No inline feedback markup here — for that flow use `review4content`.
