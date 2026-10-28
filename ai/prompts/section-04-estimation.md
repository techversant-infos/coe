# 📊 Section 4 — Prompt for 3-Point Estimation

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Calculate development effort accurately using the PERT formula before starting the sprint.

---

## 📋 Table of Contents

- [What is 3-Point Estimation?](#what-is-3-point-estimation)
- [PERT Formula](#pert-formula)
- [The Prompt](#the-prompt)
- [What This Prompt Produces](#what-this-prompt-produces)
- [Tips for Better Estimates](#tips-for-better-estimates)

---

## What is 3-Point Estimation?

3-Point Estimation calculates development effort using three scenarios:

| Scenario | Symbol | Description |
|----------|--------|-------------|
| **Optimistic** | O | Best case — everything goes smoothly |
| **Most Likely** | M | Realistic estimate based on normal conditions |
| **Pessimistic** | P | Worst case — includes blockers, rework, delays |

---

## PERT Formula

```
PERT Weighted Average = (O + 4M + P) / 6
```

> The formula gives **4× weight to the Most Likely** estimate, making it more accurate than a simple average.

---

## The Prompt

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

---

## What This Prompt Produces

- ✅ Per-feature estimation table with O / M / P / PERT columns
- ✅ Separate rows for Dev and QA effort
- ✅ Risk and buffer notes per feature
- ✅ Final total estimated hours for the complete module
- ✅ A risk summary to share with the Project Manager

---

## Tips for Better Estimates

| Tip | Why It Helps |
|-----|-------------|
| Always specify the tech stack | Estimates vary significantly between Java and Node.js |
| Include team composition | 1 junior dev vs 1 senior dev changes the numbers |
| Ask for risk notes per feature | Surfaces hidden complexity early |
| Use PERT, not averages | Weighted formula gives more reliable results |
| Share TOTAL row with the PM | Gives a single number for sprint planning |

---

> 💡 **Pro Tip:** Replace `[Your Stack]` with your actual stack before using the prompt. The more specific you are, the more accurate the estimates will be.

---

*Section 4 of 9 · Developer Prompt Handbook · Employee Management Module*
