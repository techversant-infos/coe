# create-learning-phase

> Creates a new learning phase within the Techversant Engineering Academy with structured lessons, exercises, and assessment.

## Overview

This command scaffolds a complete learning phase within the Engineering Academy structure (`engineering-academy/`). It generates the directory structure, creates lesson files, designs exercises, and builds an assessment rubric aligned with Techversant competency levels.

## Usage

```bash
/create-learning-phase [discipline] [topic] [options]
```

## Parameters

### Required
- **discipline** - Academy discipline folder (e.g., `00-engineering-foundations`, `01-software-engineering`, `02-quality-engineering`)
- **topic** - The learning topic (e.g., `git-workflow`, `playwright-basics`, `dev-excellence`)

### Optional Flags
- `--subfolder` - Sub-discipline path (e.g., `automation/playwright`, `web-development/frontend`)
- `--duration` - Estimated duration in weeks (default: 4)
- `--level` - Competency level: Foundation/Practitioner/Advanced/Expert (default: Foundation)
- `--prerequisites` - Comma-separated list of prerequisite topics
- `--phase` - Phase number (default: 1)

## Examples

```bash
/create-learning-phase 02-quality-engineering playwright-basics --subfolder automation/playwright --level Foundation
/create-learning-phase 00-engineering-foundations git-workflow --level Foundation
/create-learning-phase 01-software-engineering react-fundamentals --subfolder web-development/frontend --level Practitioner
/create-learning-phase 00-engineering-foundations dev-excellence --prerequisites "git-workflow"
```

## What It Creates

### Directory Structure
```
engineering-academy/<NN-discipline>/<topic>/
├── README.md                    # Learning path overview
├── phase-1/
│   ├── README.md                # Phase overview
│   ├── lessons/
│   │   ├── lesson-1.md          # First concept
│   │   ├── lesson-2.md          # Second concept
│   │   └── lesson-3.md          # Third concept
│   ├── exercises/
│   │   ├── exercise-1.md        # Practice exercise 1
│   │   ├── exercise-2.md        # Practice exercise 2
│   │   └── exercise-3.md        # Practice exercise 3
│   └── assessment.md            # Phase assessment
```

### Content Generated
- **Learning path README**: Overview, prerequisites, phase map
- **Phase README**: Learning objectives, overview, estimated time, competency level
- **3 Lessons**: Core concepts with examples, mapped to Techversant standards
- **3 Exercises**: Hands-on practice with hints and solutions
- **1 Assessment**: Rubric-based evaluation aligned to competency level
- **Index update**: Refreshes the discipline README with new content

## Process Flow

1. **Analyze Topic**: Calls learning-path-architect to determine appropriate structure and competency level
2. **Create Lessons**: Calls relevant coach agent based on discipline (qa-automation-coach, playwright-engineer, etc.)
3. **Design Exercises**: Uses hands-on-assignment-design skill
4. **Build Assessment**: Uses assessment-rubric-design skill mapped to competency level
5. **Review**: Optionally runs curriculum-reviewer for quality check
6. **Index Update**: Updates the discipline README with new learning path

## Academy Discipline Mapping

| Discipline Code | Area | Agent |
|-----------------|------|-------|
| `00-engineering-foundations` | Git, AI usage, communication, dev excellence | javascript-basics-coach |
| `01-software-engineering` | Web, mobile, backend, full-stack | javascript-basics-coach |
| `02-quality-engineering` | Manual testing, automation, Playwright | qa-automation-coach, playwright-engineer |
| `03-platform-engineering` | DevOps, cloud, Kubernetes | (pending agent) |
| `04-architecture` | Solution architecture, system design | (pending agent) |
| `05-engineering-leadership` | Team lead, engineering manager | (pending agent) |
| `06-ai-engineering` | AI-assisted development, prompt engineering | (pending agent) |

## Competency Levels

| Level | Description | Duration |
|-------|-------------|---------|
| Foundation | New to the topic, building fundamentals | 4-6 weeks |
| Practitioner | Can apply with guidance | 6-8 weeks |
| Advanced | Works independently, mentors others | 8-10 weeks |
| Expert | Sets direction, designs solutions | 10-12 weeks |

## Integration

- Uses `.claude/agents/learning-path-architect.md` for curriculum design
- Uses discipline-specific agents (qa-automation-coach, playwright-engineer, etc.)
- References skills in `.claude/skills/`
- Follows all rules in `.claude/rules/`
- Uses templates in `.claude/templates/`
- Output maps to `engineering-academy/<NN-discipline>/<topic>/`
