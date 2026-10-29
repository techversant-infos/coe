# CLAUDE.md

Guidance for Claude Code in this repository. The shared rules for every AI agent are in AGENTS.md, imported here:

@AGENTS.md

## Claude-Specific Notes

- Tag commits you help write with `[ai-assisted: claude]`.
- `.claude/settings.json` allows read-only tools and the link check without a prompt. Keep it narrow, and put
  personal settings in `.claude/settings.local.json`, which is git-ignored.

## The .claude Kit (Academy Content)

The kit creates and reviews Engineering Academy content. See [.claude/README.md](./.claude/README.md) for the
quick start.

| Folder | Contents |
|--------|----------|
| `.claude/commands/` | 5 slash commands, listed below |
| `.claude/agents/` | 6 agents: learning path architect, curriculum reviewer, QA automation coach, JavaScript basics coach, Playwright engineer, repo maintainer |
| `.claude/skills/` | 6 teaching methods, such as assessment rubric design and hands-on assignment design |
| `.claude/rules/` | 4 content rules: course content, beginner-friendly writing, markdown structure, automation standards |
| `.claude/templates/` | 5 templates: phase, lesson, exercise, assessment, weekly plan |

| Command | Purpose |
|---------|---------|
| `/create-learning-phase` | Create a phase with lessons, exercises and an assessment |
| `/create-exercise` | Create a hands-on exercise |
| `/create-assessment` | Create an assessment rubric |
| `/review-learning-phase` | Review a phase against the content rules |
| `/update-learning-path-index` | Rebuild the learning path index in `engineering-academy/README.md` |
