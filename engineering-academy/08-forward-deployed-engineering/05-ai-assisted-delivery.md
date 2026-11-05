# 05. AI-Assisted Delivery

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Coding agents help FDEs deliver faster on unfamiliar systems. Using them safely means knowing where they must stop.
Back to the [roadmap](./README.md).

## Coding agents

Coding agents such as Claude Code, Cursor and Copilot read code, make changes and run commands for you.

**What to learn:**

- Which tool fits which task, and [the tools Techversant approves](../../ai/guides/ai-team-best-practices.md#2-tool-selection-standards)
- Giving an agent a clear task, context and a way to check its work
- Managing sessions, context and cost

**Resources:**

- [AI Usage](../00-engineering-foundations/02-ai-usage.md)
- [Claude Developer Cheat Sheet](../../ai/guides/claude-dev-cheatsheet.md)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)

**Level:** Foundation · Core

## Delegation levels and the Red Zone

For every task, decide how much to hand to an agent. Some work is never delegated: authentication and authorisation,
encryption and keys, personal and payment data, production database migrations.

**What to learn:**

- The four delegation levels and how to choose one
- Recognising Red Zone work in a client codebase
- Stopping and escalating when a task turns into Red Zone work

**Resources:**

- [AI Era Coding Guidelines: delegation levels](../../standards/general/ai-era-coding-guidelines.md#21-delegation-levels)
- [AI Era Coding Guidelines: Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)

**Level:** Foundation · Core

## Agent rules, permissions and CI

Instruction files such as `CLAUDE.md` and `AGENTS.md` guide an agent, but they enforce nothing. Tool permissions,
branch protection and CI checks are what actually stop a mistake.

**What to learn:**

- Writing a short, useful instruction file for a client repository
- Limiting what an agent may read, edit and run
- Branch protection and CI as the real safety net

**Resources:**

- [AI Team Best Practices: project memory](../../ai/guides/ai-team-best-practices.md#4-project-memory--setup-standard)
- [AI Team Best Practices: non-negotiables](../../ai/guides/ai-team-best-practices.md#non-negotiables--no-exceptions),
  including "no AI agent pushes directly to main"

**Level:** Practitioner · Core

## Reviewing agent output

An agent checking its own work is not a review. Agent changes need tests and an independent human review.

**What to learn:**

- Reading every line of a generated change before committing it
- Checking that tests really test the change
- Explaining what you accepted from the agent, and what you rejected and why

**Resources:** [AI Team Best Practices: code review](../../ai/guides/ai-team-best-practices.md#6-code-review-standards)

**Level:** Practitioner · Core

## Building prototypes with AI agents

A working prototype in hours lets the client react to something real instead of a document.

**What to learn:**

- Building a throwaway prototype fast, with synthetic or approved data only
- Deciding what the prototype must prove
- Prototypes never ship to production without the normal review and tests

**Resources:** learn on engagements, with a lead. Pair with [Discovery](./09-client-delivery.md#discovery).

**Level:** Practitioner · Optional

## Project: Deliver a Feature with a Coding Agent, Safely

**Brief:** Use an approved coding agent to add two features to the service request tracker from stage 02: closing
several requests at once, and an "overdue" filter. Neither needs any sign-in code. If a feature needs a database
migration, write it yourself: the agent may not touch the migrations folder. Set up the guardrails first.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The repository has a short instruction file (`AGENTS.md` or `CLAUDE.md`) with commands, conventions and the
  folders the agent must not touch
- [ ] The agent's permissions deny edits to the database migrations folder and to `.github/workflows/`, and your notes
  show a denied attempt
- [ ] The repository is in the Techversant GitHub organisation, and branch protection requires CI to pass and one
  human approval before merging to `main`
- [ ] The pull request states the delegation level you chose for each task
- [ ] The pull request lists what the agent wrote, what you changed, and at least one suggestion you rejected and why
- [ ] A reviewer other than you reads every line and approves

Previous: [04. Applied AI](./04-applied-ai.md) · Next: [06. Integration Engineering](./06-integration-engineering.md)
