# Exercise 1: Performance Profiling

> Profile a ColdFusion application to identify bottlenecks.

## Objective

Learn to use profiling tools to find performance issues.

## Scenario

**Application:** Order processing system
**Issue:** Page takes 8 seconds to load

## Instructions

### Part 1: Request Timeline Analysis

Using debug output, analyze this request:

| Step | Duration | Threshold | Status |
|------|----------|-----------|--------|
| Application startup | 45ms | 100ms | ✅ |
| Session check | 12ms | 50ms | ✅ |
| Database query 1 | 2500ms | 100ms | ❌ |
| Database query 2 | | 100ms | |
| Database query 3 | | 100ms | |
| Template rendering | | 200ms | |
| Include files (3) | | 100ms | |
| External API call | | 1000ms | |

**Slowest steps:** _________________________________

### Part 2: Query Analysis

Examine these queries:

```cfml
<!--- Query A: Users with orders --->
<cfquery name="slowQuery">
    SELECT u.*, o.*
    FROM users u, orders o
    WHERE u.id = o.user_id
</cfquery>

<!--- Query B: Get all users, then loop for orders --->
<cfquery name="users">
    SELECT * FROM users
</cfquery>

<cfloop query="users">
    <cfquery name="orders">
        SELECT * FROM orders WHERE user_id = #users.id#
    </cfquery>
</cfloop>
```

**Issues:**

| Query | Problem | Impact |
|-------|---------|--------|
| A | | |
| B | | |

### Part 3: Implement Solution

Fix the N+1 query problem:

```cfml
<!--- FIXED: Single query with JOIN --->

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________
```

### Part 4: Measure Improvement

Document before/after:

| Metric | Before | After |
|--------|--------|-------|
| Query execution time | 2500ms | |
| Total request time | 8000ms | |
| Database round trips | 101 | |
