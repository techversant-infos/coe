# Lucee vs Adobe ColdFusion

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

> Quick reference comparing Lucee and Adobe ColdFusion for migration decisions.

---

## Overview

| Aspect | Adobe ColdFusion | Lucee |
|--------|------------------|-------|
| License | Commercial | LGPL 2.1 (open source) |
| Cost | ColdFusion 2025: yearly subscription only, no perpetual license | Free; optional paid support |
| Vendor | Adobe | Lucee Association Switzerland |
| Support | Adobe support | Community + commercial |
| Release cycle | A new major version about every two years (2016, 2018, 2021, 2023, 2025), with numbered updates | Long-term support and stable lines, with frequent patch releases |

---

## Key Differences

### Function Compatibility

| Function | Adobe CF | Lucee | Notes |
|----------|----------|-------|-------|
| `entityLoad()` | ✅ | ✅ | Full ORM support |
| `querySim()` | ✅ | ✅ | Test data generation |
| `imageRead()` | ✅ | ✅ | Image manipulation |
| `cfpdf` | ✅ | ⚠️ | Extension required |
| `cfdocument` | ✅ | ⚠️ | Extension required |
| `cfexchange` | ✅ | ❌ | Replace with REST |
| `createObject("java")` | ✅ | ✅ | Java integration |
| `sessionStorage` | ACF syntax | Redis syntax | |

### Tags

| Tag | Adobe CF | Lucee | Notes |
|-----|----------|-------|-------|
| `<cfchart>` | ✅ | ⚠️ | Extension for advanced |
| `<cfform>` | ✅ | ⚠️ | Basic only |
| `<cfgrid>` | ✅ | ⚠️ | Basic only |
| `<cfpdf>` | ✅ | ⚠️ | Extension required |
| `<cfdocument>` | ✅ | ⚠️ | Extension required |
| `<cfmediaplayer>` | ✅ | ❌ | Replace with HTML5 |

### Configuration

| Setting | Adobe CF | Lucee |
|---------|----------|-------|
| Datasource config | Admin UI | Admin UI |
| Session scope | `sessionstorage="mysql"` | `sessionstorage="redis"` |
| Application.cfc | ✅ | ✅ |
| ORM config | `this.ormsettings` | `this.ormsettings` |

---

## Migration Considerations

### When to Choose Lucee

✅ No budget for Adobe licensing
✅ Open-source preference
✅ Active community support acceptable
✅ Standard CFML features used
✅ Want latest language features

### When to Stay with Adobe

✅ Depend on `<cfpdf>`, `<cfdocument>` heavily
✅ Enterprise support contract required
✅ Legacy dependencies on ACF-specific features
✅ Team trained on Adobe-specific quirks
✅ Customer/vendor requires Adobe

---

## Common Migration Issues

### Issue 1: PDF Generation

**Problem:** `<cfpdf>` and `<cfdocument>` require Lucee extensions

**Solution:**

```cfml
// Install via Lucee Admin > Extensions > PDF
// Or use third-party: wkhtmltopdf, Prince XML
```

### Issue 2: Session Storage

**Adobe syntax:**

```cfm
<cfapplication sessionstorage="mysql" ...>
```

**Lucee syntax:**

```cfm
<cfapplication sessionstorage="redis" ...>
```

### Issue 3: Java Integration

Lucee may need different JAR paths:

```cfm
// Adobe
createObject("java", "path.to.Class");

// Lucee - may need absolute path
createObject("java", "/path/to/lib/Class");
```

---

## Quick Compatibility Check

Run this before migration:

```cfml
<!--- Check for problematic patterns --->
<cfset issues = []>

<!--- PDF usage --->
<cfif findnocase("<cfpdf", fileContents)>
    <cfset arrayAppend(issues, "cfpdf found - extension needed")>
</cfif>

<!--- Exchange usage --->
<cfif findnocase("<cfexchange", fileContents)>
    <cfset arrayAppend(issues, "cfexchange found - replace with REST")>
</cfif>

<!--- Output ---><cfdump var="#issues#">
```

---

## Resources

- [Lucee Documentation](https://docs.lucee.org/)
- [Lucee Extensions](https://download.lucee.org/)
- [CFML Reference](https://cfdocs.org/)
