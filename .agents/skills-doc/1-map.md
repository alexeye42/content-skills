# Skills map

The orchestrators are frames; the skills they run sit inside. Services used by
almost every skill are badges on the cards instead of arrows (see the legend).

```mermaid
flowchart TB
  H(("Human"))

  subgraph GO["go4content ❓💾🗂 — full pipeline"]
    direction TB
    subgraph S1["Stage 1 · create the article"]
      direction LR
      DI["discuss-ideas ❓💾⛔"]:::optional
      FI["find-ideas"]:::optional
      CP["create-plan ❓💾⛔"]
      FF["find-facts"]:::optional
      CK{{"check-plan 💾⛔"}}
      CD["create-draft 🗂"]
      CO{{"create-outline ❓💾⛔"}}
      CS["create-sections 📜💾🗂"]
      DI -.->|"on offer"| FI
      CP -.->|"on offer"| FF
      DI --> CP --> CK --> CD -->|"split"| CS
      CO -->|"generate"| CS
    end
    subgraph S2["Stage 2 · revise: A or B ⛔"]
      direction TB
      subgraph IMP["improve4content ❓💾⛔📜🗂<br/>the AI edits"]
        IA["improve-article"]
      end
      subgraph REV["review4content ❓💾⛔📜🗂<br/>the human edits"]
        FA["feedback-abstracts ⛔"]
        FB["feedback 💾"]
        FA -->|"strict"| FB
      end
    end
    S1 --> S2
  end

  H -->|"/go4content"| GO

  subgraph LEG["Legend"]
    direction LR
    L1["❓ asks the human<br/>(qna-manager)"]
    L2["💾 commits<br/>(git-commit-flow)"]
    L3["⛔ stops and waits<br/>for the human"]
    L4["📜 runs<br/>a script"]
    L5["🗂 updates CONTENT.md<br/>(sync-4content)"]
    L6["optional<br/>step"]:::optional
    L7{{"gate: the<br/>human approves"}}
    L1 ~~~ L2 ~~~ L3 ~~~ L4 ~~~ L5 ~~~ L6 ~~~ L7
  end
  GO ~~~ LEG

  classDef optional stroke-dasharray: 5 5
```

- **Stage 1** has two roads to the section files. In case 1B the sections are
  **split** from a draft written to a plan; the discussion of ideas is optional
  (the words `discuss` / `full` turn it on), and both web searches run only if the
  human accepts the offer of `discuss-ideas` or `create-plan`. In case 1A
  (braindump) and 1C with a rough draft the sections are **generated** from an
  outline the human approves at the gate; a final draft of 1C is split as is
  ([go4content process](2-go4content.md)).
- **Stage 2** is two orchestrators of their own: `go4content` hands the article to
  one of them, and the human can also start either one directly
  (`/improve4content`, `/review4content`).
- Every content skill can also be run directly by its prompt words
  ([matrix](README.md#where-each-skill-is-used)).
