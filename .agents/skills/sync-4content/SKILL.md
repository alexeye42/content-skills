---
name: sync-4content
description: Bring the content-base entry (CONTENT.md) of one piece folder in line with its files - add the entry if missing, raise the status, set the dates and the summary. Invoked by other *4content skills after they create a folder or a file; also when the prompt says "update the content base".
argument-hint: <piece-folder> [variant_of=<entry>]
---

# Sync (4content)

`CONTENT.md` in the project root is the content base: the topics and the pieces with
their statuses and dates. Its format is its own `## Properties` section; read it
first. If `CONTENT.md` does not exist, do nothing and return: the project does not
keep a content base.

Input: one piece folder `<topic>/<N.n-code>`; optionally `variant_of` — the entry
heading of the piece this folder is a channel version of (`go4content`, *Other
channels*). Without a folder ("update the content base"), sync every piece folder of
the topic folders (`000-*` excluded), one commit for all.

## Steps

1. **Find the entry** `### <folder name>` in `## Pieces`. None → create it, placed by
   `start_date`, with `topic` (the top-level folder), `start_date` (today) and
   `variant_of` if given. A topic without a `## Topics` entry gets one: `summary`
   from the pieces it holds, `start_date` today.

2. **Status by the files.** The highest that holds; the status only grows, so a lower
   result leaves the entry as is. `ready` and `published` are never set here: the
   human states them (`project_rules.md`, *Content base*).

   | Status | Sign in the folder |
   |---|---|
   | `planned` | empty folder |
   | `dumped` | `n_dump.mkd` |
   | `drafted` | `n_draft.mkd` (in older folders `n_draft.md`) |
   | `written` | section files `n-*.md`, none with a `🤖 **AI wrote:**` or `➕ **Must add:**` callout |

   On a raise, set the date of each status reached on the way (`dump_date`,
   `draft_date`, `written_date`) to today, unless it is already set.

3. **Summary.** Write it when the entry has none or the status was raised: 1–2
   English sentences with the main thesis, from `n_outline.mkd`, else `n_plan.mkd`
   (its Thesis), else the intro of `n_draft.mkd` or of the section files, else
   `n_dump.mkd`.

4. If invoked by the human prompt (not by another skill), **commit** via `git-commit-flow`, author `ai`, only `CONTENT.md`:
   `fix(content-base): ai updated <entry heading> in CONTENT.md`. 
   Otherwise, `CONTENT.md` must be committed by the skill that invoked this one, along with its own work.

## Notes
- Touch only the entry of this folder (and its topic when created); never reorder or
  rewrite other entries unless the human requests it.
- Empty properties are not written; dates are `YYYY-MM-DD`.
