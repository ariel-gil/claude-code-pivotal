# Example Skill: /digest

A daily or weekly digest that summarises what happened across your connected services.

---

## The Skill File

Save as `.claude/skills/digest/SKILL.md`:

```markdown
# /digest - Generate Activity Digest

Summarise recent activity across all connected services.

## Arguments
- Period: "daily" (default) or "weekly"

## Steps

1. **Email**: Search Gmail for all emails from the last [period]. Group by sender, highlight action items
2. **Calendar**: List all events from the last [period]. Note which had meeting notes
3. **Slack**: Search for messages mentioning me or in key channels from the last [period]
4. **Local files**: Check git log for recent commits. Check domains/ for state changes
5. **Tasks**: Check Todoist for completed and overdue tasks

## Output Format

### Email Summary
- [Count] emails received, [count] requiring action
- Key threads: [list with one-line summaries]

### Meetings
- [List of meetings with outcomes if notes exist]

### Slack Highlights
- [Key messages and threads]

### Tasks
- Completed: [list]
- Overdue: [list]
- Added: [list]

### Key Decisions Made
- [Any decisions captured in meeting notes or emails]

### Action Items Carried Forward
- [Anything unresolved that needs attention]

## Rules
- Be concise. This is a summary, not a transcript
- Highlight anything time-sensitive or blocking
- Flag if any connected service returned errors
```

## Why This Is Useful

- **Monday morning**: Run `/digest weekly` to catch up on everything from the previous week
- **End of day**: Run `/digest daily` to see what you accomplished and what's pending
- **After time away**: Run `/digest` to quickly get context on what happened while you were gone

## Adapting It

Replace the specific services with whatever you have connected. The pattern is the same:

1. Pull recent activity from each service
2. Summarise by category
3. Highlight what needs attention
4. List unresolved action items

Start with just email and calendar. Add services as you connect them.
