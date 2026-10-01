---
trigger: model_decision
description: General writing quality for any content — apply when writing, rewriting, translating, or editing prose. See writing_antipatterns.md for the marker checklist.
globs: ["**/*.md", "**/*.mkd"]
---

# Writing Rules

General prose quality for any content type. Per-type files (e.g. `article_rules.md`)
add specifics on top; `format_rules.md` covers markdown; `writing_antipatterns.md`
is the marker checklist; `audience_rules.md` says who you write for and in which tone.

The final judge is whether a paragraph reads like a native speaker talking to a colleague.
- If a construction is allowed by the rules but reads clunky — rewrite it.
- If it's flagged by the rules but reads natural and precise — keep it.

## Content Requirements

### When translating or re-writing
The text is in the piece's target language (`audience_rules.md`, *Resolving the
language*) and sounds natural to its native speakers.
- Accurately convey not only the literal meaning, but also nuances and tone.
- If some parts of the text are not in the target language, translate them into it.
- When re-writing:
  - Re-write only sentences that are hard to read, poorly written, redundant, or
    repetitive — to improve clarity and make them sound better.
  - Enrich the vocabulary and sometimes use idioms, especially semi-formal ones:
    at most one idiom per paragraph or list, comprehensible to non-native
    speakers when the text is in English.
  - Check the text for spelling, grammatical, and punctuation errors and fix them.
  - Change as little of the original text as possible: the text is the author's,
    and the requirements here are the only reasons to touch it.

### Anti-Fluff Policy (rewriting)
- **Be concise:** prefer the shorter expression. Keep the text as short as
  possible while fully preserving the original meaning and details.
- **No fluff adverbs/adjectives:** add no filler words for emphasis (e.g.
  "exactly", "practically", "safely", "effectively", "various", "pure", "sheer").
- **Keep it simple:** keep simple, clear words rather than replacing them with
  complex or formal ones (e.g. "massive" → "exorbitant", "much" → "considerably").
- **Preserve terminology:** repeat a term rather than switch to a synonym to avoid
  the repetition. Consistent terminology (e.g. repeating "step" instead of
  switching to "stage") is crucial for technical clarity.

## When writing from scratch

### Cohesion and flow
- Each sentence answers the question raised by the previous one. The reader should
  not have to guess how one thought connects to the next.
- Connections should be meaning-based, not word-based. Don't add extra "because",
  "therefore" where the logic is already clear.
- Paragraphs should follow each other without feeling like a jump to a new topic.

### Start with substance
- Begin with the point, not the backstory. No "In today's world…", "We all know
  that…", or sentences that merely announce that information is coming.
- Don't write transition paragraphs between blocks. The heading already gives the
  context; start with the answer.

## Common rules (both when writing and re-writing)

### Paragraphs and sentences
- Short paragraphs, 2–4 sentences. One paragraph — one idea. Split two ideas into
  two paragraphs even if related. Exception: explaining a new concept or a process
  may take 4–6 sentences in one paragraph; don't shred it into 1–2-sentence bits.
- Every sentence moves the thought forward. If a sentence can be removed without
  changing the paragraph's meaning, remove it.

### Tone
- Calm and informational. No marketing, no hype, no trying to impress. Talk to the
  reader, don't broadcast. Per-channel voice is in `audience_rules.md`.
- Be direct. If something doesn't work, say so. If something matters, say it up
  front instead of leading up to it from afar.

### Concreteness
- Replace empty generalizations ("interesting experience", "useful solution",
  "works better") with specifics, or cut them. Ask "better in what way?".
- Cut abstract market stats used as filler (projections that lead to no reader
  action). Each fact should pass: "what will the reader do with this?".

### Content Samples
- If the prompt contains "samples:", analyze the folder or file names after the
  word. If it's a folder, use all the `*.md` files in it as samples.
- From samples, match:
  - the same tone of voice;
  - the same style, including typical sentence structures and section length;
  - the same vocabulary — concrete words — for relevant situations.

### Word choice (when no samples are given)
If the prompt does NOT contain "samples:", use these when translating/re-writing:
- Assess word choice and find better, more compelling alternatives to overused,
  cliché, or weak choices.
- Strive for contextually appropriate, engaging text.
- Pay attention to idiomatic expressions and wordplay, preserving the essence of
  the original.
