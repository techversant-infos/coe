# update-learning-path-index

> Updates the master learning path index with all available phases and progress tracking.

## Overview

This command scans the learning-paths directory, aggregates all available learning phases, and generates a master index file that provides navigation and progress tracking across all learning paths.

## Usage

```bash
/update-learning-path-index [options]
```

## Parameters

### Optional Flags
- `--force` - Force update even if no changes detected (default: false)
- `--include-pending` - Include phases marked as work-in-progress (default: true)
- `--output` - Output file (default: `learning-paths/index.md`)
- `--generate-readme` - Also update learning-paths/README.md (default: false)

## Examples

```bash
/update-learning-path-index
/update-learning-path-index --generate-readme
/update-learning-path-index --force --output learning-paths/catalog.md
```

## Output Format

```markdown
# Learning Paths Index

This index provides navigation across all available learning paths in the AI Learning Platform.

## Available Learning Paths

| Path | Status | Phases | Total Duration | Description |
|------|--------|---------|---------------|-------------|
| [QA Automation](qa-automation) | ✅ Complete | 4 | 16 weeks | End-to-end testing with Playwright |
| [JavaScript Basics](javascript-basics) | 🚧 In Progress | 3 of 5 | 12 weeks | Programming fundamentals |
| [Playwright Engineering](playwright-engineering) | 🚧 Coming Soon | 0 | 0 weeks | Modern test automation |

## Path Details

### [QA Automation](qa-automation)

**Description:** Comprehensive QA Automation training from manual testing to advanced automation with Playwright.

**Status:** Complete
**Duration:** 16 weeks
**Prerequisites:** None

#### Phase 1: Foundations
- **Status:** ✅ Complete
- **Duration:** 3 weeks
- **Topics:** Testing fundamentals, manual testing, bug reporting
- **[Start Phase 1](qa-automation/phase-1/)**

#### Phase 2: Test Automation Basics
- **Status:** ✅ Complete
- **Duration:** 4 weeks
- **Topics:** Automation concepts, JavaScript for testing, Playwright setup
- **[Start Phase 2](qa-automation/phase-2/)**

#### Phase 3: Advanced Automation
- **Status:** ✅ Complete
- **Duration:** 5 weeks
- **Topics:** Patterns, CI/CD, reporting, metrics
- **[Start Phase 3](qa-automation/phase-3/)**

#### Phase 4: Engineering Best Practices
- **Status:** ✅ Complete
- **Duration:** 4 weeks
- **Topics:** Code quality, flaky tests, performance, security
- **[Start Phase 4](qa-automation/phase-4/)**

---

### [JavaScript Basics](javascript-basics)

**Description:** Learn JavaScript programming from the absolute basics to ES6+ features.

**Status:** In Progress
**Duration:** 12 weeks
**Prerequisites:** None

#### Phase 1: Getting Started
- **Status:** ✅ Complete
- **Duration:** 2 weeks
- **Topics:** Environment setup, variables, operators, syntax
- **[Start Phase 1](javascript-basics/phase-1/)**

#### Phase 2: Control Flow
- **Status:** ✅ Complete
- **Duration:** 3 weeks
- **Topics:** Conditionals, loops, functions, scope
- **[Start Phase 2](javascript-basics/phase-2/)**

#### Phase 3: Data Structures
- **Status:** ✅ Complete
- **Duration:** 3 weeks
- **Topics:** Arrays, objects, JSON, data manipulation
- **[Start Phase 3](javascript-basics/phase-3/)**

#### Phase 4: DOM Interaction
- **Status:** 🚧 In Progress
- **Duration:** 2 weeks
- **Topics:** DOM manipulation, event handling, interactive UIs
- **[Start Phase 4](javascript-basics/phase-4/)**

#### Phase 5: Next Steps
- **Status:** ⏳ Upcoming
- **Duration:** 2 weeks
- **Topics:** ES6+, practice projects, next steps
- **Coming soon...**

---

### [Playwright Engineering](playwright-engineering)

**Description:** Advanced Playwright training for experienced automation engineers.

**Status:** Coming Soon
**Duration:** TBD weeks
**Prerequisites:** JavaScript basics, testing fundamentals

**[Track Progress](javascript-basics/)**

## Statistics

- Total Learning Paths: 3
- Complete Phases: 7
- In Progress Phases: 1
- Upcoming Phases: 4
- Total Estimated Duration: 28 weeks

## Navigation

Use the table above to navigate to learning paths, or click on phase names to access specific content.

## Progress Tracking

- Complete status: All files exist and are valid
- In progress: Phase is being created or reviewed
- Upcoming: Not yet created
- Locked: Requires prerequisites to be completed

## Maintenance

This index is automatically maintained by the learning platform. Content updates will be reflected here.

For issues with navigation, please run `/update-learning-path-index`.
```

## Process Flow

1. **Scan Directory**: Recursively scan `learning-paths/` for all phase directories
2. **Collect Metadata**: Parse README.md files for phase information
3. **Validate Structure**: Check each phase has required files
4. **Calculate Progress**: Determine completion status based on phase structure
5. **Generate Index**: Create the master index with navigation
6. **Generate README** (if requested): Update the learning-paths/README.md

## Quality Controls

- [ ] All learning paths are listed
- [ ] Phase metadata is accurate
- [ ] Links are valid and working
- [ ] Status correctly reflects actual progress
- [ ] Duration estimates are consistent

## Integration

- Uses `.claude/agents/repo-maintainer.md` for maintenance logic
- Follows `.claude/rules/markdown-structure.md`
- Uses `.claude/templates/` for consistent formatting