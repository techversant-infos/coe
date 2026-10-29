# Exercise 1: Compatibility Scan

> Run automated compatibility checks and document issues.

## Objective

Learn to use automated tools and manual review to identify Lucee migration issues.

## Scenario

**Application:** E-commerce platform

- ~120 CFM files
- CF 2018
- Uses cfpdf, cfchart, cfexchange
- Custom authentication
- MSSQL database

## Instructions

### Part 1: Automated Scanning

Use these tools to scan the codebase:

**Server settings with CFConfig:**

```bash
# Install CFConfig into CommandBox (once)
box install commandbox-cfconfig

# Export the Adobe ColdFusion server settings (datasources, mail, mappings) to a file
box cfconfig export from=/path/to/ColdFusion2025/cfusion/ to=adobe-config.json
```

CFConfig moves server settings, not code. Import the file into the Lucee test server as the
[CFConfig usage guide](https://cfconfig.ortusbooks.com/using-the-cli/usage) describes. Find code
incompatibilities with the search below and by running the test suite on Lucee.

**Manual Code Search:**

Search for these patterns:

| Pattern | Files Found | Issue Type |
|---------|-----------|------------|
| `cfpdf` | | Extension needed |
| `cfchart` | | Extension needed |
| `cfexchange` | | No equivalent |
| `getPageContext()` | | Adobe only |
| `createObject("java", "...")` | | Check compatibility |
| `sessionstorage="mysql"` | | Lucee uses Redis |

### Part 2: Compatibility Matrix

Document each issue:

| Issue | Location | Severity | Lucee Behavior | Fix Required |
|-------|----------|----------|-----------------|--------------|
| cfpdf usage | orders.cfm | High | Not supported | Install PDF extension |
| | | | | |

### Part 3: Extension Audit

| ACF Extension | Used? | Replacement Available | Migration Effort |
|---------------|-------|----------------------|-----------------|
| cfpdf | | | |
| cfchart | | | |
| cfexchange | | | |
| cfsolr | | | |
| cfpresentation | | | |
| cfpdfcrypt | | | |

### Part 4: Function Compatibility Check

Check these functions:

| Function | Adobe CF | Lucee | Action Required |
|----------|----------|-------|-----------------|
| `getBaseTemplatePath()` | Yes | Yes | None |
| `imageResize()` | | | |
| `querySim()` | | | |
| `spreadsheet` functions | | | |
| `isJson()` | | | |
| `deserializeJSON()` | | | |

### Part 5: Summary Report

Complete the compatibility summary:

**Summary:**

| Category | Issues Found | High Severity | Medium | Low |
|----------|-------------|---------------|--------|-----|
| Extensions | | | | |
| Functions | | | | |
| Tags | | | | |
| Configuration | | | | |
| **Total** | | | | |

**Estimated Migration Effort:** ___ hours

**Critical Blockers:**

1. ___________________________________________________
2. ___________________________________________________

## Expected Outcome

1. Completed compatibility scan
2. Issue matrix with severity
3. Extension replacement plan
4. Summary report

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Automated scanning attempted | 15 |
| Manual review thorough | 20 |
| Issue matrix complete | 25 |
| Extension plan realistic | 20 |
| Summary accurate | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
