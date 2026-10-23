# How the content skills fit together

Diagrams of the `*4content` skill system, one per file. They render on GitHub; in an
IDE preview you may need a mermaid extension.

Read them top-down — each level answers its own question:

1. [Skills map](1-map.md) — which skills each orchestrator runs.
2. Processes and files:
   - [go4content process](2-go4content.md) — order, branches, and human stops of
     creating an article;
   - [Artifact flow](3-artifacts.md) — which file is made from which;
   - [Plan statuses](4-plan-statuses.md) — how the content plan moves from discussion
     to draft;
   - [improve4content process](5-improve4content.md) — the AI edits, the human
     reviews;
   - [review4content process](6-review4content.md) — the AI marks up, the human
     edits.
3. [Life of a callout](7-callouts.md) — the markup protocol inside the feedback
   skills.

## Legend

| Shape / badge | Meaning |
|---|---|
| frame | an orchestrator, or a stage of one |
| box | a content skill |
| double-sided box | a call to another orchestrator or a script |
| hexagon | the agent stops and waits for the human (a gate) |
| parallelogram | a file |
| dashed border | an optional step |
| ❓ | asks the human through `qna-manager` |
| 💾 | commits through `git-commit-flow` |
| ⛔ | waits for the human's answer or edits |
| 📜 | runs a script |
| 🗂 | updates `CONTENT.md` through `sync-4content` |

Cases of `go4content`: **1A** braindump → outline → generated sections; **1B**
[discussion of ideas] → plan → check → draft → split; **1C** your own draft → split
as is (or, for a draft of notes, outline → generated sections).

## Where each skill is used

A number is the step in the pipeline; ×N means once per file or part. Case 1C has
two roads: final draft (split) / rough draft (outline).

| Skill | Role | 1A | 1B | 1C | improve4content | review4content | Prompt words |
|---|---|---|---|---|---|---|---|
| `go4content` | orchestrator | ● | ● | ● | — | — | `/go4content` |
| `discuss-ideas-4content` | content ❓💾⛔ | — | 1 (optional) | — | — | — | "discuss ideas" |
| `find-ideas-4content` | content | — | inside 1, on offer | — | — | — | "find ideas" |
| `create-plan-4content` | content ❓💾⛔ | — | 2 | — | — | — | "make a plan" |
| `find-facts-4content` | content | — | inside 2, on offer | — | — | — | "find facts" |
| `check-plan-4content` | content 💾⛔ | — | 3 | — | — | — | "check the plan" |
| `create-draft-4content` | content 🗂 | — | 4 | — | — | — | "write the draft" |
| `create-outline-4content` | content ❓💾⛔ | 1 | — | — / 1 | — | — | "build the outline" |
| `create-sections-4content` | content 📜💾🗂 | 2 (generate) | 5 (split) | 1 (split) / 2 (generate) | — | — | "create section files", "split the draft as is" |
| `improve4content` | orchestrator | 3A | 6A | 2A / 3A | ● | — | `/improve4content` |
| `improve-article-4content` | content | | | | ×N files | — | "improve the article" |
| `review4content` | orchestrator | 3B | 6B | 2B / 3B | — | ● | `/review4content` |
| `feedback-4content` | content 💾 | | | | — | ×(k−1) parts, score at the end | "give feedback" |
| `feedback-abstracts-4content` | composite ⛔ | | | | — | last part, re-score | "title options" |
| `qna-manager` | service | round 0, gaps | round 0, discussion, gaps, channels | round 0 (channels), gaps | audience | round 0, reactions | "ask questions" |
| `sync-4content` | service 🗂 | ● | ● | ● | at the end | at the end | "update the content base" |
| `git-commit-flow` | service | ● | ● | ● | ● | ● | — |
