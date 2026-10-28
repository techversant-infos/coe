# Exercise 4: Full End-to-End Migration

> Execute a complete Lucee migration on a sample application.

## Objective

Demonstrate end-to-end migration skills on a small application.

## Scenario

**Application:** Simple task management app
- 15 CFM files
- CF 2018
- MSSQL database (3 tables)
- Basic authentication
- Uses cfquery, cfform, cfdiv

## Instructions

### Part 1: Pre-Migration Checklist

Complete before starting:

| Checklist Item | Status | Notes |
|---------------|--------|-------|
| Source code backed up | ☐ | |
| Database backed up | ☐ | |
| Compatibility scan completed | ☐ | |
| Issues documented | ☐ | |
| Lucee environment installed | ☐ | |
| Rollback plan defined | ☐ | |

### Part 2: Compatibility Issues Found

| Issue | File | Fix |
|-------|------|-----|
| cfdiv usage | dashboard.cfm | Replace with AJAX |
| cfform | login.cfm | Replace with HTML form |
| | | |

### Part 3: Fix Compatibility Issues

**Replace cfdiv:**
```cfml
<!--- OLD: Adobe CF cfdiv --->
<cfdiv bind="url:taskList.cfm" />

<!--- NEW: jQuery AJAX --->
<div id="taskList">
    <script>
        $(document).ready(function() {
            $('#taskList').load('taskList.cfm');
        });
    </script>
</div>
```

**Replace cfform:**
```cfml
<!--- OLD: Adobe CF cfform --->
<cfform name="loginForm">
    <cfinput type="text" name="username" required="true">
    <cfinput type="password" name="password" required="true">
    <cfinput type="submit" value="Login">
</cfform>

<!--- NEW: HTML form --->

_______________________________________________________________

_______________________________________________________________
```

### Part 4: Test Plan

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| Login with valid credentials | Redirect to dashboard | | |
| Login with invalid credentials | Show error | | |
| Create new task | Task appears in list | | |
| Delete task | Task removed | | |
| Session timeout | Redirect to login | | |
| Database connection | Query executes | | |

### Part 5: Migration Summary

Complete the summary:

**Application:** Simple Task Manager
**Migration Date:** ________________
**Duration:** ___ hours

| Phase | Time | Issues Found |
|-------|------|-------------|
| Compatibility scan | | |
| Code fixes | | |
| Database migration | | |
| Testing | | |
| Deployment | | |

**Total Issues Found:** ___
**Critical Blockers:** ___
**Resolved Issues:** ___

## Expected Outcome

1. Complete pre-migration checklist
2. Documented fixes
3. Test results
4. Migration summary

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Pre-migration complete | 15 |
| Issues properly addressed | 25 |
| Code fixes working | 25 |
| Testing thorough | 20 |
| Documentation complete | 15 |
| **Total** | **100** |

**Passing Score:** 70/100
