## 2. AI-Powered Writing: Example Workflow

Let’s look at a workflow for writing a long post (article) with an AI copilot. What work should be delegated to AI?

Github Copilot’s documentation [recommends](https://docs.github.com/en/copilot/tutorials/copilot-chat-cookbook/document-code/write-discussions-or-blog-posts) using the AI features of an IDE for brainstorming, outlining, drafting, and refining blog posts.

*I believe a writer should invest their main cognitive effort in the creative parts of the work. That’s the only way to achieve high quality without spending a lot of time on the more technical parts.*

![A typical human-AI workflow when writing a piece](human-AI_workflow_steps.png)

As I have a large backlog of my own ideas, **I don’t use AI for brainstorming**. If I did, I would probably choose a chatbot for that, because brainstorming is the most creative and unstructured process and rarely fits into a predefined IDE workflow.

*Here’s my default workflow:*

1. Start with brain-dumping (no AI).
2. Generate an outline **with AI**, then rethink and improve it.
3. Draft section files **with AI**, using the brain dump and outline.
4. Review and expand sections that weren’t described clearly enough in the brain dump. I may expand some sections **myself** and others **with AI**.
5. Validate at a high level to ensure the article isn’t too long, contains only relevant ideas, and has a smooth flow. At this step, I often remove paragraphs (saving them for future posts) and rewrite the introduction and conclusion.
6. Refine and polish the text **with AI**, especially when the original brain dump is not in English, as the AI’s translation at Step 3 isn’t good enough. I also enhance any English phrases added during Steps 4–5.

Below, I explain these steps in more detail for Trae IDE. The workflow—and even the “rules” files—can be the same **for Cursor or VS Code with an AI plugin like OpenAI Codex or Claude Code**.

### Step 1. Brain-dumping

Create a new folder and a `braindump.mkd` file, then write or dictate your ideas freely.

- Dictation is easy with [Wispr Flow](https://wisprflow.ai/): place the cursor in the file editor, hold the hotkey (`Fn` on Mac or `Ctrl+Win` on Windows by default), and speak.
- If you’re not a native English speaker, write or dictate **in your language**. The AI will later translate non-English parts into English.
- No rigid structure is required, but light Markdown **formatting** (e.g., bullets and headings) helps the AI produce meaningful sections in the next step.
- Unless prompted explicitly, the AI preserves the **order** of ideas from the dump, so consider restructuring it before proceeding.
- You may add `<TBD>` tags where extra paragraphs or sections are needed. My [outline_rules.md](https://aevdokimov.notion.site/outline_rules-mkd-2a5b9feda2ef8052bc39c75ed4c7a7ba) will convert those tags into AI-generated content later.

### Step 2. Creating an Outline

Generate `1ss_outline.mkd` using a prompt like `Write an outline from #braindump.mkd` or `Write an outline #folder-name`.

- Here, `#braindump.mkd` is a link to the file created at Step 1. It’s faster to add it by dragging and dropping the file into the prompt.
- If you use `#folder-name` instead of the file, the AI agent will find the braindump file within that folder.

Edit the generated outline carefully, as it defines the article’s structure.

- The outline file includes `@` lines for future section file names (e.g., `@0-intro`).
- Alternatively, you may remove all `@` lines except one; this option is discussed in the next step.

![Folders and outline](200.1a-folders-and-outline.png)

### Step 3. Generating section files

This is where an IDE does a lot of technical work. With one prompt, it performs multiple file operations that can’t be done in chatbots like ChatGPT.

Use a prompt such as: `Create sections #folder-name according to outline_rules and article_rules using samples: #another-folder-name`.

- [outline_rules.md](https://aevdokimov.notion.site/outline_rules-mkd-2a5b9feda2ef8052bc39c75ed4c7a7ba) clarifies how to interpret the prompt and covers technical details like file naming.
- `article_rules.md` sets content requirements, Markdown formatting, and how to use examples to mimic tone and style.

![This is how the AI agent starts responding to the prompt above](200.1a-create-sections.png)

You can generate a single draft file instead of multiple section drafts. This way, you’ll have less to do at the final step when your polished post is copied to a social network or blogging platform. However, I **don’t recommend** this approach:

1. Posts longer than ~1000 words are hard for LLMs to process reliably, despite their larger context windows. Splitting the text into section files improves quality.
2. Typically, writers need multiple section files at Step 4, “Expanding.” It’s more convenient to keep several file tabs open, one of them being the current writing. Other tabs can be used for reference or to write down random thoughts that come to mind but don’t belong in the current section. If you go back and forth within one file, you easily lose writing focus.

### Step 4. Expanding and Validating

At Step 3, my rules prohibit introducing new ideas beyond the initial braindump unless a `<TBD>` placeholder appears. Consequently, AI-generated sections are often shorter than a good article requires, making expansion necessary.

Prompts like `Expand #file-name.md using samples: #another-file-name.md` can help, but it’s better to specify exactly what needs expanding and what micro-ideas to add.

Even when a prompt is rich with your ideas, the quality of AI output can be unpredictable. The expanded version might be superficial and miss the original meaning. Therefore, it's wise to save the shorter version to Git before expanding with AI; the next section covers how to do this.

*In many cases, I expand manually because it can be more difficult to set the task for the AI and then validate its mediocre output.*

This is similar to a common problem for AI coders: it's often faster to write the code yourself than to craft a series of prompts to get code of the same quality. We are accustomed to thinking as we write, so shifting to an "AI manager" mindset can be a difficult transition for non-managers.

---

This step also includes manual tasks like adding links and images, which cannot be automated with AI. You decide:
- which web pages are most relevant;
- how to get images: Google search, AI generation, non-AI diagramming, or a mix.

By the way, AI IDEs aren’t great at image generation yet—you have to use ChatGPT, Gemini, or specialized image generators.

### Step 5. Committing Before AI Changes

In plain English, a `commit` saves a snapshot of your workspace files to Git with a message. Git is the most popular version control system for developers. You have to [install Git on Windows](https://git-scm.com/install/windows), while it’s built-in on macOS. To use Git in Cursor, Trae, or VS Code, follow [this guide](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git); clone or initialize a Git repository.

In the IDE, use the Commit button in the Source Control tab.

- For the first commit of a post, start the message with `feat:` to follow [conventions](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#summary).
- After the colon, add the article code (folder name).
- There is no need to write longer commit descriptions if you follow this workflow.
- AI-generated commit messages work well for code but not for prose.

You also need to understand the `push` command, which sends committed files to a remote repository (typically GitHub). In the IDE, pushing is done by clicking Sync Changes button after committing.

![Commit in Trae IDE](200.1-committing.png)

Always commit before refining to effectively track upcoming AI edits.

### Step 6. AI-Driven Refining and Polishing

Prompt the Builder agent: `Enhance #file-name1.md #file-name2.md according to article_rules.md`. With less attentive AI models like GPT-5, it's best to copy the most critical rules into the prompt, for example:

`Re-write ONLY sentences which are hard to read, poorly written, redundant or repetitive, to improve clarity and make them sound better. Ensure that you make as little change to the original text as possible.`

In response, the agent analyzes the folder and edits the given file(s). While Accept/Reject controls appear in the editors, the way the IDE highlights differences between the old and new versions of a long paragraph is not very convenient.

Therefore, it’s better to open the changed file in the Source Control tab. You’ll see the last committed version on the left and the AI-enhanced version on the right, with word-level diffs:

![AI edits: side-by-side comparison with Git diff](200.1a-diff-200.1a.1.png)

- Colored highlights reveal exactly which words were changed, added, or removed.
- Correct the right-side edits if needed, including by copying phrases from the original left-side version.
- Click Accept when a paragraph looks good.
- If your original is better, restore it using the right-arrow button located between the two versions. This is possible even after accepting changes.
