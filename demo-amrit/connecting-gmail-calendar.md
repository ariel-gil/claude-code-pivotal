# Connecting Gmail + Calendar via MCP

The highest-ROI integration you can set up. Once Claude can read your inbox and calendar, meeting prep, email drafting, and daily briefings become possible.

---

## What You Need

- Claude Code installed and working
- A Gmail / Google Workspace account
- A Zapier account (free tier works for testing, Professional for serious use)

## Option 1: Zapier MCP (Easiest)

Zapier provides a Model Context Protocol server that connects Claude Code to hundreds of services, including Gmail and Google Calendar. This is the fastest path.

### Setup Steps

1. **Create a Zapier account** at zapier.com if you don't have one
2. **Go to the MCP integration page**: In Zapier, search for "MCP" or "AI Actions"
3. **Enable Gmail and Google Calendar actions**: Connect your Google account and enable the actions you want (search emails, read emails, find events, create events)
4. **Get your MCP server URL**: Zapier will give you an MCP endpoint URL
5. **Add it to Claude Code**: Add the MCP server configuration to your `.claude/settings.json`:

```json
{
  "mcpServers": {
    "zapier": {
      "type": "url",
      "url": "YOUR_ZAPIER_MCP_URL_HERE"
    }
  }
}
```

6. **Restart Claude Code** or run `/mcp` to reconnect

### What You Can Do

Once connected, you can:
- **Search emails**: "Find emails from robert@example.com in the last week"
- **Read emails**: "Read the email about the meeting agenda"
- **Find events**: "What's on my calendar today?"
- **Create events**: "Schedule a meeting with X on Friday at 2pm"

## Option 2: Google MCP Servers (Direct)

If you prefer a direct connection without Zapier, there are community MCP servers for Google services. These require more technical setup but have no usage limits.

Search for "Google Calendar MCP server" or "Gmail MCP server" on GitHub. Setup typically involves:

1. Creating a Google Cloud project
2. Enabling the Gmail and Calendar APIs
3. Setting up OAuth credentials
4. Running the MCP server locally

## Tips

- **Start with read-only actions**. Search and read emails before you enable sending
- **Test with low-stakes queries first**. "What's on my calendar today?" before "Send an email to my boss"
- **Zapier free tier** gives you 100 tasks/month. That's enough for testing but not daily use. Upgrade if you're using it regularly
- **Privacy**: Be aware that email content passes through the MCP server. Use Zapier's enterprise features or self-hosted servers if you're handling sensitive data

## Example: Daily Briefing Query

Once Gmail and Calendar are connected, a simple briefing becomes:

```
Check my Gmail for important emails from the last 24 hours.
Check my Google Calendar for today's events.
Summarise: what needs my attention today?
```

This is the building block for automated briefings (see: Setting Up Automated Briefings).
