# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Center of Excellence (CoE) standards repository** for Techversant Engineering. It contains:
- Engineering guidelines and best practices for multiple stacks (PHP, ColdFusion, Node.js)
- AI-assisted development standards and workflows
- The **Engineering Academy** — structured learning paths for skill development
- Career progression guidance and learning level definitions

## .claude Kit Reference

For AI-assisted learning content creation, see:
- `.claude/README.md` - Quick start guide for learning content commands
- `.claude/commands/` - 5 slash commands for creating and managing learning content
- `.claude/agents/` - 6 specialized AI agents for different coaching roles
- `.claude/skills/` - 6 reusable teaching methodologies
- `.claude/rules/` - 4 content quality and writing standards
- `.claude/templates/` - 5 standardized content templates

## Repository Structure

```
coe/
├── engineering-academy/           # Learning paths and career growth
│   ├── 00-engineering-foundations/
│   ├── 01-software-engineering/
│   ├── 02-quality-engineering/
│   ├── 03-platform-engineering/
│   ├── 04-architecture/
│   ├── 05-engineering-leadership/
│   ├── 06-ai-engineering/
│   ├── learning-levels/
│   └── career-progression/
├── general/                       # Universal standards (AI era, REST APIs)
├── git/                           # Git workflow documentation
├── php/                           # PHP/Laravel standards
├── cf/                            # ColdFusion/CFML standards
├── nodejs/                        # Node.js/TypeScript standards
├── ai/                            # AI tools and prompt templates
├── audit/                         # Code audit checklists
├── learning-paths/                # Additional learning content
└── neural/                        # Neural/network patterns
```

## Git Workflow

**Multi-Stage Promotion Model:**
```
feature branch → dev (auto-deploy) → staging (manual) → main (verified) → tag (prod deploy)
```

**Branch naming:** `feature/<JIRA-ID>-<description>`

**Commit format:** [Conventional Commits](https://www.conventionalcommits.org/)
```
feat(module): add user login
fix(module): handle null pointer
docs(module): update API guide
```

**Merge rules:** PR review + CI required. Never force-push to shared branches.

## Engineering Academy (.claude)

The `.claude/` folder contains AI tools for creating and managing learning content:

| Folder | Purpose |
|--------|---------|
| `.claude/commands/` | Slash commands for creating learning content |
| `.claude/agents/` | AI agents for different coaching roles |
| `.claude/skills/` | Teaching methodologies and standards |
| `.claude/rules/` | Content quality and writing standards |
| `.claude/templates/` | Reusable content templates |

### Available Commands

| Command | Purpose |
|---------|---------|
| `/create-learning-phase` | Create a new learning phase with lessons, exercises, assessment |
| `/create-exercise` | Generate hands-on practice activities |
| `/create-assessment` | Build evaluation rubrics |
| `/review-learning-phase` | Quality review of learning content |
| `/update-learning-path-index` | Refresh the learning path catalog |

### Learning Path Structure

Learning paths live in `engineering-academy/` organized by discipline:
- **00-engineering-foundations** — Git, AI usage, communication, secure engineering
- **01-software-engineering** — Web, mobile, backend development
- **02-quality-engineering** — Manual testing, automation, Playwright
- **06-ai-engineering** — AI-assisted development and testing

## AI-Assisted Development Standards

**Human-in-the-Loop (Mandatory):**
- Review every line of AI output before committing
- Never commit code you cannot explain
- Tag AI-assisted commits: `[ai-assisted: claude]`
- Use delegation levels: 🟢 FULL DELEGATE → 🟡 COLLABORATE → 🟠 HUMAN-LED → 🔴 NEVER DELEGATE

**Red Zone (Manual Only — Never Delegate):**
- Authentication & authorization
- Encryption & key management
- PII handling & payment processing
- Production database migrations

## Key Files Reference

| File | Purpose |
|------|---------|
| `engineering-academy/README.md` | Engineering Academy overview |
| `engineering-academy/02-quality-engineering/README.md` | QA/Automation learning paths |
| `general/ai-era-coding-guidelines.md` | AI-assisted development principles |
| `git/Techversant_Git_Workflow.md` | Full branching, commits, rollback, CI/CD |

## Editor Config

Uses `.editorconfig`: UTF-8, 2-space indentation (except PHP uses 4), LF line endings.