---
trigger: manual
description: User profile — the audience, the author, and the publishing channels. Referenced from audience_rules.md, article_rules.md, and metadata_rules.md; edit it for your own audience and channels, the skills never need to change.
---

# Audience Profile

Edit this file for your own audience, author, and channels. The rules read it; the
`*4content` skills never need to change.

## General audience
- Language: English
- Audience: **DESCRIBE HERE**

## Author
- Native language: not English — judge wording as a native editor would.
- Voice: colloquial — jokes, smileys, and slang are the author's style, not
  mistakes.

## Channels

The channel is the letter suffix of the piece folder (`N.n<suffix>-code`, e.g.
`207.2m-agent-skills`) and of its file prefixes (`2m-intro.md`). A folder without a
suffix uses *Defaults*. A field missing from a channel is taken from *Defaults*.

### Medium
- Suffix: `m`
- Language: English
- Headings: top-level sections `###`, subsections `####`
- Metadata: title + subtitle (subtitle is for preview and SEO, not shown in the story)
- Audience: **DESCRIBE HERE**

### LinkedIn
- Suffix: `in`
- Language: English
- Headings: top-level sections `###`, subsections `####`
- Metadata: post text (no subtitle)
- Audience: **DESCRIBE HERE**

### Substack
- Suffix: `ss`
- Language: English
- Headings: top-level sections `##`, subsections `###`
- Metadata: title + subtitle
- Audience: **DESCRIBE HERE**

### Defaults (no suffix or unknown suffix)
- Language: from *General audience*
- Headings: top-level sections `##`, subsections `###`
- Metadata: title + subtitle
- Audience: asked from the human (`audience_rules.md`, *Resolving the audience*)