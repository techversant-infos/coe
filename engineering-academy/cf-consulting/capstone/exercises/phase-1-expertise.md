# Phase 1 Exercise: Request Lifecycle Analysis

> Analyze the BlogCFC5 request lifecycle.

---

## Objective

Trace a request through BlogCFC5 to understand ColdFusion request handling.

---

## Exercise 1A: Application.cfc Analysis

**File:** `blogCFC6/Application.cfc`

Answer these questions:

1. What application-level settings are configured?
2. What scopes are used (application, session, request)?
3. Is there any custom error handling?
4. What does `onApplicationStart` initialize?

---

## Exercise 1B: Request Flow

Trace what happens when a user visits `client/index.cfm`:

1. Which Application.cfc events fire?
2. What CFC methods are called?
3. What database queries execute?
4. How is the page rendered?

**Hint:** Enable debugging in ColdFusion Administrator to see the request timeline.

---

## Exercise 1C: Component Dependencies

Map the dependency chain for `entry.cfc`:

```
entry.cfc
  ├── depends on: _______________
  ├── calls: _______________
  └── includes: _______________
```

---

## Exercise 1D: Identify Performance Issues

Examine the query patterns in `entry.cfc`. Find:

| Issue | Location | Query Code |
|-------|----------|------------|
| N+1 query | | |
| Missing index | | |
| No caching | | |
| Inefficient JOIN | | |

---

## Deliverable

Create a document showing:

1. Request flow diagram
2. Component dependency map
3. Performance issues found
4. Recommendations for optimization
