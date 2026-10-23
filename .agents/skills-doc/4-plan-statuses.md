# Plan statuses

`n_plan.mkd` moves through the statuses of `rules/plan_rules.md`. The planning
skills do not know the mode; they act on the status: it tells them where to start and
what to offer the human.

```mermaid
stateDiagram-v2
  [*] --> preliminary: discuss-ideas
  preliminary --> preliminary: a round of questions, find-ideas
  preliminary --> structured: create-plan
  [*] --> structured: create-plan without discussion
  structured --> reviewed: the human read it and said «ok»
  reviewed --> reviewed: check-plan adds remarks
  reviewed --> checked: «apply» — plan rewritten, Checks section
  checked --> [*]: create-draft
```

Not drawn: `check-plan` also works on a `structured` plan if the human skips the
review, and `create-draft` on a `structured` or `reviewed` one if the human skips the
check. In both cases the skill first offers the skipped step.
