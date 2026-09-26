---
name: go4content
description: Run the full article pipeline, from a braindump or a human draft to a finished article with title and subtitle. Invoke via "/go4content <path> [discuss|plan]" (also "go for content").
argument-hint: <path> [discuss|plan]
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
| **1B full** | medium | `n_dump.mkd` | [discuss ideas ⇄ find ideas] → plan (+ find facts on request) → plan review → check → draft → outline → sections |
| **1C draft** | maximal | `n_draft.mkd` written by the human | outline → sections |

Auto-detection: `n_draft.mkd` exists → 1C; the prompt says "discuss" or "full" → 1B
starting with the discussion of ideas; the prompt says only "plan" → 1B starting
with the plan; otherwise 1A. The detected mode is confirmed in round 0.

The mode names are for this file and the README only. **In chat, never name a mode
("1A", "1B"…)** — the human may not have read the README; describe the steps in
plain words instead.

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
   question). Questions, in the language of the user's prompt:
   - the detected mode, described in plain words, e.g. for 1B with the discussion:
     "First we discuss the ideas of your dump, then I build a plan and write the
     draft. Correct?"; for 1A: "I'll ask about the gaps in your dump and go straight
     to the section files. Correct?";
   - no suffix only: the audience and up to two personas; write the answer as the
     `## Audience` section of `n_qna.md` (`audience_rules.md`, *Resolving the
     audience*).
   Wait for the answers.

4. Pipeline by mode; pass the piece folder and the audience to each step:
   - **1A:** `create-outline-4content` (its gap questions go to `n_qna.md` as the
     next round) → `create-sections-4content`.
   - **1B:**
     1. With the discussion only: `discuss-ideas-4content`, round after round, until
        the human says enough (it offers `find-ideas-4content` itself).
     2. `create-plan-4content` — it offers `find-facts-4content`, asks the gap
        questions, and ends with the human's review of the plan.
     3. `check-plan-4content` — findings in the plan, then the rewrite on "apply".
        "apply" means rewrite the plan AND go on to the draft; on "apply and stop",
        stop after the rewrite and wait.
     4. `create-draft-4content`. Then announce the next steps in plain words, in the
        language of the user's prompt: "The draft is ready: `n_draft.mkd`. Next I'll
        split the article into sections, one file per section, and then we'll polish
        it: either I edit and you check, or I mark up my remarks and you edit."
     5. `create-outline-4content` → `create-sections-4content`.
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
- The skills of 1B know nothing about modes: they act on the plan's status and
  sections (`plan_rules.md`).
