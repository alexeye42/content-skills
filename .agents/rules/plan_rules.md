# Plan Rules

The content plan `n_plan.mkd` of an article: its statuses, sections, and what the
agent may put into it. The plan is an editorial schema, not a draft. Used by
`discuss-ideas-4content`, `find-ideas-4content`, `create-plan-4content`,
`check-plan-4content`, and `create-draft-4content`.

## Frontmatter

```
---
status: preliminary | structured | reviewed | checked
title: <draft title>
subtitle: <draft subtitle>
---
```

`title` and `subtitle` are required from `structured` on; before that they are
optional.

## Statuses

| Status | Set by | What the plan gains |
|---|---|---|
| `preliminary` | `discuss-ideas-4content` | Source & facts, Thesis, Ideas |
| `structured` | `create-plan-4content` | Structure; Thesis if it was missing; marks on Ideas |
| `reviewed` | `create-plan-4content`, on the human's "ok" after reading the plan | the human's own edits |
| `checked` | `check-plan-4content`, after the rewrite | Checks |

A status only moves forward. A human edit after `checked` does not reset it. A plan
may skip `preliminary` (built directly by `create-plan-4content`).

## Sections

In this order; a section appears only once the status that brings it is reached.

### `## Source & facts`
- The sources, one per line. Typical ones are `n_dump.mkd` and `n_findings.mkd`;
  any other file (including notes of a general research outside the piece
  folder) or URL is allowed.
- Then the key facts, numbers, names, and artifacts (code, checklists) taken from
  them.
- On a conflict between sources, the more recent one wins; name both in the plan.

### `## Thesis`
The spine only: the article's main claim in 1–2 sentences — what the article argues
and what every block converges on. The hook, the turn, and the ending are NOT part of
the thesis; they are blocks of Structure.

### `## Ideas`
Exists only when the plan was started by `discuss-ideas-4content`; its absence is
normal. One idea per bullet, followed by its source in brackets: `(dump)`,
`(human)`, `(findings: <URL>)`, `(agent)` — a new idea the agent proposed in the
discussion, `(agent: connection)` — a thought connecting existing ideas.

- While the status is `preliminary`, the section is a workspace: ideas are added,
  refined after the human's answers, or removed when the human rejects them.
- From `structured` on, the text of an idea is never edited. `create-plan-4content`
  puts exactly one mark at the start of each bullet:
  - `[Accepted]` — in the plan as is;
  - `[Transformed]` — in the plan partially or modified, the rest dropped or parked;
  - `[Parked]` — not for this article (may serve another one);
  - `[Rejected]`.

### `## Structure`
Written by `create-plan-4content`, built per `article_rules.md`. One subsection per
block:

```
### Block N — <heading>
- Role: <the block's job in the argument: hook, support for the thesis, objection,
  turn, ending…>
- Content: <one sentence — what the block tells the reader>
- Boundaries: includes […]; excludes […]
- Key facts: […]
- Artifacts: […]
```

The hook, the turn (if any), and the ending are blocks with the matching `Role`.

### `## Checks`
Written by `check-plan-4content` after the rewrite: a record of what was checked. One
subsection per criteria group, each with a one-line verdict and a list of what was
changed, what the human declined, and what stays as `[Insert …]`:
- `### Argument` — the thesis holds; the strongest reader objection is addressed;
  the turn is earned; limits of particular studies are not presented as limits in
  principle.
- `### Flow` — every block moves the argument forward; filler test; block size.
- `### Facts` — why the reader needs each fact; missing material.
- `### Duplication` — facts that appeared more than once and the single block where
  each one stays.
- `### Plan ≠ draft` — polished phrasings removed (only if there were any).

## Content rules

- **Facts** (claims about the world: numbers, studies, names, prices, dates) come
  only from the sources in Source & facts, in every skill. What is missing becomes an
  `[Insert …]` placeholder; never invent it.
- **Ideas while discussing.** `discuss-ideas-4content` may propose new ideas of its
  own (source `(agent)`) — generating ideas together with the human is its job. The
  human accepts or rejects them.
- **Ideas while planning and checking.** `create-plan-4content` and
  `check-plan-4content` add no new ideas. Allowed:
  - thoughts connecting existing ideas, including a turn;
  - a thesis that restates or realizes an existing idea — not a thesis that is a new
    idea.

  Such contributions are proposed to the human as a question or shown to them at the
  plan review.
- **Plan ≠ draft.** No polished phrasings: they leak into the text.
- Every fact and artifact is tied to exactly one block of Structure.
- The structure follows the reader's questions and the thesis, not the order of the
  source.
