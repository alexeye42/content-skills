---
trigger: model_decision
description: How to resolve the audience, the channel, and the target language of a piece. Read before research, planning, drafting, and editing; the audience and channel data live in profile/audience.md.
globs: ["**/*.md", "**/*.mkd"]
---

# Audience Rules

The audience, the author, and the channels are data, not rules: they live in
`profile/audience.md` (one section per channel: suffix, language, headings, metadata,
audience). Edit that file for your own audience; this file only says how to resolve
them.

## Resolving the audience (for `*4content` skills)
Look in this order; the first hit wins:
1. The `## Audience` section of the piece's `n_qna.md` (`Audience:` and `Personas:`
   lines, right under the file title).
2. The channel by the folder-name suffix — its `Audience` in `profile/audience.md`,
   no personas.
3. Neither (no suffix, no `## Audience`): the orchestrator asks the human for the
   audience and up to two personas through `qna-manager` (an ordinary question),
   then writes the answer itself as the `## Audience` section at the top of
   `n_qna.md`, right under the file title:
   ```
   ## Audience
   Audience: <who>
   Personas: <up to two, or "none">
   ```
   Every later skill reads it from there. Child skills never ask — they report
   "audience unresolved" and stop.

## Resolving the channel
The channel is the letter suffix of the piece folder (`N.n<suffix>-code`) and of its
file prefixes. Its fields (`Language`, `Headings`, `Metadata`, `Audience`) come from
the matching `###` section of `profile/audience.md`; a field the channel does not
set, or a folder without a suffix, uses the *Defaults* section there.

## Resolving the language
The target language of the piece's text is the channel's `Language`; without one,
the `Language` of *General audience*; without that, English. The language of the
human's prompt does not change it.
