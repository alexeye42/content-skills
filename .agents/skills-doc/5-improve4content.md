# improve4content process

The AI edits, the human reviews — one file at a time, so that the human's
corrections become lessons for the next file.

```mermaid
flowchart TD
  s(["/improve4content folder [instructions]"]) --> aud{"Audience<br/>known?"}
  aud -->|"no"| q["❓ qna-manager →<br/>## Audience in n_qna.md"]
  aud -->|"yes"| read
  q --> read["Read the whole article,<br/>intro first"]
  read --> f["Next file n-*.md"]
  f --> c["💾 commit check<br/>human or human/ai, never ai"]
  c --> ia["improve-article-4content<br/>+ instructions + lessons"]
  ia --> stop{{"⛔ The human reviews the uncommitted diff,<br/>edits, says «next»"}}
  stop -->|"redo"| c
  stop -->|"skip"| more
  stop -->|"next"| les["Lessons: 3–5 patterns<br/>from the human's edits"]
  les --> more{"More files?"}
  more -->|"yes"| f
  more -->|"no"| t["Title / subtitle / post options<br/>at the top of the intro"]
  t --> pick{{"⛔ «title 2», «subtitle 1»<br/>or a hand edit"}}
  pick --> fin["💾 commit, 🗂 sync-4content, report"]
  fin --> mk{"Markup<br/>left?"}
  mk -->|"yes"| rem(["Remind of the open<br/>AI wrote / Must add"])
  mk -->|"no"| b{{"⛔ Build the article?"}}
  b --> build[["📜 sections-to-markdown.py → dist/"]]
```

The commit comes **before** the AI's edit, not after: the human reviews the edit as
an uncommitted diff in the IDE.
