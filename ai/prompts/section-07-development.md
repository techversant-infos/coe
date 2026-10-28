# 🚀 Section 7 — Prompt for Starting Development

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Ask all setup and configuration questions before writing a single line of code — preventing mismatched assumptions and expensive rework.

---

## 📋 Table of Contents

- [Why Ask Before Coding?](#why-ask-before-coding)
- [The Prompt](#the-prompt)
- [Questions the AI Will Ask You](#questions-the-ai-will-ask-you)
- [What Gets Generated After You Answer](#what-gets-generated-after-you-answer)
- [Generation Order Reference](#generation-order-reference)
- [Tips for Development Prompts](#tips-for-development-prompts)

---

## Why Ask Before Coding?

Starting development without clarifying questions leads to:

- ❌ Code generated for the wrong language or framework version
- ❌ Missing authentication setup discovered halfway through
- ❌ Wrong pagination strategy requiring a complete rewrite
- ❌ Hard delete implemented when soft delete was required

> ✅ **This prompt fixes all of that** — by asking every setup question upfront, before generating a single line of code.

---

## The Prompt

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

---

## Questions the AI Will Ask You

Answer each of these clearly before code generation begins:

| Question | Options / Examples |
|----------|-------------------|
| **Programming language & version** | Java 17, Node.js 20, Python 3.11 |
| **Framework & version** | Spring Boot 3.2, Express 4, FastAPI 0.110 |
| **Database type & version** | MySQL 8.0, PostgreSQL 15, MongoDB 7 |
| **Authentication** | JWT / OAuth2 / Session / None |
| **Validation rules** | Email format, name length, salary range, etc. |
| **API response format** | Standard wrapper `{ status, data, message }` or plain object |
| **Error handling** | Custom error codes or standard HTTP status only |
| **Pagination type** | Page-based `?page=1&size=10` or cursor-based |
| **Delete type** | Soft delete (set `is_active = false`) or hard delete (remove row) |
| **Unit tests** | Yes / No — coverage percentage if yes |
| **Logging** | What to log (requests, errors, DB queries) and at what level (INFO, DEBUG, ERROR) |

---

## What Gets Generated After You Answer

The AI generates all 9 components in order:

### 1. 📁 Project Folder Structure
Complete folder tree with layer responsibilities.

### 2. 🧩 Model / Entity Class
All fields, data types, validations, and ORM annotations.

### 3. 🗃️ Repository / DAO Layer
Database access layer with CRUD methods and custom queries.

### 4. ⚙️ Service Layer
Full business logic including validation, error handling, and data transformation.

### 5. 🌐 Controller
All REST endpoints with correct HTTP methods, request/response mapping, and status codes.

### 6. 🔧 Configuration File
Database connection, server port, and application settings.

### 7. ✅ Input Validation
Field-level validation rules with meaningful error messages per field.

### 8. 🚨 Global Exception Handler
Centralised error handling with consistent response format across all endpoints.

### 9. 🧪 Sample Unit Test
Unit test for the Service layer covering happy path and key edge cases.

---

## Generation Order Reference

```
Project Folder Structure
       ↓
Model / Entity Class
       ↓
Repository / DAO Layer
       ↓
Service Layer
       ↓
Controller
       ↓
Configuration File
       ↓
Input Validation
       ↓
Global Exception Handler
       ↓
Sample Unit Test
```

---

## Tips for Development Prompts

| Tip | Why It Helps |
|-----|-------------|
| Always specify exact versions | `Spring Boot 3.2` behaves differently from `Spring Boot 2.7` |
| Clarify soft vs hard delete upfront | Changing this after generation is expensive |
| Define the API response format first | Affects every controller and exception handler |
| State validation rules per field | Prevents vague or incorrect annotations |
| Request tests from the start | Retrofitting tests is harder than generating them together |

---

> 💡 **Pro Tip:** The `Do NOT write any code` instruction is critical. Without it, the AI will often skip the questions and jump straight to generating generic code. Keep that line in the prompt exactly as written.

---

*Section 7 of 9 · Developer Prompt Handbook · Employee Management Module*
