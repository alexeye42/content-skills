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

    with open(output_filepath, 'w') as outfile:
        for i, filename in enumerate(md_files):
            with open(os.path.join(full_path, filename), 'r') as infile:
                content = infile.read()
                content = re.sub(r'<delete>.*?</delete>', '', content, flags=re.IGNORECASE | re.DOTALL)
                outfile.write(content.strip())
                if i < len(md_files) - 1 and not content.endswith('\n\n'):
                      outfile.write('\n\n')

    print(f"Successfully created '{output_filename}' in '{os.path.relpath(dist_folder, project_root)}'.")

if __name__ == "__main__":
    main()