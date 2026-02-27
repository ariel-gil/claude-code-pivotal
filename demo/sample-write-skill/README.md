# Sample `/write` Skill

This folder shows how to build a Claude Code **custom skill** that matches your writing style.

## The Core Idea

You don't describe your style to Claude — you just give it samples of your writing at different levels of formality (blog post, technical paper, reflective essay, etc.), and **Claude analyzes them itself** to extract your patterns.

That's it. Drop in your writing, Claude figures out your voice.

## Structure

```
.claude/
  skills/
    write.md    <-- The skill prompt (includes writing samples inline)
```

Everything lives in one file. The placeholder snippets in `write.md` cover five registers (casual, technical, persuasive, instructional, formal). Replace them with your own writing.

## How to Set This Up

1. Copy `write.md` into your project's `.claude/skills/` folder
2. Replace the placeholder snippets with 2-5 pieces of your own writing
   - Include different registers: a blog post, a technical explanation, a personal reflection
   - Claude needs to see your range to match the right tone
3. Invoke with `/write` in Claude Code

## Why This Works

The skill tells Claude to **read your samples first and extract your style patterns itself** before editing anything. This means:

- You don't need to articulate your own style (hard to do accurately)
- Claude picks up on things you wouldn't think to mention (sentence rhythm, how you use transitions, when you break formality)
- Different formality levels let Claude match the right register to the piece you're working on
