# AI Guides and Prompts

> How Techversant engineers use AI tools day to day: guides, prompt templates, reusable skills and training material.

The rules themselves (human review, delegation levels, Red Zone) live in the
[AI Era Coding Guidelines](../standards/general/ai-era-coding-guidelines.md). The documents here show how to apply them.

## Guides

| Document | Use it for |
|----------|------------|
| [AI Usage Standards](./guides/ai-team-best-practices.md) | Team practices for AI-assisted work, tool choice and governance |
| [Claude Cheat Sheet](./guides/claude-dev-cheatsheet.md) | Prompts, session controls and do's and don'ts for daily Claude use |
| [Claude Code Token Efficiency Guide](./guides/claude-code-token-usage-guide.md) | Keeping sessions small and choosing a model for each task |

## Prompts

The [Developer Prompt Handbook](./prompts/developer-handbook-full.md) gives the prompt formula and summarises each stage.
Each stage also has its own file with the full prompt and tips:

| Stage | Prompt |
|-------|--------|
| 4 | [3-point estimation](./prompts/section-04-estimation.md) |
| 5 | [Planning](./prompts/section-05-planning.md) |
| 6 | [Database schema and indexes](./prompts/section-06-database.md) |
| 7 | [Starting development](./prompts/section-07-development.md) |
| 8 | [Code review](./prompts/section-08-code-review.md) |
| 9 | [Pull requests and PR messages](./prompts/section-09-pull-request.md) |

## Skills Library

Reference copies of agent skills, adapted from the open-source
[agency-agents](https://github.com/msitarzewski/agency-agents) collection. They are not loaded automatically. The
skills Claude Code uses in this repository live in `.claude/skills/`.

| Skill | Role |
|-------|------|
| [api-tester](./skills-library/api-tester/SKILL.md) | API test design and execution |
| [compliance-auditor](./skills-library/compliance-auditor/SKILL.md) | Compliance and audit review |
| [devops-automator](./skills-library/devops-automator/SKILL.md) | CI/CD and infrastructure automation |
| [security-engineer](./skills-library/security-engineer/SKILL.md) | Application security review |
| [technical-writer](./skills-library/technical-writer/SKILL.md) | Documentation templates and style |

## Presentations

| Document | Use it for |
|----------|------------|
| [AI Productivity (slides, PDF)](./presentations/ai-productivity.pdf) | Team session on productive, safe AI use |
| [Presentation Blueprint](./presentations/presentation-blueprint.md) | Speaker notes and slide plan for the deck above |
