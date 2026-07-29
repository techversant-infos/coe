# Exercise 4: Security Assessment

> Find and document security issues in a legacy ColdFusion application.

## Objective

Learn to conduct a focused security assessment of ColdFusion applications.

## Scenario

**Application:** Online banking portal
**Criticality:** HIGH (financial data)

## Instructions

### Part 1: Review Authentication Code

Examine this login code:

```cfml
<!--- Vulnerable login.cfc --->
component {
    
    remote struct function login(required string username, required string password) {
        
        // Check credentials
        local.query = queryExecute(
            "SELECT user_id, role 
             FROM users 
             WHERE username = '#arguments.username#' 
             AND password = '#arguments.password#'"
        );
        
        if (local.query.recordCount == 1) {
            session.userId = local.query.user_id;
            session.role = local.query.role;
            return { success: true };
        }
        
        return { success: false, message: "Invalid login" };
    }
}
```

**Issues Found:**

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Part 2: Review Session Management

Examine this session code:

```cfml
<!--- session.cfm --->
<cffunction name="createSession">
    <cfargument name="user">
    
    <cfset SESSION.userId = arguments.user.id>
    <cfset SESSION.userName = arguments.user.username>
    <cfset SESSION.loggedIn = true>
    <cfset SESSION.cart = []>
    
    <cfreturn true>
</cffunction>
```

**Issues Found:**

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Part 3: Review File Upload

Examine this upload code:

```cfml
<!--- upload.cfm --->
<cffile action="upload" 
        fileField="document" 
        destination="#ExpandPath('./uploads/')#"
        nameConflict="overwrite">

<cfoutput>
    File uploaded: #cffile.serverFile#
    Type: #cffile.contentType#
</cfoutput>
```

**Issues Found:**

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Part 4: Review Output Handling

Examine this display code:

```cfml
<!--- userProfile.cfm --->
<cfquery name="getUser">
    SELECT * FROM users WHERE id = #url.id#
</cfquery>

<cfoutput>
    <h1>#getUser.username#</h1>
    <p>Email: #getUser.email#</p>
    <p>Notes: #getUser.notes#</p>
</cfoutput>
```

**Issues Found:**

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | | | |
| 2 | | | |

### Part 5: Server Configuration Review

Review this configuration:

| Setting | Current Value | Risk | Recommendation |
|---------|--------------|------|----------------|
| CFIDE accessible | Yes | | |
| Debug enabled | Yes | | |
| Error handling | Default | | |
| RDS enabled | Yes | | |
| Stack traces | Shown | | |

### Part 6: Complete Security Assessment Checklist

For the banking portal scenario:

| Category | Item | Status | Finding |
|----------|------|--------|---------|
| **Authentication** | | | |
| | Password hashing | | |
| | Brute force protection | | |
| | Session fixation prevention | | |
| **Authorization** | | | |
| | Role-based access | | |
| | Direct object reference | | |
| **Input Validation** | | | |
| | SQL injection | | |
| | XSS prevention | | |
| | File upload validation | | |
| **Data Protection** | | | |
| | PII encryption | | |
| | Sensitive data logging | | |
| **Server** | | | |
| | CFIDE secured | | |
| | SSL/TLS | | |
| | Security headers | | |

### Part 7: Risk Summary

Create a risk matrix:

| Risk | Likelihood | Impact | Risk Level | Mitigation |
|------|------------|--------|------------|------------|
| | | | | |
| | | | | |
| | | | | |

### Part 8: Remediation Plan

| Priority | Issue | Effort | Cost | Timeline |
|----------|-------|--------|------|----------|
| P1 - Critical | | | | |
| P2 - High | | | | |
| P3 - Medium | | | | |

## Expected Outcome

1. Completed code review with identified issues
2. Server configuration assessment
3. Risk matrix
4. Prioritized remediation plan

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| SQL injection issues identified | 15 |
| XSS issues identified | 15 |
| Session issues identified | 15 |
| Server config issues identified | 15 |
| Risk assessment accurate | 20 |
| Remediation plan logical | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
