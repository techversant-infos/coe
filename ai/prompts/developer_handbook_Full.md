# 🛠️ Developer Prompt Handbook — Employee Module

> **A complete reference of AI prompts for every stage of building the Employee Management Module.**
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

> **3-Point Estimation** calculates development effort using three scenarios:
> - **O** = Optimistic (best case)
> - **M** = Most Likely (realistic)
> - **P** = Pessimistic (worst case)
>
> **PERT Formula:** `(O + 4M + P) / 6`

### ✅ Proper Prompt — 3-Point Estimation for Employee Module

```
You are a senior software engineer and project estimator.

I need a 3-Point Estimation for the Employee Management Module.

Features to estimate:
  1. Create Employee API (POST)
  2. Update Employee API (PUT)
  3. Delete Employee API (DELETE)
  4. Get Employee by ID (GET)
  5. Get All Employees with pagination (GET)

Tech Stack: [Your Stack — e.g., Java + Spring Boot + MySQL]
Team: 1 Backend Developer, 1 QA Engineer

For each feature provide:
  - Optimistic estimate (hours)
  - Most Likely estimate (hours)
  - Pessimistic estimate (hours)
  - PERT Weighted Average using formula: (O + 4M + P) / 6
  - Development effort breakdown
  - QA / Testing effort breakdown
  - Risk and buffer notes

Format: Present as a table.
Add a TOTAL row at the bottom with the overall PERT estimate.
Add a brief risk summary below the table.
```

### 📦 What This Prompt Produces

- ✅ Per-feature estimation table with O / M / P / PERT columns
- ✅ Separate rows for Dev and QA effort
- ✅ Risk and buffer notes per feature
- ✅ Final total estimated hours for the complete module
- ✅ A risk summary to share with the Project Manager

---

## 5. Prompt for Planning (with Questions)

> A well-structured planning prompt tells the AI to ask clarifying questions **BEFORE** generating any plan. This ensures the output is tailored to your actual team, timeline, and constraints — not a generic template.

### ✅ Proper Prompt — Planning with Clarifying Questions

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

### 💡 Why Ask Questions First?

- ✅ Avoids wrong assumptions about team capacity and tech stack
- ✅ Uncovers hidden requirements like auth, compliance, and deployment
- ✅ Produces a plan that reflects your actual constraints — not a generic one
- ✅ Saves significant rework time later in the project lifecycle

---

## 6. Prompt for Database Schema, Table & Index Creation

> Use this prompt to generate a complete, production-ready database setup for the Employee module. A well-scoped prompt produces ready-to-execute SQL — not generic examples that still need significant editing.

### ✅ Proper Prompt — Schema, Table & Index for Employee Module

```
You are a senior database architect.

Create a complete database setup script for an Employee Management Module.

Database Engine: [Your DB — e.g., MySQL 8.0 / PostgreSQL 15]

Deliver the following in order:

1. CREATE SCHEMA statement
   Schema name: employee_db

2. CREATE TABLE for 'employee' with ALL of these fields:
   - id            : Primary Key, Auto Increment, Not Null
   - employee_code : VARCHAR(20), Unique, Not Null
   - first_name    : VARCHAR(100), Not Null
   - last_name     : VARCHAR(100), Not Null
   - email         : VARCHAR(150), Unique, Not Null
   - phone         : VARCHAR(20), Nullable
   - department    : VARCHAR(100), Not Null
   - designation   : VARCHAR(100), Not Null
   - salary        : DECIMAL(12,2), Not Null
   - joining_date  : DATE, Nullable
   - is_active     : BOOLEAN, Default TRUE
   - created_at    : TIMESTAMP, Default CURRENT_TIMESTAMP
   - updated_at    : TIMESTAMP, Auto-update on row change

3. Constraints:
   - NOT NULL on required fields
   - UNIQUE on email and employee_code
   - DEFAULT values where applicable

4. CREATE INDEX statements for performance on:
   - email         (login and search lookups)
   - department    (filter by department queries)
   - is_active     (active employee listing queries)
   - joining_date  (date range report queries)

5. Add SQL comments on each field explaining its purpose.

Format: Clean, executable SQL script with section headers as comments.
Constraint: Script must run without errors on a fresh database.
```

### 📦 Output Checklist

- ✅ Schema creation SQL with correct database name
- ✅ Table with all fields, correct data types, and proper constraints
- ✅ Primary key, unique keys, and foreign key definitions
- ✅ Index creation for all performance-critical columns
- ✅ SQL comments explaining each field
- ✅ Script ready to execute — no placeholder values

---

## 7. Prompt for Starting Development

> Before writing any code, use this prompt to have the AI ask all the setup questions it needs, then generate the complete implementation. Starting with questions prevents mismatched assumptions and avoids expensive rework.

### ✅ Proper Prompt — Development Kickoff with Questions

```
You are a senior software developer.

I want to start building an Employee Management Module.

Features:
  - Create Employee (POST)
  - Update Employee (PUT)
  - Delete Employee (DELETE)
  - Get Employee by ID (GET)
  - Get All Employees with pagination (GET)

IMPORTANT: Before writing any code, ask me ALL the questions
you need to set up and build the project correctly.

Your questions must cover (but are not limited to):
  - Programming language and exact version
  - Framework and version
  - Database type, version, and connection details format
  - Authentication required? (JWT / OAuth / Session / None)
  - Validation rules for each employee field
  - API response format (standard wrapper or plain object?)
  - Error handling strategy (custom error codes?)
  - Pagination type: page-based or cursor-based?
  - Soft delete or hard delete for Delete Employee?
  - Unit test coverage required?
  - Logging requirements (what to log and at what level?)

Do NOT write any code until I have answered all your questions.

After I answer, generate in this order:
  1. Project folder structure
  2. Model / Entity class with all fields and annotations
  3. Repository / DAO layer
  4. Service layer with full business logic
  5. Controller with all REST endpoints and correct HTTP methods
  6. Configuration file (DB connection, server port, settings)
  7. Input validation with field-level error messages
  8. Global exception handler with meaningful error responses
  9. Sample unit test for the Service layer
```

### 💡 Why Ask Before Coding?

- ✅ Prevents generating code for the wrong tech stack or version
- ✅ Clarifies business rules like soft delete vs hard delete upfront
- ✅ Avoids missing auth, logging, or validation requirements
- ✅ Produces production-ready code from the first attempt

---

## 8. Prompt for Code Review

> Use this prompt to get a structured, thorough code review from the AI. A well-scoped review prompt produces actionable findings with severity ratings — not vague comments like *"this could be improved"*.

### ✅ Proper Prompt — Code Review for Employee Module

```
You are a senior software engineer with 10+ years of experience,
specialising in code quality, security, and best practices.

Please conduct a thorough code review of my Employee Management
Module code provided below.

Review the following areas and check each one systematically:

CODE QUALITY
  1. Clean code principles (readability, naming, single responsibility)
  2. SOLID principles — identify any violations with explanation
  3. DRY principle — identify any duplicated logic

SECURITY
  4. SQL Injection vulnerabilities
  5. Input validation gaps — missing or insufficient validation
  6. Sensitive data exposure in logs or API responses

PERFORMANCE
  7. N+1 query problems
  8. Missing or incorrect database index usage
  9. Inefficient loops, queries, or data processing

BEST PRACTICES
  10. Correct and appropriate use of framework annotations
  11. Exception handling completeness and meaningful error messages
  12. API response structure consistency across all endpoints
  13. Language naming conventions (class, method, variable)

TESTING
  14. Missing unit or integration tests
  15. Edge cases not covered by existing tests

For EACH issue found, provide:
  - File name and method / line reference (if applicable)
  - Clear description of the problem
  - Severity: HIGH / MEDIUM / LOW
  - Corrected code snippet showing the fix

End with:
  - Overall code quality score out of 10
  - Summary of top 3 priority fixes

[PASTE YOUR CODE BELOW THIS LINE]
```

### 📊 Review Coverage Summary

| Area | What Gets Checked |
|------|------------------|
| Code Quality | Clean code, SOLID principles, DRY violations, naming conventions |
| Security | SQL injection, validation gaps, sensitive data in logs |
| Performance | N+1 queries, missing indexes, inefficient processing |
| Best Practices | Annotations, exception handling, API response consistency |
| Testing | Missing unit or integration tests, uncovered edge cases |

---

## 9. Prompts for Pull Request & PR Messages

> Use the following two prompts: the first to get step-by-step Git instructions for creating a branch and raising a PR, and the second to generate a professional PR message ready for your team review.

---

### Prompt A — Create Branch & Raise Pull Request

```
You are a senior Git and version control engineer.

I have completed development of the Employee Management Module.

Features completed:
  - Create Employee (POST)
  - Update Employee (PUT)
  - Delete Employee (DELETE)
  - Get Employee by ID (GET)
  - Get All Employees with pagination (GET)

Guide me step by step to:
  1. Create a new feature branch from the main / develop branch
     - Follow Git branch naming conventions
     - Suggested format: feature/employee-management-crud
  2. Stage and commit my changes with a proper commit message
     - Follow conventional commit format
  3. Push the new branch to the remote repository
  4. Raise a Pull Request targeting the develop branch
  5. Assign reviewers and add appropriate labels

Format: Numbered step-by-step Git commands, each with a one-line
explanation of what it does and why.
Include: Branch naming conventions and commit message best practices.
```

---

### Prompt B — Write a Professional PR Message

```
You are a senior developer writing a professional Pull Request
description for team code review.

Write a complete PR message for the following completed work:

Feature: Employee Management Module
Branch: feature/employee-management-crud
Target Branch: develop

Changes Made:
  - REST APIs: Create, Update, Delete, Get Employee
  - Input validation for all employee fields
  - Global exception handler with consistent error responses
  - Database connection and schema setup
  - Unit tests for the Service layer

Include ALL of these sections in the PR message:
  1. PR Title (concise and descriptive)
  2. Summary of Changes (what was built and why)
  3. Type of Change:
     [ ] Bug fix   [x] New feature   [ ] Refactor   [ ] Docs
  4. Related Ticket / Issue number: [e.g., JIRA-101]
  5. How to Test (step-by-step testing instructions for reviewer)
  6. Pre-Merge Checklist:
     - [ ] Code compiles without errors
     - [ ] All unit tests pass
     - [ ] No merge conflicts with target branch
     - [ ] Code reviewed by at least 1 peer
     - [ ] APIs tested with Postman or equivalent
     - [ ] No hardcoded credentials or sensitive data
  7. Screenshots / API response samples placeholder
  8. Notes for Reviewer (anything needing special attention)
```

---

### 🌿 Git Branch Naming Quick Reference

| Branch Type | Naming Format |
|-------------|--------------|
| New Feature | `feature/employee-management-crud` |
| Bug Fix | `bugfix/fix-employee-delete-null-check` |
| Hotfix | `hotfix/employee-email-duplicate-error` |
| Refactor | `refactor/employee-service-layer-cleanup` |
| Release | `release/v1.0.0-employee-module` |

---

### 📝 Conventional Commit Message Format

```
Format: <type>(<scope>): <short description>

Examples:
feat(employee): add create and update REST APIs
fix(employee): handle null pointer in delete service method
test(employee): add unit tests for employee service layer
refactor(employee): extract validation logic to separate class
docs(employee): add Swagger annotations to controller endpoints
```

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
