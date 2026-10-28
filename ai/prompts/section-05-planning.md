# 📅 Section 5 — Prompt for Planning the Employee Module

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Generate an accurate, tailored development plan by asking all clarifying questions first — before producing any output.

---

## 📋 Table of Contents

- [Why Ask Questions Before Planning?](#why-ask-questions-before-planning)
- [The Prompt](#the-prompt)
- [Questions the AI Will Ask You](#questions-the-ai-will-ask-you)
- [What the Plan Will Include](#what-the-plan-will-include)
- [Why This Approach Works](#why-this-approach-works)

---

## Why Ask Questions Before Planning?

Most AI-generated plans fail because they make assumptions. This prompt forces the AI to **ask first, plan second** — ensuring every output reflects your real constraints.

> ❌ **Without questions:** Generic plan that doesn't fit your team, stack, or deadline.
>
> ✅ **With questions:** A plan built around your actual situation.

---

## The Prompt

```
You are a senior software project planner.

I want to build an Employee Management Module with the following features:
  - Create Employee
  - Update Employee
  - Delete Employee
  - Get Employee by ID
  - Get All Employees with pagination

IMPORTANT: Before creating any plan, ask me ALL the clarifying
questions you need to generate an accurate and complete plan.

Your questions must cover (but are not limited to):
  - Technology stack and version preferences
  - Team size, roles, and availability
  - Project deadline or sprint duration
  - Database preference (SQL / NoSQL)
  - Authentication and authorisation requirements
  - Deployment environment (cloud / on-premise / hybrid)
  - Starting from scratch or integrating with existing codebase?
  - API documentation requirements (e.g., Swagger / OpenAPI)?
  - Testing requirements (unit / integration / end-to-end)?
  - Any compliance or data security requirements?

Do NOT generate the plan until I have answered all your questions.

After I answer, generate:
  1. Phase-wise development plan with clear phases
  2. Milestones and deliverables per phase
  3. Timeline estimate based on my answers
  4. Risk factors and mitigation strategies
  5. Definition of Done for each feature
```

---

## Questions the AI Will Ask You

Before generating the plan, the AI will ask about:

| Topic | Example Questions |
|-------|------------------|
| **Tech Stack** | Which language, framework, and DB version are you using? |
| **Team** | How many developers? What are their experience levels? |
| **Timeline** | What is the project deadline or sprint duration? |
| **Database** | SQL or NoSQL? Any existing schema? |
| **Auth** | Is authentication required? JWT / OAuth / Session / None? |
| **Deployment** | Cloud, on-premise, or hybrid environment? |
| **Codebase** | Starting from scratch or integrating into an existing project? |
| **Docs** | Do you need Swagger / OpenAPI documentation? |
| **Testing** | Unit, integration, or end-to-end tests required? |
| **Compliance** | Any data security or regulatory requirements? |

> ✏️ **Answer each question clearly.** The more detail you provide, the more accurate and useful the plan will be.

---

## What the Plan Will Include

Once you answer all questions, the AI generates:

1. **Phase-wise development plan** — clear phases with objectives
2. **Milestones and deliverables** — what is delivered at each phase
3. **Timeline estimate** — based on your actual team and deadline
4. **Risk factors and mitigation strategies** — proactive issue handling
5. **Definition of Done** — clear acceptance criteria for each feature

---

## Why This Approach Works

- ✅ Avoids wrong assumptions about team capacity and tech stack
- ✅ Uncovers hidden requirements like auth, compliance, and deployment
- ✅ Produces a plan that reflects your actual constraints — not a generic one
- ✅ Saves significant rework time later in the project lifecycle

---

> 💡 **Pro Tip:** Copy the prompt exactly as written. The `IMPORTANT` keyword and `Do NOT generate` instruction are critical — they prevent the AI from skipping ahead and producing a generic plan before you answer.

---

*Section 5 of 9 · Developer Prompt Handbook · Employee Management Module*
