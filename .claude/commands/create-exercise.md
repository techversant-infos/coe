# create-exercise

> Creates a hands-on exercise for a specific concept or lesson.

## Overview

This command generates a complete exercise with step-by-step instructions, hints, and a solution. It creates practical learning activities that reinforce theoretical concepts.

## Usage

```bash
/create-exercise [concept] [options]
```

## Parameters

### Required
- **concept** - The concept to practice (e.g., "css-selectors", "array-methods", "playwright-locators")

### Optional Flags
- `--type` - Exercise type: code-completion/debugging/build-from-scratch/refactor/integration (default: code-completion)
- `--topic` - Topic category: qa-automation/javascript-basics/playwright-engineering/custom (default: custom)
- `--duration` - Estimated duration in minutes (default: 45)
- `--difficulty` - Beginner/Intermediate/Advanced (default: Beginner)
- `--lesson-ref` - Reference lesson (for linking)
- `--output` - Output directory (default: `learning-paths/<topic>/exercises/`)

## Examples

```bash
/create-exercise css-selectors --topic javascript-basics --duration 30 --difficulty beginner
/create-exercise debug-failed-test --type debug --topic qa-automation --difficulty intermediate
/create-exercise build-login-form --type build --topic javascript-basics --duration 60
/create-exercise refactor-page-objects --type refactor --topic playwright-engineering
```

## Exercise Types

### Code Completion
Provide partially completed code with blanks to fill.
- Best for: Learning syntax and API usage
- Use: `--type code-completion`

### Debugging
Provide broken code with intentional errors.
- Best for: Understanding error patterns and debugging
- Use: `--type debug`

### Build from Scratch
Provide requirements and ask learner to build from scratch.
- Best for: Applying concepts independently
- Use: `--type build`

### Refactor
Provide working but poorly written code to improve.
- Best for: Learning best practices and patterns
- Use: `--type refactor`

### Integration
Combine multiple concepts in a larger task.
- Best for: Synthesizing knowledge and skills
- Use: `--type integration`

## Output Format

```markdown
## Exercise: [Title]

**Duration:** XX minutes
**Difficulty:** Beginner/Intermediate/Advanced
**Type:** Code Completion/Debugging/Build/Refactor/Integration

**Objective:** [What learner will practice]

**Prerequisites:**
- [Concept 1] from [Lesson reference]
- [Concept 2] from [Lesson reference]

**Instructions:**
1. Step-by-step guidance
2. Clear actions for learner
3. Measurable criteria

**Expected Outcome:**
- [Specific result 1]
- [Specific result 2]
- [Specific result 3]

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
Direct assistance without full solution
</details>

<details>
<summary>Solution</summary>

[Complete solution with explanation]

</details>
```

## Process Flow

1. **Analyze Concept**: Determine the learning objective and prerequisite knowledge
2. **Choose Exercise Type**: Based on complexity and learning goal
3. **Create Instructions**: Write clear, step-by-step guidance
4. **Design Hints**: Progressive hints that guide without revealing
5. **Build Solution**: Complete, well-documented solution
6. **Link to Content**: Reference relevant lessons and prerequisites

## Quality Controls

- [ ] Instructions are unambiguous and actionable
- [ ] Hints provide appropriate scaffolding
- [ ] Solution is complete and educational
- [ ] Duration estimate is realistic
- [ ] Exercise directly supports stated objective
- [ ] Example error messages are learner-friendly

## Integration

- Uses `.claude/agents/javascript-basics-coach.md` for JavaScript exercises
- Uses `.claude/agents/qa-automation-coach.md` for QA exercises
- Uses `.claude/agents/playwright-engineer.md` for Playwright exercises
- References `.claude/skills/hands-on-assignment-design/SKILL.md`
- Follows `.claude/rules/beginner-friendly-writing.md`
- Uses `.claude/templates/exercise-template.md`