# Pattern: Outline-to-Draft Chaining

A workflow where your outline is the single source of truth, and the draft is a downstream artifact that updates automatically when the outline changes.

---

## The Problem

Most people write outlines, then write drafts, then when they change the outline they manually update the draft. This is error-prone and tedious, especially with collaborator feedback loops.

## The Pattern

```
outline.md  -->  [skill/prompt]  -->  draft.md
    ^                                     |
    |            feedback                 |
    +-------------------------------------+
```

1. **Outline** lives in one file. This is what you edit directly
2. **Research notes / sources** live in separate files
3. A **skill** reads the outline + sources and generates the draft
4. When you change the outline, re-run the skill. The draft updates to match
5. When you get feedback on the draft, update the outline (not the draft), then regenerate

## Example Skill: /generate-draft

```markdown
# /generate-draft - Generate Draft from Outline

Read the outline and source materials, then generate or update the draft.

## Steps

1. Read `outline.md` for the current structure and key points
2. Read all files in `sources/` for supporting material, citations, and data
3. Read `draft.md` if it exists (to preserve any manually-approved sections)
4. Generate a new draft that:
   - Follows the outline's structure exactly
   - Incorporates relevant material from the sources
   - Preserves the voice and style from style.md
   - Marks sections that changed since the last version with [UPDATED]
5. Write the result to `draft.md`
6. Print a summary of what changed

## Rules
- The outline is the source of truth. If the outline and draft disagree, the outline wins
- Don't add sections that aren't in the outline
- Don't remove content that the outline still calls for
- Flag if a source contradicts the outline
```

## Extending the Chain

The same pattern works for any transformation:

```
outline  -->  draft  -->  slides
literature review  -->  gap analysis  -->  research questions
interview notes  -->  stakeholder map  -->  policy brief
data analysis  -->  results section  -->  blog post
```

Each step reads from the previous output and applies a transformation. Change something upstream, re-run the chain, and everything downstream updates.

## Why This Matters

This is the shift from "using Claude as something you ask questions to" to "using Claude as plumbing." Data flows in, gets transformed, flows out. You control the pipeline. The individual steps are automated.

## Getting Started

1. Split your current working document into an outline file and a draft file
2. Write a simple skill that reads the outline and generates the draft
3. Test it: change the outline, re-run, check that the draft updates correctly
4. Iterate: add source files, add feedback loops, extend the chain
