# More Ideas — Things to Try with Claude Code

Already done the basics in the README? Here are more things to try, broken down by the kind of work you do.

---

## For everyone

### Draft and iterate on writing
Point Claude at a rough draft, outline, or voice memo transcript:
> "Here's a rough draft. Restructure it, tighten the language, and flag gaps in the argument. Don't add claims I haven't made — use [placeholder] tags for anything missing."

Then iterate: "Make the intro punchier", "This section is too long", "Rewrite section 3 to lead with the example".

### Paper outlining and argument structuring
> "Here's my rough argument for [claim]. Help me structure this as a paper outline. What sections do I need? Where are the gaps? What objections should I anticipate?"

### Build a writing skill
See `sample-write-skill/` — drop in 2-4 pieces of your own writing at different formality levels, and Claude learns your voice. No need to describe your style yourself.

---

## For technical safety fellows

### Experiment scaffolding
> "Set up a Python script that runs [model] on [dataset/task], logs results to a CSV, and prints a summary table at the end."

Claude can handle the boilerplate so you focus on what to test and what the results mean.

### Code review and debugging
Point Claude at a repo or script you're working with:
> "Read through this codebase and explain what it does. Then flag anything that looks buggy or fragile."

Or when stuck:
> "This script throws [error] when I run it. Read the code, figure out why, and fix it."

### Explore an unfamiliar codebase
If you're working with someone else's repo (e.g. a benchmark suite, a training pipeline):
> "Read through this repo and give me a map: what are the key files, how does data flow through the system, and where would I add [new feature]?"

### Run and analyze experiments
> "Run this script with parameters X, Y, Z. Collect the outputs, make a comparison table, and tell me which configuration performed best and why."

---

## For governance fellows

### Policy document analysis
Drop a regulation, standard, or policy proposal into your folder:
> "Read this document. Summarize the key obligations, who they apply to, and what enforcement mechanisms exist. Then list the main ambiguities or gaps."

### Compare frameworks across jurisdictions
> "I have [EU AI Act summary] and [US executive order summary] in this folder. Compare them: where do they agree, where do they diverge, and what's covered by one but not the other?"

### Stakeholder mapping
> "For [policy area], map the key stakeholders: who supports stronger regulation, who opposes it, and what are their stated reasons? Flag where stated reasons might differ from actual incentives."

### Draft policy memos or briefings
> "Write a 2-page briefing on [topic] for [audience]. It should cover: what the issue is, why it matters now, what the options are, and what we recommend. Keep it concrete — no filler."

### Theory of change stress-testing
> "Here's my theory of change for [project]. Red-team it: what assumptions am I making? Which ones are most likely to be wrong? What would have to be true for this to actually work?"

### Build a tracker or database
> "Create a spreadsheet (CSV) tracking [AI governance initiatives / lab commitments / standard-setting bodies]. Columns: name, jurisdiction, status, key dates, relevance to [your topic]."

Claude can build the structure and populate what it knows — you verify and fill gaps.

### Deliberation and consultation design
> "I'm designing a consultation process for [topic]. Help me think through: who should participate, what questions to ask, how to structure the sessions, and how to synthesize inputs into something actionable."

---

## Improving your setup over time

The real payoff comes from iterating on your CLAUDE.md and skills. When Claude does something you like, add it as an instruction. When it does something annoying, add a rule against it. Your workspace gets smarter with you.

Some things to add to CLAUDE.md as you discover them:
- "Always show your sources when making factual claims"
- "When I say 'draft', give me a rough version first — don't over-polish"
- "Never use bullet points for things that should be paragraphs"
- "Push back if my argument has obvious holes"
