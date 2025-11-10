
**Version:** 1.0  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Contributers:** Nandu S 

# ColdFusion Code Review Checklist

The following checklist focuses on what reviewers can verify directly in a **code diff** or **pull request**.

## 📁 1. Structure & Organization
- CFCs live in logical packages/folders reflecting their responsibility (e.g., `/services`, `/models`).
- File, component, and function names are **descriptive and consistently cased**.
- Each CFC or function adheres to the **Single Responsibility Principle (SRP)**.
- `output="false"` is set on all CFCs/CFMs unless explicit output is required.
- Large templates or components are **modularized** into smaller includes/components.

## ⚙️ 2. Component Implementation
- Constructors (`init`) only **assign arguments** or **set defaults** — no DB queries, HTTP calls, or I/O.
- Every function declares an **access modifier** (`public`, `private`, `package`, or `remote`).
- Functions declare **returntype** where helpful and actually return that type.
- All variables are **scoped (`var`, `local`)** to prevent leakage.
- Shared functionality is extracted into **helpers or parent CFCs** instead of duplication.

## 💻 3. CFScript & Language Use
- **CFScript** is preferred; tags are used only when clearer or necessary.
- Use **implicit struct/array literals** (`{}`, `[]`) instead of `structNew()` or `arrayNew()`.
- Replace `isDefined()` with **`structKeyExists()`**; use **null-safe (`?.`)** and **Elvis (`?:`)** operators.
- Avoid **unsafe dynamic evaluation** (`evaluate()`, `cfexecute()`) unless justified.
- Prefer **switch/case** over long `if/elseif` chains.

## 🗄️ 4. Database Interaction
- All dynamic values in `<cfquery>` use **`<cfqueryparam>`**.
- Each query has an explicit **datasource**, **name**, and reasonable **timeout**.
- Avoid executing queries inside tight loops — use batching or joins.
- Large result sets are **paginated** or **limited**.
- Multi-step writes are wrapped in **`<cftransaction>`** for atomicity.

## 🔒 5. Security (Code-Level)
- User input is **validated and sanitized** before storage or output.
- Output encoding (`encodeForHTML`, `encodeForURL`, etc.) is applied consistently.
- Passwords are hashed using **bcrypt, PBKDF2, or Argon2** with salt and iterations.
- File uploads are validated (extension, MIME type, size) and stored **outside the webroot**.
- Cookies use **secure**, **httponly**, and **samesite** attributes.
- External calls via `cfhttp` enforce **TLS** and **SSL certificate verification**.
- Stack traces or detailed errors are **never exposed to clients**.

## 🧯 6. Error Handling & Logging
- Risky operations are wrapped in **`try/catch`** with targeted exception handling.
- Errors are **not swallowed silently** — log with context (e.g., userId, IP, request ID).
- Global error handler (`onError`) routes unhandled exceptions to a centralized logger/monitor.
- Logging uses appropriate severity levels: `info`, `warn`, `error`, `fatal`.

## ⚡ 7. Performance
- Redundant `<cfinclude>` calls are eliminated; compiled includes are cached when feasible.
- Heavy computations or repeated lookups are cached (`cacheGet`, `cachePut`, or `cachedwithin`).
- Query/template caching includes proper **expiry policies**.
- Long-running or duplicate queries are optimized and indexed appropriately.

## 🔍 8. Scope & State Management
- All function variables are properly **scoped (`var`, `local`)**.
- Writes to shared application or session data are **protected with `<cflock>`**.
- Session variables are **cleared** on logout or session end.
- Avoid storing large data structures in session/application scopes.

## 🌐 9. API / Remote Services
- Remote methods declare **parameter hints** and **return types** for clarity.
- All incoming parameters are validated for **type**, **format**, and **length**.
- Responses include appropriate **Content-Type headers** (`application/json`, etc.).
- Secrets, tokens, or passwords are **never logged** or returned in responses.
- APIs use consistent **HTTP status codes** and **structured error payloads**.

## 📂 10. File & Resource Handling
- File/stream handles are **closed in `finally` blocks** or cleanup sections.
- Temporary files are deleted after use to prevent storage leaks.
- Binary/PDF/Excel generation templates sanitize data to prevent injection or corruption.
- File operations handle **exceptions** gracefully with fallback logic.

## 🧩 11. Miscellaneous Code Checks
- No **deprecated tags or functions** (`cfchart` old attrs, `cfdocumentitem`, etc.).
- Application lifecycle methods (`onApplicationStart`, `onRequestStart`, etc.) are **efficient**.
- `this.secureJSON` and `this.secureJSONPrefix` are used for JSON responses.
- No hard-coded credentials or paths exist in the codebase.
- Version control ignores compiled files, logs, and `.env` secrets.

---
✅ **Use this checklist during every code review** to catch common ColdFusion issues before merge.  
It ensures cleaner, safer, and more maintainable applications across all Techversant ColdFusion projects.
