# Claude Code Power User Cheat Sheet

Quick reference for features beyond the basics.

---

## Modes

| Command | What It Does |
|---------|--------------|
| `/plan` | Enter plan mode: Claude researches and proposes a plan before writing code. Good for complex tasks |
| `/compact` | Compress conversation history. Use when context gets long and Claude starts forgetting earlier parts |
| `/fast` | Toggle fast output mode. Same model, faster responses |
| `/insights` | Generate usage analytics report. Shows your patterns, tool usage, session stats |
| `/mcp` | Reconnect MCP servers without restarting Claude Code |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Tab` | Toggle between Plan and Act modes |
| `Esc` | Cancel current generation / interrupt Claude |
| `Ctrl+C` | Exit Claude Code |

## Model Selection

Claude Code can switch between models mid-conversation:

- **Opus 4.6**: Most capable. Use for complex reasoning, multi-step tasks, research
- **Sonnet 4.6**: Fast and capable. Good default for most tasks
- **Haiku 4.5**: Fastest and cheapest. Good for simple edits, quick questions

Switch with: `claude --model claude-sonnet-4-6` (at startup) or configure in settings.

## Background Tasks

Run long tasks in the background while you keep working:

- Claude Code can execute commands with `run_in_background` and notify you when done
- Combine with hooks (see hooks-examples.md) for desktop notifications on completion

## Skills (Slash Commands)

Skills are reusable prompts saved as markdown files in `.claude/skills/`.

**Create a skill:**
1. Create `.claude/skills/my-skill/SKILL.md`
2. Write the prompt instructions in markdown
3. Use it: `/my-skill [optional arguments]`

See `your-first-skill.md` for a full walkthrough.

## Agents

Agents are specialised personas with their own tool access and memory.

**Create an agent:**
1. Create `.claude/agents/my-agent.md`
2. Define: role, personality, available tools, rules

Agents are launched via the Task tool or by name in conversation.

## Hooks

Hooks are shell commands that run at lifecycle events. Add to `.claude/settings.json`.

| Event | When It Fires |
|-------|---------------|
| `SessionStart` | New session begins |
| `PreToolUse` | Before any tool call (can block it) |
| `PostToolUse` | After a tool call completes |
| `Notification` | When Claude sends a notification |

See `hooks-examples.md` for ready-to-use configurations.

## MCP (Model Context Protocol)

Connect Claude to external services. Add servers to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "service-name": {
      "type": "url",
      "url": "https://your-mcp-server-url"
    }
  }
}
```

Common MCP services: Gmail, Google Calendar, Slack, Google Sheets, Fitbit, Todoist.

See `connecting-gmail-calendar.md` for setup walkthrough.

## CLAUDE.md Architecture

| File | Scope | Purpose |
|------|-------|---------|
| `~/.claude/CLAUDE.md` | Global (all projects) | Identity, writing style, general rules |
| `.claude/CLAUDE.md` | Project-specific | Project context, collaborators, deadlines |
| `~/.claude/style.md` | Global | Writing style rules (shared across projects) |

Global loads first, then project-specific. Project rules override global when they conflict.

## Useful Patterns

- **Domain files**: Track different areas (work, health, study) in separate files with a central flags hub
- **Outline-to-draft chaining**: Outline as source of truth, draft regenerated from it
- **Automated briefings**: Headless mode + scheduler = daily briefings
- **Multi-agent critique**: Build something, then deploy specialist agents to critique it from different angles

## Privacy & Security

- **Turn off training data sharing** in your Anthropic account settings if working on sensitive material
- **Use `.gitignore`** for briefings, personal domain files, and anything with sensitive data
- **Guard hooks** can block dangerous commands before they execute
- **Redact before sharing**: Create redacted versions of CLAUDE.md and domain files for demos or repos
