# review-learning-phase

> Reviews a learning phase within the Engineering Academy for quality, accuracy, and Techversant standards compliance.

## Overview

This command runs a comprehensive quality review of a learning phase within `engineering-academy/`, checking against Techversant quality standards, competency frameworks, and pedagogical principles.

## Usage

```bash
/review-learning-phase [phase-path] [options]
```

## Parameters

### Required
- **phase-path** - Path to the phase directory (e.g., `engineering-academy/02-quality-engineering/automation/playwright/phase-1`)

### Optional Flags
- `--depth` - Review depth: quick/full/comprehensive (default: full)
- `--focus` - Focus area: content/assessments/exercises/all (default: all)
- `--level` - Verify alignment with competency level (Foundation/Practitioner/Advanced/Expert)
- `--generate-report` - Generate a detailed review report (default: false)
- `--suggest-fixes` - Auto-generate fix suggestions (default: false)

## Examples

```bash
/review-learning-phase engineering-academy/02-quality-engineering/automation/playwright/phase-1
/review-learning-phase engineering-academy/00-engineering-foundations/dev-excellence --level Foundation --depth comprehensive
/review-learning-phase engineering-academy/01-software-engineering/web-development/frontend/react/phase-1 --focus content
```

## Review Checklist

### 1. Academy Alignment
- [ ] Path is in the correct discipline folder
- [ ] Content aligns with the competency level
- [ ] Prerequisites link to existing learning paths
- [ ] Maps to existing standards in `general/`, `php/`, `cf/`, `nodejs/`

### 2. Content Quality
- [ ] Learning objectives are measurable and specific
- [ ] Content is accurate and up-to-date
- [ ] Examples are correct and runnable
- [ ] Explanations are clear and beginner-friendly
- [ ] Prerequisites are accurately stated

### 3. Pedagogy
- [ ] Content progresses logically from simple to complex
- [ ] Concepts build on each other appropriately
- [ ] Common misconceptions are addressed

### 4. Exercises
- [ ] Every concept has a corresponding exercise
- [ ] Exercise difficulty matches competency level
- [ ] Hints provide appropriate scaffolding

### 5. Assessments
- [ ] Assessments align with learning objectives
- [ ] Rubrics are clear and measurable
- [ ] Passing criteria are fair and realistic

### 6. Techversant Standards
- [ ] Code follows the relevant Techversant coding standards
- [ ] Stack-specific conventions are applied correctly
- [ ] REST API patterns follow `general/rest-api-best-practices.md`

## Process Flow

1. **Load Phase**: Read all files in the specified phase directory
2. **Review Academy Alignment**: Check discipline placement and competency level
3. **Review Content**: Check pedagogical quality and accuracy
4. **Review Standards Compliance**: Verify alignment with Techversant coding standards
5. **Quality Scoring**: Assign quality scores to each dimension
6. **Report Generation**: Create review report with findings and recommendations

## Output Format

### Quick Review
```
Phase Review: engineering-academy/02-quality-engineering/automation/playwright/phase-1

Overall Score: 8.2/10
Competency Level: ✅ Foundation (correctly aligned)

Strengths:
✅ Clear learning objectives
✅ Good exercise variety
✅ Aligns with Techversant automation standards

Issues:
⚠️  Lesson 2: Missing code example for concept X
⚠️  Exercise 3: Hint 2 is too revealing
❌ Assessment: Rubric criterion unclear

Recommendations:
1. Add example to Lesson 2
2. Revise Hint 2 in Exercise 3
3. Clarify assessment criterion
```

## Integration

- Uses `.claude/agents/curriculum-reviewer.md` for review logic
- Follows `.claude/rules/course-content-rules.md`
- Follows `.claude/rules/beginner-friendly-writing.md`
- Cross-references `general/`, `php/`, `cf/`, `nodejs/` for stack standards
- Checks against `.claude/templates/` for structure compliance