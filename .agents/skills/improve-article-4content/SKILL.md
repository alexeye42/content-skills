---
name: improve-article-4content
description: Final edit of an article or its section .md files. Use when the prompt says "improve the article" / "edit the article".
---

# Improve Article (4content)

Final edit of an article: its content, its formatting, or both — depending on the
prompt. The content type is fixed (article). This skill is self-contained.

You must follow:
- `writing_rules.md` — Content Requirements and prose quality (+ `writing_antipatterns.md`);
- `article_rules.md` — article-specific rules (heading override, intro/conclusion);
- `format_rules.md` — markdown formatting and placeholders;
- `audience_rules.md` — the audience (*Resolving the audience*) and channel voice.
- *Agent callouts* in `format_rules.md`: leave paragraphs under `AI wrote` and
  `Must add` callouts untouched — they wait for the author.

## Steps

1. Identify the target files. Edit ONLY the `*.md` / `*.mkd` files explicitly
   referenced in the prompt.
2. For each target file, apply the Content Requirements from `writing_rules.md` and the
   article-specific rules from `article_rules.md`. Match the channel voice from
   `audience_rules.md`.
3. Ensure proper markdown per `format_rules.md`, applying the article heading-level
   override from `article_rules.md`.
4. Read through the edited text to ensure:
   - it sounds natural to native speakers of the piece's target language
     (`audience_rules.md`, *Resolving the language*);
   - all requirements are met;
   - changes are minimal and necessary.
5. Run the `writing_antipatterns.md` checklist over the result.
