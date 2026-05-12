# conventions.md

This file documents how lesson plans and course materials are written so
agents can produce content that matches existing style.

## Lesson Plan Template

Every `lesson_plan.md` follows this structure in order:

```markdown
## Essential Questions

- Question 1?
- Question 2?

## Lesson Plan

Brief prose paragraph(s) describing purpose and context.

> Note: Instructor-only aside about timing or logistics.

### Setup

- Material or link needed before class
- Another preparation item

### Actual Lesson

- Review of previous class
  - Sub-point
    - Deeper detail
- Main activity
  - Instructions
- Wrap-up / reflection

### Homework

- Assignment description
```

Optional trailing sections: `### Resources`, `### Extensions`, `### Other possible homeworks`

## Formatting Rules

- No YAML frontmatter — metadata is implicit in directory naming
- `##` for top-level sections, `###` for subsections
- Nested bullets (`-`) for lesson flow; never numbered lists in the body
- **Bold** for key vocabulary and critical teacher instructions
- Backticks for commands, filenames, assignment titles, tool names
- `> Note:` blockquotes for instructor-only asides
- Inline markdown links: `[text](url)`
- Fenced code blocks with language tag for code examples and ChatBot prompts
- Inline timing hints: "Give 5m to journal", "~10 minutes"

## Tone and Voice

- First person, teacher's perspective ("I", "my")
- Informal, action-oriented, practical
- Includes pedagogical notes about pacing and common student confusion
- Direct instructions: "Go!" signals independent work time

## Recurring Lesson Patterns

- Start with "Review" of previous lesson
- "Code Review" or "TIL Review" — spin the wheel to pick a student
- Walk through activity as a class before releasing to independent work
- "Go!" = students work independently or in pairs
- End with reflection, debrief, or homework setup
- Explicit notes about when to reconvene the class

## Assessment Conventions (assessment.md)

- Same `## Essential Questions` and `## Lesson Plan` headers
- Numbered questions (may start from 0)
- Multiple choice answers as sub-bullets with `-`
- Code in answers uses fenced blocks

## Wheaties Problem Sets

"Wheaties" = recurring problem sets that build Python fluency:
- Topics: strings, lists, data structures, advanced data structures, grab bag, comprehensions
- Each topic has a `_structured.md` (scaffolded) and `_unstructured.md` (no hints) variant
- Students are assigned structured or unstructured based on skill level
- Problems are cumulative and reference prior problem set concepts

## Pedagogical Frameworks Referenced

- **Skills Assessments** — progressive multi-day coding challenges
- **Discussion-based lessons** — use `common_docs/discussion_rubric.pdf`, include journaling, circle-up, debrief
