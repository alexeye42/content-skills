import os
import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 <skill-dir>/scripts/sections-to-markdown.py <relative_folder_path>")
        return

    folder_path = sys.argv[1]
    # The folder path is relative to the current directory (normally the project root).
    project_root = os.getcwd()
    full_path = os.path.join(project_root, folder_path)

    if not os.path.isdir(full_path):
        print(f"Error: The path '{folder_path}' does not exist or is not a folder.")
        return

    md_files = sorted([f for f in os.listdir(full_path) if f.endswith('.md') and not f.endswith('_qna.md')])

    if len(md_files) <= 1:
        print(f"Error: The folder '{folder_path}' must contain more than one .md file.")
        return

    folder_name = os.path.basename(folder_path)
    output_filename = f"{folder_name}.md"
    dist_folder = os.path.join(full_path, 'dist')
    if not os.path.exists(dist_folder):
        os.makedirs(dist_folder)
    output_filepath = os.path.join(dist_folder, output_filename)

    parts = []
    for filename in md_files:
        with open(os.path.join(full_path, filename), 'r', encoding='utf-8') as infile:
            content = infile.read()
        # <delete> blocks may carry attributes, e.g. <delete reason="...">
        content = re.sub(r'<delete\b[^>]*>.*?</delete>', '', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'\n{3,}', '\n\n', content).strip()
        if content:
            parts.append(content)

    # Files are stripped, so the separator is always needed: a file ending with
    # blank lines must not glue the next file's heading to its last line.
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        outfile.write('\n\n'.join(parts) + '\n')

    print(f"Successfully created '{output_filename}' in '{os.path.relpath(dist_folder, project_root)}'.")

if __name__ == "__main__":
    main()