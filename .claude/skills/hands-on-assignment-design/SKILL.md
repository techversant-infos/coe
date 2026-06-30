# Hands-On Assignment Design

Guidelines for creating effective hands-on exercises that reinforce learning concepts and build practical skills.

## When to Use This Skill

Use this skill when:
- Designing exercises for any learning path
- Creating practical assignments to accompany lessons
- Building coding challenges or lab exercises
- Structuring project-based learning activities

## Exercise Design Principles

### Learning Objective Alignment
Every exercise must:
1. Directly support a specific learning objective
2. Provide appropriate challenge for the learner's level
3. Include clear success criteria
4. Offer scaffolding without doing the work

### Progressive Difficulty
- **Level 1 (Introduction)**: Follow-along, highly guided
- **Level 2 (Guided Practice)**: Fill in gaps, hints provided
- **Level 3 (Independent Practice)**: Complete from specification
- **Level 4 (Challenge)**: Extension beyond requirements

### Exercise Types

#### Code Completion
Provide partially completed code with blanks to fill.
- Best for: Learning syntax and patterns
- Example: "Complete the function to sort an array"

#### Debugging
Provide broken code and ask learner to fix it.
- Best for: Understanding error patterns
- Example: "This test has 3 bugs. Find and fix them"

#### Build from Scratch
Provide requirements and ask learner to build.
- Best for: Applying concepts independently
- Example: "Build a function that validates email addresses"

#### Refactoring
Provide working but poorly written code.
- Best for: Learning best practices
- Example: "Refactor this test suite to use Page Object Model"

#### Integration
Combine multiple concepts in a larger task.
- Best for: Synthesizing knowledge
- Example: "Build a test suite that covers login, search, and checkout"

## Exercise Structure Template

### Header
```markdown
## Exercise [N]: [Title]

**Duration:** XX minutes
**Difficulty:** Beginner/Intermediate/Advanced
**Type:** Code Completion/Debugging/Build/Refactor/Integration
```

### Objective
```markdown
**Objective:** [Single sentence describing what learner will practice]
```

### Prerequisites
```markdown
**Prerequisites:**
- [Concept 1] from [Lesson reference]
- [Concept 2] from [Lesson reference]
```

### Instructions
```markdown
**Instructions:**
1. Step-by-step guidance
2. Clear and actionable steps
3. No ambiguity
```

### Expected Outcome
```markdown
**Expected Outcome:**
- [Specific result 1]
- [Specific result 2]
- [Specific result 3]
```

### Hints
```markdown
<details>
<summary>Hint 1: [Category]</summary>
Gentle nudge in the right direction
</details>

<details>
<summary>Hint 2: [Category]</summary>
More specific guidance
</details>

<details>
<summary>Hint 3: [Category]</summary>
Direct assistance without giving full solution
</details>
```

### Solution
```markdown
<details>
<summary>Solution</summary>

[Complete solution with explanation]

</details>
```

## Exercise Quality Checklist

- [ ] Clear, measurable objective
- [ ] Prerequisites are accurate
- [ ] Instructions are unambiguous
- [ ] Expected outcome is specific
- [ ] Hints provide progressive help
- [ ] Solution is complete and well-explained
- [ ] Duration estimate is realistic
- [ ] Difficulty level matches target learner
- [ ] Exercise directly supports learning objective

## Common Mistakes to Avoid

1. **Vague instructions**: "Make it better" vs. "Refactor to reduce duplication"
2. **Missing context**: Don't assume learners know unstated prerequisites
3. **No success criteria**: Learners need to know when they're done
4. **Jumping difficulty**: Each exercise should build on the previous
5. **Too much hand-holding**: Challenge learners to think independently
6. **No real-world relevance**: Use realistic scenarios when possible
