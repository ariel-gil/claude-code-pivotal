#!/usr/bin/env python3
"""
Claude Code safety hook - blocks dangerous commands that slip past settings.json rules.
Place at: ~/.claude/hooks/safety_check.py
"""

import json
import sys
import re

# Patterns that are always blocked, regardless of settings.json
BLOCKED_PATTERNS = [
    r"rm\s+-rf\s+/",           # rm -rf / (root deletion)
    r"rm\s+-rf\s+~",           # rm -rf ~ (home deletion)
    r"rm\s+-rf\s+\$HOME",      # rm -rf $HOME
    r":\(\)\{.*\}",            # fork bomb
    r"dd\s+if=.*of=/dev/",     # dd to block device
    r"mkfs\.",                  # format filesystem
    r">\s*/dev/sd",            # write to disk device
    r"curl.+\|\s*(bash|sh)",   # curl pipe to shell
    r"wget.+\|\s*(bash|sh)",   # wget pipe to shell
    r"chmod\s+777\s+/",        # chmod 777 on system paths
    r"sudo\s+rm",              # sudo rm anything
    r"sudo\s+dd",              # sudo dd anything
]

def is_dangerous(command: str) -> tuple[bool, str]:
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True, f"Blocked pattern: {pattern}"
    return False, ""

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)  # Can't parse input, let it through

    tool_name = data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)  # Only checking Bash commands

    command = data.get("tool_input", {}).get("command", "")
    if not command:
        sys.exit(0)

    dangerous, reason = is_dangerous(command)
    if dangerous:
        print(f"BLOCKED: {reason}", file=sys.stderr)
        sys.exit(2)  # Exit 2 = block the action

    sys.exit(0)  # Allow

if __name__ == "__main__":
    main()
