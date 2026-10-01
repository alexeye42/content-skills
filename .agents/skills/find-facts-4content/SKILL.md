---
name: find-facts-4content
description: Gather external facts for a content piece - links that support its ideas, examples that illustrate them, numbers, tools, reference articles. Use when the prompt contains "find facts" (or "gather facts"). Writes findings to n_findings.mkd. Searches in English regardless of prompt language.
---

# Find Facts (4content)

Collect external facts for a content piece: sources to cite, examples, numbers,
tools, reference articles. Output goes to `n_findings.mkd` in the piece folder.
**Search in English regardless of the prompt language**, whatever the piece's target
language, restricted to the current and previous year.

Work in the main context (no subagents). Write findings incrementally — do not hold
research data in context.

## Steps

1. Read the source/topic and the piece folder. If `n_plan.mkd` exists, read its
   Thesis (and Structure, if present) as context for the questions. Resolve the
   audience and the channel per `audience_rules.md`. If the caller or the human said
   what they want found (links supporting the ideas, illustrating examples, other
   facts), focus on that.
2. Frame 8–12 reader questions for the topic (what / how / why / where / cost /
   limits / alternatives / what's next). Pick the relevant ones; add topic-specific
   questions. Start a new run block in `n_findings.mkd` (see format) with the
   question list.
3. Research the questions **one at a time**:
   - 1–2 English web searches per question; fetch a page when you need detail.
   - Do a "latest / current" recon query before searching for specifics; never put
     remembered versions, dates, or model names into a query. Trust search over memory.
   - **Append the result to the run block immediately** after each question.
4. Find 2–3 reference articles on the topic (for an audience close to the project's).
   For each, record the URL, its structure, what works, and what could be improved.
   These are references for writing, not text to copy.
5. Append the run's summary subsections (see format).

## n_findings.mkd format

The file may be written by several runs, of this skill and of
`find-ideas-4content`. The header is written once, when the file is created; every
run appends its own block below and never edits earlier blocks.

```markdown
Topic: <topic>
Audience: <from audience_rules.md, with the channel>

## Run <YYYY-MM-DD> — find-facts

### Reader questions
<8–12 questions>

### Findings

#### <Question>
<Found information>
Sources: <URL1>, <URL2>

### Key facts & numbers
<concrete facts, numbers, names usable in the text>

### Examples & analogies
<real-life examples and analogies that explain the topic simply>

### Tools & references
<concrete tools/resources: name, link, what it does>

### Reference articles
<URL — structure — what works — what to improve>

### What wasn't found
<questions without reliable answers>

### Sources
<full list of URLs of this run>
```

## Rules
- Don't invent facts — everything must be confirmed by search.
- Don't rely on training data for specific facts, numbers, prices, or dates.
- If sources conflict, record both variants with their URLs.
- Write nothing into `n_plan.mkd`; the plan takes facts from `n_findings.mkd`.
