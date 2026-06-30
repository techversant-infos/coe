> **Migration notice:** This folder is retained for compatibility during the academy migration. The canonical version now lives in [engineering-academy/](../engineering-academy/). Update your bookmarks.

# Automation Engineer Learning Path

> **Objective:** Transform manual testers into automation engineers who can own end-to-end and API test automation — using Playwright as the CoE standard.
> **Status:** Draft for pilot batch review — v0.1.

---

## 📍 You are here

```
learning-paths/
├── automation-engineer/   ← You are here
│   ├── README.md                  (this file)
│   ├── intermediate.md            (the curriculum — 6 phases, 22 topics)
│   └── roadmap-gap-analysis.md      (reviewer-only — coverage mapping)
├── dev-excellence/        (recommended pre-req)
├── react/                (for frontend automation context)
└── nextjs/               (for full-stack automation context)
```

---

## 🎯 What this path is for

**The Problem:** Manual testers at Techversant lack a clear path to automation engineering. They test manually, know what good testing looks like, but have no structured way to learn automation. Meanwhile, "learning by osmosis" produces inconsistent automation skills across teams.

**The Solution:** A structured learning path that starts from "what is a good manual test" and builds up to "what is a good automated test" — using Playwright as the CoE standard. Same standards as the dev-excellence curriculum (learn / mini-task / self-check), but adapted for testing.

**Who this is for:**

- **🔵 Manual testers who want to automate** (entering Phase 1-3): You test manually now. You want to write code that does what you do manually. By Phase 3, you'll be automating E2E tests.
- **🟡 Automation engineers who want to mature** (entering any phase): You already automate. You want to level up — better test design, CI integration, mentoring. Start at whatever phase matches your current level.

---

## 📚 What's in this folder

| File | What's in it | Who reads it |
|---|---|---|
| [README.md](./README.md) | This index | First time you land in the folder |
| [**intermediate.md**](./intermediate.md) | The 6 phases, 22 topics, learn / mini-task / self-check structure | Main curriculum — every learner |
| [roadmap-gap-analysis.md](./roadmap-gap-analysis.md) | Reviewer-only — maps this path to the testing-landscape and flags what's covered / skipped intentionally | CoE reviewers, tech leads |

---

## 🚦 Where to start

### First: Take the self-assessment

**If you answer "yes" to most of these, start at Phase 1:**

- I execute manual test cases as part of my role
- I've seen code but never written more than a snippet
- I understand "what a test should verify" but not "how to automate it"
- I've never run a test from the command line

**If you answer "yes" to most of these, start at Phase 3 or 4:**

- I write automated tests in at least one framework (any: Cypress, Selenium, Playwright, custom)
- I understand locator strategies and can debug a failing test
- I've run tests in CI but not set up the pipeline myself
- I want to learn API automation and CI integration

**If you answer "yes" to most of these, start at Phase 5:**

- I own the test automation suite for my team
- I understand page object patterns and can apply them
- I can debug a test failure without guessing
- I want to level up to test reporting, accessibility testing, and mentoring

### Then: Choose your entry point

| Your profile | Start at | Duration |
|---|---|---|
| Manual tester, never coded | [Phase 1: Automation Mindset](./intermediate.md#phase-1-automation-mindset-beginner) | 1 week |
| Manual tester, basic code familiarity | [Phase 2: Playwright Fundamentals](./intermediate.md#phase-2-playwright-fundamentals-intermediate) | 2 weeks |
| Existing automation engineer, basic Playwright | [Phase 3: Test Design & Maintenance](./intermediate.md#phase-3-test-design-maintenance-intermediate) | 1 week |
| Automation engineer, want to mature | [Phase 4: API Automation](./intermediate.md#phase-4-api-automation-advanced) or Phase 5+ | 2-3 weeks |
| Want to lead automation | [Phase 6: Quality & Maturity](./intermediate.md#phase-6-quality-maturity-leadership-track) | 1 week |

**Pair-friendlier:** Yes — the format is the same as dev-excellence: one evolving codebase, live refactor, before-after. Find a pair who matches your level.

---

## 🎯 Prerequisites (complete before Phase 1)

Before starting Phase 1, make sure you have:

- **Access to a test codebase** where you can create a PR. If you're between projects, your tech lead should provide a sandbox repo.
- **A GitHub account** with push access to the test repo.
- **A code editor installed** (VS Code recommended).
- **Node.js 18+ installed** locally (`node --version` to verify).
- **Basic command-line comfort** (`cd`, `ls`, `git status` don't scare you).
- **Completed dev-excellence Phase 1-2** OR have 6+ months of manual testing experience. The curriculum teaches automation, not testing fundamentals.

---

## 🔗 Related paths

| Path | When to use it |
|---|---|
| [Dev Excellence Curriculum](../dev-excellence/curriculum.md) | Pairs with this path — provides the coding discipline foundation |
| [React Learning Path](../react/intermediate.md) | Frontend context for E2E test understanding |
| [Next.js Learning Path](../nextjs/intermediate.md) | Full-stack context for E2E + API test understanding |
| [REST API Best Practices](../../general/rest-api-best-practices.md) | Pairs with Phase 4 (API automation) — the CoE's API standard |
| [Git Workflow](../../git/Techversant_Git_Workflow.md) | For the commit conventions this path uses |

---

## 🤖 AI delegation guidance

The [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) apply. For this path specifically:

- **🟡 COLLABORATE tier** (most topics) — AI can draft Playwright test snippets, refactor locator strategies, and generate test assertion ideas. Human owns the test design and "what to automate" decision.
- **🟠 HUMAN-LED tier** (Phase 5-6 — CI integration, test reporting, accessibility testing) — The pipeline setup and reporting configuration decisions are human. AI can suggest YAML snippets but the design is human.
- **🔴 NEVER DELEGATE tier** — test maintenance and test triage. Don't delegate the judgment of "is this test flaky or is the code broken?" to AI.

---

## 📊 Document control

| Field | Value |
|---|---|
| Document | Automation Engineer Learning Path |
| Version | 0.1 (draft — 6 phases, 22 topics) |
| Owner | CoE QA Working Group |
| Review Cycle | Quarterly |
| Status | Draft for pilot batch review |
| Related | [intermediate.md](./intermediate.md), [roadmap-gap-analysis.md](./roadmap-gap-analysis.md), [REST API Best Practices](../../general/rest-api-best-practices.md), [Dev Excellence Curriculum](../dev-excellence/curriculum.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026