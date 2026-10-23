import html
import os
import re
import sys

try:
    from markdown_it import MarkdownIt
except ImportError:
    sys.exit("Error: markdown-it-py is not installed. Run: python3 -m pip install markdown-it-py")

CSS = """
body { max-width: 720px; margin: 2em auto; padding: 0 16px; font-family: Georgia, serif; line-height: 1.6; }
.subtitle { font-size: 1.25em; color: #555; margin-top: -0.5em; }
img { max-width: 100%; }
"""


def extract_subtitle(text):
    """Return the text of an HTML comment placed right under the first H1, or None.

    Only blank lines may separate the heading from the comment.
    """
    heading = re.search(r'^# .+$', text, flags=re.MULTILINE)
    if not heading:
        return None
    comment = re.compile(r'[ \t]*\n(?:[ \t]*\n)*[ \t]*<!--(.*?)-->', re.DOTALL).match(text, heading.end())
    if not comment:
        return None
    return ' '.join(comment.group(1).split()) or None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 <skill-dir>/scripts/markdown-to-html.py <path/to/file.md>")
        return

    md_path = sys.argv[1]
    if not os.path.isfile(md_path):
        print(f"Error: The file '{md_path}' does not exist.")
        return

    with open(md_path, 'r', encoding='utf-8') as infile:
        text = infile.read()

    subtitle = extract_subtitle(text)
    # Every HTML comment is dropped: the subtitle is already taken, the rest
    # (a LinkedIn post, author notes) is not part of the article body.
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Raw HTML stays disabled, so tags like <subscribe> remain visible as text
    # instead of silently disappearing.
    md = MarkdownIt('commonmark', {'html': False}).enable(['strikethrough', 'table'])
    body = md.render(text)

    h1 = re.search(r'<h1>(.*?)</h1>', body, flags=re.DOTALL)
    if h1:
        title = html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip()
        if subtitle:
            body = body[:h1.end()] + f'\n<p class="subtitle">{html.escape(subtitle)}</p>' + body[h1.end():]
    else:
        title = os.path.splitext(os.path.basename(md_path))[0]
        print("Warning: no '# ' heading found; the file name is used as the title.")

    page = (
        '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n'
        f'<title>{html.escape(title)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n'
        f'{body}</body>\n</html>\n'
    )

    html_path = os.path.splitext(md_path)[0] + '.html'
    with open(html_path, 'w', encoding='utf-8') as outfile:
        outfile.write(page)

    print(f"Successfully created '{html_path}'.")
    placeholders = re.findall(r'\[([^\]]*)\]\((?:url|#xxxx)\)', text)
    if placeholders:
        print("Placeholder links to fill in: " + '; '.join(f"[{p}]" for p in placeholders))


if __name__ == "__main__":
    main()
