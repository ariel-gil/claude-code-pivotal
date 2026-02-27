# Pattern: Multi-Agent Critique

Build something with Claude, then deploy multiple specialist agents to critique it from different expert perspectives.

---

## The Problem

When Claude builds something for you, it has blind spots. A single perspective, no matter how capable, will miss things that a different expert would catch immediately. Code that runs perfectly might have statistical flaws. A data pipeline that's technically correct might produce results that contradict domain knowledge.

## The Pattern

```
[Build Phase]          [Critique Phase]
                       ┌─ Agent 1: Data Quality
Claude builds    -->   ├─ Agent 2: Domain Expertise
the artifact           ├─ Agent 3: Code Review
                       └─ Agent 4: Methodology
                              |
                       [Synthesis: fix issues, iterate]
```

1. **Build**: Let Claude (or a team of agents) create the initial artifact
2. **Deploy critics**: Launch multiple agents simultaneously, each with a different expert perspective
3. **Synthesise**: Review the critiques, fix the issues, iterate

## Why Multiple Agents?

Each agent approaches the same artifact from a fundamentally different angle:

| Agent Role | What It Catches |
|-----------|-----------------|
| **Data quality auditor** | Missing data, encoding errors, impossible values, temporal inconsistencies |
| **Domain expert** | Results that contradict established knowledge, missing variables, wrong assumptions |
| **Code reviewer** | Bugs, inefficiencies, edge cases, poor practices |
| **Methodology reviewer** | Statistical errors, wrong metrics, overfitting, invalid comparisons |
| **Writing reviewer** | Unclear arguments, unsupported claims, structural problems |

A code reviewer won't catch that your model contradicts domain knowledge. A domain expert won't catch that your AUC metric is measuring the wrong thing. You need both.

## Setting Up Critique Agents

You can run critique agents using Claude Code's Task tool or as separate sessions.

### As a Skill

Create a `/critique` skill that spawns multiple review passes:

```markdown
# /critique - Multi-Perspective Review

Run multiple critique passes on the specified artifact.

## Steps

1. Read the artifact at the specified path
2. Run a data quality review: check for missing data, impossible values, temporal issues
3. Run a domain expertise review: check if results make sense given established knowledge
4. Run a methodology review: check statistical validity, metrics, assumptions
5. Run a writing/clarity review: check arguments, structure, unsupported claims
6. Synthesise: list all issues found, ranked by severity, with suggested fixes
```

### As Separate Agents

Create agents in `.claude/agents/` with specific expertise:

- `data-auditor.md`: "You are a data quality specialist. Your job is to find data issues..."
- `domain-expert.md`: "You are an expert in [field]. Review this artifact for domain errors..."
- `methodology-reviewer.md`: "You are a statistician. Check the methodology for..."

## When to Use This

- After building any quantitative model or data pipeline
- After writing a research paper or policy brief
- After creating a complex analysis
- Any time the cost of an undetected error is high

## Tips

- **Run critics in parallel** when possible. They're independent of each other
- **Be specific about the domain**. A generic "review this" is less useful than "review this as a nuclear policy expert"
- **Let critics disagree**. If two agents flag contradictory issues, that's valuable information
- **Iterate**: Fix the issues, then run the critics again. Second-pass catches are often the most subtle
- **Not just for code**: This pattern works for writing, analysis, proposals, anything with multiple quality dimensions
