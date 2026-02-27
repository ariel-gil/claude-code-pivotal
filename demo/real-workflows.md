# Real Workflows — Examples From a Few Months of Daily Use

The basics are easy. The interesting question is: what happens when you actually use Claude Code every day for a while? This page walks through real workflows built over ~1 month of daily use. 

One thing that does hold up: **the value compounds**. Each skill, memory entry, and CLAUDE.md rule is small on its own. Together they add up to something noticeably more useful than a fresh install.

---

## 1. Handwriting transcription pipeline

**What it does:** Photographs of handwritten meeting notes go in, structured markdown comes out — with domain-specific jargon handled correctly, action items extracted, and outputs split into per-person running logs.

**The pipeline:**
1. Read image(s) of handwritten notes
2. Load a domain vocabulary file (org names, research terms, people) to disambiguate messy handwriting
3. Apply a template to structure the output (status, pain points, next steps, rough notes)
4. Save structured transcription to an outputs folder
5. Spawn a subagent to generate summaries

**What makes it interesting:**
- **Domain context file** — a vocabulary list of ~90 terms (org names, acronyms, research jargon) that Claude uses to disambiguate unclear handwriting. "MATS" not "mats", "Pivotal" not "pivotal". This alone dramatically improved accuracy.
- **Template system** — different note types get different output structures. Meeting notes get status/pain points/next steps. General notes get freeform transcription.
- **Multi-step orchestration** — the skill chains three phases (transcribe → summarize → split), each building on the previous output.
- **Subagents for parallelism** — the summary generation and log splitting run as background agents, so you're not waiting for each step.

**Honest assessment:** This was the most ambitious skill I built, and it worked — but it was also more complex than it needed to be. The multi-step pipeline had enough edge cases (name normalization, deduplication, prep notes vs. meeting content) that maintaining it became its own task. I eventually switched to a different workflow for meeting notes. It's a good demo of **what's possible**, but also a lesson in **not over-engineering skills**. A simpler version (just transcribe + domain context, no splitting/summarizing) would have been 80% of the value at 20% of the complexity.

**Key pattern to steal:** The domain context file. If you work in any specialized field, a vocabulary list that Claude loads before transcription/analysis tasks is a cheap way to dramatically improve accuracy. Works for handwriting, audio transcription, or even document analysis.

---

## 2. Task triage with adversarial self-review

**What it does:** Pulls all tasks from Todoist (via MCP), compares them against a goals file, categorizes everything, and writes a structured triage report. Then spawns a subagent to red-team the report before finalizing.

**The flow:**
1. Pull tasks from Todoist using MCP tools (read-only — never mutates)
2. Read `goals.md` (stable reference of what matters) and previous task summary
3. Categorize every task: goal alignment, urgency, actionability
4. Write a triage report with sections: Do This Week / Delegate or Defer / Needs Clarification / Gap Analysis
5. Spawn a red-team subagent that reads the draft and challenges it
6. Incorporate valid critiques into the final report

**What makes it interesting:**
- **MCP integration** — Todoist tasks come in through the Model Context Protocol, not copy-paste. The skill specifies exactly which MCP tools to call and in what order.
- **Gap analysis** — cross-references goals against tasks to find: goals with no tasks, orphan tasks with no goal, priority mismatches, stale items overdue by >2 weeks.
- **Red-team subagent** — after the main analysis, a separate agent critiques the categorizations. This catches things like miscategorized tasks, missed gaps, or questionable priority calls. The critiques go into a "Review Notes" section so you can see what was challenged.
- **Read-only safety** — the skill explicitly forbids mutating Todoist. All suggested changes go into a checklist that the user reviews and executes manually.

**Key pattern to steal:** The adversarial subagent. Any time Claude produces an analysis or recommendation, spawning a second agent to critique it is cheap and catches real mistakes. You can do this in any context — paper drafts, code reviews, policy analysis.

---

## 3. Layered instructions (CLAUDE.md)

This isn't a single skill — it's the foundational pattern that makes everything else work.

**Three layers:**
```
~/.claude/CLAUDE.md              # Global: applies to everything
├── preferences (commit often, use PowerShell, etc.)
├── editing rules (minimal edits, confirm before large changes)
└── external tool rules (never mutate Todoist without permission)

project/CLAUDE.md                # Project-level: structure, navigation rules
├── folder structure and what lives where
├── project list with descriptions
├── conventions (archive format, wikilinks, etc.)
└── skill documentation

project/subproject/CLAUDE.md     # Subproject-level: specific context
├── what this subproject is about
├── key files and their purpose
└── project-specific rules
```

**Why it matters:** Claude reads all three at conversation start. This means:
- Global preferences (like "never silently delete Todoist tasks") apply everywhere
- Project structure is always loaded, so Claude navigates the repo correctly
- Subproject context means you don't have to re-explain what you're working on

**The compound effect:** Every time Claude does something you like, add it as an instruction. Every time it does something annoying, add a rule against it. After a few weeks, your CLAUDE.md captures your working style better than you could describe it upfront.

