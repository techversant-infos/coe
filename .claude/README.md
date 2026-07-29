# Engineering Academy .claude Kit

AI-assisted toolkit for creating and managing Techversant Engineering Academy learning content. All commands are slash commands available in Claude Code.

## Quick Start

### Core Commands (5)

| Command | Purpose |
|---------|---------|
| `/create-learning-phase` | Create a new learning phase with lessons, exercises, assessment |
| `/create-exercise` | Generate hands-on practice activities |
| `/create-assessment` | Build rubric-based evaluations aligned to competency levels |
| `/review-learning-phase` | Quality review against Techversant standards |
| `/update-learning-path-index` | Refresh the master academy catalog |

---

## Command Reference

### 1. `/create-learning-phase`

Scaffolds a complete learning phase within `engineering-academy/<NN-discipline>/<topic>/`.

```bash
/create-learning-phase [discipline] [topic] [--options]
```

**Examples:**
```bash
/create-learning-phase 02-quality-engineering playwright-basics --subfolder 02-automation/playwright --level Foundation
/create-learning-phase 00-engineering-foundations git-workflow
/create-learning-phase 01-software-engineering react-fundamentals --subfolder web-development/frontend --level Practitioner
```

**What it creates:**
```
engineering-academy/<NN-discipline>/<topic>/phase-1/
├── README.md
├── lessons/
│   ├── lesson-1.md
│   ├── lesson-2.md
│   └── lesson-3.md
├── exercises/
│   ├── exercise-1.md
│   ├── exercise-2.md
│   └── exercise-3.md
└── assessment.md
```

---

### 2. `/create-exercise`

Generates hands-on exercises for specific concepts within an academy discipline.

```bash
/create-exercise [discipline] [concept] [--options]
```

**Examples:**
```bash
/create-exercise 00-engineering-foundations git-merge --level Practitioner
/create-exercise 02-quality-engineering playwright-locators --subfolder 02-automation/playwright
/create-exercise 01-software-engineering react-state --subfolder web-development/frontend --phase 2
```

---

### 3. `/create-assessment`

Builds rubric-based evaluations aligned to Techversant competency levels.

```bash
/create-assessment [discipline] [topic] [--options]
```

**Examples:**
```bash
/create-assessment 02-quality-engineering playwright-basics --subfolder automation/playwright --type summative
/create-assessment 00-engineering-foundations git-workflow --level Foundation
/create-assessment 01-software-engineering react-fundamentals --type formative --duration 30
```

**Competency Levels:**

| Level | Description | Passing Score |
|-------|-------------|---------------|
| Foundation | New to topic, building basics | 70% |
| Practitioner | Can apply with guidance | 75% |
| Advanced | Works independently, mentors others | 80% |
| Expert | Sets direction, designs solutions | 85% |

---

### 4. `/review-learning-phase`

Runs a quality review of a learning phase against Techversant standards.

```bash
/review-learning-phase [phase-path] [--options]
```

**Examples:**
```bash
/review-learning-phase engineering-academy/02-quality-engineering/automation/playwright/phase-1
/review-learning-phase engineering-academy/00-engineering-foundations/git-workflow --level Foundation --generate-report
```

---

### 5. `/update-learning-path-index`

Refreshes the master catalog for the Engineering Academy.

```bash
/update-learning-path-index --generate-discipline-readmes
```

---

## Academy Discipline Mapping

| Code | Discipline | Subfolders |
|------|------------|------------|
| `00-engineering-foundations` | Git, AI usage, secure dev, communication, dev excellence | `dev-excellence` |
| `01-software-engineering` | Web, mobile, backend, full-stack | `web-development/frontend`, `web-development/backend`, `mobile-development` |
| `02-quality-engineering` | Manual testing, automation, Playwright, strategy | `automation/playwright`, `strategy`, `manual-testing` |
| `03-platform-engineering` | DevOps, cloud, Kubernetes | (content pending) |
| `04-architecture` | Solution architecture, system design | (content pending) |
| `05-engineering-leadership` | Team lead, engineering manager | (content pending) |
| `06-ai-engineering` | AI-assisted development, testing, prompt engineering | `ai-assisted-development`, `ai-assisted-testing`, `prompt-engineering` |

---

## Agents (6)

Agents are invoked automatically by commands, but can also be referenced directly.

| Agent | Role | Used By |
|-------|------|---------|
| `learning-path-architect` | Designs curricula aligned to competency framework | `/create-learning-phase` |
| `qa-automation-coach` | Creates QA and automation content | discipline `02-quality-engineering` |
| `playwright-engineer` | Creates Playwright-specific content | `--subfolder automation/playwright` |
| `javascript-basics-coach` | Creates JS foundational content | discipline `01-software-engineering`, `00-engineering-foundations` |
| `curriculum-reviewer` | Quality assurance against Techversant standards | `/review-learning-phase` |
| `repo-maintainer` | Repository structure and index management | `/update-learning-path-index` |

---

## Skills (6)

Reusable teaching methodologies agents reference:

| Skill | Purpose |
|-------|---------|
| `qa-curriculum-design` | QA learning path structure (phases, exercises, assessments) |
| `beginner-javascript-training` | JS fundamentals curriculum design |
| `playwright-training` | Playwright test automation curriculum |
| `hands-on-assignment-design` | Exercise design principles and templates |
| `assessment-rubric-design` | Rubric creation and evaluation criteria |
| `markdown-course-authoring` | Markdown formatting and structure for learning content |

---

## Rules (4)

Hard standards all content must follow:

| Rule | Purpose |
|------|---------|
| `course-content-rules.md` | Content structure, pedagogy, tech accuracy, language |
| `beginner-friendly-writing.md` | Writing style for all competency levels |
| `automation-engineering-standards.md` | Code standards, test patterns, security for QA content |
| `markdown-structure.md` | File organization, formatting, naming conventions |

---

## Templates (5)

Standardized structures for consistent content:

| Template | Used For |
|----------|----------|
| `phase-template.md` | Learning phase README |
| `lesson-template.md` | Individual lessons |
| `exercise-template.md` | Hands-on exercises |
| `assessment-template.md` | Evaluations with rubrics |
| `weekly-plan-template.md` | Study schedules |

---

## Workflow Example: Creating a Playwright Path

```bash
# 1. Create Phase 1
/create-learning-phase 02-quality-engineering playwright-basics --subfolder 02-automation/playwright --level Foundation

# 2. Add an exercise
/create-exercise 02-quality-engineering playwright-locators --subfolder 02-automation/playwright

# 3. Create assessment
/create-assessment 02-quality-engineering playwright-basics --subfolder automation/playwright

# 4. Review it
/review-learning-phase engineering-academy/02-quality-engineering/automation/playwright/phase-1

# 5. Update the academy index
/update-learning-path-index --generate-discipline-readmes
```

---

## Content Structure Rules

Every learning phase must have:
- `READMEME.md` with learning objectives and overview
- 3–4 lessons with clear, measurable objectives
- 3–4 hands-on exercises with progressive hints and solutions
- 1 assessment with a detailed rubric
- Prerequisites and next-step references

---

## Tips

- Use `--level` correctly: Foundation starts simple, Expert expects complex scenarios
- Use `--subfolder` to target specific academy sub-areas
- Reference existing paths via `--prerequisites` to build connected learning journeys
- Always run `/update-learning-path-index` after adding content
- Content paths are `engineering-academy/<NN-discipline>/<NN-subfolder>/<topic>/`
