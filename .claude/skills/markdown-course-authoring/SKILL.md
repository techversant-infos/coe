# Markdown Course Authoring

Standards and patterns for authoring learning content in markdown format.

## When to Use This Skill

Use this skill when:
- Writing lessons, exercises, or assessments
- Creating README files for learning paths
- Authoring any learning content in markdown
- Formatting content for learners

## Markdown Structure for Learning Content

### Lesson Structure
```markdown
# Lesson: [Title]

**Duration:** XX minutes
**Prerequisites:** [What learners need to know]

## Learning Objectives

By the end of this lesson, learners will be able to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Introduction

[Context and motivation for the topic]

## Core Concepts

### Concept 1

[Explanation with examples]

<details>
<summary>Example</summary>

[Code example or demonstration]

</details>

### Concept 2

[Explanation with examples]

## Hands-On Practice

See `exercises/exercise-N.md` for practice activities.

## Summary

[Key takeaways from the lesson]

## Next Steps

- Proceed to [Lesson N+1]
- Review [concept reference]
```

### Exercise Structure
See `.claude/skills/hands-on-assignment-design/SKILL.md` for exercise templates.

### Assessment Structure
See `.claude/skills/assessment-rubric-design/SKILL.md` for assessment templates.

## Formatting Standards

### Headings
- `#` - Lesson/exercise/assessment title
- `##` - Major sections
- `###` - Sub-sections
- Use consistent hierarchy

### Lists
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Use `- [ ]` for checkboxes (learning objectives)

### Code Blocks
- Always specify language for syntax highlighting
- Use comments to explain code
- Provide complete, runnable examples
```javascript
// Example: Clear, commented code
function example() {
  // Explanation of what happens here
  return "result";
}
```

### Callouts and Emphasis
- **Bold** for key terms
- `Code` for inline code references
- Blockquotes for tips or warnings
- Details/summary for hints and solutions

### Links
- Use relative paths for internal links
- Use descriptive link text: [Lesson 2](../phase-1/lesson-2.md)
- Link to prerequisites, exercises, and assessments

## Accessibility

- Use descriptive headings for screen readers
- Provide alt text for images
- Ensure sufficient color contrast in formatted text
- Use lists for step-by-step instructions
- Avoid relying on color alone for meaning

## Quality Checklist

- [ ] Clear, descriptive title
- [ ] Learning objectives listed (if applicable)
- [ ] Prerequisites stated
- [ ] Code examples are complete and runnable
- [ ] Links are relative and descriptive
- [ ] Consistent heading hierarchy
- [ ] No ambiguous language
- [ ] Spelling and grammar checked
- [ ] Formatting is consistent
- [ ] Accessibility standards met

## Resources

- Follows `.claude/rules/markdown-structure.md`
- Follows `.claude/rules/course-content-rules.md`
- Follows `.claude/rules/beginner-friendly-writing.md`