# Content base

The topics and pieces of this project: what each is about, its status and dates. Kept up to date by `sync-4content` and by the human's statements (`.agents/rules/project_rules.md`, *Content base*).

## Properties

Conventions for the topic and piece entries below.

- `## Topics`: one entry per top-level folder `N-topic-code`. A topic may be a series of articles or a broader group of related ones.
- `## Pieces`: one entry per piece folder `N.n<suffix>-code` (where suffix defines a channel), ordered by `start_date`. The heading is the folder name; the path is `<topic>/<heading>`. A planned piece without a folder is `### planned-<slug>`: it gets its final number / folder name when its dump appears. `000-*` folders are not listed.
- An empty property is not written. All dates are `YYYY-MM-DD`.

| Property | Where | Required | Value |
|---|---|---|---|
| `topic` | piece | yes | the top-level folder name |
| `status` | piece | yes | see *Statuses* |
| `summary` | topic, piece | yes, except for `planned` status | 1–2 sentences: what the topic is about, or the main thesis of the piece |
| `start_date` | topic, piece | yes | the date of the first commit with the folder name |
| `dump_date` | piece | for `dumped` and later, if there was a dump | the day the dump was written |
| `draft_date`, `written_date`, `ready_date` | piece | no | the day the status was reached |
| `publication_date`, `publication_url` | piece | for `published` | the publication date and address |
| `variant_of` | piece | no (yes for a version in another channel) | the original piece's folder |
| `target_date` | piece | no | the planned publication date |

A date is set when its status is reached and never changes afterwards.

### Statuses

The status only grows.

| Status | When |
|---|---|
| `planned` | the piece idea is recorded; there is no folder or it is empty |
| `dumped` | `n_dump.mkd` exists — the source for a quick or full `go4content` run |
| `drafted` | `n_draft.mkd` exists |
| `written` | section files exist, none with a `🤖 AI wrote` or `➕ Must add` callout |
| `ready` | the piece went through the AI edit (`improve4content`) or the feedback revision (`review4content`), and the human said it is ready; a built file in `dist/` does not matter |
| `published` | published; `publication_date` and `publication_url` are set |

## Topics

### 207-agent-skills
- summary: <what the topic is about>
- start_date: 2026-01-15

## Pieces

### 207.2m-agent-skills
- topic: 207-agent-skills
- status: drafted
- summary: <the main thesis of the piece>
- start_date: 2026-01-15
- dump_date: 2026-01-15
- draft_date: 2026-01-20
