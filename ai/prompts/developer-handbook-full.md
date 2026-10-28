# 🛠️ Developer Prompt Handbook — Employee Module

**Status:** Needs review · **Owner:** TBD · **Last updated:** 2026-10-28 · **Next review:** 2026-07-21

> **A complete reference of AI prompts for every stage of building the Employee Management Module.**
> Sections 4–9 are summaries here. Each one links to its own file, which holds the full prompt and tips.
> Covers: Technology Setup · Estimation · Planning · Database Schema · Development · Code Review · Pull Request

---

## 📋 Table of Contents

| # | Section | Purpose |
|---|---------|---------|
| [3](#3-how-to-use-prompts-at-technology-level) | Technology Level Prompts | Anchor prompts to your exact tech stack |
| [4](#4-prompt-for-3-point-estimation) | 3-Point Estimation | Estimate effort using the PERT formula |
| [5](#5-prompt-for-planning-with-questions) | Planning with Questions | Generate accurate, tailored project plans |
| [6](#6-prompt-for-database-schema-table--index-creation) | Database Schema & Index | Create production-ready SQL setup |
| [7](#7-prompt-for-starting-development) | Starting Development | Kickoff with questions before coding |
| [8](#8-prompt-for-code-review) | Code Review | Get structured, severity-rated code review |
| [9](#9-prompts-for-pull-request--pr-messages) | Pull Request & PR Messages | Create branches and write professional PRs |

---

## The Developer Prompt Formula

> Always use this formula when writing developer prompts:

```
[Role] + [Tech Stack & Version] + [Context] + [Task] + [Format] + [Constraints]
```

---

## 3. How to Use Prompts at Technology Level

> When starting any development task, always anchor your prompt to the exact technology stack. Without this, the AI will make assumptions that may not match your environment, version, or architecture style.

### ✅ Proper Prompt — Employee Module Technology Setup

```
You are a senior software architect.

I am starting a new project to build an Employee Management Module.

Tech Stack:
  - Backend  : [Your language & framework — e.g., Java 17 + Spring Boot 3]
  - Database : [Your DB — e.g., MySQL 8.0]
  - Build    : [Your build tool — e.g., Maven / Gradle]
  - Testing  : [Your test framework — e.g., JUnit 5 + Mockito]

Features to build:
  - Create Employee (POST)
  - Update Employee (PUT)
  - Delete Employee (DELETE)
  - Get Employee by ID (GET)
  - Get All Employees with pagination (GET)

Task: Recommend the best project structure and architecture pattern
for this module. Include folder structure with responsibilities for each layer.

Format: Show folder tree first, then explain each folder's purpose.

Constraints: Follow clean architecture. Keep it modular and testable.
```

### 💡 What Makes This Prompt Effective

| Element | Why It Matters |
|---------|---------------|
| Role assigned | AI responds as a senior architect, not a generic assistant |
| Stack is explicit | No assumption about language, framework, or DB version |
| All features listed | AI scopes the architecture to match the full module |
| Format specified | Folder structure first, then explanation |
| Constraints defined | Clean architecture and testability are required |

---

## 4. Prompt for 3-Point Estimation

> **Purpose:** Calculate development effort accurately using the PERT formula before starting the sprint.

The full prompt, what it produces, and tips: **[Section 4 — Prompt for 3-Point Estimation](./section-04-estimation.md)**

---

## 5. Prompt for Planning (with Questions)

> **Purpose:** Generate an accurate, tailored development plan by asking all clarifying questions first — before producing any output.

The full prompt, what it produces, and tips: **[Section 5 — Prompt for Planning the Employee Module](./section-05-planning.md)**

---

## 6. Prompt for Database Schema, Table & Index Creation

> **Purpose:** Generate a complete, production-ready database setup — schema, table, constraints, and indexes — ready to execute on a fresh database.

The full prompt, what it produces, and tips: **[Section 6 — Prompt for Database Schema, Table & Index Creation](./section-06-database.md)**

---

## 7. Prompt for Starting Development

> **Purpose:** Ask all setup and configuration questions before writing a single line of code — preventing mismatched assumptions and expensive rework.

The full prompt, what it produces, and tips: **[Section 7 — Prompt for Starting Development](./section-07-development.md)**

---

## 8. Prompt for Code Review

> **Purpose:** Get a structured, thorough code review with severity-rated findings — not vague comments like *"this could be improved"*.

The full prompt, what it produces, and tips: **[Section 8 — Prompt for Code Review](./section-08-code-review.md)**

---

## 9. Prompts for Pull Request & PR Messages

> **Purpose:** Get step-by-step Git instructions for creating a branch and raising a PR, and generate a professional PR message ready for team review.

The full prompt, what it produces, and tips: **[Section 9 — Prompts for Pull Request & PR Messages](./section-09-pull-request.md)**

---

## 📌 Quick Reference — Prompt Formula Checklist

> Use this checklist before submitting any developer prompt:

```
[ ] Role assigned         — "You are a senior [role]..."
[ ] Tech stack stated     — Language, framework, DB, version
[ ] Context provided      — What you are building and why
[ ] Task is clear         — Exact output you need
[ ] Format specified      — Table / code / list / folder tree
[ ] Constraints defined   — Architecture rules, style, limits
[ ] Questions requested   — If setup is complex, ask first
```

---

## ⚠️ Developer Prompt Anti-Patterns

> Avoid these common mistakes that produce poor AI output:

| ❌ Bad Prompt Pattern | ✅ Fix |
|----------------------|--------|
| `write employee api` | Specify language, framework, DB, and all 5 CRUD operations |
| `create database tables` | Name the DB engine, all fields, constraints, and indexes |
| `review my code` | List every review area with severity format and output structure |
| `make a plan` | Ask for clarifying questions first before generating the plan |
| `create a PR` | Specify branch name, target branch, changes made, and all checklist items |

---

*Last updated: 27 March 2026 · Audience: Developers & Tech Leads · Module: Employee Management*
