# Developer Excellence Curriculum â€” Folder Index

> **Audience:** All developers across web, mobile, and backend teams. Tech-agnostic.
> **Status:** Draft for cross-team review â€” v0.1 pilot.
> **Reading time:** 90 seconds for this README; 20 minutes for the full curriculum + gap analysis.

---

## ðŸ“ You are here

```
learning-paths/
â”œâ”€â”€ dev-excellence/   â† You are here
â”‚   â”œâ”€â”€ README.md                  (this file)
â”‚   â”œâ”€â”€ curriculum.md              (the curriculum â€” 7 phases, 20 topics, tech-agnostic)
â”‚   â”œâ”€â”€ how-to-teach.md            (facilitator-only â€” how to run a pilot batch)
â”‚   â”œâ”€â”€ gap-analysis.md            (reviewer-only â€” coverage matrix)
â”‚   â””â”€â”€ stack-translations/        (per-stack translations of every topic)
â”‚       â”œâ”€â”€ webdev/
â”‚       â”‚   â”œâ”€â”€ frontend.md        (web frontend)
â”‚       â”‚   â””â”€â”€ backend.md         (server-side)
â”‚       â””â”€â”€ mobile/
â”‚           â””â”€â”€ stacks.md          (iOS, Android)
â”œâ”€â”€ nextjs/                  (tech path: web frontend)
â””â”€â”€ react/                   (tech path: React core)
```

## ðŸŽ¯ What this curriculum is for

The **Developer Excellence Curriculum** is a *cross-cutting* learning track. It doesn't teach a framework â€” it teaches **the habits and decisions** that determine whether code is clean, maintainable, testable, and scalable.

Use it when a developer:

- Is past the "I can write code" stage and needs to write **good** code
- Reviews PRs and wants a shared rubric to push back on
- Owns a feature end-to-end and needs to think about design *before* coding
- Is being considered for a tech-lead track

It complements (does not replace) the tech-specific paths. After finishing the React or Next.js path, the developer is *fluent in a stack*. After finishing this curriculum, they're *fluent in the discipline that makes a stack work over time.*

## ðŸ“š What's in this folder

| File | What's in it | When to open it |
|---|---|---|
| [README.md](./README.md) | This index | First time you land in the folder |
| [**curriculum.md**](./curriculum.md) | The 7 phases, 20 topics, code-review questions, mini-tasks â€” *tech-agnostic* | When you want to learn or apply the discipline |
| [**how-to-teach.md**](./how-to-teach.md) | Facilitator-only â€” how to run a pilot batch | When you're planning or running a pilot |
| [**stack-translations/webdev/frontend.md**](./stack-translations/webdev/frontend.md) | Stack-specific translation â€” web frontend | Pair with `curriculum.md` for every web frontend developer |
| [**stack-translations/webdev/backend.md**](./stack-translations/webdev/backend.md) | Stack-specific translation â€” server-side | Pair with `curriculum.md` for every backend developer |
| [**stack-translations/mobile/stacks.md**](./stack-translations/mobile/stacks.md) | Stack-specific translation â€” mobile | Pair with `curriculum.md` for every mobile developer |
| [**gap-analysis.md**](./gap-analysis.md) | Reviewer-only â€” what the curriculum covers, partially covers, and deliberately skips | When you're reviewing scope (tech lead, CoE review) |

## ðŸš¦ Where to start

- **ðŸ†• New joiner (1â€“3 months in)** â€” start at [Phase 1](./curriculum.md#phase-1-foundational-coding-discipline-beginner). Don't try to read it all at once. Pick *one* topic per week, apply it to your real PRs, and ask for code review on the change.
- **ðŸ‘€ Pilot batch planner** â€” start with [how-to-teach.md](./how-to-teach.md). It defines the format (one evolving codebase, live refactor, before/after). Pick 3â€“5 developers, run for 6â€“8 weeks, revisit at Week 2.
- **ðŸ§‘â€ðŸ« Senior developer / tech lead** â€” start at the [gap analysis](./gap-analysis.md). Use it to challenge scope ("is *this* in the curriculum? if not, why not?"), and to feed the Week-2 review back into v0.2.
- **ðŸ¤– Reviewer (CoE audit)** â€” start at the [Document Control](./curriculum.md#document-control) and the [gap analysis](./gap-analysis.md) coverage table. This curriculum is human-led; AI-assisted drafting is OK, but the rubric is owned by humans.

## ðŸ”— Related paths

| Path | When to use it |
|---|---|
| [React path](../../01-software-engineering/web-development/frontend/react/intermediate.md) | Before this curriculum â€” gives you a stack to *apply* the discipline to |
| [Next.js path](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md) | After the React path, before or alongside this curriculum |
| [REST API Best Practices](../../general/rest-api-best-practices.md) | Pairs with [Phase 4](./curriculum.md#phase-4-api-architectural-thinking-advanced) (RESTful API Design) |
| [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) | Pairs with [Phase 6](./curriculum.md#phase-6-code-review-excellence-advanced) (Code Review Excellence) â€” the two-layer review model |
| [Node.js Code Review Checklist](../../nodejs/nodejs-typescript-code-review-checklist.md) | Stack-specific â€” pair with Phase 6 if you're on a Node.js product |
| [PHP Code Review Checklist](../../php/php-coding-standards.md) | Stack-specific â€” pair with Phase 6 if you're on a Laravel product |

## ðŸ¤– AI delegation guidance

The [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) apply. For this curriculum specifically:

- **ðŸŸ¡ COLLABORATE tier (most topics)** â€” AI can draft examples, refactor before/after code blocks, and generate code-review-question variants. Human owns the rubric and the "right answer" to a question.
- **ðŸŸ  HUMAN-LED tier (Phase 7 â€” Senior Developer Mindset)** â€” Architectural Decision Records and mentoring practice are human-led. AI can suggest a structure for an ADR, but the *decision* and the *trade-off analysis* are human.
- **ðŸ”´ NEVER DELEGATE tier** â€” none of the curriculum content is in the Red Zone. But code review *of Red Zone code* (auth, payments, prod migrations) absolutely is â€” see the [Code Review Excellence phase](./curriculum.md#phase-6-code-review-excellence-advanced) and the AI Era Coding Guidelines for the two-layer model.

## ðŸ§­ Path length and pacing

| Metric | Value |
|---|---|
| Phases | 7 (Phase 1â€“6 core, Phase 7 lead-track) |
| Topics | 20 |
| Suggested run length | 6â€“8 weeks (one topic per session, with mini-task follow-up) |
| Effort per week | 3â€“5 hours (1.5h session + 2â€“3h mini-task) |
| Pair-friendly | Yes â€” [how-to-teach.md](./how-to-teach.md) is built for two |
| Pre-requisite | Comfortable shipping features in at least one production codebase (in whatever stack the team uses â€” web, backend, or mobile) |

## ðŸ“Š Document control

| Field | Value |
|---|---|
| Document | Developer Excellence Curriculum â€” Folder Index |
| Version | 0.3 (translation docs restructured to 'What changes + Mini-task + Watch' format; unverified YouTube links replaced with search hints pending tech-lead verification) |
| Owner | CoE Web Working Group (with cross-team feedback from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft â€” first cross-team review open |
| Related | [curriculum.md](./curriculum.md), [stack-translations/](./stack-translations/), [gap-analysis.md](./gap-analysis.md), [React Learning Path](../../01-software-engineering/web-development/frontend/react/intermediate.md), [Next.js Learning Path](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
