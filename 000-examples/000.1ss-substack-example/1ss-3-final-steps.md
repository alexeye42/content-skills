## Final Steps

When all section files are ready, build them into a single, ready-to-publish document.

- Use a simple [Python script](https://aevdokimov.notion.site/sections_to_one-py-2a6b9feda2ef806286a1e2ed38ff52f8) to combine sections into one Markdown file. Run: `python sections_to_one.py "parent-folder-name/main-folder-name"`. Using AI for this concatenation would be unnecessary overhead.
- For most blogging platforms, Google Docs is the best intermediate. Use **“Paste from Markdown”** (enable it in Tools → Preferences if missing). It supports key Markdown features, including `---` separators.

The only thing to do manually in Google Docs is to **insert images** where you see placeholders. If this is too tedious and you’re tech-savvy, you can vibe-code a Markdown-to-HTML conversion and fill a Google Doc via its API, uploading images to a public URL that the Google Docs can fetch.