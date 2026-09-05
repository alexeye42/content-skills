---
name: feedback-4content
description: Give inline feedback on 1–3 section files of an article (callouts + ==highlights==, per-section scores in chat), apply or clean that feedback on command, or score sections only. Use when the prompt says "give feedback", "review the section", "apply feedback", "score the sections"; also invoked by review4content and go4content.
---

# Feedback (4content)

Inline feedback on a part of an article — 1 to 3 section files — for a human who
will rewrite the text themselves. The markup is readable in any markdown preview;
scores and overall suggestions go to chat. Three modes: **review** (default),
**apply**, **score**.

Rules to follow: `writing_rules.md` (+ `writing_antipatterns.md`),
`format_rules.md`, `article_rules.md` (heading levels by channel), `audience_rules.md`
(audience and channel). Calibrations — strictness, what never to flag, score
anchors — come from `profile/editorial.md`.

## Input

- 1–3 section files (`n-*.md`); other `*.mkd` files in the folder are ignored, the
  outline included.
- Optional: **audience / personas** (at most two personas; without them, resolve per
  `audience_rules.md` — *Resolving the audience* — and stop if unresolved); **patterns** learned from
  the human's edits of earlier parts; a **remark limit** (e.g. "1–2 per section" for
  a re-run); **strict** flag (used for intro and conclusion); the **article's intro**
  as context for the angle of the piece.

## Mode: review

### What to flag

Phrase level — only what a native reader would stumble on:
- wrong or weak word choice, grammar mistakes, typos;
- awkward expressions, overly long or over-structured sentences;
- unclear logical flow, poor transitions, vague pronoun references;
- heavy passive voice; headings inconsistent with each other or with the text.

Never flag: a paragraph under an `AI wrote` callout or a `Must add` paragraph (they
wait for the author), and the items of the *Never flag* list in
`profile/editorial.md` (formatting, links, the author's voice, missing facts).

**Strictness.** Two levels, defined in `profile/editorial.md` (*Strictness*): the
default for middle sections, and `strict` — set by the caller, normally for the
intro and conclusion. A **remark limit** caps the total number of callouts per
section, all types counted together. **Patterns** from the caller
override both (e.g. "the author keeps long sentences with lists — don't flag them").

**Shortening** is always on, but only for whole paragraphs with clearly redundant
content (repeats another paragraph, no value for the audience) — not "could be
tighter". The author decides, so mark generously among such paragraphs only.

### Markup

A callout line before the paragraph, a blank line, then the paragraph with the
fragment wrapped in `==double equals==`. Callout labels are ALWAYS in English,
whatever the article's language; the recommendation text is in the language of
the user's prompt.

```
> 💬 **Should improve:** <what is wrong and what to aim for>

Text of the paragraph with the ==weak fragment== highlighted.
```

| Callout | When | Highlight |
|---|---|---|
| `> 💬 **Should improve:**` | reading stumbles; the author may disagree | `==fragment==` |
| `> ‼️ **Must improve:**` | a blunder: typo, grammar error, broken meaning | `==fragment==` |
| `> ✂️ **Should shorten:**` | a whole paragraph is redundant; say what to keep, if anything | none — the callout targets the whole next paragraph |
| `> ➕ **Should add:**` | something is missing and the reader will notice; stands alone where the addition belongs | none |
| `> ➕ **Must add:**` | written by the generation skills (`format_rules.md`): author-only material; never filled by the agent | none |
| `> 🤖 **AI wrote:**` | written by the generation skills: the agent's gap text, awaiting the author's check | `==fragment==` |

- One callout per paragraph; several fragments in one paragraph are listed in one
  callout, in order, under the most severe label (`Must improve` wins).
- Highlights may sit inside headings (`## ==Weak heading==`).
- Do NOT change the text itself in review mode — only add callouts and `==…==`.

### Scores (chat only)

For each section, three criteria on a 1–10 scale:

1. **Readability** — sentences and cohesion.
2. **Wording** — choice of words and expressions, judged as a native editor would
   (the author's native language and voice: *Author* in the profile referenced from
   `profile/editorial.md`).
3. **Usefulness for the audience** — what the reader takes away: a decision or an
   action from some sections, understanding and the bigger picture from others.
   Both count. With personas, give one score per persona: `8/7`.

Scale anchors: `profile/editorial.md`, *Score anchors* — do not be harsher than
they say.

Chat output per section: one line `<section file> — readability 8, wording 9,
usefulness 8/7`, then an **overall suggestion** (one paragraph, above the level of
single phrases, no quotes): mandatory for ≤6, optional for 7–8, none for 9–10.
Nothing else — no quotes with alternatives, no repetition of the callouts.

When the caller asks for it (`review4content` always does), hand the overall
suggestions to `qna-manager` for its *General feedback* section, so the human can
respond there or in chat.

## Mode: apply

Triggered by "apply feedback" (or the orchestrator). Scope is all marked places,
regardless of callout type, with these exceptions:

- `Should add` is NEVER applied unless the human explicitly asks for that item;
  then write the missing paragraph at the callout's position and remove the callout.
  `Must add` and `AI wrote` are never touched by any command.
- Inline exclusions edited by the human: `Should NOT improve`, `Must NOT improve`,
  `Should NOT shorten` → remove the callout and the `==…==`, change nothing.
- Inline reservations: `I should improve`, `I must improve`, `I should shorten`
  → leave the callout and the highlight untouched, change nothing (the human will
  edit by hand).
- Free-form exclusions in the prompt ("don't apply the shortenings in section 3")
  work the same way.

For each remaining marked place:
- `==fragment==` → write the improved fragment, then the old one struck through:
  `new fragment ~~old fragment~~`.
- `Should shorten` → the shortened paragraph, then the old paragraph as a separate
  struck-through paragraph `~~…~~` (two paragraphs, not the inline pattern); if
  nothing is worth keeping, just strike the paragraph through.
- Remove the callout once applied.

Clean-up commands. "Ordinary" below means every callout except the human's
reservations (`I …`) and the add-callouts (`Should add`, `Must add`, `AI wrote`):
- **"remove markup"** — works with or without a prior apply: strip the ordinary
  callouts and their `==…==`; delete every `~~old~~` and keep the new text. Places
  the human already cleaned by hand are simply skipped. `I …` and add-callouts stay.
- **"remove all markup"** — the "article is done" command. First list in chat every
  `I …` and add-callout still in the files (file, label, first words) and ask for an
  explicit confirmation — the human may have overlooked them. Only then strip
  everything: all callouts, every `==…==`, every `~~old~~` (the new text stays).
There is no revert command: to keep the old text in a place, the human deletes the
new fragment and the `~~` by hand.
Commit every apply/remove run via `git-commit-flow`, author `ai`.

## Mode: score

Triggered by "score the sections" (or the orchestrator). Scores and overall
suggestions only, no markup — used by the orchestrator for the final table. Same criteria and anchors as in review mode.
