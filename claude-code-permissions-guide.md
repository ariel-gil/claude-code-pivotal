# Claude Code Permissions: Starter Guide

**Goal:** Stop approving every action without giving up safety.

## How It Works

Your `settings.json` has an **allow** list (auto-approved) and a **deny** list (always blocked). Everything else prompts you. Strategy: **pre-approve the safe stuff, let everything else prompt.**

## Setup

Copy `starter-settings.json` to `.claude/settings.local.json` in your project folder. The starter config auto-approves:

- **Read-only tools** (`Read`, `Glob`, `Grep`, `WebSearch`, `WebFetch`) — can't change anything
- **Safe bash** (`git`, `ls`, `dir`) — local, reversible

File edits, writes, and everything else still prompt you.

## Permission Modes

You can also switch modes during a session with `/permissions`:

- **`acceptEdits`** — auto-approves file edits, still prompts for bash. Good middle ground. Edits are scoped to the project folder Claude was opened in — it can't touch files elsewhere on your system.
- **`plan`** — read-only, Claude can explore but not change anything.

## Expanding Over Time

When you find yourself approving the same thing repeatedly, add it to the allow list. Common additions:

- `Bash(pip install:*)`, `Bash(npm install:*)` — package installs
- `Bash(python:*)` — running scripts (note: Claude can write then run arbitrary code)
- `Edit`, `Write` — if you commit often and find the prompts tedious

## What Permissions Don't Cover

- **Overwriting uncommitted files** — the main real risk. Commit often.
- **Bad decisions** — permissions control what actions happen, not whether they're good ideas. Review still matters.
