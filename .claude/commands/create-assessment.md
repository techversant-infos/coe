# create-assessment

> Creates an assessment for an Engineering Academy learning phase with rubrics and evaluation criteria aligned to competency levels.

## Overview

This command generates a comprehensive assessment for a learning phase within `engineering-academy/`. Assessments are competency-level aligned (Foundation, Practitioner, Advanced, Expert) and follow Techversant quality standards.

## Usage

```bash
/create-assessment [discipline] [topic] [options]
```

## Parameters

### Required
- **discipline** - Academy discipline folder (e.g., `00-engineering-foundations`, `02-quality-engineering`)
- **topic** - The learning topic (e.g., `git-workflow`, `playwright-basics`)

### Optional Flags
- `--subfolder` - Sub-discipline path (e.g., `automation/playwright`, `web-development/frontend`)
- `--phase` - Phase number (default: 1)
- `--type` - Assessment type: formative/summative/capstone (default: summative)
- `--level` - Competency level: Foundation/Practitioner/Advanced/Expert (default: Foundation)
- `--duration` - Estimated duration in minutes (default: 60)

## Examples

```bash
/create-assessment 02-quality-engineering playwright-basics --subfolder automation/playwright --phase 1
/create-assessment 00-engineering-foundations git-workflow --level Foundation
/create-assessment 01-software-engineering react-fundamentals --subfolder web-development/frontend --type formative
```

## Competency Level Guidelines

### Foundation
- Tests recall and basic application
- Clear right/wrong answers
- Passing score: 70%
- May reference lesson materials

### Practitioner
- Tests ability to apply skills independently
- Scenario-based problems
- Passing score: 75%
- Limited resources allowed

### Advanced
- Tests problem-solving and judgment
- Open-ended challenges
- Passing score: 80%
- Restricted resources

### Expert
- Tests strategy, design, and leadership
- Portfolio or project-based
- Passing score: 85%
- No resource restrictions (authentic work)

## Integration

- Uses `.claude/agents/learning-path-architect.md` for assessment design
- Uses discipline-specific coach agents
- References `.claude/skills/assessment-rubric-design/SKILL.md`
- Follows `.claude/rules/course-content-rules.md`
- Uses `.claude/templates/assessment-template.md`
- Output maps to `engineering-academy/<NN-discipline>/<topic>/phase-<N>/assessment.md`
