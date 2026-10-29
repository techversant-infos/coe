# Engineering Foundations

**Status:** Active · **Owner:** TBD · **Last updated:** 2026-10-29 · **Next review:** 2027-01-02

This section contains the shared baseline every engineer needs before specializing into software engineering, quality engineering, platform work, architecture, or AI engineering.

The goal is not to duplicate stack-specific guidance. The goal is to make sure every engineer shares the same operating habits: Git workflow, AI usage, secure engineering, communication, documentation, code review, and clean-code discipline.

## Pilot Draft

A redesigned Foundations course is in pilot. The current course below stays in use until the pilot ends.

**Outcome:** a learner can safely deliver a small change to an existing application, using approved AI tools, with
appropriate supervision. This is a foundations qualification, not a claim of independent full-stack expertise.

**How it teaches:** through one training application, a small service-request tracker written in TypeScript. Learners
work through the same sequence as real work: understand the application, clarify a request, change it, diagnose a
failure, review, ship. The 14 modules are the reference material for that sequence. About two-thirds of the time is
practice.

**Routes:**

- **Freshers:** modules 01–14 in order, with feedback checkpoints after modules 06 and 10, then the
  [assessment](./assessment.md).
- **Experienced staff:** take the assessment first, study the modules mapped to any row below the minimum, then repeat
  those rows on a new task variant.

### Pilot files

| File | Pilot status |
|------|--------------|
| [06. Working with Existing Systems](./06-working-with-existing-systems.md) | Full draft |
| [09. Testing, Debugging and Verification](./09-testing-debugging-and-verification.md) | Full draft |
| [Assessment](./assessment.md) | Draft rubric, passing rules and safety criteria |
| [Facilitator Guide](./facilitator-guide.md) | Pilot plan, scoring and exit criteria |

### Module outlines

The other modules are outlines until the pilot shows what learners need. AI-assisted delivery runs through all of
them rather than sitting in one module.

| # | Module | Covers |
|---|--------|--------|
| 01 | How We Build Software | The delivery lifecycle as one connected loop: intent, acceptance criteria, agent context, implementation, verification, deployment, operational feedback. Agents speed up steps; they do not replace engineering judgement. |
| 02 | Problem Framing and Specs | Clarifying an unclear request; acceptance criteria that become the agent's context. Documentation in proportion: one issue and one pull request for a small change, separate spec or plan files only when they help. Forward Deployed Engineering basics: scoping a problem with the people who have it. |
| 03 | Git and Pull Requests | The pull request as the record that links request, commits, test evidence, review and deployment |
| 04 | AI-Assisted Development | Choosing delegation boundaries for each task; the Red Zone; why agent output needs tests and an independent review |
| 05 | Context Engineering | Instruction files such as `AGENTS.md` and `CLAUDE.md` guide an agent but enforce nothing. Tool permissions, sandboxing, branch protection and CI enforce. Least privilege for agents. |
| 06 | Working with Existing Systems | Full draft |
| 07 | Clean Code | Code that people can review quickly, whoever or whatever wrote it |
| 08 | Design Principles | When a principle helps, what it costs, and when to escalate a design question |
| 09 | Testing, Debugging and Verification | Full draft |
| 10 | APIs and Data Boundaries | Contracts, validation, and changes that keep callers and data working |
| 11 | Secure Engineering | OWASP basics, plus AI-specific risks: prompt injection, secrets in prompts, agent tool access |
| 12 | Code Review | Independent review of human and agent changes; finding the material issues first |
| 13 | Shipping and Operating | Deployment, health checks and rollback. Production signals start investigations; automated fixes need explicitly bounded authority. |
| 14 | Communication and Stakeholders | Status updates, decision records when they are worth writing, customer conversations, explaining what you accepted or rejected from AI output |

## Current Course

| Foundation | Use this when |
|---|---|
| [Git Workflow](./01-git-workflow.md) | You need the branching, commit, PR, and release model |
| [AI Usage](./02-ai-usage.md) | You use Codex, Claude Code, Cursor, Copilot, or another AI coding assistant |
| [Secure Engineering](./03-secure-engineering.md) | You touch auth, access control, secrets, PII, payments, APIs, or production data |
| [Communication](./04-communication.md) | You write PRs, RFCs, status updates, bug reports, or handoff notes |
| [Developer Excellence Curriculum](./05-dev-excellence/01-curriculum.md) | You want the core engineering discipline path: clean code, SOLID, testing, review, ownership |

## Recommended Order

1. [Git Workflow](./01-git-workflow.md)
2. [AI Usage](./02-ai-usage.md)
3. [Secure Engineering](./03-secure-engineering.md)
4. [Communication](./04-communication.md)
5. [Developer Excellence Curriculum](./05-dev-excellence/01-curriculum.md)

## Guidance Layers

- [Learning Levels](../learning-levels/) - understand Foundation / Practitioner / Advanced / Expert
- [Career Progression](../career-progression/01-transition-overview.md) - see your upgrade path

## Completion Evidence

- You can open a PR that follows the Techversant workflow.
- You can explain when AI use is safe, when it requires collaboration, and when it is forbidden.
- You can identify common security review risks before a reviewer catches them.
- You can read and apply the Developer Excellence review checklist.
- You can write a clear PR description, bug report, and technical handoff.
