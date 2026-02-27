# Your First Skill: A Step-by-Step Guide

Skills are reusable workflows you can trigger with a slash command. They're just markdown files. Here's how to build one.

---

## The Anatomy of a Skill

A skill lives at `.claude/skills/[skill-name]/SKILL.md`. That's it. One markdown file in the right directory.

```
your-project/
  .claude/
    skills/
      my-skill/
        SKILL.md    <-- this is the entire skill
```

## Step 1: Pick Something You Do Repeatedly

Good first skills:
- **Paper review**: You always review papers the same way
- **Meeting prep**: You always want the same context before meetings
- **Email draft**: You always draft emails with the same structure
- **Literature search**: You always search for papers in the same databases
- **Weekly review**: You check the same things every Sunday

## Step 2: Write the SKILL.md

Here's the simplest possible skill:

```markdown
# /my-skill - [What It Does]

[One sentence describing the skill]

## Steps
1. [First thing Claude should do]
2. [Second thing Claude should do]
3. [Third thing Claude should do]

## Rules
- [Any constraints or preferences]
```

That's a working skill. When you type `/my-skill`, Claude reads this file and follows the instructions.

## Step 3: Add Arguments (Optional)

```markdown
## Arguments
- [What the user passes after the slash command]
```

Example: For `/meeting-prep Stefan Torges`, the argument is "Stefan Torges".

## Step 4: Add Allowed Tools (Optional)

By default, skills can use any tool Claude has access to. To restrict:

```markdown
## Allowed Tools
Read, Glob, Grep, WebSearch, WebFetch
```

This is useful for skills that should be read-only (no file editing).

## Step 5: Test It

1. Open Claude Code in your project
2. Type `/my-skill` (or `/my-skill [argument]`)
3. Watch what happens
4. Iterate: if Claude does something wrong, add a rule against it

---

## Example: A Simple Literature Search Skill

```markdown
# /lit-search - Literature Search

Search for recent papers on a topic and produce a structured summary.

## Arguments
- Topic or research question to search for

## Steps
1. Search the web for recent papers (last 2 years) on the given topic
2. Find at least 5 relevant papers
3. For each paper, extract:
   - Title, authors, year, venue
   - Key finding (1-2 sentences)
   - Methodology
   - Relevance to my research (HIGH/MEDIUM/LOW)
4. Produce a summary table
5. Recommend which papers I should read in full

## Rules
- Prefer peer-reviewed papers over preprints where possible
- Note if a paper is a preprint
- Don't include papers I've already cited (check my local files)
```

## Tips

- **Start simple, iterate.** Your first version doesn't need to be perfect
- **Add rules when Claude gets things wrong.** "Don't use WebFetch for Google Docs" is a real rule born from experience
- **Skills can call agents.** A `/review-paper` skill can delegate to a `paper-reviewer` agent
- **Background skills exist.** Set `user_invocable: false` for skills that run automatically (like context-awareness monitoring)
