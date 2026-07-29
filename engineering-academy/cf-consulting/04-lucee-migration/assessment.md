# Phase 4 Assessment: Lucee Migration

> Test your Lucee migration knowledge and skills.

**Time:** 1.5 hours | **Passing:** 70%

---

## Section A: Compatibility (25 points)

### A1: Identify Issues (15 points)

For each Adobe CF feature, identify if it works in Lucee:

| Feature | Lucee Compatible? | Alternative |
|---------|-------------------|-------------|
| `cfpdf action="read"` | No | PDF extension or PDFtk |
| `cfchart` | | |
| `createObject("java", "ArrayList")` | | |
| `querySim()` | | |
| `spreadsheet_*` functions | | |
| `cfschedule` | | |

### A2: Migration Risk (10 points)

Rate migration risk for this app:

- CF 2018, 50 files, plain CFM
- Uses: cfpdf, cfchart, custom authentication
- MSSQL database

| Risk Factor | Risk Level | Mitigation |
|-------------|------------|------------|
| Extension dependencies | | |
| Plain CFM structure | | |
| Custom auth | | |
| **Overall Risk** | | |

---

## Section B: Extension Replacement (25 points)

### B1: PDF Migration (15 points)

Write Lucee-compatible code to read a PDF file:

```cfml
// Replace: <cfpdf action="read" source="doc.pdf" name="pdfDoc">

// Lucee solution:
_______________________________________________________________

_______________________________________________________________
```

### B2: Chart Migration (10 points)

How would you replace a cfchart in Lucee?

**Approach:**
_______________________________________________________________
**Tools:**
_______________________________________________________________
**Effort estimate:** _______________________________________

---

## Section C: Docker & Deployment (25 points)

### C1: Dockerfile (15 points)

Write a production-ready Dockerfile for Lucee:

```dockerfile
# Complete this Dockerfile

FROM ___________________________________

# Security best practices?

_______________________________________________________________

# How do you handle configuration?

_______________________________________________________________

EXPOSE 8080
CMD ___________________________________
```

### C2: Session Management (10 points)

How do you configure distributed sessions in Lucee?

| Setting | Value | Why |
|---------|-------|-----|
| Session storage | | |
| Redis config | | |
| Timeout | | |

---

## Section D: Troubleshooting (25 points)

### D1: Common Issues (15 points)

Match each issue with its cause and solution:

| Issue | Cause | Solution |
|-------|-------|----------|
| PDF generation fails | | |
| Session loss | | |
| Slow startup | | |
| cfquery error | | |
| Image resize broken | | |

### D2: Debug This Error (10 points)

**Error:** "Component method 'xxx' not found in application"

**Diagnosis:**
_______________________________________________________________

**Fix:**
_______________________________________________________________

---

## Answer Key

### Section A
- A1: Most Adobe CF functions have Lucee equivalents or need extensions
- A2: Medium risk overall; cfpdf/cfchart are main blockers

### Section B
- B1: Use PDF extension, PDFtk, or external service
- B2: ChartJS, Highcharts, or FusionCharts

### Section C
- C1: Multi-stage build, non-root user, secrets via env
- C2: Redis for distributed sessions

### Section D
- D1: PDF extension needed, Redis sessions, compile caching, parameter check, image extension
- D2: Function not defined or misspelled in CFC

---

## Scoring

| Section | Points |
|---------|--------|
| A: Compatibility | 25 |
| B: Extension Replacement | 25 |
| C: Docker | 25 |
| D: Troubleshooting | 25 |
| **Total** | **100** |

**Passing:** 70/100
