# Claude Cheat Sheet — Developer Edition
**Techversant Infotech · Engineering CoE**
*"Don't let AI work for you. Work better with AI."*

---

## 1. THE PROMPT FORMULA

> **Context + Task + Constraints + Format = Useful Output**

| Element | What to include | Example |
|---------|----------------|---------|
| **Context** | Stack, file name, what you've already tried | `In our Node.js + Express API (PostgreSQL, JWT auth)...` |
| **Task** | One specific action only | `...the /api/users/:id endpoint throws 500 when ID doesn't exist.` |
| **Constraints** | What NOT to touch / change | `Fix only the error handling. Don't change the JWT middleware.` |
| **Format** | How you want the output | `Return the corrected function only. No explanation needed.` |

### Weak vs Strong — Side by Side

| ❌ Weak | ✓ Strong |
|--------|---------|
| `Fix the user API` | `In our Node.js + Express API, /api/users/:id throws 500 when user doesn't exist. Return 404 with { error: 'user_not_found' }. Fix only the error handling — don't touch validation or JWT middleware. Return corrected code only.` |
| `Write tests` | `Write Jest unit tests for the getUserById() function in /src/services/userService.js. Cover: happy path, user not found (404), and DB connection error. Use our existing mock pattern from /tests/mocks/db.mock.js.` |
| `Review my code` | `Review the following Node.js function for: security issues, missing error handling, and performance problems. Flag only issues — don't rewrite the function.` |

### 5 Golden Rules
1. **One task per prompt** — chained prompts confuse output and waste tokens
2. **Name the file and function** — never say "this code"
3. **State what NOT to change** — Claude will optimise everything otherwise
4. **Specify the format** — "code only", "bullet points", "max 3 options"
5. **Give it a role** — `"Act as a senior PHP security reviewer for the following..."`

---

## 2. DO'S & DON'TS

### ✅ Always Do
- Review every line of AI output before committing — if you can't explain it, don't commit it
- Paste only the relevant function + ~10 lines of surrounding context (not the whole file)
- Use `/compact` when sessions get long — before context fills up, not after
- Use `/clear` when switching to a completely new task
- Tag PRs with the AI tool used: `[ai-assisted: claude]`
- Set up `CLAUDE.md` and `.cursorrules` on every active project
- Treat AI-generated code like a PR from a fast junior dev — review it properly

### ❌ Never Do
- Paste credentials, API keys, `.env` files, or client data into any AI prompt
- Skip human review because "Claude already checked it"
- Commit code you cannot explain line by line
- Use Claude for auth, encryption, password hashing, or PII handling (Red Zone)
- Let an AI agent push directly to a production branch
- Use your personal AI account for work code — use approved tools only
- Paste entire 500-line files to ask about one function

---

## 3. DELEGATION LEVELS — What to Hand Off

| Level | When to use | Examples |
|-------|------------|---------|
| 🟢 **FULL DELEGATE** — hand it off, review output | Low risk, repetitive, easy to verify | Unit test stubs, PR descriptions, commit messages, README/docs, boilerplate, code comments, CRUD scaffolding |
| 🟡 **COLLABORATE** — AI drafts, you steer & validate | Needs domain judgment to verify | Business logic, API integrations, DB queries, error handling, refactoring, config files |
| 🟠 **HUMAN-LED** — you drive, AI suggests only | Needs architectural context | System design, complex debugging, performance optimisation, API contracts, critical flows |
| 🔴 **NEVER DELEGATE** — manual only, always | Sensitive, irreversible, or security-critical | Auth & authorisation, encryption, PII handling, payment processing, production DB migrations, security middleware |

### The Delegation Test — Ask Before Every Task
1. Can the output be verified quickly without deep context? → **higher delegation**
2. Does it need domain knowledge Claude doesn't have? → **lower delegation**
3. Could a wrong output silently reach production? → **never delegate**

> **The rule: Delegate the typing. Never delegate the thinking.**

---

## 4. COMMANDS & SHORTCUTS

### In-Session Commands
| Command | When to use |
|---------|------------|
| `/compact` | Use before context window fills up. Saves ~60% tokens. Use proactively on long sessions. |
| `/clear` | Switching to a completely different task. Clears all context — fresh start. |
| `/review` | (Custom) Triggers your project's code-reviewer agent from `.claude/commands/` |
| `/test` | (Custom) Triggers your test-generator agent — generates tests in your project's style |
| `/doc` | (Custom) Triggers your docs-writer agent — writes docs in your project's voice |

### Model Selection — Right Model = Better Output + Lower Cost
| Model | Use When | Cost |
|-------|---------|------|
| **Claude Haiku** | Fast, repetitive tasks: test gen, doc summaries, boilerplate | Low |
| **Claude Sonnet** | Daily dev work — best quality/cost ratio. Your default choice. | Medium |
| **Claude Opus** | Architecture decisions, complex reasoning, critical debugging only | High |

> Don't use Opus for tasks Sonnet handles well. It costs significantly more for the same output.

---

## 4a. SESSION FLOW CONTROLS — Branching After a Prompt

After every Claude response, you have five ways to steer what happens next. Most developers only use one (re-prompting). Knowing all five saves significant time and tokens.

```
Your prompt or response
         │
         ├── continue   → Claude paused mid-task, keep going
         ├── rewind     → Wrong direction, go back to before it happened
         ├── clear      → New task entirely, wipe the slate
         ├── compact    → Session getting long, compress and continue
         └── subagent   → Hand a specific sub-task to a specialist
```

---

### CONTINUE — Keep going, don't stop here

**When:** Claude pauses mid-task waiting for your signal before proceeding to the next step.

**Why it matters:** Typing a new prompt instead of `continue` can cause Claude to drift from the pattern it established earlier in the same task.

**Example:**
> You ask Claude to refactor your auth module across 6 files. It completes files 1–3 and pauses.
> You type: `continue`
> Claude picks up exactly at file 4 — same approach, same naming conventions, no drift.
>
> ❌ If you typed "yes do the rest" instead — Claude restarts its reasoning and may subtly change patterns from files 1–3.

---

### REWIND — That was wrong, go back

**When:** Claude misunderstood the requirement and went several messages in the wrong direction. Continuing to correct it drags the wrong context forward.

**Why it matters:** Saying "no wait, ignore all that" in a new prompt doesn't fully clear the bad path — Claude partially carries it forward. Rewind cuts it cleanly.

**Example:**
> You ask Claude to fix a slow PostgreSQL query. It assumes missing indexes and starts rewriting your schema across 3 messages.
> You realise it's actually a missing JOIN condition — nothing to do with indexes.
> You **rewind** to before the schema conversation and re-prompt:
> `"The slowness is in the JOIN logic on line 34, not the schema. Fix only the query."`
> Claude now approaches it fresh — no schema baggage, no wrong assumptions.

---

### CLEAR (`/clear`) — New task, completely clean slate

**When:** Switching to an unrelated task after a long session.

**Why it matters:** Stale context bleeds invisibly into new tasks — wrong file references, wrong patterns, wrong assumptions based on what you were doing before.

**Example:**
> Morning: 45 minutes debugging a Node.js memory leak with Claude.
> Afternoon: you want to build a new React dashboard component.
> You type `/clear` before starting.
> Claude has zero memory of the memory leak, the Node.js files, or the backend context.
> Your React prompts get clean, focused output — not subtly influenced by backend context that has nothing to do with your component.
>
> ❌ Without `/clear` — Claude might reference patterns from your Node.js session when generating React code.

---

### COMPACT (`/compact`) — Session getting long, don't lose the thread

**When:** You've been working in the same session for a while and the context window is filling up.

**Why it matters:** When the context window is full, Claude silently drops the oldest content — which could be your CLAUDE.md rules, the architecture decisions you agreed on, or the constraints you set at the start. Compact preserves what matters in a compressed form.

**Example:**
> You've spent an hour building a POST `/api/orders` endpoint — schema, controller, validation, error handling.
> Context window is getting full.
> You type `/compact`.
> Claude summarises: *"We're building POST /api/orders in Express with Knex. Returns 201 on success, 422 on validation failure. Controller at /src/controllers/orders.js."*
> You get ~60% of your context back and continue writing tests and middleware without starting over.
>
> ✅ Rule: Compact **before** the window fills — not after. Once it's full, the oldest content is already gone.

---

### SUBAGENT — Hand a sub-task to a specialist

**When:** You need a specific piece of work done to a consistent standard — code review, test generation, documentation — that you do repeatedly across projects.

**Why it matters:** A general Claude session that wrote your code will tend to approve what it built. A subagent configured with your team's review standards will catch things the original session rationalised away. Subagents also save you from re-explaining your standards every single time.

**Example:**
> You finish writing a new service class and want it reviewed.
> You type `/review` — this triggers your `code-reviewer.md` subagent.
> The subagent is pre-configured with your team's rules:
> *"Flag any raw SQL, check for missing try/catch, verify no sensitive data is logged, confirm error responses match our 4xx format."*
> It reviews with those exact rules — every time, consistently — without you typing them again.
>
> Same for `/test` → triggers `test-generator.md` which already knows your Jest setup, mock patterns, and test file naming convention.
> Same for `/doc` → triggers `docs-writer.md` which already knows your JSDoc style and tone.

**Subagent files live in:** `.claude/agents/` — define once, reuse on every project.

---

### Quick Decision Guide

| Situation | Use |
|-----------|-----|
| Claude paused mid-task, waiting for signal | `continue` |
| Claude went the wrong direction (2+ messages deep) | `rewind` |
| Switching to a completely different task | `/clear` |
| Long session, context window filling up | `/compact` |
| Repeated task that needs consistent standards | subagent (`/review`, `/test`, `/doc`) |

---

## 5. PROJECT MEMORY — SET UP ONCE, SAVE HOURS

### Minimum File Structure (Set This Up Today)
```
your-project/
├── CLAUDE.md                        ← Claude reads this automatically at session start
├── .cursorrules                     ← Cursor behaviour rules
├── .github/
│   └── copilot-instructions.md      ← Copilot workspace context
└── .claude/
    ├── agents/
    │   ├── code-reviewer.md         ← /review — reviews PRs to your standards
    │   ├── test-generator.md        ← /test — generates tests your way
    │   └── docs-writer.md           ← /doc — writes docs in your voice
    └── commands/
        └── (your slash commands)
```

### CLAUDE.md — Minimum Template (Copy & Fill In)
```markdown
# Project Context
Stack: Node.js 20, Express, PostgreSQL 14, React 18
Style: ESLint Airbnb, async/await only, no raw SQL (use Knex)
Test framework: Jest + Supertest
Patterns: logger.info('msg', { context }), Knex for queries
Off-limits: /src/auth/, /src/middleware/security.js
Branch convention: feature/TICKET-123-short-description
PR convention: always include what was changed + why
```

> Without CLAUDE.md — every session starts from zero.
> With CLAUDE.md — Claude knows your stack, patterns, and no-go zones before you type a word.

---

## 6. TOOL SELECTION — RIGHT TOOL, RIGHT TASK

| Task | Best Tool |
|------|----------|
| Architecture planning, complex reasoning | **Claude** |
| Multi-file code generation & refactoring | **Cursor Composer** |
| Inline autocomplete while coding | **Cursor Tab / Copilot** |
| Unit test generation | **Claude or Copilot** |
| Debugging with a stack trace | **Claude** |
| PR description & commit messages | **Copilot** |
| General Q&A (no codebase context needed) | **ChatGPT** |
| Code review before opening a PR | **Claude** |

> Using Claude for inline autocomplete = asking your architect to write unit tests.
> Technically possible. Complete waste of context and cost.

---

## 7. CONTEXT HYGIENE — DON'T WASTE TOKENS

### What Burns Tokens
- Pasting entire files for a one-function question
- Re-explaining context Claude already has in the same session
- Asking vague questions that need 3 clarifying rounds
- No `CLAUDE.md` — re-explaining your stack every session

### What Saves Tokens
- Paste only the relevant function + ~10 lines of surrounding context
- Reference file names and line numbers: `in /src/routes/users.js line 42`
- Use `/compact` before context fills — not when it's already full
- Use `/clear` between completely different tasks
- One task per prompt — no mega-prompts chaining 5 requests

---

## 8. TWO-LAYER REVIEW — NON-NEGOTIABLE

```
AI-Generated Code
       │
       ▼
┌──────────────────────────────────────────┐
│  LAYER 1 — AI Pre-Review (before PR)     │
│  Ask Claude: logic gaps, edge cases,     │
│  test coverage, style violations         │
└──────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│  LAYER 2 — Human Review (always)         │
│  You: business logic, architecture fit,  │
│  security paths, explainability          │
└──────────────────────────────────────────┘
       │
       ▼
   Approved to Merge
```

> **If you can't explain every line — don't merge it.**
> AI pre-review is a helper. Human review is mandatory. These are not the same thing.

---

## 9. AI FOR TESTING — QUICK REFERENCE

| Test Type | What to ask Claude |
|-----------|-------------------|
| Unit test stubs | `Write Jest tests for [function]. Cover: happy path + 2 edge cases. Use mocks from [path].` |
| Edge case discovery | `List all the ways this function could fail or produce unexpected output.` |
| Coverage gaps | `What code paths in this file aren't covered by the existing tests?` |
| Regression test | `Write a test that would have caught this bug: [paste the bug description].` |

> Never merge AI-generated tests without reading them.
> AI tests what it thinks the code should do — not necessarily what it should actually do.

---

## 10. GOVERNANCE — QUICK REFERENCE CARD

| Rule | Details |
|------|---------|
| **Review everything** | All AI-generated code gets human review before merge. No exceptions. |
| **Tag your PRs** | Add `[ai-assisted: claude]` + which sections were generated |
| **No secrets in prompts** | No credentials, API keys, `.env`, or client data — ever |
| **Red Zone = manual only** | Auth, encryption, PII, payments, prod migrations — always human |
| **Escalate if unsure** | AI suggests something you can't explain → escalate to lead, don't commit |
| **No agent to prod** | No AI agent writes to production branches or live databases |

---

*Techversant Infotech · Engineering CoE · April 2026*
*For the full playbook and governance guide — refer to the AI F1 Playbook presentation.*
