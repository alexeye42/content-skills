# Agent Instructions
The project is about writing texts in markdown with the `*4content` skills,
not program code. 

## Rules

Rules are located in `.agents/rules`:
- `project_rules.md` — project structure and file naming
- `audience_rules.md` — how to resolve the audience, the channel, and the target language of a piece
- `profile/audience.md` — user profile: the audience, the author, and the channels (suffix, language, headings, metadata); edit it for your own audience
- `profile/editorial.md` — user profile: editorial calibrations for feedback and review (strictness, never-flag list, score anchors, part size, title/subtitle limits)
- `writing_rules.md` — general prose quality and content requirements
- `writing_antipatterns.md` — neurotext-marker checklist (used with `writing_rules.md`)
- `format_rules.md` — markdown formatting and placeholder conventions
- `article_rules.md` — per-type rules for long-form articles
- `outline_rules.md` — outline files and titles/subtitles for articles
- `metadata_rules.md` — title/subtitle (or post text) requirements and the options notation in the intro file

## Git commits

After completing an AI generation of any content (not skills, rules, or code),
commit via the `git-commit-flow` skill with author `ai`. If the user signals they
edited files ("I reviewed it", "check my edits", "commit my changes"), commit via
`git-commit-flow` with author `human` before following other instructions. At the
start of every session run `git status --short` and commit uncommitted content
files with author `human/ai` before doing anything else.

If `git-commit-flow` is not installed, commit yourself with the message
`<feat|fix>(<folder>): <ai|human> <verb in past tense> <files touched>`. If the
folder is not under git, skip the commits and say so once.

