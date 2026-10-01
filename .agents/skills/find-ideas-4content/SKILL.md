---
name: find-ideas-4content
description: Search the web for ideas that feed the discussion of an article - evidence for its ideas, objections to its thesis, non-obvious angles, examples - and add them to the Ideas of a preliminary plan (n_plan.mkd). Use when the prompt says "find ideas"; also offered by discuss-ideas-4content after each round.
---

# Find Ideas (4content)

Web research driven by the article's own ideas, run while they are still being
discussed. Raw findings go to `n_findings.mkd`; the ideas drawn from them go into the
Ideas section of `n_plan.mkd` for the human to accept or reject in the next round of
discussion. **Search in English regardless of the prompt language**, restricted to
the current and previous year.

Work in the main context (no subagents). Write findings incrementally — do not hold
research data in context.

## Steps

1. Read `n_plan.mkd` (format: `plan_rules.md`). It must be `preliminary`, with the
   Thesis and Ideas sections: no plan or no Ideas — say that the ideas have to be
   discussed first (`discuss-ideas-4content`) and stop; `structured` or later — the
   ideas are already marked, so say that facts for a built plan come from
   `find-facts-4content` and stop. Read the sources it lists.
2. Derive 4–8 search questions from the Thesis and the Ideas — not generic reader
   questions:
   - which ideas need evidence or a source to cite;
   - what objections a reader of the piece's audience (`audience_rules.md`,
     *Resolving the audience*) would raise against the thesis, and what answers them;
   - what non-obvious angles, cases, or examples the topic has that the plan lacks;
   - where studies or models are limited, so the article doesn't overclaim.
   If the human said what they want found, focus on that. Start a new run block in
   `n_findings.mkd` (see format) with the questions.
3. Research the questions **one at a time**:
   - 1–2 English web searches per question; fetch a page when you need detail.
   - Do a "latest / current" recon query before searching for specifics; never put
     remembered versions, dates, or model names into a query. Trust search over memory.
   - **Append the result to the run block immediately** after each question.
4. Append the run's summary: the ideas drawn from the findings, each with the
   evidence type (experiment, survey, case, opinion) and its limits; what wasn't
   found; the sources.
5. Update the plan:
   - a finding that only supports an existing idea is evidence, not a new idea: add
     it to Source & facts with its URL;
   - a new angle, case, or objection becomes a bullet in Ideas with the source
     `(findings: <URL>)`, written as an idea, not as a quote.
   Do not change the existing ideas or the Thesis; the human decides in the next
   round.
6. Report in chat briefly: how many ideas were added and the strongest one or
   two.

## n_findings.mkd format

The file may be written by several runs, of this skill and of
`find-facts-4content`. Create the header only if the file does not exist; every run
appends its own block and never edits earlier blocks.

```markdown
Topic: <topic>
Audience: <from audience_rules.md, with the channel>

## Run <YYYY-MM-DD> — find-ideas

### Search questions
<4–8 questions>

### Findings

#### <Question>
<Found information>
Sources: <URL1>, <URL2>

### Ideas drawn
- <idea> — <evidence type, limits> — <URL>

### What wasn't found
<questions without reliable answers>

### Sources
<full list of URLs of this run>
```

## Rules
- Don't invent facts — everything must be confirmed by search.
- Don't rely on training data for specific facts, numbers, prices, or dates.
- If sources conflict, record both variants with their URLs.
- Aim for ~10–15 searches per run; don't pad for the sake of count.
- A limit of one study or model is reported as such, never as a limit in principle.
