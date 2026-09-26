---
name: discuss-ideas-4content
description: Think an article's ideas through with the human before planning - a preliminary plan (n_plan.mkd) with the thesis and ideas, rounds of questions in n_qna.md where the agent contributes its own ideas, until the human says enough. Use when the prompt says "discuss ideas" / "let's discuss the piece"; also invoked by go4content.
---

# Discuss Ideas (4content)

A discussion of the article's ideas with the human, before any structure. The agent
is a co-author here: it reads the source, proposes its own ideas, merges and
connections, points out weak spots and reader objections, and offers thesis variants.
The result is a preliminary `n_plan.mkd` — Source & facts, Thesis, Ideas — that
`create-plan-4content` turns into a structure. Format and content rules:
`plan_rules.md`.

Work in the main context (no subagents).

## Steps

1. **Inputs.** Read the source in full (usually `n_dump.mkd`; any other file or
   research folder named in the prompt). Resolve the audience per `audience_rules.md`
   (*Resolving the audience*). Check `n_plan.mkd`:
   - absent — create it with `status: preliminary`: Source & facts (the sources and
     the facts found in them), Thesis (your reading of the source's spine), Ideas
     (the source's ideas, your own ideas, and connections, each with its source).
   - `preliminary` — continue from it.
   - `structured` or later — the ideas are already structured: say so and stop.

2. **One round of questions**, 3–5 of them, through `qna-manager` as the next round
   of `n_qna.md`. The explanations are your substantive contribution: new ideas,
   merges of ideas, weak spots, objections a reader of this audience would raise,
   thesis variants. Each question carries your recommendation, so "yes" is a complete
   answer. Add your new ideas to the plan's Ideas section right away, with the
   source `(agent)`, so the human sees them in the plan too.

3. Commit via `git-commit-flow`, author `ai`. Wait for the answers.

4. **Update the plan.** If the human edited the plan or answered in the files,
   commit via `git-commit-flow`, author `human`, first. Then update the Thesis and
   Ideas by the answers: add accepted ideas, refine the ones the human adjusted,
   remove the ones they rejected (the rejection stays in `n_qna.md`).

5. **Ask whether to go on**, in the language of the user's prompt: "Shall I ask
   more questions, or is that enough? I can also search the web for ideas, examples,
   and objections to your thesis."
   - more questions — back to step 2;
   - a search — run `find-ideas-4content` (with what the human wants found, if they
     said), then back to step 2 with the found ideas as material;
   - enough — commit via `git-commit-flow` (author `ai`) and report in chat: the
     thesis in one line and the number of ideas in the plan. The status stays
     `preliminary`.

## What a useful contribution looks like
- **A spine, not a list.** A dump is usually a set of reasons or observations. Look
  for the one shift or claim they all serve; that is the thesis to propose.
- **A merge.** Two ideas that are the same mechanism seen from two sides ("the
  human sees defects" + "the human knows what matters now" → "the human is a cheap
  sensor of the situation").
- **The bait.** A tempting wrong conclusion the reader already holds, which the
  article refutes — a ready hook.
- **The objection.** Where a reader of this audience will argue, and how the claim
  survives it (often by narrowing it: "costly" instead of "impossible").
- **The missing resolution.** A problem the dump raises but does not resolve — ask
  whether this article resolves it or hands it over to another one.

## Rules
- Facts come only from the sources; ideas may be new (`plan_rules.md`, *Content
  rules*).
- NEVER open with a summary of the human's dump: they wrote it. Every round must
  add something they did not have.
- NEVER turn the ideas into sections or an order yet: a dump's order is rarely the
  article's order, and fixing it early kills the merges.
- NEVER let an `(agent)` idea carry a number, a study, or a name: a new idea is
  reasoning; its facts come from the sources or from a search.
- NEVER state a claim about AI (or any fast-moving field) as a limit in principle
  when the source only supports "today's models" or "at today's cost" — readers
  will refute it with the next release.
- Do not write Structure and do not mark ideas — both belong to
  `create-plan-4content`.
- No log of the reasoning: the current state is the plan, the decisions are the
  rounds of `n_qna.md`.
