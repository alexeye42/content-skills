import argparse
import html
import io
import os
import re
import sys

try:
    from google.auth.exceptions import RefreshError
    import httplib2
    from google.auth.transport.requests import Request
    from google_auth_httplib2 import AuthorizedHttp
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseUpload
except ImportError:
    sys.exit("Error: Google API libraries are not installed. Run: "
             "python3 -m pip install google-api-python-client google-auth-oauthlib")

# Full Drive access: the narrower drive.file scope cannot put files into a
# folder the app did not create itself.
SCOPES = ['https://www.googleapis.com/auth/drive']
CONFIG_DIR = os.path.expanduser('~/.config/gdrive-access')
IMAGE_PLACEHOLDER = '<span style="background-color:#ffff00">[IMAGE: {}]</span>'


def get_credentials(client_secret_path):
    token_path = os.path.join(CONFIG_DIR, 'token.json')
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except RefreshError:
            creds = None
    if not creds or not creds.valid:
        if not os.path.isfile(client_secret_path):
            sys.exit(f"Error: OAuth client file '{client_secret_path}' not found. "
                     "See 'Google Docs export' in the gdrive-access README for the one-time setup.")
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, SCOPES)
        creds = flow.run_local_server(port=0)
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(token_path, 'w', encoding='utf-8') as token_file:
        token_file.write(creds.to_json())
    os.chmod(token_path, 0o600)
    return creds


def folder_id_from(value):
    match = re.search(r'/folders/([\w-]+)', value)
    return match.group(1) if match else value


def replace_images(page):
    """Google Docs cannot import images by relative paths, so each one becomes a highlighted marker."""
    def placeholder(match):
        tag = match.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        label = src.group(1) if src else '?'
        if alt and alt.group(1):
            label += f' — {alt.group(1)}'
        return IMAGE_PLACEHOLDER.format(label)
    return re.sub(r'<img\b[^>]*>', placeholder, page)


def plain_text(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def pt(value):
    return {'magnitude': value, 'unit': 'PT'}


def paragraph_style_request(element, style, fields):
    return {'updateParagraphStyle': {
        'range': {'startIndex': element['startIndex'], 'endIndex': element['endIndex']},
        'paragraphStyle': style,
        'fields': fields,
    }}


def run_text(elements):
    return ''.join(e.get('textRun', {}).get('content', '') for e in elements)


def is_rule(paragraph):
    elements = paragraph['elements']
    return any('horizontalRule' in e for e in elements) and not run_text(elements).strip()


def separate_rules(docs, doc_id):
    """Give every horizontal rule a paragraph of its own.

    The HTML import puts a rule into the paragraph next to it, e.g. into the
    heading that follows it, so the line and the heading share one line.
    """
    content = docs.documents().get(documentId=doc_id).execute()['body']['content']
    breaks = []
    for element in content:
        elements = element.get('paragraph', {}).get('elements', [])
        for i, run in enumerate(elements):
            if 'horizontalRule' not in run:
                continue
            if run_text(elements[:i]):
                breaks.append(run['startIndex'])
            if run_text(elements[i + 1:]).strip('\n'):
                breaks.append(run['endIndex'])
    # From the end, so an inserted break does not shift the indices still to come.
    requests = [{'insertText': {'location': {'index': index}, 'text': '\n'}}
                for index in sorted(set(breaks), reverse=True)]
    if requests:
        docs.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()


def format_paragraphs(docs, doc_id, title, subtitle):
    """Set the Title/Subtitle named styles and the spacing between paragraphs.

    The HTML import leaves most paragraphs with no space after them and zeroes the
    space above headings, so the text reads as one block of line breaks.
    """
    content = docs.documents().get(documentId=doc_id).execute()['body']['content']
    paragraphs = [e for e in content if 'paragraph' in e]
    named = {}
    for text, style in ((title, 'TITLE'), (subtitle, 'SUBTITLE')):
        for element in paragraphs:
            runs = run_text(element['paragraph']['elements'])
            if text and runs.strip() == text and id(element) not in named:
                named[id(element)] = style
                break

    requests = []
    for i, element in enumerate(paragraphs):
        paragraph = element['paragraph']
        if id(element) in named:
            requests.append(paragraph_style_request(element, {'namedStyleType': named[id(element)]}, 'namedStyleType'))
            continue
        if is_rule(paragraph):
            # Split off a heading, the rule keeps its style; a rule is never a heading.
            style = {'namedStyleType': 'NORMAL_TEXT', 'spaceAbove': pt(0), 'spaceBelow': pt(10)}
            requests.append(paragraph_style_request(element, style, 'namedStyleType,spaceAbove,spaceBelow'))
            continue
        if paragraph['paragraphStyle'].get('namedStyleType', '').startswith('HEADING'):
            spacing = {'spaceAbove': pt(18), 'spaceBelow': pt(6)}
        elif 'bullet' in paragraph:
            next_paragraph = paragraphs[i + 1]['paragraph'] if i + 1 < len(paragraphs) else {}
            last_item = 'bullet' not in next_paragraph
            spacing = {'spaceAbove': pt(0), 'spaceBelow': pt(10 if last_item else 4)}
        else:
            spacing = {'spaceAbove': pt(0), 'spaceBelow': pt(10)}
        requests.append(paragraph_style_request(element, spacing, 'spaceAbove,spaceBelow'))

    if requests:
        docs.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()


def main():
    parser = argparse.ArgumentParser(description="Create a Google Doc from an HTML file made by markdown-to-html.py.")
    parser.add_argument('html_path', help="path to the .html file")
    parser.add_argument('--folder', default=os.environ.get('ACCESS_GDOC_FOLDER',
                            'https://drive.google.com/drive/folders/1wdGOI-l6HqA4Vw17KBClSAEzGfyEv_2d'),
                        help="Drive folder ID or URL (default: $ACCESS_GDOC_FOLDER)")
    parser.add_argument('--client-secret',
                        default=os.environ.get('ACCESS_GOOGLE_CLIENT_SECRET',
                                               os.path.join(CONFIG_DIR, 'client_secret.json')),
                        help="OAuth client JSON (default: $ACCESS_GOOGLE_CLIENT_SECRET "
                             "or ~/.config/gdrive-access/client_secret.json)")
    args = parser.parse_args()

    if not args.folder:
        sys.exit("Error: no Drive folder given. Pass --folder or set ACCESS_GDOC_FOLDER.")
    if not os.path.isfile(args.html_path):
        sys.exit(f"Error: The file '{args.html_path}' does not exist.")

    with open(args.html_path, 'r', encoding='utf-8') as infile:
        page = infile.read()

    title_tag = re.search(r'<title>(.*?)</title>', page, flags=re.DOTALL)
    title = plain_text(title_tag.group(1)) if title_tag else ''
    subtitle_tag = re.search(r'<p class="subtitle">(.*?)</p>', page, flags=re.DOTALL)
    subtitle = plain_text(subtitle_tag.group(1)) if subtitle_tag else None

    # The piece code before the first hyphen of the file name, e.g. "205.1m" for "205.1m-insights.html".
    prefix = os.path.splitext(os.path.basename(args.html_path))[0].split('-', 1)[0]
    name = f'{prefix} {title}'.strip()

    # The page stylesheet is for browsers; in the doc it would override the named styles.
    page = re.sub(r'<style>.*?</style>', '', page, flags=re.DOTALL)
    page = replace_images(page)

    creds = get_credentials(args.client_secret)
    # Converting HTML to a doc can take longer than the default 60-second read timeout.
    # A timed-out create may still have made the doc, so it is never retried.
    http = AuthorizedHttp(creds, http=httplib2.Http(timeout=300))
    drive = build('drive', 'v3', http=http)
    docs = build('docs', 'v1', http=http)

    media = MediaIoBaseUpload(io.BytesIO(page.encode('utf-8')), mimetype='text/html', resumable=False)
    created = drive.files().create(
        body={'name': name, 'mimeType': 'application/vnd.google-apps.document',
              'parents': [folder_id_from(args.folder)]},
        media_body=media, fields='id,webViewLink', supportsAllDrives=True,
    ).execute()

    separate_rules(docs, created['id'])
    format_paragraphs(docs, created['id'], title, subtitle)

    print(f"Successfully created Google Doc '{name}': {created['webViewLink']}")


if __name__ == "__main__":
    main()
