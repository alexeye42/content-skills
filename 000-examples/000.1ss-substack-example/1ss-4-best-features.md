## The Best AI IDE Features

I use Trae IDE for writing texts for three main reasons:

- Diff-based review of AI enhancements (see Step 6).
- Reusing typical AI instructions across posts.
- Reusing previous articles as my writing style examples, which provides important context for the AI.

As for the famous [Tab Autocompletion](https://cursor.com/docs/tab/overview), it also considers the file contents as context for the AI. However, you can’t control that context. For creative writing, autocompletion tends to produce templated wording and paraphrased repetitions—fine for code, but a recipe for AI slop in prose. I don’t recommend relying on tab autocompletion for long-form writing.

Generating an outline from a brain dump and creating draft section files from it are time-consuming technical operations. Using AI here saves time, but it’s not a game-changer. Expanding a text with AI often doesn’t help much either.

What helps most is AI **refining** (Step 6), especially when combined with word-level comparison in the IDE.

## AI Models to Use for This Workflow

For Step 6, I performed a lot of tests and finally opted for the **Gemini Pro** model. Unlike OpenAI’s GPT models, Gemini makes only essential changes as required. Unlike Claude, it sounds more natural in English and corrects overly direct translations from Russian. However, Gemini is bad at outlining for some reason.

For most of the previous steps, I used to select **Claude Sonnet** models: 3.5, 3.7, and 4.0. This is because Claude follows instructions diligently and doesn’t make its own random decisions. However, Claude was removed from Trae in November 2025, as Anthropic tightened its policy restricting its use on Chinese-owned platforms.

So, I switched to **GPT-5 High.** It thinks longer, but its outcome is sometimes even better than Claude's. For example, GPT-5 found and used an example of my previous outline. This idea hadn't occurred to me before, but I liked it and added a corresponding instruction to `outline_rules.md` to make outlining even more stable.

I noticed only two pitfalls with GPT-5 when I wrote a draft post rather than a brain dump:
- Sometimes, it removes random hyperlinks at Step 3.
- Rephrasing by GPT-5 can lose the original emotion or details.

Nevertheless, these drawbacks don't matter for the braindump-based workflow described above. Just use Gemini at the refining step.