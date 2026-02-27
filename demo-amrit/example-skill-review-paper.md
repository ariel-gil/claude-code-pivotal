# Example Skill: /review-paper

Save this as `.claude/skills/review-paper/SKILL.md` to create a `/review-paper` slash command.

---

```markdown
# /review-paper - Deep Paper Review

Review a research paper with structured analysis.

## Arguments
- Paper URL, file path, or title to search for

## Steps

1. **Obtain the paper**: If given a URL, fetch it. If given a file path, read it. If given a title, search for it
2. **Read the full paper** before commenting
3. **Produce a structured review** with these sections:

### Quick Take (2-3 sentences)
What is this paper about and does it succeed?

### Key Claims and Evidence
- List the paper's main claims
- For each: what evidence supports it? How strong is the evidence?
- Extract specific quantitative results (tables, figures, p-values, effect sizes)

### Methodology Assessment
- What methods did they use?
- Are they appropriate for the research question?
- What are the key limitations?
- What controls or comparisons are missing?

### Relevance to My Research
[Customize this section to your areas]
- How does this connect to [your research area 1]?
- How does this connect to [your research area 2]?
- Are there ideas, methods, or datasets I could use?

### What I Would Do Differently
- Methodological improvements
- Extensions or follow-up questions
- Alternative interpretations of the results

### Bottom Line
- Should I cite this? In what context?
- Should I read the related work it references?
- Priority: [HIGH / MEDIUM / LOW] for my research agenda

## Rules
- Read the FULL paper before commenting
- Be honest about weaknesses, don't be generous just because it's published
- Distinguish between "this is wrong" and "this is a reasonable choice I disagree with"
- Note if the paper is a preprint vs. peer-reviewed
```

---

## How This Works

When you type `/review-paper https://arxiv.org/abs/2401.12345`, Claude will:
1. Fetch the paper
2. Read it completely
3. Produce the structured review above

## Customization Ideas

- Add a "Relevance to [specific project]" section
- Add a "Would [specific collaborator] find this useful?" check
- Include a "Tweet-length summary" at the end
- Add citation format output (BibTeX, Chicago, etc.)
