# Phase 1 Assessment: ColdFusion Deep Expertise

> Test your mastery of ColdFusion internals and advanced concepts.

## Instructions

Answer all questions. Show your work where applicable.

**Time:** 2 hours
**Passing Score:** 70%

---

## Section A: Request Lifecycle (15 points)

### A1. Order the following Application.cfc events in the correct order: (5 points)

```
a) onRequest
b) onRequestStart
c) onSessionStart
d) onApplicationStart
e) onRequestEnd
```

**Correct Order:** _________________________________

### A2. Explain when `onError` is triggered vs. `cftry/cfcatch`: (5 points)

___________________________________________________________
___________________________________________________________
___________________________________________________________

### A3. What is the difference between `cfinclude` and `cfscript` component calls in terms of scope? (5 points)

___________________________________________________________
___________________________________________________________

---

## Section B: JVM and Performance (20 points)

### B1. JVM Memory (10 points)

Given a server with 8GB RAM:

a) What would you set for `-Xms` and `-Xmx`? (2 points)
___________________________________________________________

b) Why should `-Xms` and `-Xmx` typically be equal? (4 points)
___________________________________________________________
___________________________________________________________

c) What happens when the heap fills up? (4 points)
___________________________________________________________

### B2. Garbage Collection (10 points)

a) Name two GC algorithms suitable for ColdFusion: (2 points)
1. _________________________________
2. _________________________________

b) What is the purpose of `-XX:MaxGCPauseMillis`? (4 points)
___________________________________________________________

c) Why might you want to avoid very large heap sizes (>4GB)? (4 points)
___________________________________________________________

---

## Section C: Security (20 points)

### C1. SQL Injection Prevention (8 points)

Given this vulnerable code:

```cfml
<cfquery name="getUser">
    SELECT * FROM users 
    WHERE username = '#form.username#'
</cfquery>
```

a) What is the vulnerability? (2 points)
___________________________________________________________

b) Write the secure version: (6 points)
```cfml
<cfquery name="getUser">
    ___________________________________________
    ___________________________________________
</cfquery>
```

### C2. XSS Prevention (6 points)

Explain why this is vulnerable and how to fix it:

```cfml
<cfoutput>
    Welcome, #userComment#
</cfoutput>
```

**Vulnerability:** ___________________________________________________________

**Fix:** ___________________________________________________________

### C3. CSRF Protection (6 points)

What is CSRF and name two ways to prevent it in ColdFusion? (6 points)
___________________________________________________________
___________________________________________________________

---

## Section D: Caching (15 points)

### D1. Cache Types (5 points)

Match each cache type with its scope:

| Cache Type | Scope |
|-----------|-------|
| 1. Variable scope cache | a) Shared across all users and servers |
| 2. Application scope cache | b) Single user, single request |
| 3. Server scope cache | c) Single user, multiple requests |

**Answers:** 1.___ 2.___ 3.___

### D2. Cache Implementation (10 points)

Write the code for caching a database query with a 10-minute TTL:

```cfml
<cfquery name="products" ___________________________________>
    ________________________________________________________
    ________________________________________________________
</cfquery>
```

What is the main limitation of this approach? (4 points)
___________________________________________________________

---

## Section E: Advanced CFML (15 points)

### E1. Component Inheritance (8 points)

```cfml
component name="BaseService" {
    public void function init() {
        variables.config = {};
    }
    
    public void function log(message) {
        writeLog(file="app", text=arguments.message);
    }
}

component name="UserService" extends="BaseService" {
    public void function init() {
        super.init();
        variables.db = "users";
    }
    
    public array function getUsers() {
        this.log("Fetching users");
        // implementation
    }
}
```

a) What is the output of this.log in UserService? (4 points)
___________________________________________________________

b) How would you call the parent's init from UserService.init()? (4 points)
___________________________________________________________

### E2. ORM Concepts (7 points)

a) What is lazy loading in ColdFusion ORM? (3 points)
___________________________________________________________

b) Why might lazy loading cause performance issues? (4 points)
___________________________________________________________

---

## Section F: Troubleshooting (15 points)

### F1. Debug the slow query (7 points)

This query is slow. Identify the problem and suggest a fix:

```cfml
<cfquery name="slowQuery">
    SELECT o.*, u.*, p.* 
    FROM orders o, users u, products p
    WHERE o.user_id = u.id 
    AND o.product_id = p.id
    AND o.created_date > '2023-01-01'
</cfquery>
```

**Problem:** ___________________________________________________________

**Fix:** ___________________________________________________________

### F2. Session issue (8 points)

A user's session seems to "reset" occasionally. List 3 possible causes and how to diagnose each:

| # | Possible Cause | Diagnosis |
|---|---------------|-----------|
| 1 | | |
| 2 | | |
| 3 | | |

---

## Answer Key

### Section A
- A1: d → c → b → a → e (onAppStart, onSessStart, onReqStart, onRequest, onReqEnd)
- A2: onError catches unhandled exceptions from any scope. cftry/cfcatch catches exceptions in the try block only.
- A3: cfinclude inherits the calling scope. Component calls have isolated local scope.

### Section B
- B1a: -Xms2g -Xmx2g (or 50-75% of RAM)
- B1b: Prevents heap resizing overhead and out-of-memory errors
- B1c: Garbage collection kicks in, then OutOfMemoryError
- B2a: G1GC, ZGC, SerialGC
- B2b: Sets target maximum pause time for G1GC
- B2c: Longer GC pauses, memory fragmentation

### Section C
- C1a: SQL injection - user input directly in query
- C1b: Use cfqueryparam
- C2: XSS - user input rendered without encoding
- C3: Cross-Site Request Forgery. Fix: CSRF tokens, SameSite cookies.

### Section D
- D1: 1-b, 2-a, 3-a
- D2: cachedWithin with createTimeSpan

### Section E
- E1a: "Fetching users" - it inherits the log method
- E1b: super.init()
- E2a: Related entities loaded only when accessed
- E2b: N+1 query problem

### Section F
- F1: Cartesian product without proper joins or WHERE conditions
- F2: See troubleshooting table template

---

## Scoring Guide

| Section | Points | Your Score |
|---------|--------|------------|
| A: Request Lifecycle | 15 | |
| B: JVM/Performance | 20 | |
| C: Security | 20 | |
| D: Caching | 15 | |
| E: Advanced CFML | 15 | |
| F: Troubleshooting | 15 | |
| **Total** | **100** | |

**Passing Score:** 70/100
