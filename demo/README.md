# Claude Code Workshop — Getting Started

Welcome! This is a companion repo for the Claude Code workshop. Start here, explore at your own pace.

## First things first

You only need to know three things to get started:

1. **Type naturally.** Claude Code is a terminal app, but you talk to it like a person. Ask it to do things in plain English.
2. **It works on files.** Point it at a folder, and it can read, edit, create, and search files in that folder.
3. **You approve changes.** Claude will ask before editing your files. You can accept, reject, or ask it to try something different.

### The few things you need right now
| What | How |
|------|-----|
| Undo the last edit | `Esc x2` or `Ctrl+Shift+-` |
| Auto-accept an edit | `Shift+Tab` |
| Add a file to your message | Type `@` and start typing the filename |
| Paste an image | `Alt+V` |
| Start over | `/clear` |
| Newline (without sending) | `Shift+Enter` |

That's it. Everything else you can pick up as you go.

---

## Try this first (~5 min)

The fastest way to see what Claude Code does:

1. Ask it: **"Read buggy_app.py and find the bugs"**
2. Watch it read the file, identify issues, and suggest fixes
3. Approve or reject each edit
4. If you don't like a change, hit `Esc x2` to undo it

---

## Try this next: set up your personal workspace (~10 min)

This is where Claude Code gets interesting. You can give it persistent instructions that carry across every conversation.

1. Look at `CLAUDE.md.example` in this folder — it's a sample instructions file
2. Create a file called `CLAUDE.md` in your project folder and add your own instructions
3. Claude reads this automatically at the start of every conversation

What to put in it:
- What you're working on and why
- How you like things written or structured
- Things Claude should always or never do

Check out `user-context.md.example` for an example of adding personal context (your background, working style) so Claude tailors responses to you.

**Global preferences:** Put a CLAUDE.md at `~/.claude/CLAUDE.md` and it applies across all your projects.

---

## What's in this folder

| File / Folder | What it is |
|---------------|------------|
| `CLAUDE.md.example` | Sample project instructions file |
| `user-context.md.example` | Sample "about me" section for your CLAUDE.md |
| `buggy_app.py` | Python script with intentional bugs — good for a first test |
| `sample-write-skill/` | Example custom `/write` skill that matches your writing style |
| `IDEAS.md` | Bigger list of things to try — broken down by technical safety and governance |

---

## Quick reference

Come back to this section when you need it. No need to memorize anything upfront.

### Essential commands
| Command | What it does |
|---------|-------------|
| `/help` | Show all available commands |
| `/clear` | Start a fresh conversation |
| `/compact` | Compress conversation context when it gets long |
| `/model` | Switch between models mid-conversation |
| `/add-dir <path>` | Add a folder to the current session (doesn't need to be a git repo) |

### Keyboard shortcuts
| Shortcut | What it does |
|----------|-------------|
| `Esc x2` or `Ctrl+Shift+-` | Revert the last file change (your main undo) |
| `Shift+Tab` | Auto-accept the proposed edit |
| `Ctrl+C` | Cancel current generation |
| `Escape` | Back out of current input / clear input |
| `Shift+Enter` | Newline without sending |
| `@` | Reference a file by path |
| `Alt+V` | Paste an image |
| `Meta+P` | Switch model (same as `/model`) |
| `Meta+O` | Toggle fast mode |
| `Ctrl+O` | Toggle verbose output |

### Input prefixes
| Prefix | What it does |
|--------|-------------|
| `!` | Run a bash command directly (e.g. `! ls`) |
| `/` | Slash commands (e.g. `/help`, `/model`, `/clear`) |
| `@` | Reference a file path |
| `&` | Run something in the background |

### Adding images & files
You can paste images with `Alt+V`, drag files into the terminal, or type `@` to reference files by path. Useful for sharing error screenshots, PDFs, or diagrams.

### Model names

You probably won't need these right away, but when you want to switch models with `/model`, the exact IDs are:

| Name | Model ID | When to use |
|------|----------|-------------|
| Opus | `claude-opus-4-6` | Hard problems, planning, nuanced judgment |
| Sonnet | `claude-sonnet-4-6` | Everyday work, good balance of speed and quality |
| Haiku | `claude-haiku-4-5` | Quick/cheap tasks, simple edits |

You can also launch with a specific model: `claude --model claude-sonnet-4-6`

---

## Do I need Git / GitHub?

No. You can point Claude Code at any folder on your machine with `/add-dir` and start working immediately.

That said, Git is worth setting up eventually because **it limits damage** — if Claude deletes or overwrites something, you can always get it back. And it's easy to use through Claude: just ask "commit my changes" or "push to GitHub" and Claude handles the git commands for you.

If you're not ready for that yet, `Esc x2` (revert) is your safety net.

---

## More things to explore

Once you're comfortable with the basics, try these:

### Build a custom writing skill
Look inside `sample-write-skill/` — it shows how to make a `/write` command that matches your voice. The key idea: drop in 2-4 pieces of your own writing at different formality levels, and Claude analyzes your style itself. See its `README.md` for setup instructions.

### Synthesize a pile of documents
Drop a folder of PDFs into your working directory (or use `/add-dir`), then:
> "Read all the files in this folder and write a structured synthesis. Focus on areas of agreement, disagreement, and open questions."

Then stress-test it:
> "Now red-team this synthesis — what are the strongest objections, what did we miss, what claims are weakest?"

### Literature review
> "Search for recent work on [topic]. For each paper: title, authors, key claims, and how it relates to [your question]."

**Caveat:** Claude sometimes fails to fetch certain URLs (paywalls, rate limits) and silently moves on to less relevant sources. Add this to your CLAUDE.md:
```
When doing web searches or fetching URLs: if a fetch fails or returns an error,
explicitly flag it (e.g. "Could not access [URL] — got [error]").
Do not silently substitute other sources.
```

### More ideas
See **[IDEAS.md](IDEAS.md)** for a bigger list broken down by technical safety and governance work.

---

## Useful principles

- **Agents, not chatbots.** Claude Code works behind the scenes — reading files, running code, searching — and returns informed results. The chat output is secondary.
- **Audio input is underrated.** Try Wispr Flow, voice recording on your phone, or native dictation (`Win+H` on Windows).
- **Work in markdown.** Claude reads and writes text-based files best. Keep a simple folder structure.
- **Delegation mindset.** Think: "How would I hand this to a capable but context-poor junior researcher?" Give success criteria, then check output — don't babysit the process.
- **Your CLAUDE.md improves over time.** When Claude does something you like, add it as an instruction. When it does something annoying, add a rule against it.
- **Try things, throw away what doesn't work.** Tools change fast; what failed 3 months ago might work now.
