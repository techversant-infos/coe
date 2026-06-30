# create-learning-phase

> Creates a new learning phase with structured lessons, exercises, and assessment.

## Overview

This command scaffolds a complete learning phase based on the specified topic and curriculum design principles. It generates the directory structure, creates lesson files, designs exercises, and builds an assessment rubric.

## Usage

```bash
/create-learning-phase [topic] [options]
```

## Parameters

### Required
- **topic** - The learning topic (e.g., "qa-automation-basics", "javascript-variables", "playwright-setup")

### Optional Flags
- `--type` - Topic type (qa-automation, javascript-basics, playwright-engineering, custom)
- `--duration` - Estimated duration in days (default: 5)
- `--prerequisites` - Comma-separated list of prerequisites
- `--level` - Beginner/Intermediate/Advanced (default: Beginner)
- `--output` - Output directory (default: `learning-paths/<topic>/phase-1`)

## Examples

```bash
/create-learning-phase qa-automation-basics --type qa-automation --duration 10
/create-learning-phase javascript-variables --type javascript-basics --duration 5 --prerequisites "no-experience-required"
/create-learning-phase playwright-data-driven --type playwright-engineering --level intermediate
```

## What It Creates

### Directory Structure
```
learning-paths/<topic>/phase-1/
├── README.md                    # Phase overview
├── index.md                     # Lesson index
├── lessons/
│   ├── lesson-1.md              # First concept
│   ├── lesson-2.md              # Second concept
│   └── lesson-3.md              # Third concept
├── exercises/
│   ├── exercise-1.md            # Practice exercise 1
│   ├── exercise-2.md            # Practice exercise 2
│   └── exercise-3.md            # Practice exercise 3
└── assessment.md               # Phase assessment
```

### Content Generated
- **Phase README**: Learning objectives, overview, estimated time
- **3 Lessons**: Core concepts with examples
- **3 Exercises**: Hands-on practice with hints and solutions
- **1 Assessment**: Rubric-based evaluation
- **Index**: Navigation between lessons and exercises

## Process Flow

1. **Analyze Topic**: Calls learning-path-architect to determine appropriate structure
2. **Create Lessons**: Calls relevant coach agent based on topic type
3. **Design Exercises**: Uses hands-on-assignment-design skill
4. **Build Assessment**: Uses assessment-rubric-design skill
5. **Review**: Optionally runs curriculum-reviewer for quality check
6. **Index Update**: Updates learning path master index

## Output Example

After running the command, you'll see:

```
✅ Created learning-paths/qa-automation-basics/phase-1/
├── README.md (532 lines)
├── index.md (120 lines)
├── lessons/
│   ├── lesson-1.md (241 lines)
│   ├── lesson-2.md (285 lines)
│   └── lesson-3.md (298 lines)
├── exercises/
│   ├── exercise-1.md (156 lines)
│   ├── exercise-2.md (198 lines)
│   └── exercise-3.md (178 lines)
└── assessment.md (315 lines)

Total: 2,023 lines of content created.
```

## Integration

- Uses `.claude/agents/learning-path-architect.md` for curriculum design
- Uses topic-specific agents (qa-automation-coach, javascript-basics-coach, etc.)
- References skills in `.claude/skills/`
- Follows all rules in `.claude/rules/`
- Uses templates in `.claude/templates/`