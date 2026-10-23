# go4content process

From a folder with a braindump or a draft to section files, then to one of the two
revision orchestrators. Hexagons are the places where the agent stops and waits for
the human.

```mermaid
flowchart TD
  start(["/go4content folder [discuss | plan]"]) --> parse["Folder N.n-code, channel,<br/>mode by files and prompt,<br/>🗂 sync-4content"]
  parse --> c1["💾 commit check"]
  c1 --> r0{{"❓⛔ Round 0 (qna-manager):<br/>the steps in plain words — correct?<br/>audience, if no suffix<br/>1C: other channels, final or rough"}}
  r0 --> mode{"Mode"}

  mode -->|"1A quick<br/>n_dump.mkd"| CO
  mode -->|"1B, «discuss»<br/>or «full»"| DI
  mode -->|"1B, «plan» only"| CP
  mode -->|"1C, final draft"| SPL
  mode -->|"1C, rough draft<br/>or «improve»"| CO

  DI["discuss-ideas-4content<br/>❓ a round of questions, 💾"] --> more{{"⛔ More questions,<br/>a search, or enough?"}}
  more -->|"more"| DI
  more -->|"search"| FI["find-ideas-4content"]
  FI --> DI
  more -->|"enough"| CP

  CP["create-plan-4content"] --> ffq{{"⛔ Find links,<br/>examples, facts?"}}
  ffq -->|"yes"| FF["find-facts-4content"]
  ffq -->|"no"| gaps
  FF --> gaps["❓ gap questions →<br/>plan structured, 💾"]
  gaps --> rev{{"⛔ Plan review:<br/>the human edits, «ok»"}}
  rev --> CK["check-plan-4content:<br/>remarks as callouts in the plan, 💾"]
  CK --> react{{"⛔ «Should NOT …», answers,<br/>then «apply»"}}
  react --> RW["plan rewritten,<br/>Checks section, 💾"]
  RW -->|"apply"| CD["create-draft-4content 🗂"]
  RW -.->|"apply and stop:<br/>pause"| CD
  CD --> ch{{"❓⛔ Other channels?"}}
  ch -.->|"suffixes"| SIB[/"sibling folders<br/>with a copy of the draft 🗂"/]
  ch --> SPL

  CO["create-outline-4content<br/>❓ gap questions"] --> og{{"⛔ Outline gate:<br/>the human edits, «ok», 💾"}}
  og --> GEN["create-sections-4content:<br/>generate from the outline 💾🗂"]

  SPL["create-sections-4content:<br/>⛔ missing headings,<br/>📜 split as is, translate 💾🗂"]

  SPL --> fin{{"⛔ Revision:<br/>A — the AI edits, B — the human edits"}}
  GEN --> fin
  fin -->|"A"| IMP[["improve4content"]]
  fin -->|"B"| REV[["review4content"]]
  IMP --> done(["Finished article,<br/>title and subtitle chosen"])
  REV --> done
```

In chat the agent never names a mode by its code: round 0 describes the steps in
plain words ("First we discuss the ideas of your notes, then I build a plan and write
the draft. Correct?").
