# create-assessment

> Creates an assessment for a learning phase with rubrics and evaluation criteria.

## Overview

This command generates a comprehensive assessment for a learning phase, including practical tasks, evaluation rubrics, and passing criteria. It measures learner mastery of phase objectives.

## Usage

```bash
/create-assessment [phase-topic] [options]
```

## Parameters

### Required
- **phase-topic** - The phase topic to assess (e.g., "qa-automation-basics", "javascript-fundamentals", "playwright-setup")

### Optional Flags
- `--type` - Assessment type: formative/summative/capstone (default: summative)
- `--duration` - Estimated duration in minutes (default: 60)
- `--output` - Output directory (default: `learning-paths/<topic>/phase-1/assessment.md`)

## Examples

```bash
/create-assessment qa-automation-basics --type formative --duration 30
/create-assessment javascript-fundamentals --type summative
/create-assessment playwright-setup --type capstone --duration 90
```

## Assessment Types

### Formative
- Quick checks for understanding
- Used during learning (after each lesson)
- Low stakes, multiple attempts allowed
- Typically 5-10 minutes
- Can be: quizzes, quick practicals, concept checks

### Summative
- Evaluates mastery at phase completion
- Higher stakes, single attempt recommended
- Typically 30-60 minutes
- Can be: practical projects, comprehensive quizzes

### Capstone
- Validates complete competency
- Major project applying all phase concepts
- Typically 60-120 minutes
- Should be: real-world project, portfolio piece

## Output Format

```markdown
# Assessment: [Title]

**Type:** Formative/Summative/Capstone
**Duration:** XX minutes
**Estimated Effort:** XX points

## Learning Objectives Assessed

By completing this assessment, you will demonstrate ability to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Instructions

[Clear instructions for what the learner needs to do]

## Assessment Tasks

### Task 1: [Title]

**Objective:** [What this task evaluates]
**Requirements:**
- Requirement 1
- Requirement 2

**Success Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Task 2: [Title]

[Similar structure for additional tasks]

## Grading Rubric

| Criteria | Weight | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|----------|--------|---------------|----------------|----------------|---------------|
| **Criterion 1** | 25% | Description | Description | Description | Description |
| **Criterion 2** | 30% | Description | Description | Description | Description |
| **Criterion 3** | 25% | Description | Description | Description | Description |
| **Criterion 4** | 20% | Description | Description | Description | Description |

## Passing Criteria

- Minimum passing score: X out of 4 (Y%)
- Must achieve "Proficient" or better on core criteria
- Maximum attempts: [Number]

## Feedback Process

1. Self-assessment using rubric
2. Automated checks (if applicable)
3. Instructor review (if applicable)
4. Detailed feedback with improvement areas
5. Resources for remediation

## Next Steps

- If passed: Proceed to [next phase]
- If failed: Review [concepts] and retake
- Resources: [links to relevant materials]
```

## Process Flow

1. **Load Phase**: Read phase objectives and content
2. **Design Tasks**: Create practical tasks that assess objectives
3. **Build Rubric**: Define clear, measurable criteria with weights
4. **Set Passing Criteria**: Define minimum competency levels
5. **Create Feedback Plan**: Plan how learners receive feedback

## Quality Controls

- [ ] All learning objectives are assessed
- [ ] Tasks are practical, not theoretical
- [ ] Rubric criteria are measurable
- [ ] Passing criteria are fair and realistic
- [ ] Instructions are clear and complete
- [ ] Feedback is actionable

## Integration

- Uses `.claude/agents/learning-path-architect.md` for assessment design
- Uses topic-specific coach agents for practical tasks
- References `.claude/skills/assessment-rubric-design/SKILL.md`
- Follows `.claude/rules/course-content-rules.md`
- Uses `.claude/templates/assessment-template.md`