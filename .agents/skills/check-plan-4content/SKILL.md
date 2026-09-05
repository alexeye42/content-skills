---
name: check-plan-4content
description: Adversarially review a content plan (n_plan.mkd) and gate it on human approval. Use when the prompt says "check the plan" / "review the plan".
---

# Check Plan (4content)

Adversarially review `n_plan.mkd` and gate it on explicit human approval. You review
in the main context and rewrite the plan yourself — do not delegate; you're faster
and won't break the gathered facts.

## Review criteria

1. Flow: each block moves the argument forward, not treading water.
2. Filler test: "can this block be removed with no loss to the reader?" — if yes, cut it.
3. Fact value: ask "why does the reader need this?" of every fact.
4. Duplication: no single point living in two blocks.
5. Plan ≠ draft: remove polished "nice phrasings" — they leak into the text; the plan
   is an editorial schema.
6. Missing material: if the plan lists an artifact or fact absent from the
   findings/source, ask the user at approval; if not provided, leave an explicit
   "[Insert …]" placeholder — never invent.
7. Size sanity: one block = one task/idea; merge kindred aspects, never glue different
   tasks together.

Article criteria sit on top: the intro/conclusion rules from `article_rules.md`;
findings data overrides the source.

## Steps

1. Read `n_plan.mkd` in full. Load `article_rules.md` + the criteria above + the
   findings/source for cross-checking.
2. Apply the criteria and **rewrite the plan yourself** where needed.
3. **Approval gate:** show the plan and a short report of what you changed. Wait for
   explicit approval ("ok", "go", "write"). Do NOT proceed to drafting
   until the plan is explicitly approved.
