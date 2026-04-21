# 🔀 Section 9 — Prompts for Pull Request & PR Messages

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Get step-by-step Git instructions for creating a branch and raising a PR, and generate a professional PR message ready for team review.

---

## 📋 Table of Contents

- [Prompt A — Create Branch & Raise Pull Request](#prompt-a--create-branch--raise-pull-request)
- [Prompt B — Write a Professional PR Message](#prompt-b--write-a-professional-pr-message)
- [Git Branch Naming Quick Reference](#git-branch-naming-quick-reference)
- [Conventional Commit Message Format](#conventional-commit-message-format)
- [PR Pre-Merge Checklist](#pr-pre-merge-checklist)
- [Tips for PR Prompts](#tips-for-pr-prompts)

---

## Prompt A — Create Branch & Raise Pull Request

> Use this prompt to get step-by-step Git commands for creating your feature branch, committing, and raising a PR.

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

## Prompt B — Write a Professional PR Message

> Use this prompt to generate a complete, professional PR description ready to paste directly into GitHub, GitLab, or Bitbucket.

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

## Git Branch Naming Quick Reference

| Branch Type | Naming Format | When to Use |
|-------------|--------------|-------------|
| New Feature | `feature/employee-management-crud` | Adding new functionality |
| Bug Fix | `bugfix/fix-employee-delete-null-check` | Fixing a non-critical bug |
| Hotfix | `hotfix/employee-email-duplicate-error` | Urgent production fix |
| Refactor | `refactor/employee-service-layer-cleanup` | Code cleanup, no behaviour change |
| Release | `release/v1.0.0-employee-module` | Preparing a release version |

---

## Conventional Commit Message Format

```
Format: <type>(<scope>): <short description>
```

### Commit Type Reference

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature added | `feat(employee): add create and update REST APIs` |
| `fix` | Bug fix | `fix(employee): handle null pointer in delete service method` |
| `test` | Adding or updating tests | `test(employee): add unit tests for employee service layer` |
| `refactor` | Code restructure, no behaviour change | `refactor(employee): extract validation logic to separate class` |
| `docs` | Documentation updates | `docs(employee): add Swagger annotations to controller endpoints` |
| `chore` | Build, config, or tooling changes | `chore(employee): update Maven dependencies` |
| `perf` | Performance improvement | `perf(employee): add index on email column for faster lookups` |

---

## PR Pre-Merge Checklist

Before requesting a review, verify every item below:

```
[ ] Code compiles without errors
[ ] All unit tests pass locally
[ ] No merge conflicts with the target branch
[ ] PR has been self-reviewed (read your own diff first)
[ ] Code reviewed by at least 1 peer
[ ] All REST APIs tested with Postman or equivalent tool
[ ] No hardcoded credentials, API keys, or sensitive data
[ ] Swagger / API documentation updated if endpoints changed
[ ] Database migrations included if schema changed
[ ] Logging added at appropriate levels
```

---

## Tips for PR Prompts

| Tip | Why It Helps |
|-----|-------------|
| List every feature completed in the prompt | AI generates testing steps for each one |
| Specify the target branch | Prevents PRs raised to the wrong branch |
| Include the related ticket number | Links the PR to your project management tool |
| Ask for a pre-merge checklist | Catches issues before the reviewer sees them |
| Use conventional commit format | Enables automatic changelog generation |
| Self-review before requesting peers | Reduces back-and-forth in the review cycle |

---

> 💡 **Pro Tip for Prompt B:** Update the `Changes Made` section with your actual changes before using the prompt. The more specific your changes list, the more accurate and useful the generated PR message will be.

---

*Section 9 of 9 · Developer Prompt Handbook · Employee Management Module*
