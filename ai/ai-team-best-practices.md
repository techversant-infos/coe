# AI Usage Standards — Techversant Engineering
**Version:** 1.0
**Owner:** Engineering CoE
**Applies to:** All engineering roles using AI-assisted development
**Review cycle:** Quarterly

> These are standards, not suggestions. They apply to all projects, all roles, all AI tools.

---

## 1. Core Principles

| Principle | Standard |
|-----------|----------|
| Speed vs. correctness | AI increases speed. It does not increase correctness. Validation is mandatory. |
| Ownership | The developer who commits AI-generated code owns it. Fully. |
| Transparency | All AI-assisted PRs must be tagged. No silent AI usage on shared codebases. |
| Judgment | If you cannot explain what the AI produced — do not commit it. Escalate. |
| Confidentiality | No client data, credentials, or business logic enters any public AI tool. |

---

## 2. Tool Selection Standards

Use the right tool for the task. Do not duplicate tools for the same job.

| Task | Primary Tool | Fallback |
|------|-------------|---------|
| Architecture planning, complex reasoning | Claude | — |
| Multi-file editing, refactoring | Cursor | — |
| Inline autocomplete | Copilot | Cursor Tab |
| PR descriptions, commit messages | Copilot | Claude |
| Test generation (full suite) | Claude | Cursor Chat |
| Explain unfamiliar code | Claude or Cursor Chat | — |
| Quick boilerplate / one-liners | Copilot | Cursor Tab |
| General Q&A, non-code exploration | ChatGPT | Claude |
| Design-to-code, UI prototyping | v0.dev | — |

**Rule:** Claude Opus is reserved for architecture decisions and complex reasoning only. Sonnet for daily dev work. Haiku for repetitive tasks (test generation, doc summaries, fast completions).

---

## 3. Prompt Standards

Every prompt must include: **Context + Task + Constraints + Format**

### Required elements

| Element | What to include |
|---------|----------------|
| Context | Stack, file name, function name, what you've already tried |
| Task | Specific action — not a description of the problem |
| Constraints | What NOT to change, libraries to avoid, line limits |
| Format | Code block / bullet list / table / max N options |

### Prohibited patterns

- Vague task descriptions ("fix this", "make it better", "clean this up")
- Pasting entire files when only a function is relevant
- Chained mega-prompts — one task per prompt
- Re-explaining context that CLAUDE.md already contains
- Prompts without specifying output format for non-trivial requests

### Prompt example (reference)

```
Stack: Node.js 20, Express, PostgreSQL 14 (Knex query builder).
File: /src/api/users/getUser.js
Issue: /api/users/:id throws 500 when user ID does not exist.
Expected: return 404 { error: 'user_not_found', code: 404 }
Task: Fix the error handling in getUser only.
Constraints: Do not modify the JWT middleware. Do not change the function signature.
Format: Return corrected code block only. No explanation.
```

---

## 4. Project Memory — Setup Standard

Every active project must have the following before AI tools are used:

### Required files

| File | Location | Purpose |
|------|----------|---------|
| CLAUDE.md | Project root | Claude project context — stack, standards, off-limits |
| .cursorrules | Project root | Cursor coding style and conventions |
| code-reviewer.md | .claude/agents/ | /review subagent — PR review with team standards |

### CLAUDE.md minimum content

```markdown
# Project: [Name]
Stack: [Languages, frameworks, DB, cloud]
Style: [Linting rules, async patterns, query conventions]
Test framework: [Framework + conventions]
Patterns: [Logger format, error response format, naming conventions]
Off-limits: [Folders or files AI must not modify]
Branch: [Current branch naming convention]
```

### .cursorrules minimum content

```
- Language: [e.g., TypeScript strict mode]
- Framework: [e.g., Next.js App Router]
- Style: [e.g., functional components only, no class components]
- Imports: [e.g., use absolute imports from @/]
- Testing: [e.g., always write tests alongside new functions]
- Avoid: [e.g., no inline styles, no raw SQL]
```

**Standard:** CLAUDE.md and .cursorrules must be in place before the first AI session on any new project. Responsibility: Tech Lead or most senior developer on the project.

---

## 5. Development Workflow Standard

The following flow is mandatory for all AI-assisted development tasks:

```
PLAN → VALIDATE → BUILD → AI CHECK → HUMAN REVIEW → TEST → MERGE
```

| Step | Tool | Who | Non-negotiable |
|------|------|-----|---------------|
| PLAN | Claude | Developer | Yes — always plan before coding |
| VALIDATE | — | Developer | Yes — confirm plan is correct before building |
| BUILD | Cursor / Copilot | Developer | No — use judgment on tooling |
| AI CHECK | Claude / Copilot Chat | Developer | No — recommended for complex code |
| HUMAN REVIEW | Peer / Lead | Reviewer | Yes — no AI PR without human review |
| TEST | All | Developer | Yes — tests written alongside code, not after |
| MERGE | Lead / Peer | Reviewer | Yes — explicit approval required |

**Minimum for simple tasks:** PLAN → BUILD → HUMAN REVIEW → MERGE
**Never acceptable:** TASK → BUILD → MERGE (no plan, no review)

---

## 6. Code Review Standards

### PR requirements for AI-assisted code

Every PR that contains AI-generated or AI-modified code must:

- [ ] Be tagged with `ai-assisted` label
- [ ] Include which tool(s) were used (in PR description)
- [ ] Have passed AI pre-review (Claude / Copilot Chat) before human review
- [ ] Have full human review — no exceptions
- [ ] Include tests for any new logic
- [ ] Have reviewer confirm they understand the logic (not just that it compiles)

### Reviewer checklist

| Check | Required |
|-------|---------|
| Does the code solve the right problem? | Yes |
| Does it follow team patterns and conventions? | Yes |
| Are edge cases handled — not just the happy path? | Yes |
| Are there tests — written by a human, not just AI-generated stubs? | Yes |
| Is there anything in this PR you cannot explain? | Escalate if yes |
| Does it touch any off-limits zones (auth, PII, encryption)? | Reject if yes |

### Two-gate rule

Gate 1 (AI): Claude or Copilot Chat pre-review → catches logic gaps, missing edge cases, pattern violations
Gate 2 (Human): Peer or lead review → catches business logic fit, security implications, architectural drift

Both gates are mandatory. Gate 2 cannot be skipped because Gate 1 ran.

---

## 7. Session Management Standards

| Control | When to use |
|---------|------------|
| `continue` | Claude paused mid-task — use continue, not re-prompt |
| Rewind | Claude went in the wrong direction — cut cleanly, re-prompt with correction |
| `/clear` | Switching to a different task or codebase — clear stale context |
| `/compact` | Context filling during a long session — compact before it fills |
| Subagent `/review` | Running a PR review — triggers code-reviewer.md with team standards |

**Rule:** Re-prompting is not the same as recalculating. When Claude goes wrong — rewind. Don't try to redirect mid-path.

---

## 8. Delegation Standards

Use this framework before every AI-assisted task:

| Level | When | Examples |
|-------|------|---------|
| **Full Delegate** | Output is mechanical, verifiable, low-risk | Boilerplate, CRUD scaffolding, test stubs, PR descriptions |
| **Collaborate** | Needs domain judgment to validate | Business logic, integrations, query optimisation, refactoring |
| **Human-led** | Requires your architectural context | System design, API contracts, data models, critical flows |
| **Never Delegate** | Sensitive, irreversible, or security-critical | Auth, encryption, PII, production incidents, architecture decisions |

**Decision test (run before every task):**
1. Can the output be verified quickly and completely? → higher delegation acceptable
2. Does it require domain context that AI doesn't have? → lower delegation required
3. Could a wrong output reach production without detection? → never delegate

**The rule:** Delegate the typing. Never delegate the thinking.

---

## 9. Governance Rules

### Non-negotiables — no exceptions

1. All AI-generated code receives human review before merge
2. No credentials, API keys, passwords, or client data in any AI prompt
3. Auth, encryption, and PII handling: manual development only
4. "If you cannot explain it — do not commit it. Escalate."
5. No AI agent has write access to production systems
6. No AI agent pushes directly to main or production branches

### What to escalate

Escalate to your tech lead if:
- AI output conflicts with known architecture decisions
- AI suggests accessing or modifying off-limits files
- You cannot explain what the AI-generated code does
- AI generates code touching auth, encryption, or PII handling
- You are unsure whether a task belongs in "full delegate" or "never delegate"

### Data classification — what must NOT enter AI tools

| Data type | Public AI tools | Internal / Claude API |
|-----------|----------------|----------------------|
| Source code (non-sensitive) | Allowed with judgment | Allowed |
| Auth logic, encryption code | Never | With explicit approval |
| Client data (any) | Never | Never |
| API keys, secrets, .env | Never | Never |
| Business logic (sensitive) | Never | With explicit approval |
| Architecture diagrams | Allowed with judgment | Allowed |

---

## 10. Role-Specific Standards

### Developers

- Set up CLAUDE.md and .cursorrules before first AI session on any project
- Plan with Claude before writing any non-trivial code
- Read every line of AI-generated code before committing
- Write tests alongside code — not after
- Tag every AI-assisted PR with `ai-assisted` + tool name
- Log AI task types in sprint notes (for team metrics)

### QA Engineers

- Use Claude for initial test case generation — review and extend, do not just accept
- Treat AI-generated test suites as a starting point, not a complete set
- The 20% requiring real judgment (user flows, undocumented edge cases, UX intuition) is yours — do not delegate it
- Verify AI-generated tests against the actual business requirement, not just the code

### Tech Leads

- Maintain CLAUDE.md per project — keep it accurate and current
- Define and maintain the team's AI off-limits zones per project
- Set up and own the team's agent library (.claude/agents/)
- Add `ai-assisted` to PR template as a required label
- Review AI-generated code on core logic with extra scrutiny — not less
- Track AI metrics per sprint: PR cycle time, rework rate, AI-assist rate, defect escape rate

### Architects

- Architecture decisions are human-led — AI is a sounding board only
- Document AI usage boundaries per project in the project CLAUDE.md
- Define what constitutes "off-limits" for AI in each project context
- Review and approve any AI-suggested architectural changes before implementation
- Maintain the organisation-level AI governance reference (this document)

### Delivery Managers

- Include AI-assisted task rate in sprint retrospective review
- Track PR cycle time as a primary AI productivity indicator
- Flag any team reporting significant rework on AI-assisted tasks for tech lead review
- AI usage does not replace delivery estimates — do not use AI capability to justify reduced timelines without team confirmation

---

## 11. Metrics — What to Track Per Sprint

| Metric | How to measure | Target direction |
|--------|---------------|-----------------|
| PR cycle time | Git: open to merge, hours | ↓ |
| Rework rate | PRs needing >1 review round, % | ↓ |
| AI-assisted task rate | Self-reported in sprint log | Track, don't target |
| Defect escape rate | Bugs found post-merge per sprint | ↓ |
| Test coverage delta | Coverage % before vs. after sprint | ↑ |

**Industry benchmarks (for reference):**
- Test writing: AI reduces authoring time by 40–60%
- PR descriptions: ~10 minutes saved per PR
- Boilerplate / scaffolding: 50–70% time reduction
- Bug investigation: AI-assisted root cause analysis ~30% faster
- Code review prep: AI pre-review catches ~20–30% of issues before human review

These are industry averages. Track your own numbers. Don't assume these apply automatically.

---

## 12. Prompt Library — Starting Templates

Copy, adapt, and use. Add team-specific ones to Confluence.

### Explain unfamiliar code
```
Stack: [Stack]. File: [path]. Explain what [function/block] does.
Focus on: side effects, dependencies, and anything that could break.
Format: bullet points, plain language.
```

### Generate tests
```
Stack: [Stack]. Test framework: [Jest/PHPUnit/etc].
File: [path]. Function: [name].
Generate unit tests covering: success case, [edge case 1], [edge case 2], error handling.
Format: [describe/it blocks]. Output code only.
```

### Review code before PR
```
Stack: [Stack]. Review this code for: logic gaps, edge cases, security issues, pattern violations.
Our standards: [paste relevant CLAUDE.md section].
Format: bullet list of issues only. No praise. Flag severity: low / medium / high.
```

### Debug an issue
```
Stack: [Stack]. File: [path]. Function: [name].
Issue: [exact error or behaviour].
What I've tried: [list].
Do not: [what you don't want changed].
Return: root cause first, then fix. Code only.
```

### Refactor for readability
```
Stack: [Stack]. File: [path].
Refactor [function/section] for readability. Do not change behaviour or external API.
Follow: [style rules from CLAUDE.md].
Return: refactored code block. No explanation unless you removed something.
```

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-21 | Initial release |
