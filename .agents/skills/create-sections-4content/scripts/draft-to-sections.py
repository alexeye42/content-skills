"""Split a draft file into section files without changing the text.

Usage:
    python3 <skill-dir>/scripts/draft-to-sections.py <path/to/n_draft.mkd> [path/to/n_outline.mkd] [--force]

The draft is split BEFORE every top-level section heading. The top-level heading
level is detected from the draft itself: `##` if any `##` headings exist,
otherwise `###` (channels whose heading level is `###`). Everything
above the first section heading (the title, the subtitle comment, the intro)
becomes the first chunk.

Section file names are `<n>-<code>.md`, where `<n>` is the prefix of the draft
file name (`1m_draft.mkd` -> `1m`) and `<code>` comes, in order, from the
`@code` lines of the outline (`<n>_outline.mkd` next to the draft, or the path
given as the second argument). When there is no outline, or its `@` count does
not match the number of chunks, codes are derived from the headings:
`0-intro` for the first chunk, `<index>-<slug>` for numbered headings,
`conclusion` for a heading containing "conclusion", and a plain slug otherwise.

Existing section files are never overwritten unless `--force` is given.
"""

import os
import re
import sys

HEADING_RE = re.compile(r"^(#{2,3})\s+(.*)$")
CODE_RE = re.compile(r"^@([A-Za-z0-9][A-Za-z0-9.-]*)\s*$")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def heading_level(line, in_fence):
    if in_fence:
        return None
    m = HEADING_RE.match(line)
    return len(m.group(1)) if m else None


def detect_top_level(lines):
    levels = set()
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        lvl = heading_level(line, in_fence)
        if lvl:
            levels.add(lvl)
    if 2 in levels:
        return 2
    if 3 in levels:
        return 3
    return None


def split_chunks(lines, top_level):
    chunks, current = [], []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
        if heading_level(line, in_fence) == top_level and current:
            chunks.append(current)
            current = []
        current.append(line)
    if current:
        chunks.append(current)
    return chunks


def outline_codes(path):
    if not path or not os.path.isfile(path):
        return []
    codes = []
    for line in read_lines(path):
        m = CODE_RE.match(line.strip())
        if m:
            codes.append(m.group(1))
    return codes


def slugify(text, max_words=3):
    words = re.findall(r"[A-Za-z0-9]+", text.lower())
    return "-".join(words[:max_words]) or "section"


def heading_code(chunk, position):
    if position == 0:
        return "0-intro"
    title = HEADING_RE.match(chunk[0]).group(2).strip()
    if "conclusion" in title.lower():
        return "conclusion"
    m = re.match(r"^(\d+)[.)]?\s+(.*)$", title)
    if m:
        return f"{m.group(1)}-{slugify(m.group(2))}"
    return slugify(title)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    if not args:
        print(__doc__)
        return 1

    draft_path = args[0]
    if not os.path.isfile(draft_path):
        print(f"Error: draft file '{draft_path}' not found.")
        return 1
    folder = os.path.dirname(os.path.abspath(draft_path))
    base = os.path.basename(draft_path)
    prefix = base.split("_", 1)[0]
    if prefix == base:
        print(f"Error: draft file name must look like '<n>_draft.mkd', got '{base}'.")
        return 1

    outline_path = args[1] if len(args) > 1 else os.path.join(folder, f"{prefix}_outline.mkd")

    lines = read_lines(draft_path)
    top_level = detect_top_level(lines)
    if not top_level:
        print("Error: no '##' or '###' headings found in the draft.")
        return 1
    chunks = split_chunks(lines, top_level)

    codes = outline_codes(outline_path)
    if codes and len(codes) != len(chunks):
        print(f"Warning: outline has {len(codes)} '@' codes but the draft has "
              f"{len(chunks)} chunks; falling back to heading-derived codes.")
        codes = []
    if not codes:
        codes = [heading_code(chunk, i) for i, chunk in enumerate(chunks)]

    targets = [os.path.join(folder, f"{prefix}-{code}.md") for code in codes]
    existing = [t for t in targets if os.path.exists(t)]
    if existing and not force:
        print("Error: these files already exist (use --force to overwrite):")
        for t in existing:
            print(f"  {os.path.relpath(t)}")
        return 1

    for chunk, target in zip(chunks, targets):
        text = "\n".join(chunk).rstrip("\n") + "\n"
        with open(target, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote {os.path.relpath(target)} ({len(chunk)} lines)")

    print(f"Split '{os.path.relpath(draft_path)}' into {len(chunks)} files "
          f"(top-level headings: {'#' * top_level}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
