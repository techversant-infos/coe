# Markdown Structure

Techversant CoE standards for markdown file structure and formatting. All content in `engineering-academy/` and `learning-paths/` must follow these conventions.

## File Organization

### Engineering Academy Structure
```
engineering-academy/
└── <NN-discipline>/
    ├── README.md              # Discipline overview
    └── <topic>/
        ├── README.md          # Learning path overview
        ├── phase-1/
        │   ├── README.md      # Phase overview
        │   ├── lessons/
        │   │   ├── lesson-1.md
        │   │   └── lesson-2.md
        │   ├── exercises/
        │   │   ├── exercise-1.md
        │   │   └── exercise-2.md
        │   └── assessment.md
        └── phase-2/
            └── ...
```

### Naming Conventions
- Use kebab-case for all file names
- Prefix files with type: `lesson-`, `exercise-`, `assessment-`
- Use sequential numbering: `lesson-1.md`, `lesson-2.md`
- Use descriptive suffixes: `phase-1`, `phase-2`

### File Paths
- Use relative paths for internal links: `[Lesson 2](./lesson-2.md)`
- Use forward slashes for cross-path links: `[QA Path](../qa-automation/)`
- Avoid absolute paths for portability

## Markdown Formatting Standards

### Headings
- `#` - Document title (only one per file)
- `##` - Major sections
- `###` - Sub-sections
- `####` - Minor sub-sections
- Maintain consistent hierarchy

### Lists
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Use `- [ ]` for checkboxes (learning objectives)
- Indent sub-items with 2 spaces

### Code Blocks
- Always specify language for syntax highlighting
- Include full, runnable examples
- Use comments to explain key points
- Show expected output when relevant

```markdown
```javascript
// Example with comments
function greet(name) {
  return `Hello, ${name}!`;
}
// Expected: "Hello, World!"
```
```

### Tables
- Use tables for structured data
- Keep columns aligned
- Use consistent formatting

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

### Blockquotes
- Use for notes, tips, and warnings
- Use > for blockquotes
- Keep them concise

```markdown
> **Note:** This is an important point.
> Use > for callouts and tips.
```

### Details/Summary
- Use for collapsible content (hints, solutions)
- Provide clear summary text
- Include full content inside

```markdown
<details>
<summary>Click to reveal solution</summary>

Hidden solution content here

</details>
```

## Document Structure Templates

### README Template
```markdown
# Learning Path Title

> Brief description of the learning path

## Overview

[What this path teaches and why it matters]

## Prerequisites

- [ ] Prerequisite 1
- [ ] Prerequisite 2

## Learning Path

### Phase 1: Title
- **Duration:** X weeks
- **Topics:** List of topics
- **Status:** Complete/In Progress/Upcoming
- [Start Phase 1](phase-1/)

### Phase 2: Title
[Similar structure]

## Progress

- [ ] Phase 1: Not started
- [x] Phase 2: Complete

## Resources

- [Link 1](url)
- [Link 2](url)
```

### Phase README Template
```markdown
# Phase Title

> Phase description and goals

## Overview

[What this phase covers]

## Learning Objectives

By the end of this phase, you will be able to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Prerequisites

- [Link to previous phase]
- [List of required knowledge]

## Contents

### Lessons
1. [Lesson 1](lessons/lesson-1.md)
2. [Lesson 2](lessons/lesson-2.md)
3. [Lesson 3](lessons/lesson-3.md)

### Exercises
1. [Exercise 1](exercises/exercise-1.md)
2. [Exercise 2](exercises/exercise-2.md)
3. [Exercise 3](exercises/exercise-3.md)

### Assessment
- [Phase Assessment](assessment.md)

## Time Estimate

- Lessons: X hours
- Exercises: Y hours
- Assessment: Z hours
- **Total:** T hours

## Success Criteria

- Complete all lessons
- Pass all exercises
- Pass assessment with score >= 70%
```

## Quality Checklist

- [ ] File uses correct template
- [ ] Headings follow hierarchy (no skipped levels)
- [ ] All links use relative paths
- [ ] Code blocks have language specified
- [ ] Lists use consistent formatting
- [ ] Tables are properly formatted
- [ ] No trailing whitespace
- [ ] Lines under 120 characters when possible
- [ ] No blank lines between heading and content

## Common Mistakes

### ❌ Skipped heading levels
```markdown
# Title
#### Skipped ## and ###
```

### ✅ Correct hierarchy
```markdown
# Title
## Section
### Sub-section
```

### ❌ Inconsistent list formatting
```markdown
- Item 1
* Item 2  (mixed - and *)
+ Item 3  (mixed - and *)
```

### ✅ Consistent formatting
```markdown
- Item 1
- Item 2
- Item 3
```

### ❌ Missing language specifier
```javascript
const x = 1;
```

### ✅ With language specifier
```javascript
const x = 1;
```