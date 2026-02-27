# Hook Examples

Hooks are shell commands that run automatically at specific lifecycle events. Add them to `.claude/settings.json`.

---

## SessionStart: Auto-Inject Context

Runs when a new Claude Code session starts. Useful for injecting the current date, time, and working directory.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'echo \"Session started: $(date \"+%Y-%m-%d %H:%M %Z\"). Working directory: $(pwd)\"'"
          }
        ]
      }
    ]
  }
}
```

**Why this is useful:** Claude doesn't know what time it is or where it's running unless you tell it. This hook solves that automatically.

---

## PreToolUse: Guard Against Dangerous Commands

Runs before every Bash command. Blocks destructive operations.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash /path/to/guard-dangerous-commands.sh"
          }
        ]
      }
    ]
  }
}
```

**The guard script** (`guard-dangerous-commands.sh`):
```bash
#!/bin/bash
# Extract the command from Claude's tool input
COMMAND=$(echo "$CLAUDE_TOOL_INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('command',''))" 2>/dev/null)

# Block dangerous patterns
if echo "$COMMAND" | grep -qiE '(rm -rf /|git push --force|git reset --hard|git clean -fd|drop table|truncate table)'; then
  echo "BLOCKED: Dangerous command detected: $COMMAND"
  exit 2  # Exit code 2 = block the tool call
fi

exit 0  # Exit code 0 = allow
```

**How it works:** Exit code 0 = allow. Exit code 2 = block. The hook reads the command Claude is about to run and checks it against patterns.

---

## Notification: Desktop Alert When Done

Runs when Claude sends a notification (typically after completing a long task).

**Windows (PowerShell):**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -NoProfile -Command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show($env:CLAUDE_NOTIFICATION, 'Claude Code')\""
          }
        ]
      }
    ]
  }
}
```

**Mac (osascript):**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"'$CLAUDE_NOTIFICATION'\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**Linux (notify-send):**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' \"$CLAUDE_NOTIFICATION\""
          }
        ]
      }
    ]
  }
}
```

---

## Putting It All Together

A complete hooks section in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'echo \"Session started: $(date \"+%Y-%m-%d %H:%M %Z\"). Working directory: $(pwd)\"'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/guard-dangerous-commands.sh"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "your-platform-notification-command-here"
          }
        ]
      }
    ]
  }
}
```
