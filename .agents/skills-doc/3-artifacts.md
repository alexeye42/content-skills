# Artifact flow

Files are parallelograms, skills are rounded boxes. `n_plan.mkd` is one file that
moves through statuses ([plan statuses](4-plan-statuses.md)); the edge labels show
the status after a step. An outline appears only where the sections are generated:
from a braindump (1A) or a rough draft (1C). A draft written to a plan (1B) and a
final human draft (1C) are split by a script as is.

```mermaid
flowchart TD
  H(("Human"))
  dump[/"n_dump.mkd"/]
  findings[/"n_findings.mkd"/]
  plan[/"n_plan.mkd"/]
  draft[/"n_draft.mkd"/]
  outline[/"n_outline.mkd"/]
  sections[/"n-*.md<br/>sections"/]
  dist[/"dist/N.n-code.md"/]
  export[/"dist/…html,<br/>Google Doc"/]
  base[/"CONTENT.md"/]

  DI("discuss-ideas")
  FI("find-ideas")
  FF("find-facts")
  CP("create-plan")
  CK("check-plan")
  CD("create-draft")
  CO("create-outline")
  SPLIT[["📜 draft-to-sections.py"]]
  GEN("create-sections:<br/>generate")
  IA("improve-article")
  FB("feedback<br/>feedback-abstracts")
  BUILD[["📜 sections-to-markdown.py"]]
  EXP[["📜 markdown-to-html.py,<br/>html-to-gdoc.py"]]
  SYNC("sync-4content")

  H -->|"1A, 1B"| dump
  H -->|"1C"| draft
  dump --> DI
  DI -->|"preliminary"| plan
  plan --> FI
  FI --> findings
  FI -->|"+ Ideas"| plan
  dump --> FF --> findings
  dump --> CP
  findings --> CP
  plan <-->|"structured"| CP
  plan <-->|"callouts → checked"| CK
  plan --> CD
  CD --> draft
  dump -->|"1A"| CO
  draft -->|"1C rough"| CO
  CO --> outline
  outline --> GEN
  dump -->|"1A: verbatim"| GEN
  draft -->|"1B, 1C final"| SPLIT
  GEN --> sections
  SPLIT --> sections
  sections <-->|"2A: edits in place"| IA
  sections <-->|"2B: callouts ==…=="| FB
  sections --> BUILD --> dist
  dist -.->|"on request"| EXP --> export
  SYNC --> base
```

Not drawn, to keep the picture readable:
- `n_qna.md`: `qna-manager` writes it for `go4content`, `discuss-ideas`,
  `create-plan`, `create-outline`, `improve4content`, and `review4content`; every
  skill reads its `## Audience` section.
- The calls to `sync-4content`: `go4content`, `create-draft`, `create-sections`,
  `improve4content`, and `review4content` run it; it derives the status of the
  piece's entry from the files in the folder.
