# Content Skills

A skill system for writing long-form content (articles or other pieces) with an AI agent 
inside your favorite tool — Claude Cowork/Code, Codex, Cursor IDE, Antigravity IDE, 
or any agent that reads skills from a folder.
- It takes a braindump or a draft and help you transform it into a polished article: 
  section files, revised text, a chosen title and subtitle. 
- The human stays in the loop at every gate, and the work happens in files under git
  rather than in the chat: questions and answers land in a Q&A file, 
  feedback is markup inside the section files, 
  every AI pass is a commit you can view as diff in your IDE or another tool.

## How it works

- **A piece is a folder** `N.n<suffix>-code` (e.g. `207.2m-agent-skills`) holding
  your braindump `n_dump.mkd` or draft `n_draft.mkd`; the suffix names the
  publishing channel. Intermediate files are `*.mkd`, the final section files are
  `n-*.md`, and a build step assembles them into one file in `dist/`.
- **Three layers.** The skills are never edited. The rules rarely. Your profile in
  `.agents/rules/profile/` — audience, author, channels, editorial taste — is the
  layer you own: two markdown files, edited once.
- **Git is the review surface.** The agent commits its own passes as `ai` and your
  edits as `human`; before the next part it reads your diff and adapts.

## The three orchestrators (workflows)

1. **`go4content` — creation.** `/go4content <folder>` detects one of three cases by
  the effort you want to spend: 
  - **1A quick** (braindump → gap questions → outline → sections; with `AI wrote` / 
    `Must add` callouts where the dump had nothing),
  - **1B full** (fact research → editorial plan you approve → draft → outline → sections),
  - **1C draft** (your own draft → outline → sections)
  It ends by handing the article to #2 or #3 flow below.
2. **`improve4content` — the AI edits, you review.** AI-edited files left as an 
  uncommitted diff for you to read & edit in the IDE; the lessons from your corrections 
  are carried into the next file; title and subtitle options at the end.
3. **`review4content` — the AI gives feedback, you edit.** The article is split into
  parts of 1–3 sections; each part gets inline callouts with highlighted fragments
  and scores; you rewrite (or say `apply feedback`); the agent reads your diff before
  the next part; intro, conclusion, title and subtitle come last; a before/after
  score table closes the run.

Behind them are nine content processing skills, `qna-manager` for asking questions and
storing your answers, and `git-commit-flow` for commit automation. Prompt words, 
the markup notation, commands, and example sessions: `.agents/skills/go4content/README.md`.

## Example article

`000-examples/000.1ss-substack-example/` is a finished article produced with this
workflow, kept as a sample of what the pipeline delivers: the outline
`1ss_outline.mkd` and the section files `1ss-*.md`, one per top-level section (the
`ss` suffix is the Substack channel, so sections use `##` headings and the intro
carries the subtitle as a comment under the title). The article itself is about
writing in an AI IDE, so it doubles as background reading. 

## Install

The repository is a ready writing workspace: you will write your articles in it and
commit them, so start from a repository you own rather than from a clone of this
one.

1. Get your own copy. On GitHub, click **Use this template** and create a new
   repository from it — a private one is fine, your drafts are yours — or **Fork**
   it if you prefer to keep the link to this repository visible. Then clone your
   repository:
   ```
   git clone https://github.com/<you>/<your-repo>.git
   ```
   To receive skill updates later, add this repository as a second remote and
   merge from it when you want:
   ```
   git remote add upstream https://github.com/alexeye42/content-skills.git
   git pull upstream main
   ```
   Your articles and the skills live in different folders, so the merges stay
   clean as long as you edit only your profile and your pieces.

2. **Claude Cowork/Code, Cursor:** run the setup script once — it creates `.claude/skills` 
   and `.claude/rules` pointing to `.agents/skills` and `.agents/rules` (symlinks on
   macOS/Linux, directory junctions on Windows, no admin rights needed):
   ```
   scripts/setup-claude.sh          # macOS / Linux
   scripts\setup-claude.cmd         # Windows, cmd
   scripts\setup-claude.ps1         # Windows, PowerShell
   ```
   **Codex, Antigravity:** nothing to do — they read `.agents/` directly.

3. Add `git-commit-flow` from the
   [workflow-skills](https://github.com/alexeye42/workflow-skills) repository — it
   is the one skill kept outside this one. Copy its folder into `.agents/skills/`
   (or into your global skills folder):
   ```
   git clone --depth 1 https://github.com/alexeye42/workflow-skills.git /tmp/workflow-skills
   cp -r /tmp/workflow-skills/skills/git-commit-flow .agents/skills/
   ```
   Without it the agent falls back to plain `git commit` in the same message
   format (the fallback is in `AGENTS.md`).

4. **Edit your profile** — the only files meant for you to change:
   - `.agents/rules/profile/audience.md` — your audience, your author notes
     (native language, voice), your channels: for each one its folder suffix,
     language, heading levels, specific audience.
   - `.agents/rules/profile/editorial.md` — how strict the feedback is, what it
     never flags, the score anchors, the review part size, the title/subtitle
     limits. This file may be left unchanged.

**Adding the skills to an existing project instead:** copy `.agents/skills/*` and
`.agents/rules/*` into your project's skills and rules folders (Claude Code:
`.claude/skills`, `.claude/rules`), and append the *Rules* and *Git commits*
sections of this repository's `AGENTS.md` to your `CLAUDE.md` / `AGENTS.md`. The
skills refer to rules by bare file name and to their own scripts relative to the
skill folder, so any layout works as long as the instruction file names the rules
path.

## Start using it

Create a folder, put `n_dump.mkd` or `n_draft.mkd` in it, and say `/go4content <folder>`.

## Repository layout

```
.agents/skills/            12 *4content skills + qna-manager (scripts/ and references/ inside)
.agents/rules/             8 rule files + profile/ (audience.md, editorial.md)
000-examples/              a finished article as a sample: outline and section files
scripts/                   setup-claude.sh / .cmd / .ps1
AGENTS.md, CLAUDE.md       agent instructions — identical apart from the first lines
```

