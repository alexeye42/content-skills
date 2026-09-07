---
name: qna-manager
description: Ask the human clarifying questions through the best available channel (agent question tool, chat, or a *_qna.md file) and keep every round recorded in the qna file. Invoked by orchestrator skills that need answers or want an exchange recorded; also when the user says "ask questions", "clarify first".
---

# qna-manager

One entry point for every question an orchestrator skill wants to ask the human. The
caller supplies the questions; this skill decides the channel, asks, waits, and
records the round in the Q&A file so the decision history lives in one place.

## Input from the caller

- **Round title** — e.g. "Round 2 — section split".
- **Questions** — each with an explanation (context, contradiction found, your
  recommendation) and the question itself; optionally 2–4 answer options with one
  marked *(recommended)*.
- **Q&A file** — path, or the file/folder the task is about (the name is derived,
  see *Q&A file*).
- Optional **`record: no`** — ask but do not write to the file (e.g. an
  orchestrator's own round 0 about its work plan; this skill's automatic channel
  question from *Channel selection* step 1 still fires on that first call).

## Channel selection

1. **Question tool** — the first time this skill runs in a session and a question
   tool exists, ask ONE question through the tool: "Should every round go to a
   `_qna.md` file, or should I ask inline (question tool when available, chat
   otherwise)?" Remember the answer for the session; it decides file vs inline only —
   "inline" still prefers the tool per step 2. Tools by agent:
   - Claude Code (and Claude Cowork, which runs the same agent engine — verify in
     practice): `AskUserQuestion` — 1–4 questions per call, 2–4 options each.
   - Codex: `request_user_input` — silently unavailable unless
     `[features] default_mode_request_user_input = true` is set in `config.toml`;
     if the call does nothing, tell the user about the flag and fall back to chat.
   - Antigravity IDE: `notify_user`.
   - Cursor, Windsurf, Copilot, others: no tool → chat.
2. **Per round:** the user chose "file", OR the round has 5+ questions → **file**.
   Otherwise → the **tool** (≤4 questions per call), or **chat** when no tool exists.
3. A round asked in chat or through the tool is still written to the Q&A file
   afterwards, with the answers filled in. The human's answers are copied
   verbatim (trimmed), never paraphrased.

## Question principles

- One question per item; never bundle two questions into one `Qn`.
- No "X or Y?" alternatives: commit to a recommendation and let the user correct it.
  > ❌ "Should the file go to the post folder, or the project root?"
  > ✅ "I'll put the file in the post folder. Correct? (If not, name the location.)"
- Open questions by default, phrased so that "yes/ok" is a complete answer; add a
  hint that invites details. Use options (A, B, C[, D], the last one open — "Other,
  please specify") when the choice space is known.
- Count: 3–5 for one main unknown, 6–10 for several independent unknowns, never more
  than 12 per round. When in doubt, ask fewer — another round is cheap.
- Language: the language of the user's prompt, unless requested otherwise.

## Q&A file

Name ends with `_qna.md`. If the caller gave no path: use the folder of the file the
task is about; base the name on that file's prefix (`123_draft.md` → `123_qna.md`;
`1-intro.md` in `205.1ru-x/` → `1_qna.md`). Without any file reference, invent a
2-word task name (`section-split_qna.md`) and ask the user to correct it.

If a `*_qna.md` already exists in the location, read it: if it belongs to the current
task, append; otherwise create a new file with a numeric suffix (`1_qna.md` taken
→ `1-2_qna.md`) and tell the user which name you picked.

```
### Q&A: <Task title>
<1–2 sentences of task context>

## Round 1 Questions (<MM/DD/YYYY>)

### [Section X]

Q1: <explanation + question>
A1: <blank for the user, or the answer received via tool/chat>

Q2: <explanation + question>
   A. <option, 3–10 words>
   B. <option> (recommended)
   C. Other (please specify)
A2:
```

Rounds are numbered consecutively across the file.

Callers may keep their own fixed sections right under the file title (e.g. the
`## Audience` section of `audience_rules.md`); this skill never writes or edits
them and appends rounds below them.

### Recording an exchange

A caller may also ask to record something that was NOT asked as a question — e.g.
the human's reaction in chat to a suggestion the agent made. Such an exchange is an
ordinary round: the agent's statement as `Qn`, the human's words as `An` (blank
when the human said they will answer in the file). Nothing is recorded before the
human reacts.

## Waiting and resuming

- File channel: write the file, then tell the user in chat:
  > Questions are in `<path>`. Answer inline and type "replied" when done.
  Stop and wait. On resume, scan for blank `An:` items in ALL rounds; if any, list
  them and ask the user to fill them in before proceeding.
- Tool/chat channel: wait for the answers, then record the round.
- Return the answers to the caller in a compact form (question id → answer).

## Anti-patterns

- Never print questions to chat when the channel is the file.
- Never rewrite or "clean up" earlier rounds or the human's answers.
- Never invent an answer for a blank item.
