# Exercise 1: Request Lifecycle Tracing

> Trace a ColdFusion request from HTTP request to response.

## Objective

Understand the complete ColdFusion request lifecycle by tracing and documenting a request's execution path through the server.

## Prerequisites

- ColdFusion server (Adobe CF or Lucee)
- Access to ColdFusion Administrator
- Sample CF application

## Instructions

### Part 1: Configure Tracing

1. Enable request debugging in ColdFusion Administrator
2. Enable "Request Debugging Output"
3. Set debug options to show:
   - Execution times
   - Database queries
   - Variable scopes
   - Include files

### Part 2: Trace a Simple Request

1. Create or select a simple CFM file that:
   - Includes at least one other file (cfinclude)
   - Makes at least one database query
   - Uses application/session scope

2. Request the page and analyze the debug output

3. Document the following for each step:

| Step | What Happened | Time | Notes |
|------|--------------|------|-------|
| 1 | HTTP request received | | |
| 2 | Application.cfc: onRequestStart | | |
| 3 | Session check | | |
| 4 | cfinclude processing | | |
| 5 | Database query execution | | |
| 6 | Output rendering | | |
| 7 | Response sent | | |

### Part 3: Trace a Component Request

1. Create or find a CFC with at least:
   - One remote method
   - One public method
   - Some component initialization

2. Call the component from a CFM page

3. Document the additional lifecycle events

### Part 4: Identify Lifecycle Hooks

For each of these Application.cfc methods, answer:

1. **When does it execute?**
2. **What should go in it?**
3. **What should NOT go in it?**

| Method | When | What In | What Out |
|--------|------|---------|----------|
| onApplicationStart | | | |
| onApplicationEnd | | | |
| onSessionStart | | | |
| onSessionEnd | | | |
| onRequestStart | | | |
| onRequest | | | |
| onRequestEnd | | | |
| onError | | | |
| onMissingTemplate | | | |

## Expected Outcome

A document showing:

1. Annotated request timeline from debug output
2. Diagram of the request lifecycle (you can use ASCII art or describe)
3. Table identifying lifecycle hooks and their proper use
4. At least 3 insights about how CF processes requests

## Solution Template

```markdown
# Request Lifecycle Analysis

## Annotated Timeline

[Insert your table from Part 2]

## Request Lifecycle Diagram

[ASCII diagram or description]

## Lifecycle Hooks Summary

[Completed table from Part 4]

## Key Insights

1. ...
2. ...
3. ...
```

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Complete timeline documented | 20 |
| Diagram accurately represents flow | 20 |
| Lifecycle hooks properly explained | 30 |
| Insights demonstrate understanding | 20 |
| Professional presentation | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
