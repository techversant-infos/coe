# Developer Excellence Curriculum — Folder Index

> **Audience:** All developers across web, mobile, and backend teams. Tech-agnostic.
> **Status:** Draft for cross-team review — v0.1 pilot.
> **Reading time:** 90 seconds for this README; 20 minutes for the full curriculum + gap analysis.

---

## 📍 You are here

```
learning-paths/
├── dev-excellence/   ← You are here
│   ├── README.md                  (this file)
│   ├── curriculum.md              (the curriculum — 7 phases, 20 topics, tech-agnostic)
│   ├── gap-analysis.md            (reviewer-only — coverage matrix)
│   └── stack-translations/        (per-stack translations of every topic)
│       ├── webdev/
│       │   ├── frontend.md        (web frontend)
│       │   └── backend.md         (server-side)
│       └── mobile/
│           └── stacks.md          (iOS, Android)
├── nextjs/                  (tech path: web frontend)
└── react/                   (tech path: React core)
```

## 🎯 What this curriculum is for

The **Developer Excellence Curriculum** is a *cross-cutting* learning track. It doesn't teach a framework — it teaches **the habits and decisions** that determine whether code is clean, maintainable, testable, and scalable.

Use it when a developer:

- Is past the "I can write code" stage and needs to write **good** code
- Reviews PRs and wants a shared rubric to push back on
- Owns a feature end-to-end and needs to think about design *before* coding
- Is being considered for a tech-lead track

It complements (does not replace) the tech-specific paths. After finishing the React or Next.js path, the developer is *fluent in a stack*. After finishing this curriculum, they're *fluent in the discipline that makes a stack work over time.*

## 📚 What's in this folder

| File | What's in it | When to open it |
|---|---|---|
| [README.md](./README.md) | This index | First time you land in the folder |
| [**curriculum.md**](./curriculum.md) | The 7 phases, 20 topics, code-review questions, mini-tasks, teaching guide — *tech-agnostic* | When you want to learn, teach, or run a pilot batch |
| [**stack-translations/webdev/frontend.md**](./stack-translations/webdev/frontend.md) | Stack-specific translation — web frontend | Pair with `curriculum.md` for every web frontend developer |
| [**stack-translations/webdev/backend.md**](./stack-translations/webdev/backend.md) | Stack-specific translation — server-side | Pair with `curriculum.md` for every backend developer |
| [**stack-translations/mobile/stacks.md**](./stack-translations/mobile/stacks.md) | Stack-specific translation — mobile | Pair with `curriculum.md` for every mobile developer |
| [**gap-analysis.md**](./gap-analysis.md) | Reviewer-only — what the curriculum covers, partially covers, and deliberately skips | When you're reviewing scope (tech lead, CoE review) |

## 🚦 Where to start

- **🆕 New joiner (1–3 months in)** — start at [Phase 1](./curriculum.md#phase-1-foundational-coding-discipline-beginner). Don't try to read it all at once. Pick *one* topic per week, apply it to your real PRs, and ask for code review on the change.
- **👀 Pilot batch planner** — start with the [How to teach this effectively](./curriculum.md#how-to-teach-this-effectively) section. It defines the format (one evolving codebase, live refactor, before/after). Pick 3–5 developers, run for 6–8 weeks, revisit at Week 2.
- **🧑‍🏫 Senior developer / tech lead** — start at the [gap analysis](./gap-analysis.md). Use it to challenge scope ("is *this* in the curriculum? if not, why not?"), and to feed the Week-2 review back into v0.2.
- **🤖 Reviewer (CoE audit)** — start at the [Document Control](./curriculum.md#document-control) and the [Reviewer questions](./gap-analysis.md#reviewer-questions) section. This curriculum is human-led; AI-assisted drafting is OK, but the rubric is owned by humans.

## 🔗 Related paths

| Path | When to use it |
|---|---|
| [React path](../react/intermediate.md) | Before this curriculum — gives you a stack to *apply* the discipline to |
| [Next.js path](../nextjs/intermediate.md) | After the React path, before or alongside this curriculum |
| [REST API Best Practices](../../general/rest-api-best-practices.md) | Pairs with [Phase 4](./curriculum.md#phase-4-api-architectural-thinking-advanced) (RESTful API Design) |
| [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) | Pairs with [Phase 6](./curriculum.md#phase-6-code-review-excellence-advanced) (Code Review Excellence) — the two-layer review model |
| [Node.js Code Review Checklist](../../nodejs/nodejs-typescript-code-review-checklist.md) | Stack-specific — pair with Phase 6 if you're on a Node.js product |
| [PHP Code Review Checklist](../../php/php-coding-standards.md) | Stack-specific — pair with Phase 6 if you're on a Laravel product |

## 🤖 AI delegation guidance

The [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) apply. For this curriculum specifically:

- **🟡 COLLABORATE tier (most topics)** — AI can draft examples, refactor before/after code blocks, and generate code-review-question variants. Human owns the rubric and the "right answer" to a question.
- **🟠 HUMAN-LED tier (Phase 7 — Senior Developer Mindset)** — Architectural Decision Records and mentoring practice are human-led. AI can suggest a structure for an ADR, but the *decision* and the *trade-off analysis* are human.
- **🔴 NEVER DELEGATE tier** — none of the curriculum content is in the Red Zone. But code review *of Red Zone code* (auth, payments, prod migrations) absolutely is — see the [Code Review Excellence phase](./curriculum.md#phase-6-code-review-excellence-advanced) and the AI Era Coding Guidelines for the two-layer model.

## 🧭 Path length and pacing

| Metric | Value |
|---|---|
| Phases | 7 (Phase 1–6 core, Phase 7 lead-track) |
| Topics | 20 |
| Suggested run length | 6–8 weeks (one topic per session, with mini-task follow-up) |
| Effort per week | 3–5 hours (1.5h session + 2–3h mini-task) |
| Pair-friendly | Yes — the [How to teach this effectively](./curriculum.md#how-to-teach-this-effectively) section is built for two |
| Pre-requisite | Comfortable shipping features in at least one production codebase (in whatever stack the team uses — web, backend, or mobile) |

## 📊 Document control

| Field | Value |
|---|---|
| Document | Developer Excellence Curriculum — Folder Index |
| Version | 0.3 (translation docs restructured to 'What changes + Mini-task + Watch' format; unverified YouTube links replaced with search hints pending tech-lead verification) |
| Owner | CoE Web Working Group (with cross-team feedback from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft — first cross-team review open |
| Related | [curriculum.md](./curriculum.md), [stack-translations/](./stack-translations/), [gap-analysis.md](./gap-analysis.md), [React Learning Path](../react/intermediate.md), [Next.js Learning Path](../nextjs/intermediate.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
