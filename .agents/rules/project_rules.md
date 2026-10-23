---
trigger: always
globs: ["**/*"]
---

# Project Rules
These rules describe the entire project.

# Folders and Files
- Each of the project folders is usually a long-form piece like an article (managed by `article_rules.md`) or another content type with its own per-type rules file. The folder name follows `N.n-piece-code` pattern where n is like (`1`, `2m`, `3in`, `4ru`, etc.) and N is a three-digit number with leading zeros. The letters after the digit are the channel suffix (`audience_rules.md`, *Resolving the channel*).
  - Each piece folder contains markdown files ("section files"), 1 file is usually 1 section with subsections. The file name must start with the same `n-` prefix, where n is the same n as in the folder name. 
  - The folder can also contain `n_outline.mkd` file with the piece structure, managed by `outline_rules.md`.
  - Other `*.mkd` files in the piece folder (braindumps, drafts, plans, findings, etc.) are working files: read them when a skill or the human names them, otherwise ignore them.
- `000-*` folders contain special-purpose pieces, including short-form posts and notes, with simpler structure.
- Piece folders can be subfolders of a top-level folder representing a series, a topic, or a book. Top-level folder name follows `N-topic-code` pattern where N is a three-digit number with leading zeros.
- A folder may contain a `dist` subfolder. It is gitignored, so a change there cannot be reviewed or undone through git: change it only when asked. It contains:
  - image files. An image file name can be referenced in the markdown file as `![*](image-name.png)`;
  - translation file or other *.md files, you must ignore them when analyzing the piece folder.

# Content base
`CONTENT.md` in the project root, if it exists, lists the topics and the pieces with their statuses and dates; its format is its own `## Properties` section.
- The entries follow the files through `sync-4content`, which the `*4content` skills run themselves.
- `ready` and `published` come only from the human: when they say in any session that a piece is ready or published, set the entry's `status` and `ready_date` (or `publication_date` and `publication_url`; ask for the URL if it is missing) per `## Properties`.

# Building an article
"Build the article" means assembling the piece's section files into one file by running, from the project root:
```
python3 .agents/skills/go4content/scripts/sections-to-markdown.py <piece-folder>
```
It concatenates the `*.md` section files in name order (skipping filenames containing `qna`, case-insensitively, and stripping `<delete>` blocks) into `<piece-folder>/dist/<folder-name>.md`. Do not assemble the article by hand.

## HTML and Google Doc
When the human asks for an HTML file or a Google Doc of the article, first make sure `<piece-folder>/dist/<folder-name>.md` is current: if it is missing or older than any section file, build the article as above. Then run, from the project root:
```
python3 .agents/skills/go4content/scripts/markdown-to-html.py <piece-folder>/dist/<folder-name>.md
```
It writes `dist/<folder-name>.html` next to the markdown file: the first `# ` heading becomes the title, an HTML comment right under it becomes the subtitle, every other HTML comment is dropped. It also lists placeholder links (`(url)`, `(#xxxx)`) still to fill in; pass them on to the human. For an HTML file, stop here.

For a Google Doc, also run:
```
python3 .agents/skills/go4content/scripts/html-to-gdoc.py <piece-folder>/dist/<folder-name>.html
```
It creates a new doc named `<piece code> <title>` (e.g. `207.2m Agent Skills: …`) in the Drive folder from `GO4CONTENT_GDOC_FOLDER` (or `--folder <id-or-url>`), with highlighted `[IMAGE: file]` placeholders instead of images, and prints the doc link. Every run creates a new doc; it does not update an earlier one. If it fails for a missing OAuth client or folder, point the human to *Google Docs export* in the go4content README instead of working around it.
