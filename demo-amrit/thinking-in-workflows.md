# Thinking in Workflows

The mental shift from "asking Claude questions" to "building systems that compound."

---

## The Three Stages

Most people go through roughly three stages with AI tools:

### Stage 1: The Chatbot
You ask Claude a question. It answers. You ask another. This is useful but limited. Every interaction starts from scratch. There's no accumulation.

**Looks like**: "Summarise this paper." "Write an email to X." "Explain this concept."

### Stage 2: The Assistant
You give Claude context (via CLAUDE.md), connect it to your tools (via MCP), and build reusable workflows (via skills). Now it knows who you are, can access your actual data, and remembers your preferences.

**Looks like**: `/meeting-prep Stefan Torges` and getting a prep doc that pulls from Gmail, Slack, Granola, and local files. One command, three minutes, done.

### Stage 3: The Infrastructure
You start thinking about data flows. What's the source of truth? What's downstream? What can be automated? What should be chained together? You build systems where Claude is plumbing, not a conversation partner.

**Looks like**: An outline that generates a draft. A briefing that runs while you sleep. Critique agents that review your work from multiple angles simultaneously.

## How to Get to Stage 3

You don't need to get there all at once. The progression is natural:

1. **Notice repetition**. Every time you give Claude the same instruction twice, that's a workflow waiting to be built
2. **Ask "what's the source of truth?"** For any document you maintain, ask: is this the original, or is it derived from something else? If it's derived, can it be regenerated?
3. **Ask "what's downstream?"** When you change something, what else needs to change? If the answer is "I manually update three other files," that's a chain waiting to be automated
4. **Ask "does this need me?"** Some tasks require your judgment. Others just require your presence. Automate the second kind
5. **Ask "what would I build if implementation were free?"** The answer reveals workflows you've never considered because they seemed too expensive to create

## Examples of Stage 3 Thinking

| Old Way | New Way |
|---------|---------|
| Write outline, then manually write draft | Outline generates draft. Change outline, regenerate draft |
| Check email, calendar, Slack separately each morning | Automated briefing combines all three, runs before you wake up |
| Review a paper by reading and taking notes | Deploy multiple critique agents (methodology, domain, writing) in parallel |
| Track meeting action items in your head | Skill extracts action items from meeting transcript, adds to Todoist, updates project file |
| Update stakeholder list manually | Networking skill logs contacts to CRM and local backup simultaneously |

## The Key Insight

The tools don't just speed up existing workflows. They make entirely new workflows possible, ones you couldn't have imagined before because the implementation cost would have been absurd.

A solo researcher spending 30 minutes to set up a four-agent critique pipeline would never have been worth it if each "agent" was a human expert charging consulting rates. But when the marginal cost is near-zero, you start doing things that were previously only possible for well-funded teams.

That's the real shift. Not "do things faster." It's "do things that were previously impossible for someone at your scale."
