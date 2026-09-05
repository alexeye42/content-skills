# go4content — the article pipeline, for humans

`go4content` turns a braindump or a draft into a finished article: section files,
revised text, chosen title and subtitle. It orchestrates a family of `*4content`
skills; you rarely need to call them by name — this guide lists the words that
trigger each step, so you can drive the process without reading the skill files.

Two stages, each with cases:

1. **Create the article** — 1A quick / 1B full / 1C draft.
2. **Revise the article** — 2A the AI edits / 2B the AI gives feedback, you edit
   (with or without "apply").

## Install

The skills ship in https://github.com/alexeye42/content-skills — a ready writing
workspace. Its `README.md` covers cloning, the one-time `.claude` setup script for
Claude and Cursor, `git-commit-flow`, and adding the skills to an existing project.

The only files meant for you to edit are the two profile files:

- `rules/profile/audience.md` — your audience, your author notes (native language,
  voice), your channels: for each one its folder suffix, language, heading levels,
  title+subtitle or post text, audience.
- `rules/profile/editorial.md` — how strict the feedback is, what it never flags,
  the score anchors, the review part size, the title/subtitle limits.

## Before you start

- A piece folder `N.n-piece-code` (e.g. `207.2m-agent-skills`). The letters after
  the digit are the channel suffix, defined in `rules/profile/audience.md` (in this
  project: `m` Medium, `ss` Substack, `in` LinkedIn, `ru` Russian version). **No
  suffix means a custom audience** — the agent will ask who you are writing for (and
  up to two personas) and keep the answer in `n_qna.md`.
- Your source in that folder: `n_dump.mkd` (a braindump: notes, a post, fragments) or
  `n_draft.mkd` (a draft you wrote yourself).
- The agent asks questions through its question tool when it has one; otherwise in
  chat or in `n_qna.md`. On the first question it asks which you prefer: **file** or
  **inline**. Every round is recorded in `n_qna.md` either way. When questions go to
  the file, answer inline and type `replied`.

## Stage 1 — creating the article

| Case | Your effort | You provide | What the agent does | Skills, in order |
|---|---|---|---|---|
| **1A quick** | minimal | `n_dump.mkd` | asks about the gaps, builds the outline, writes the sections; what the dump lacks is written briefly under a `🤖 AI wrote` callout, what only you can supply becomes a `➕ Must add` callout | `create-outline-4content` → `create-sections-4content` |
| **1B full** | medium | `n_dump.mkd` | optional fact research, an editorial plan you approve, a full draft, then outline and sections | [`find-facts-4content`] → `create-plan-4content` → `check-plan-4content` → `create-draft-4content` → `create-outline-4content` → `create-sections-4content` |
| **1C draft** | maximal | `n_draft.mkd` | outline and sections from your draft (translated to the channel's language if needed, light grammar fixes); if the draft is final, the agent offers to split it into sections **as is** by script instead | `create-outline-4content` → `create-sections-4content` |

Start: `/go4content <folder>`. The agent detects the case (`n_draft.mkd`
present → 1C; the word `plan` or `full` in your prompt → 1B; otherwise 1A) and
confirms it in **round 0** together with the audience question (custom audience
only) and, for 1B, whether to research facts first.

Prompt words for the individual steps (when you want to run one by hand):

| Step | Say | Output |
|---|---|---|
| Research | `find facts` | `n_findings.mkd` |
| Plan | `make a plan` | `n_plan.mkd` |
| Plan review gate | `check the plan`, then `ok` / `approved` | — |
| Draft | `write the draft` | `n_draft.mkd` |
| Outline | `build the outline` | `n_outline.mkd` |
| Sections | `create section files` (add `as is` to split a final draft verbatim by script) | `n-*.md` |
| Questions on demand | `ask questions`, `clarify first` | `n_qna.md` |

After the sections exist, go through the callouts (same notation as in stage 2):

```
> 🤖 **AI wrote:** <what the agent had to make up>

A paragraph where ==this fragment== came from the agent, not from your dump.

> ➕ **Must add:** <what only you can supply — numbers, a checklist, an example>
```

Remove an `AI wrote` callout and its `==` once you have checked the text; replace
each `Must add` with your material. Revision skills leave both alone until you do.
Then move to stage 2.

## Second channel

Versions of one article for different channels differ in structure, so they live in
sibling folders that share the draft, not the sections. When
`create-outline-4content` outlines a draft (case 1C, or 1B once the draft exists),
it asks whether you plan other channels; name the suffixes and it creates
`N.n<suffix>-code/` next to the current folder with a copy of the draft (e.g.
`1ss_draft.mkd`), nothing else. Finish the current article first, then run
`/go4content <sibling-folder>`: it takes case 1C, builds that channel's own outline
and sections (translating the draft if the channel's language differs), and offers
the same revision stage.

## Stage 2 — revising the article

`go4content` asks which way you want at the end of stage 1; you can also start
either skill directly on an existing folder.

| Case | Who edits | Start | Flow |
|---|---|---|---|
| **2A improve** | the AI | `/improve4content <folder>` | one file at a time; you review each result as an uncommitted diff in your IDE, fix what you dislike, say `next`; the agent learns from your fixes for the following files; at the end it offers title/subtitle options |
| **2B review** | you | `/review4content <folder>` | the article is split into parts (1–3 files); per part the agent marks the text up and scores it; you edit and say `done`; the agent reads your diff and adapts; the intro, conclusion, title and subtitle come last; a before/after score table closes the run |

Both cases end the same way: when nothing is left marked up in the files, the agent
offers to assemble the sections into one file in `dist/`.

### 2B markup you will see in the files

```
> 💬 **Should improve:** <why and what to aim for>

A paragraph with the ==weak fragment== highlighted.
```

- `💬 Should improve` — a reader would stumble here; your call.
- `‼️ Must improve` — a blunder (typo, grammar, broken meaning).
- `✂️ Should shorten` — the whole next paragraph is redundant.
- `➕ Should add` — something is missing; never applied by the agent on its own
  (`➕ Must add` and `🤖 AI wrote` from stage 1 are never touched at all).
- `🏷️ Title options` / `Subtitle options` / `Post options` (post-text channels
  such as LinkedIn) — three
  alternatives at the top of the intro file, one marked recommended.

### 2B — without "apply"

Edit the files yourself, delete the markup as you go, then say `done`. Any callout
you leave in place is fine — the agent only reads the diff.

### 2B — with "apply"

Say `apply feedback` and the agent rewrites every marked place itself. Each rewrite
lands next to the original: `new fragment ~~old fragment~~` (for a shortened
paragraph: the new paragraph, then the old one struck through). The callout of an
applied place disappears. You then read the diff and keep or drop each change.

**Steer it before applying**, right in the file, by editing the callout label:

| You write | The agent does |
|---|---|
| `Should NOT improve` (also `Must NOT improve`, `Should NOT shorten`) | removes that callout and its `==`, changes nothing |
| `I should improve` (also `I must improve`, `I should shorten`) | leaves the callout and the `==` in place for you; changes nothing |
| a plain-language exclusion in the prompt: `apply feedback except the shortenings in section 3` | same as `Should NOT` for those places |

**Clean up** with one of two commands. "Ordinary callouts" means all of them
except your `I …` reservations and the add-callouts (`Should add`, `Must add`,
`AI wrote`).

| Command | When | What it removes | What stays |
|---|---|---|---|
| `remove markup` | after `apply feedback` once you have skimmed the diff — or instead of it, when you edit by hand | ordinary callouts, their `==`, every `~~old~~` (the new text is kept) | `I …` callouts and add-callouts, with their `==` |
| `remove all markup` | the article is done | everything — but first the agent lists every `I …` and add-callout still in the files and asks you to confirm, so you don't lose a place you meant to fix | nothing |

Typical situations:

1. You applied, skimmed, and agree with everything → `remove markup`. What is left
   in the files: your `I …` callouts and the add-callouts — read the text once
   more against them, fix those places, then `remove all markup`.
2. You applied and fixed some new fragments by hand (in places X you rewrote the
   agent's version, in places Y you already deleted the `~~old~~`) → `remove markup`
   finishes the rest; your hand-cleaned places are simply skipped.
3. In places Z you want the OLD text back: delete the new fragment and the `~~`
   around the old one by hand — there is no revert command — then `remove markup`.
4. You do not want the agent's rewrites at all → edit the text yourself, then
   `remove markup` clears the ordinary callouts and keeps your `I …` ones for the
   final read.
5. `apply feedback` did not touch some callouts (you excluded them in the prompt,
   or marked them `I …`): the excluded ones go away with `remove markup`, the `I …`
   ones stay.

Other commands: `redo part 2` re-reviews a part with fewer remarks (1–2 per section
by default); `title 2` / `subtitle 1` / `post 1` picks a title option.

## Example sessions

### Minimum human effort (1A + 2A)

```
/go4content 207.2m-agent-skills
   (round 0: "1A quick, correct? Custom audience?" — the folder has the m suffix,
    so only the mode is asked)
ok
   (the agent asks 4–8 gap questions — main thesis, missing facts, what you will
    write yourself; in the file if you chose "file")
replied
   (outline → section files with AI wrote / Must add callouts → "AI edits or your edits?")
A
   (improve4content: file 1 edited; you glance at the diff, fix two sentences)
next
   (file 2 … last file; the agent reports what it learned from your fixes)
next
   (title/subtitle options appear at the top of the intro file)
title 1
subtitle 2
   (done — the agent commits and reports the final title and subtitle)
```

Between `next`s you replace the `Must add` parts and clear the `AI wrote` callouts
you have checked; the agent never fills those for you.

### Maximum human effort (1C + 2B without apply)

```
/go4content 208.1ss-hiring-agents
   (n_draft.mkd is in the folder → "1C draft, correct?")
ok
   (outline → sections from your draft → "AI edits or your edits?")
B
   (review4content round 0: "split into 3 parts — sections 1–2, 3–4, then intro +
    conclusion. Ok?")
ok
   (part 1 marked up; scores in chat: "1-code-specs — readability 8, wording 7,
    usefulness 9")
   ... you rewrite the flagged places by hand, delete the callouts ...
done
   (the agent commits, reads your diff, posts 3–5 lines of patterns, marks up part 2)
   ... you skim part 2's callouts: two of them you change to "Should NOT improve",
   one to "I should improve" ...
apply feedback
   (every other marked place is rewritten as "new ~~old~~"; the two NOT places are
    cleared; the "I" place is untouched; commit ai)
   ... you read the diff, rewrite one new fragment by hand ...
remove markup
   (all ~~old~~ gone, ordinary callouts gone; the "I should improve" callout stays;
    commit ai)
   ... you fix the "I" place yourself and delete its callout ...
done
   (commit human, diff lessons, last part: intro + conclusion markup, title/subtitle
    options)
   ... you edit, pick the title by hand ...
done
   (final table: every section "initial → new", title/subtitle line, leftovers)
```

## Related skills

- `improve-article-4content` — the single-file editor behind `improve4content`;
  say `improve the article <file>` for a one-off edit.
- `feedback-4content`, `feedback-abstracts-4content` — the per-part and
  intro/conclusion/title feedback behind `review4content`; say `give feedback on
  <files>` or `title options` for a one-off run.
- `qna-manager` — every question the pipeline asks goes through it; say `ask
  questions` to trigger a round yourself.
- `git-commit-flow` — commits happen automatically: `ai` right after the agent's
  markup, `human` after your edits, `human/ai` before an AI edit of a reviewed file.
  Public version: https://github.com/alexeye42/workflow-skills/tree/main/skills/git-commit-flow
