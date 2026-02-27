# Setting Up Automated Briefings

Run Claude Code in headless mode on a schedule. Get a briefing file waiting for you every morning.

---

## The Concept

Claude Code can run without human interaction using the `--print` flag (headless mode). Combine this with a task scheduler, and you get automated outputs: daily briefings, inbox digests, deadline reminders.

## The Three Components

### 1. The Prompt Template

A text file that tells Claude what to do. Save it somewhere stable (e.g., `~/.claude/prompts/briefing.txt`).

```
You are generating a morning briefing. Check:

1. Gmail: Important emails from the last 24 hours (prioritise [your key contacts])
2. Google Calendar: Today's events and tomorrow's events
3. Local files: Check domains/work.md for active deadlines
4. Slack: Recent messages in key channels

Output format:
## Priority Emails
[List with one-line summaries and action needed]

## Today's Calendar
[Events with times and prep notes]

## Deadlines This Week
[From local project files]

## Action Items
[What needs doing today, ranked by urgency]

Save the output to daily-briefings/YYYY-MM-DD-morning.md
```

Customise this to your actual tools and priorities.

### 2. The Script

**Mac/Linux (bash):**
```bash
#!/bin/bash
cd /path/to/your/project
claude --print -p "$(cat ~/.claude/prompts/briefing.txt)" > "daily-briefings/$(date +%Y-%m-%d)-morning.md" 2>&1
```

**Windows (PowerShell):**
```powershell
Set-Location "C:\path\to\your\project"
$prompt = Get-Content "$env:USERPROFILE\.claude\prompts\briefing.txt" -Raw
$date = Get-Date -Format "yyyy-MM-dd"
claude --print -p $prompt | Out-File "daily-briefings\$date-morning.md" -Encoding utf8
```

### 3. The Scheduler

**Mac (launchd / cron):**
```bash
# Edit crontab
crontab -e

# Run at 8am every weekday
0 8 * * 1-5 /path/to/briefing-script.sh
```

**Linux (cron):**
```bash
crontab -e
0 8 * * 1-5 /path/to/briefing-script.sh
```

**Windows (Task Scheduler):**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily, 8:00 AM
4. Action: Start a Program
5. Program: `powershell.exe`
6. Arguments: `-ExecutionPolicy Bypass -File "C:\path\to\briefing-script.ps1"`

## Tips

- **Create the `daily-briefings/` directory** first and add it to `.gitignore` (briefings contain personal data)
- **Test the script manually** before scheduling. Run it once and check the output
- **Start simple**. Just Gmail + Calendar for your first briefing. Add services as you gain confidence
- **Error handling**: Redirect stderr to a log file so you can debug if the briefing fails silently
- **Multiple briefings**: You can run different prompts at different times (morning briefing at 8am, evening wrap-up at 6pm)
- **The `--print` flag** is what makes Claude run non-interactively. Without it, Claude expects human input

## Example Output Structure

After a week, your `daily-briefings/` folder looks like:

```
daily-briefings/
  2026-02-20-morning.md
  2026-02-20-evening.md
  2026-02-21-morning.md
  2026-02-21-evening.md
  ...
```

Each file is a self-contained briefing. Searchable. Reviewable. A log of what mattered each day.
