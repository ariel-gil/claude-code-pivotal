# The Domain Files Pattern

A pattern for using Claude Code as a persistent personal system that tracks multiple areas of your life or work.

---

## The Idea

Create separate markdown files for different domains (areas of concern). Each file tracks the current state of that domain. A central "productivity" or "hub" file collects cross-domain flags so that information from one domain can influence decisions in another.

## The Structure

```
your-project/
  domains/
    work.md          # Projects, deadlines, sprint status
    health.md        # Sleep, exercise, energy levels
    study.md         # Learning goals, progress
    productivity.md  # Daily structure, cross-domain flags hub
```

## The Hub File (productivity.md)

The key insight is the **cross-domain flags** section. Every domain writes flags here. Every domain reads them.

```markdown
# Productivity (Integration Layer)

This file is the bus. Every domain writes flags here. Every domain reads them.

## Today's One Thing
- [Your most important task for today]

## Cross-Domain Flags (Active)
_All domains write here. All domains read here._

### From Health
- [e.g., "Slept 4 hours. Low energy expected. Don't schedule deep work before noon"]

### From Work
- [e.g., "Paper deadline Mar 3. Block calendar this week"]

### From Study
- [e.g., "Exam next Tuesday. Need 2 hours/day for review"]
```

## How It Works

1. **Start a domain session**: Say "[domain] session" (e.g., "work session"). Claude reads that domain file + productivity.md
2. **Work in the domain**: Claude has full context for that area
3. **End-of-session sweep**: Run `/wrap` or manually update. Claude writes any state changes back to the domain file and updates cross-domain flags in productivity.md
4. **Cross-domain awareness**: When you start a work session, Claude sees the health flag saying you slept badly, and adjusts recommendations accordingly

## Why This Works

- **Nothing falls through cracks**: The flags system surfaces things across domains
- **No re-explaining**: Claude reads the domain file and immediately has context
- **Compounding knowledge**: Each session updates the state, so the files get more accurate over time
- **Separation of concerns**: Health stuff stays in health.md, work stuff in work.md. But the flags propagate

## Example: Health Flag Affecting Work

Your health.md tracks sleep data (manually or via Fitbit MCP):

```markdown
### Sleep (last 3 nights)
- Mon: 7h 20m (good)
- Tue: 5h 10m (poor, late working)
- Wed: 4h 30m (very poor, anxiety)
```

Your productivity.md cross-domain flag:

```markdown
### From Health
- Sleep debt accumulating. Wed was 4h30m. Recovery priority: early bedtime tonight, no deep work after 3pm
```

When you start a work session on Thursday, Claude sees this flag and suggests lighter tasks, shorter blocks, and an earlier cutoff.

## Getting Started

1. Create `domains/` directory in your project
2. Start with 2-3 domains (work + one other that matters to you)
3. Create a productivity.md with the cross-domain flags section
4. Add a `/wrap` skill that updates domain files at end of session
5. Iterate: add domains as needed, remove ones you don't use
