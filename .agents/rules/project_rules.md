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
  - There could be other `*.mkd` files in the piece folder (braindumps, drafts, etc), but they must be ignored unless they are mentioned expicitly.
- `000-*` folders contain special-purpose pieces, including short-form posts and notes, with simpler structure.
- Piece folders can be subfolders of a top-level folder representing a series, a topic, or a book. Top-level folder name follows `N-topic-code` pattern where N is a three-digit number with leading zeros.
- A folder may contain a `dist` subfolder (gitignored) that you DON'T change unless instructed. It contains:
  - image files. An image file name can be referenced in the markdown file as `![*](image-name.png)`;
  - translation file or other *.md files, you must ignore them when analyzing the piece folder.
