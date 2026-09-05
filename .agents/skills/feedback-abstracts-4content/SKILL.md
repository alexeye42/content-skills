---
name: feedback-abstracts-4content
description: Strict inline feedback on an article's framing parts — title and subtitle (three options each), introduction and conclusion — processed together. Use when the prompt says "feedback on the intro and conclusion", "title options"; also invoked by review4content as its last part.
---

# Feedback Abstracts (4content)

The framing of an article is read by everyone, so it is checked more strictly than
the middle sections: the introduction and conclusion at `strict` level, the title
and subtitle stricter still — with alternatives, because a title is chosen, not
fixed. Delegates the prose work to `feedback-4content`.

## Input

- The article folder (the intro file has "intro" in its name; the conclusion has
  "end" or "conclusion"), or the two files explicitly.
- Title and subtitle (or the post text): located per `metadata_rules.md`.
- Optional: audience / personas, patterns from earlier parts, the channel
  (`audience_rules.md`, *Resolving the channel*).

## Steps

1. Read the whole article (all section files) — the framing can only be judged
   against what the article delivers.

2. **Intro and conclusion:** run `feedback-4content` in review mode with the `strict`
   flag on both files (same markup, scores to chat). Add one check for the
   conclusion: it must sum the article up from a different angle than the
   introduction (`article_rules.md`), not restate it. If it fails, report that as
   the conclusion's overall suggestion even when the scores are 9–10.

3. **Title and subtitle:** judge the current ones against the requirements in
   `metadata_rules.md` (promise-accuracy, appeal, limits; single 1–10 score each),
   then write the options block at the top of the intro file in the *Options
   notation* of that file. Report the scores in chat as a separate line (inside
   `review4content` they stay out of its per-section table).

4. **Selection.** As in `metadata_rules.md`: the human edits by hand or says
   "title 2" / "subtitle 1" / "post 1"; apply and delete the callout block.

## Notes

- On request ("re-score the title"), judge the current title/subtitle again — score
  only, no new options — so the orchestrator gets a "new" value for its final table.
- The review markup is committed by the caller (`review4content`). Apply, accept,
  revert and remove-markup commands work (and commit) as in `feedback-4content`.
