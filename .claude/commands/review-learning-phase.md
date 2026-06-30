# review-learning-phase

> Reviews a learning phase for quality, accuracy, and adherence to standards.

## Overview

This command runs a comprehensive quality review of a learning phase, checking against established quality standards, pedagogical principles, and technical accuracy.

## Usage

```bash
/review-learning-phase [phase-path] [options]
```

## Parameters

### Required
- **phase-path** - Path to the phase directory to review (e.g., `learning-paths/qa-automation/phase-1`)

### Optional Flags
- `--depth` - Review depth: quick/full/comprehensive (default: full)
- `--focus` - Focus area: content/assessments/exercises/all (default: all)
- `--generate-report` - Generate a detailed review report (default: false)
- `--suggest-fixes` - Auto-generate fix suggestions (default: false)

## Examples

```bash
/review-learning-phase learning-paths/qa-automation/phase-1
/review-learning-phase learning-paths/javascript-basics/phase-1 --depth comprehensive --generate-report
/review-learning-phase learning-paths/playwright-engineering/phase-2 --focus exercises
```

## Review Checklist

### 1. Content Quality
- [ ] Learning objectives are measurable and specific
- [ ] Content is accurate and up-to-date
- [ ] Examples are correct and runnable
- [ ] Explanations are clear and beginner-friendly
- [ ] Prerequisites are accurately stated

### 2. Pedagogy
- [ ] Content progresses logically from simple to complex
- [ ] Concepts build on each other appropriately
- [ ] Explanations include multiple perspectives
- [ ] Common misconceptions are addressed

### 3. Exercises
- [ ] Every concept has a corresponding exercise
- [ ] Exercise difficulty matches content level
- [ ] Hints provide appropriate scaffolding
- [ ] Solutions are complete and well-explained
- [ ] Exercises are hands-on, not theoretical

### 4. Assessments
- [ ] Assessments align with learning objectives
- [ ] Rubrics are clear and measurable
- [ ] Passing criteria are fair and realistic
- [ ] Assessments measure understanding, not memorization

### 5. Technical Accuracy
- [ ] Code examples are syntactically correct
- [ ] Best practices are demonstrated
- [ ] Security considerations are addressed
- [ ] Performance implications are noted

### 6. Formatting
- [ ] Follows markdown standards
- [ ] Uses consistent terminology
- [ ] Includes all required sections
- [ ] Links are valid and descriptive

## Process Flow

1. **Load Phase**: Read all files in the specified phase directory
2. **Review Content**: Check pedagogical quality and accuracy
3. **Review Exercises**: Validate exercise quality and structure
4. **Review Assessments**: Ensure assessments are fair and aligned
5. **Quality Scoring**: Assign quality scores to each dimension
6. **Report Generation**: Create review report with findings and recommendations

## Output Format

### Quick Review
```
Phase Review: qa-automation/phase-1

Overall Score: 8.2/10

Strengths:
✅ Clear learning objectives
✅ Good exercise variety
✅ Well-structured lessons

Issues:
⚠️  Lesson 2: Missing code example for concept X
⚠️  Exercise 3: Hint 2 is too revealing
❌ Assessment: Rubric criterion unclear

Recommendations:
1. Add example to Lesson 2
2. Revise Hint 2 in Exercise 3
3. Clarify assessment criterion
```

### Full Review
```
Review Report: qa-automation/phase-1
Generated: 2026-06-26

Dimensions:
├── Content Quality: 9/10
├── Pedagogy: 8/10
├── Exercises: 9/10
├── Assessments: 7/10
├── Technical Accuracy: 10/10
└── Formatting: 9/10

Detailed Findings:
[Detailed breakdown of each issue]

Action Items:
1. [ ] [High Priority] Fix issue
2. [ ] [Medium Priority] Improve
3. [ ] [Low Priority] Polish
```

## Integration

- Uses `.claude/agents/curriculum-reviewer.md` for review logic
- Follows `.claude/rules/course-content-rules.md`
- Follows `.claude/rules/beginner-friendly-writing.md`
- Checks against `.claude/templates/` for structure compliance