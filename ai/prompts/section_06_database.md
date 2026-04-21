# 🗄️ Section 6 — Prompt for Database Schema, Table & Index Creation

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Generate a complete, production-ready database setup — schema, table, constraints, and indexes — ready to execute on a fresh database.

---

## 📋 Table of Contents

- [Why a Specific Prompt Matters](#why-a-specific-prompt-matters)
- [The Prompt](#the-prompt)
- [Employee Table — Field Reference](#employee-table--field-reference)
- [Index Reference](#index-reference)
- [Output Checklist](#output-checklist)
- [Tips for Database Prompts](#tips-for-database-prompts)

---

## Why a Specific Prompt Matters

A vague prompt like `"create employee database"` produces generic SQL with missing constraints, wrong data types, and no indexes.

> ❌ **Vague prompt:** Missing UNIQUE keys, no indexes, no comments, wrong types.
>
> ✅ **This prompt:** Every field, constraint, index, and comment — ready to run.

---

## The Prompt

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

---

## Employee Table — Field Reference

| Field | Type | Constraint | Purpose |
|-------|------|-----------|---------|
| `id` | INT | PK, Auto Increment, Not Null | Unique row identifier |
| `employee_code` | VARCHAR(20) | Unique, Not Null | Business identifier for the employee |
| `first_name` | VARCHAR(100) | Not Null | Employee first name |
| `last_name` | VARCHAR(100) | Not Null | Employee last name |
| `email` | VARCHAR(150) | Unique, Not Null | Login and communication email |
| `phone` | VARCHAR(20) | Nullable | Optional contact number |
| `department` | VARCHAR(100) | Not Null | Department the employee belongs to |
| `designation` | VARCHAR(100) | Not Null | Job title / role |
| `salary` | DECIMAL(12,2) | Not Null | Monthly or annual salary amount |
| `joining_date` | DATE | Nullable | Date the employee joined |
| `is_active` | BOOLEAN | Default TRUE | Soft delete / active status flag |
| `created_at` | TIMESTAMP | Default CURRENT_TIMESTAMP | Record creation timestamp |
| `updated_at` | TIMESTAMP | Auto-update | Last modification timestamp |

---

## Index Reference

| Index Column | Query Type | Why Indexed |
|-------------|-----------|-------------|
| `email` | Login and search | Frequent lookup by email on every login |
| `department` | Filter / GROUP BY | Common filter in department-based reports |
| `is_active` | WHERE clause | All active employee queries filter on this |
| `joining_date` | Date range queries | Reports often filter by joining period |

---

## Output Checklist

- ✅ Schema creation SQL with correct database name
- ✅ Table with all fields, correct data types, and proper constraints
- ✅ Primary key, unique keys, and foreign key definitions
- ✅ Index creation for all performance-critical columns
- ✅ SQL comments explaining each field
- ✅ Script ready to execute — no placeholder values

---

## Tips for Database Prompts

| Tip | Why It Helps |
|-----|-------------|
| Always name the DB engine and version | SQL syntax differs between MySQL and PostgreSQL |
| List every field explicitly | Prevents missing columns or wrong types |
| Specify NULL / NOT NULL per field | Avoids incorrect nullable defaults |
| Request indexes by use case | AI picks the right index type for the query pattern |
| Ask for SQL comments | Makes the schema self-documenting for the team |
| Require fresh-database compatibility | Ensures no dependencies on pre-existing objects |

---

> 💡 **Pro Tip:** Replace `[Your DB — e.g., MySQL 8.0 / PostgreSQL 15]` with your actual database engine and version. The generated SQL syntax will differ between engines — always specify.

---

*Section 6 of 9 · Developer Prompt Handbook · Employee Management Module*
