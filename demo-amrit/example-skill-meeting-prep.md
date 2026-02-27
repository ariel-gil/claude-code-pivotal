# Example Skill: /meeting-prep

Save this as `.claude/skills/meeting-prep/SKILL.md` to create a `/meeting-prep` slash command.

---

```markdown
# /meeting-prep - Meeting Preparation

Prepare for a meeting by gathering context from multiple sources.

## Arguments
- Name of the person or topic for the meeting

## Steps

1. **Search local files** for any documents mentioning this person/topic
2. **Search email** (if Gmail MCP connected) for recent correspondence
3. **Search Slack** (if connected) for recent messages or mentions
4. **Search calendar** (if connected) for meeting history
5. **Build a prep doc** with:

### Who
- Name, title, organization
- How we know each other / previous interactions
- Their research interests or role

### Context
- What have we discussed before? (from emails, Slack, meeting notes)
- What are they working on currently? (from any available sources)
- Any outstanding action items from previous conversations?

### This Meeting
- What's the agenda or likely topic?
- What do I want to get out of this meeting?
- What might they want from me?

### Talking Points
- 3-5 prepared points based on the context above
- Any questions I should ask
- Any updates I should share

### Follow-Up Plan
- What should I do after the meeting?

## Rules
- If MCP tools aren't available, work with local files only
- Don't fabricate information - only include what you actually find
- Flag if you couldn't find much context (suggests this is a new contact)
```

---

## How This Works

When you type `/meeting-prep Stefan Torges`, Claude will search across all your connected services for any mention of that person, then compile everything into a concise prep document.

## What You Need

**Minimum**: Just local files. The skill works without any MCP connections.

**Better**: Gmail MCP (search email history with this person).

**Best**: Gmail + Slack + Calendar + local files. The more sources, the better the prep doc.

## Customization Ideas

- Add a "Research their recent publications" step (with WebSearch)
- Add a "Check CRM" step if you use Google Sheets as a contact database
- Add organization-specific context (e.g., always check Forethought's project page)
