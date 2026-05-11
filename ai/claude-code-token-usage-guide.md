# Claude Code — Token Efficiency & Model Routing Guide
**Techversant CoE Initiative · Shared API Key Usage Standards**

> This guide is for all developers using the shared Claude Code API key under the CoE program.
> Token usage is pooled across the entire org. Every token you waste is a token someone else can't use.
> **Claude Opus 4.6 is NOT needed for 90% of your tasks. Use the right model for the right job.**
> Read this before you start using Claude Code in your workflow.

---

## 1. How the Shared Key Works

- One API key. One token budget. Shared across the entire team.
- Limits are enforced at the **organization level** — there is no per-user quota.
- Two limits to watch: **tokens per minute (TPM)** and **requests per minute (RPM)**.
- Hitting either limit affects everyone on the team simultaneously.
- Usage resets on a rolling basis, but sustained abuse compounds over time.

---

## 2. The Golden Rules

| # | Rule |
|---|------|
| 1 | Never paste entire files when a snippet will do |
| 2 | Always scope your request — tell Claude exactly what to look at |
| 3 | Avoid conversational back-and-forth for things you can resolve yourself |
| 4 | Use `/clear` to reset context when switching tasks |
| 5 | Don't re-explain context Claude already has in the same session |
| 6 | Prefer one precise request over three vague follow-ups |

---

## 3. Use the Right Model — The #1 Cost Lever

> Sending every task to Claude Opus 4.6 is like hiring a senior architect to rename a variable.
> Match the model to the complexity of the task.
> **All tools in this section are free. No paid subscriptions required.**

### Approved Free Tools

| Tool | Cost | Best For |
|------|------|----------|
| **Ollama** (local) | Free, runs on your machine | Most coding tasks — the default first stop |
| **OpenAI Codex** | Free tier available | Code generation, completions, scaffolding |
| **Claude Sonnet 4.6** | Shared CoE key | Reasoning, debugging, architecture |
| **Claude Opus 4.6** | Shared CoE key | Complex multi-step problems only (use sparingly) |

### Model Routing Quick Reference

| Task | Use This | Why |
|------|----------|-----|
| Boilerplate, CRUD scaffolding, repetitive patterns | **Ollama** — `qwen2.5-coder` | Free, runs locally, fast enough |
| Simple refactors, renames, extract method | **Ollama** | Zero cost |
| Syntax help, quick lookups | **Ollama** or **Codex (free)** | No API spend needed |
| Code generation, completions | **Codex (free tier)** | Purpose-built for code generation |
| Test generation (unit/feature) | **Ollama** or **Claude Sonnet 4.6** | Use Sonnet only if Ollama output quality isn't good enough |
| Debugging complex logic | **Claude Sonnet 4.6** | Reasoning quality matters here |
| Architecture decisions, ambiguous specs | **Claude Sonnet 4.6** | This is where it earns its cost |
| Multi-step reasoning, system design | **Claude Sonnet 4.6** | Justified use of shared key |
| ~~Everything~~ | ~~Claude Opus 4.6~~ | ❌ Overkill for 90% of tasks — ask yourself first |

### The Decision Rule (Keep It Simple)

```
Can Ollama handle it? → Use Ollama (always try this first)
  ↓ No / output quality not good enough
Is it code generation or completion? → Use Codex (free tier)
  ↓ No
Does it need real reasoning or debugging? → Use Claude Sonnet 4.6
  ↓ Only if Sonnet genuinely isn't enough
Is it a truly complex, multi-layered problem? → Claude Opus 4.6 (rare, justify it)
```

### Setting Up Ollama (One-Time, ~10 mins)

```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Pull recommended models
ollama pull qwen2.5-coder   # Best for code tasks — start here
ollama pull codellama        # Good fallback

# Run
ollama run qwen2.5-coder
```

Minimum hardware: **16GB RAM**. Works on most dev machines. Ask the CoE lead if you need help.

### Setting Up Codex (Free Tier)

- Sign in at [platform.openai.com](https://platform.openai.com) with a personal account
- Free tier includes access to Codex via the API playground and CLI
- Use for: scaffolding, boilerplate, code completions — not for sensitive client code
- VS Code integration: install the **OpenAI Codex** extension

### ⚠️ Privacy — What's Safe for Client Code

| Tool | Client / NDA Code | Internal Code |
|------|------------------|---------------|
| Ollama (local) | ✅ Safe — never leaves your machine | ✅ |
| Claude (CoE key) | ✅ Safe — covered under API agreement | ✅ |
| Codex (free tier) | ⚠️ Avoid — data goes to OpenAI servers | ✅ OK for internal |

**Rule of thumb: For anything under NDA or from a client repo, use Ollama or Claude only.**

---

## 4. Do's and Don'ts

### Code Generation & Completion

| ✅ Do | ❌ Don't |
|-------|---------|
| Provide function signature + expected behavior | Paste the entire controller and say "add a method" |
| Specify input/output types and edge cases upfront | Ask Claude to "figure out" what you need |
| Request only the function/class you need | Ask for full file rewrites when only one method changed |
| Use inline comments to constrain output | Let Claude generate boilerplate you'll throw away |

### Code Review & Refactoring

| ✅ Do | ❌ Don't |
|-------|---------|
| Point Claude to specific lines or methods: `"Review lines 45–90 for N+1 issues"` | Paste 500-line files and ask for a general review |
| Ask for targeted feedback: `"Check only for security issues"` | Ask for review + refactor + docs in one open-ended request |
| Provide the relevant model/schema context only | Include unrelated files "just in case" |

### Debugging & Troubleshooting

| ✅ Do | ❌ Don't |
|-------|---------|
| Include the error message + the relevant stack trace lines | Paste 200 lines of logs |
| Share only the method/block where the bug lives | Share the entire service file |
| State what you've already tried | Start fresh without context, making Claude retrace your steps |
| Specify framework + version (e.g., Laravel 11, PHP 8.2) | Leave Claude to guess the environment |

---

## 5. Efficient Prompt Patterns

### Instead of this (wasteful):
```
Here is my entire UserController.php [pastes 400 lines]. 
Can you review it and refactor it and also add PHPDoc comments 
and check for any bugs and suggest improvements?
```

### Do this (efficient):
```
Laravel 11 · UserController.php · Lines 78–112 (store method)

Issue: Validation logic is mixed with business logic.
Goal: Extract validation into a Form Request class.
Constraint: Keep existing error response format.

[paste only lines 78–112]
```

---

### Instead of this (wasteful):
```
This isn't working. Can you fix it?
[pastes entire file]
```

### Do this (efficient):
```
PHP 8.2 · Laravel 11

Error: "Trying to get property of non-object" on line 94
Method: UserService::assignRole()
Relevant code:

[paste only the method, ~15 lines]

Already tried: checking if $user is null before the call — it's not.
```

---

## 6. Context Management in Claude Code

Claude Code keeps a **running context window** within a session. This grows with every message and costs tokens on both sides.

**Best practices:**

- Use `/clear` when switching to a completely different task or file.
- Don't repeat file contents or instructions already in the session.
- Keep sessions task-scoped — one session per feature/bug, not one session per day.
- If a session is getting long (15+ exchanges), consider starting fresh with a tight summary instead.

---

## 7. What Counts as a Token

A rough mental model:

| Content | Approx. Tokens |
|---------|---------------|
| 1 line of code | ~10–15 tokens |
| 100-line PHP file | ~800–1,200 tokens |
| Full stack trace (50 lines) | ~600–900 tokens |
| "Explain this entire module" response | ~2,000–5,000 tokens |
| A precise, scoped request + response | ~300–800 tokens |

Pasting a 300-line file to ask about one method wastes ~2,000 tokens before Claude even responds.

---

## 8. Shared Key Etiquette

- **Don't run experiments in bulk.** If you're testing prompts, do it in your own Claude.ai account first.
- **Don't automate without approval.** Scripts or tools that call the API in loops must be reviewed by the CoE lead before running.
- **Don't share the key externally.** The key is for Techversant dev team members only.
- **Report anomalies.** If you notice a sudden slowdown or rate limit error, flag it in the CoE channel immediately — don't just retry in a loop.

---

## 9. Quick Reference Checklist

Before sending any request, run through this:

- [ ] **Have I picked the right model?** (Don't default to Opus — use the routing table in §3)
- [ ] Am I pasting only what the model actually needs to see?
- [ ] Is my request scoped to one specific task?
- [ ] Have I stated the language, framework, and version?
- [ ] Have I included the error or expected behavior clearly?
- [ ] Am I combining too many tasks into one prompt?
- [ ] Should I `/clear` context before starting this?
- [ ] Is this client code? If yes — am I using an approved model only?

---

## 10. Reporting & Accountability

As part of the CoE initiative, token usage will be reviewed periodically. If the shared key consistently hits rate limits, access patterns will be audited.

**CoE Lead:** Lajin | Raise issues in the CoE Slack channel or via direct message.

---

*Last updated: May 2026 · Techversant CoE Initiative*