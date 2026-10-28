
**Version:** 1.0  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Contributers:** Nandu S, Aswathy S, Deepak Jose, Lajin M J  

# ColdFusion Style Guide (Techversant CoE)

## 📚 Table of Contents
- [1. Purpose](#1-purpose)
- [2. File & Directory Structure](#2-file--directory-structure)
- [3. Code Formatting & Syntax](#3-code-formatting--syntax)
- [4. Naming Conventions](#4-naming-conventions)
- [5. CFScript Best Practices](#5-cfscript-best-practices)
- [6. Database Query Practices](#6-database-query-practices)
- [7. Security Practices](#7-security-practices)
- [8. Component Design](#8-component-design)
- [9. Error Handling](#9-error-handling)
- [10. Performance Considerations](#10-performance-considerations)
- [11. Modern CFML Features](#11-modern-cfml-features)
- [12. Final Thoughts](#12-final-thoughts)

## 1. Purpose
Welcome to the **Techversant ColdFusion Style Guide** — the definitive reference for writing clean, efficient, and maintainable CFML code.  
Following these conventions ensures consistency across projects, improves readability, and supports scalable, secure, high-performing applications.

> 💡 *Consistency reduces friction, improves collaboration, and accelerates delivery.*

## 2. File & Directory Structure
A well-organized structure is the foundation of a maintainable application.

### Recommended Layout
```
/src
  /controllers
  /models
  /views
  /services
  /handlers
/tests
/assets
  /css
  /js
  /images
/config
  /environments
/build
```

### Naming Rules
| Element | Convention | Example |
|----------|-------------|----------|
| **Directories** | lowercase-with-hyphens | `/user-management` |
| **CFCs** | PascalCase | `UserService.cfc`, `OrderProcessor.cfc` |
| **Custom Tags** | lowercase_with_underscores | `custom_form_field.cfm` |
| **Views/Templates** | descriptive | `user_profile_edit.cfm` |

**Framework Alignment:**  
If using **ColdBox**, **FW/1**, or another framework, follow its directory conventions first, then supplement with this guide.

## 3. Code Formatting & Syntax
### Indentation
- Use **2 spaces** per level (no tabs).
- Align related clauses vertically for readability.

✅ **Good**
```coldfusion
<cfif user.isActive 
  AND user.hasPermission("admin")>
  <cfset result = service.process(user)>
</cfif>
```

❌ **Bad**
```coldfusion
<cfif user.isActive AND user.hasPermission("admin")>
<cfset result = service.process(user)>
</cfif>
```

### Line Length & Wrapping
- Limit lines to **100–120 characters**.
- Break at logical boundaries and align continuations.

## 4. Naming Conventions
| Element | Convention | Example |
|----------|-------------|----------|
| **Variables** | camelCase | `userProfile`, `totalCount` |
| **Constants** | UPPER_CASE | `MAX_LOGIN_ATTEMPTS` |
| **Functions** | camelCase | `calculateTotal()`, `getUserById()` |
| **Components** | PascalCase | `UserService`, `OrderProcessor` |
| **Booleans** | is/has/can prefix | `isActive`, `hasPermission` |
| **Query results** | Prefix with `q` | `qUsers`, `qOrders` |

## 5. CFScript Best Practices
Use **CFScript** for business logic in all new or refactored modules.

### Component Template
```cfscript
component accessors="true" {
  property name="userService" inject;
  property name="logger" inject="logbox:logger:{this}";
  function init() {
    variables.config = {};
    return this;
  }
  /**
   * Get user by ID
   * @id numeric - user identifier
   * @return struct
   */
  function getUser(required numeric id) {
    var user = userService.get(id);
    if (isNull(user)) {
      throw(type="UserNotFound", message="User not found");
    }
    return user;
  }
}
```

### Modern Syntax Tips
- **Null Coalescing:** `var name = user.name ?: "Guest";`
- **Safe Navigation:** `var name = user?.profile?.name ?: "";`
- **Arrow Functions:** `activeUsers = users.filter(u => u.isActive);`

## 6. Database Query Practices
### Formatting
```coldfusion
<cfquery name="qActiveUsers" datasource="appDSN" result="qResult">
  SELECT
    U.id,
    U.username,
    U.email,
    P.first_name,
    P.last_name
  FROM users U
  INNER JOIN profiles P ON P.user_id = U.id
  WHERE
    U.is_active = 1
    AND U.role_id = <cfqueryparam value="#variables.roleId#" cfsqltype="cf_sql_integer">
  ORDER BY P.last_name, P.first_name
</cfquery>
```

### Guidelines
- Always use **`<cfqueryparam>`**.  
- Avoid `SELECT *` — specify column names.  
- Use table aliases for clarity.  
- Cache long-running queries (`cachedwithin`).  
- Paginate large results (`maxRows`, `startRow`).  
- Prefer **HQL/ORM** for entity-based logic when possible.

## 7. Security Practices
### Input Validation
```cfscript
function createUser(required struct userData) {
  param name="userData.email" type="string";
  param name="userData.password" type="string";
  if (!isValid("email", userData.email)) {
    throw(type="ValidationError", message="Invalid email");
  }
  if (len(userData.password) < 8) {
    throw(type="ValidationError", message="Password too short");
  }
}
```
### Output Encoding
| Context | Function | Example |
|----------|-----------|----------|
| **HTML** | `encodeForHTML()` | `<cfoutput>#encodeForHTML(userInput)#</cfoutput>` |
| **JS** | `encodeForJavaScript()` | `<script>var name = '#encodeForJavaScript(name)#';</script>` |
| **URL** | `encodeForURL()` | `<a href="profile.cfm?id=#encodeForURL(id)#">` |

> 🔒 Always validate input, sanitize data, and encode output. Follow **OWASP Top 10** principles.

## 8. Component Design
### Service Layer Pattern
```cfscript
component singleton accessors="true" {
  property name="userDAO" inject;
  property name="emailService" inject;
  property name="log" inject="logbox:logger:{this}";
  function createUser(required struct userData) {
    try {
      validateUserData(userData);
      var user = userDAO.create(userData);
      emailService.sendWelcomeEmail(user);
      return user;
    } catch (any e) {
      log.error("Error creating user", e);
      rethrow;
    }
  }
  private function validateUserData(required struct userData) {
    // Validation logic
  }
}
```
### Guidelines
- Follow **Single Responsibility Principle**.  
- Use **dependency injection** (WireBox/ColdSpring).  
- Keep components **stateless**.  
- Document **public methods** with annotations.  
- Use **interfaces** for major contracts.

## 9. Error Handling
### Structured Approach
```cfscript
try {
  var result = service.process(data);
} catch (ValidationException e) {
  response.status(400).json({ error: "Validation failed", details: e.details });
} catch (DatabaseException e) {
  log.error("Database error", e);
  response.status(500).json({ error: "Database operation failed" });
} catch (any e) {
  log.error("Unexpected error", e);
  response.status(500).json({ error: "An unexpected error occurred" });
}
```
**Best Practices**
- Catch **specific exceptions**.  
- Log every exception (never swallow silently).  
- Use **custom exception types** for domain logic.  
- Map exceptions to **HTTP status codes** in APIs.  
- Include unique **error IDs** for traceability.

## 10. Performance Considerations
| Area | Recommendation |
|------|----------------|
| **Query Caching** | Use `cachedwithin` judiciously for repeated queries. |
| **Session Management** | Enable only when required; set proper timeouts. |
| **Variable Scoping** | Always use `var` inside functions; avoid unscoped variables. |
| **Includes** | Minimize `<cfinclude>`; prefer reusable CFCs. |
| **Output Control** | Use `<cfsetting enablecfoutputonly="true">` in templates. |
| **Large Data** | Use pagination or streaming APIs. |
| **Profiling** | Monitor with **FusionReactor** or **SeeFusion**. |

## 11. Modern CFML Features
- **Functional Array/Struct Methods:** `users.filter(u => u.isActive).map(u => u.name)`  
- **Spread Operator:** `var all = [...arr1, ...arr2]`  
- **Closures & Arrow Functions** for concise callbacks.  
- **Member Functions:** `array.each(i => process(i))`  
- **Implicit Structs/Arrays:** `{key: "value"}` and `[1,2,3]`  
> 🎯 Target **Lucee 5+** or **Adobe ColdFusion 2021+** to leverage these capabilities.

## 12. Final Thoughts
This guide defines the **Techversant ColdFusion Code Standard** — a living reference designed to keep our CFML projects modern, maintainable, and secure.  
> 🧠 *Code is read far more often than it is written. Write for clarity — for your teammates and your future self.*  

