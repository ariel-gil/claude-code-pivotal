# Advanced Claude Code Workflows

Reference materials for building more sophisticated Claude Code setups. Companion to the AI Tools Workshop at Pivotal.

These are patterns and templates, not prescriptions. Adapt them to your research, your workflow, your brain.

---

## CLAUDE.md Templates

Starting points for different types of work:

- **[Research Project Template](CLAUDE-md-research-template.md)** - For managing multiple projects, collaborators, and deadlines
- **[Governance / Policy Template](CLAUDE-md-governance-template.md)** - For policy analysis and international coordination work

## Skills & Agents

How to build reusable workflows and specialized personas:

- **[Your First Skill](your-first-skill.md)** - Step-by-step guide to building a skill from scratch
- **[Example: /review-paper](example-skill-review-paper.md)** - A structured paper review skill
- **[Example: /meeting-prep](example-skill-meeting-prep.md)** - Cross-service meeting preparation
- **[Example: /digest](example-skill-digest.md)** - Daily/weekly activity digest across connected services
- **[Example: paper-reviewer agent](example-agent-paper-reviewer.md)** - A specialized review agent (includes skill vs. agent comparison)

## Integrations

Connecting Claude Code to external services:

- **[Connecting Gmail + Calendar](connecting-gmail-calendar.md)** - Quickstart for the highest-ROI integration
- **[Setting Up Automated Briefings](automated-briefings.md)** - Headless mode + task scheduler = briefings while you sleep

## Patterns

Architectural patterns for more powerful setups:

- **[Domain Files](domain-files-pattern.md)** - Persistent state tracking across multiple life/work domains with cross-domain flags
- **[Outline-to-Draft Chaining](outline-to-draft-chain.md)** - Using outlines as single source of truth with downstream draft generation
- **[Multi-Agent Critique](multi-agent-critique.md)** - Deploy specialist agents to critique artifacts from multiple expert perspectives
- **[Thinking in Workflows](thinking-in-workflows.md)** - The mental shift from chatbot to assistant to infrastructure
- **[Hook Examples](hooks-examples.md)** - SessionStart context, dangerous command guards, desktop notifications (Windows/Mac/Linux)

## Quick Reference

- **[Power User Cheat Sheet](power-user-cheatsheet.md)** - Modes, shortcuts, model selection, settings architecture

---

## The Progression

1. **Day 1**: Write a CLAUDE.md (use a template above)
2. **Week 1**: Build your first skill (use the guide above)
3. **Week 2**: Connect a tool via MCP (start with Gmail + Calendar)
4. **Week 3**: Start chaining workflows together
5. **Ongoing**: Iterate. Add rules when Claude gets things right or wrong
