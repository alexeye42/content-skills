---
name: create-plan-4content
description: Build the structured content plan (n_plan.mkd) of an article from its sources or from a preliminary plan of discussed ideas, then hand it to the human for review. Use when the prompt says "make a plan" / "create a plan" / "plan for".
---

# Create Plan (4content)

Build the editorial plan of an article: the thesis and the block structure the draft
will follow. Output goes to `n_plan.mkd` in the piece folder; its format, statuses,
and content rules are in `plan_rules.md`. The plan is a schema, not a draft — no
polished phrasings. It is always read by the human before it moves on.

Work in the main context (no subagents).

## Steps

1. **Inputs.** Resolve the audience per `audience_rules.md` (*Resolving the
   audience*). Check `n_plan.mkd`:
   - `preliminary` — build from it: its Source & facts, Thesis, and Ideas are the
     material; read the sources it lists as well.
   - absent — build from the source in the prompt (usually `n_dump.mkd`) and any
     `n_findings.mkd` in the folder.
   - `structured` or later — the plan is already built: say so and stop, unless the
     human explicitly asked to rebuild it.

2. **Offer a web search.** Always ask, even if `n_findings.mkd` already exists
   (question tool, or chat), in the language of the user's prompt: "Do you want me
   to find links on the web that support your ideas, examples that illustrate them,
   or other facts?" On yes, run `find-facts-4content` with what the human wants
   found, then continue. On no, build the plan from what there is.

3. **Gap questions.** If the material leaves the plan under-determined (missing facts
   or numbers, an unclear thesis, placeholders, contradictions), ask through
   `qna-manager` as the next round of `n_qna.md` BEFORE writing. Your own proposals
   — a thesis restating an existing idea, a connection between ideas, a possible
   turn — go into these questions as recommendations (*Content rules* in
   `plan_rules.md`). What stays unanswered becomes an `[Insert …]` placeholder.
   Unless the source or an earlier round already says, the round always includes:
   "Is this a standalone article, a part of a series that continues, or its final
   part?" — the answer goes into `series` (step 5).

4. Load `plan_rules.md` + `article_rules.md` + `writing_rules.md` +
   `writing_antipatterns.md` + `audience_rules.md`.

5. **Write the plan** per `plan_rules.md`:
   - Source & facts — list every source used; extract the key themes, numbers,
     facts, tool names, and artifacts.
   - Thesis — write it if missing; keep the discussed one otherwise, unless the gap
     answers changed it.
   - Ideas (if the section exists) — mark every idea `[Accepted]`, `[Transformed]`,
     `[Parked]`, or `[Rejected]`; never edit its text.
   - Structure — build it from the reader's questions and the thesis, not from the
     source's order; the hook, the turn (if any), and the ending are blocks with the
     matching `Role`. Keep every fact and artifact tied to exactly one block.
   - Frontmatter — draft `title` and `subtitle` (the first version); `series`;
     `status: structured`.

6. Commit via `git-commit-flow`, author `ai`.

7. **Review.** Stop and tell the human, in the language of their prompt: "The plan
   is in `n_plan.mkd`. Read it, edit anything you like, then say ok." Wait. On the
   signal: if the human changed the file, commit via `git-commit-flow` (author
   `human`); then set `status: reviewed` (the status line travels with the next
   commit).

## Rules
- Facts come only from the sources; no new ideas at this step — only connections
  and restatements of existing ones (`plan_rules.md`, *Content rules*).
- Don't write "nice phrasings" — the plan is a schema; phrasings belong in the draft.
- NEVER write the thesis as a topic ("AI agents and people at work"): it must be a
  claim a reader could disagree with, or the blocks have nothing to converge on.
- NEVER give a block the `Role` "background" or "context" by default: a block
  either supports the thesis, answers an objection, turns it, or goes.
- NEVER mark an idea `[Rejected]` silently for being inconvenient to the structure:
  if it is strong, it is `[Parked]` and the human sees it at the review.
