---
name: create-plan-4content
description: Build a content plan (n_plan.mkd) from source material before drafting an article. Use when the prompt says "make a plan" / "create a plan" / "plan for".
---

# Create Plan (4content)

Build the editorial plan for an article, before any draft. Output goes to
`n_plan.mkd` in the piece folder. The plan is an editorial schema, not a draft — do
not write polished phrasings that would leak into the text.

Work in the main context (no subagents).

## Steps

1. Read the source in full. Read `n_findings.mkd` if present (its data is more current
   than the source — prefer it on conflicts). Resolve the audience per
   `audience_rules.md` (*Resolving the audience*).
   **Gap questions.** If the source leaves the plan under-determined (missing facts
   or numbers, an unclear main thesis, placeholders, contradictions), ask through
   `qna-manager` as the next round of `n_qna.md` BEFORE writing the plan; what stays
   unanswered becomes an `[Insert …]` placeholder in the plan.
2. Load `article_rules.md` + `writing_rules.md` + `writing_antipatterns.md` +
   `audience_rules.md`.
3. Extract the key themes, numbers, facts, tool names, and code/other artifacts.
4. Build the structure per `article_rules.md`. For each block write: heading;
   one-sentence content; boundaries (includes / excludes); key facts; artifacts.
   - Keep every fact, tool, and artifact tied to exactly one block.
   - Build the structure from the reader's questions, not from the source's order.
5. Run the duplication check — list any fact that appears more than once and keep it
   in a single block. Write `n_plan.mkd` in the format below.

## n_plan.mkd format

```markdown
---
title: <draft title>
subtitle: <draft subtitle>
---

# Plan: <title>

## Source & facts
- Source: <path to braindump / source / n_findings.mkd>
- Tools / names: [...]
- Key numbers & facts: [...]
- Code / other artifacts: [yes/no, how many]

## Structure

### Block 1 — <heading>
- Content: <one sentence — what info goes here>
- Boundaries: includes [...]; excludes [...]
- Key facts: [...]

### Block 2 — <heading>
...

## Duplication check
- [facts mentioned more than once, and the single block where each stays]
```

## Rules
- Don't add information that isn't in the source or findings.
- Don't write "nice phrasings" — the plan is a schema; phrasings belong in the draft.
