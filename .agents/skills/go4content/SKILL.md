---
name: go4content
description: Run the full article pipeline, from a braindump or a human draft to a finished article with title and subtitle. Invoke via "/go4content <path> [plan]" (also "go for content").
argument-hint: <path> [plan]
---

# go4content (orchestrator)

Run the full article pipeline, in the main context, step by step (no subagents).
Each step runs only after the previous one completes. The pipeline ends with a
finished article: sections revised and the title/subtitle chosen.

See `README.md` in this folder for the human's guide (install, cases, prompt words,
example sessions).

## Modes

| Mode | Human effort | Source | Pipeline |
|---|---|---|---|
| **1A quick** | minimal | `n_dump.mkd` (braindump, usually incomplete) | gap questions → outline → sections (`AI wrote` / `Must add` callouts for what the dump lacks) |
| **1B full** | medium | `n_dump.mkd` | [find facts] → plan → check-plan gate → draft → outline → sections |
| **1C draft** | maximal | `n_draft.mkd` written by the human | outline → sections |

Auto-detection: `n_draft.mkd` exists → 1C; the prompt says "plan" or "full" → 1B;
otherwise 1A. The detected mode is confirmed in round 0.

## Steps

1. Parse `<path>` from the arguments. If no piece folder is given, ask the user:

   > Provide the piece folder name as `N.n-piece-code`, where `N` is a 3-digit topic
   > number, `n` is the piece index/suffix (1, 2m, 3ru…), and `piece-code` is a short
   > slug. Example: `206.1m-content-skills`.

   Create the folder per `project_rules.md` if it doesn't exist. Detect the mode and
   the channel (`audience_rules.md`, *Resolving the channel*). Read the source in full.

2. **Commit check.** `git status --short` for the folder; commit uncommitted changes
   via `git-commit-flow` (author `human` or `human/ai`) before any generation.

3. **Round 0** through `qna-manager`, recorded as the first round of `n_qna.md`
   (the file is created now; `qna-manager` first asks its own "file or inline"
   question). Questions:
   - the detected mode — "1A, correct?";
   - 1B only: run `find-facts-4content` first? (skip the question if the prompt
     already says "find facts");
   - no suffix only: the audience and up to two personas, as the **audience item**
     (`audience_rules.md`, *Resolving the audience*).
   Wait for the answers.

4. Pipeline by mode; pass the piece folder and the audience to each step:
   - **1A:** `create-outline-4content` (its gap questions go to `n_qna.md` as the
     next round) → `create-sections-4content`.
   - **1B:** `find-facts-4content` (if chosen) → `create-plan-4content` (gap
     questions before the plan) → `check-plan-4content` (block until the plan is
     explicitly approved) → `create-draft-4content` → `create-outline-4content` →
     `create-sections-4content`.
   - **1C:** `create-outline-4content` → `create-sections-4content`.

5. **Final revision.** Ask the user (in chat, or with the agent's question tool if one
   exists) which way to go:
   A. AI edits the article — run `improve4content` on the piece folder;
   B. the user rewrites it themselves from AI feedback — run `review4content` on
      the piece folder.
   Run the chosen skill. Either way the pipeline ends with a finished article,
   title and subtitle included.

## Notes
- Run each step in the main context, sequentially; do not start a step before the
  previous one is complete.
- Each step is one of the `*4content` skills above; the other channels of a piece
  are offered by `create-outline-4content` when it outlines a draft (see
  `README.md`, *Second channel*).
