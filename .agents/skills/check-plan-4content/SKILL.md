---
name: check-plan-4content
description: Adversarially check a content plan (n_plan.mkd) in two steps - mark up the findings in the plan, then, after the human's reaction, rewrite the plan and record the checks. Use when the prompt says "check the plan" / "review the plan".
---

# Check Plan (4content)

Adversarial check of `n_plan.mkd`, split into two steps with the human's feedback
between them: first the findings are marked up in the plan, then the plan is
rewritten by the human's reaction. Format, statuses, and content rules:
`plan_rules.md`.

Work in the main context (no subagents).

## Criteria

Argument:
1. The thesis holds: every block supports it, none contradicts it.
2. The strongest objection a reader of this audience would raise is addressed.
3. The turn, if there is one, is earned by the blocks before it.
4. Limits of particular studies or models are not presented as limits in principle.

Form:
5. Flow: each block moves the argument forward, not treading water.
6. Filler test: "can this block be removed with no loss to the reader?" — if yes, cut it.
7. Size sanity: one block = one task/idea; merge kindred aspects, never glue
   different tasks together.
8. Fact value: ask "why does the reader need this?" of every fact.
9. Missing material: an artifact or fact the plan lists but the sources lack.
10. Duplication: no single point living in two blocks.
11. Plan ≠ draft: no polished "nice phrasings" — they leak into the text.

Article criteria sit on top: the intro/conclusion rules from `article_rules.md`.
Everything the check adds obeys *Content rules* in `plan_rules.md`: no new facts, no
new ideas.

## Step 1 — Check

1. Read `n_plan.mkd` in full and the sources it lists. Resolve the audience per
   `audience_rules.md` (*Resolving the audience*): criterion 2 is judged for it. By
   status:
   - `reviewed` — go on;
   - `structured` — the human has not read the plan yet: say so and offer to wait
     for their review; go on if they say so;
   - `checked` — re-check only on an explicit request (the Checks section is then
     rewritten);
   - `preliminary` or no plan — stop: the plan needs `create-plan-4content` first.
2. Apply the criteria. Write each finding as a callout right in the plan, in the
   notation of `feedback-4content` (*Markup*): `> ‼️ **Must improve:**`,
   `> 💬 **Should improve:**`, `> ✂️ **Should shorten:**` (a whole block or bullet is
   redundant), `> ➕ **Should add:**` (missing material — say what is needed), with
   the fragment concerned in `==…==`. Labels in English; the text in the language of
   the user's prompt. Do NOT change the plan's text in this step.
3. Commit via `git-commit-flow`, author `ai`.
4. Stop. Tell the human how many findings are in the plan and how to react, in the
   language of their prompt: "Change a label to `Should NOT …` to decline a finding,
   answer here, or supply the missing material — then say apply." Wait.

## Step 2 — Rewrite

Triggered by "apply" (with optional exclusions: "apply except the finding on block
4" works like `Should NOT`).

1. Apply every finding the human did not decline, following their answers. Where
   the human supplied missing material, add it; where not, leave `[Insert …]`. If
   the human has already edited a place themselves, their edit stands.
2. Remove every callout and `==…==` from the plan.
3. Write the `## Checks` section per `plan_rules.md`: per criteria group, a one-line
   verdict and what was changed, declined, or left as `[Insert …]`.
4. Set `status: checked`. Commit via `git-commit-flow`, author `ai`.
5. Report in chat briefly: what changed in the plan and what stays open.
