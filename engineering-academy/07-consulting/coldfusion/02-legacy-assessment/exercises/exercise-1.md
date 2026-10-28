# Exercise 1: Framework Detection

> Identify the ColdFusion framework in use from application code.

## Objective

Learn to quickly identify ColdFusion frameworks by examining application code and structure.

## Prerequisites

- Access to sample ColdFusion applications (provided or known)
- Understanding of CFML frameworks

## Instructions

### Part 1: Identify Framework by File Structure

Examine these directory structures and identify the framework:

**Application A:**
```
/app
  /handlers
    /user.cfc
    /order.cfc
  /models
  /views
    /user
    /order
  /layouts
  /Application.cfc
```

Framework: ___________________________
Evidence: ___________________________

**Application B:**
```
/app
  /model
  /view
  /controller
  Application.cfc
```

Framework: ___________________________
Evidence: ___________________________

**Application C:**
```
/app
  /cfc
  /cfm
  /udf
  application.cfm
```

Framework: ___________________________
Evidence: ___________________________

**Application D:**
```
/app
  /modules
  /config
  /coldbox
  /handlers
  /models
  Application.cfc
```

Framework: ___________________________
Evidence: ___________________________

### Part 2: Identify Framework by Application.cfc

Examine these Application.cfc snippets:

**Snippet A:**
```cfml
component {
    variables.framework = {
        routes: [...]
    };
    
    function setupApplication() {
        new app.services.framework();
    }
}
```

Framework: ___________________________
Evidence: ___________________________

**Snippet B:**
```cfml
component extends="coldbox.system.Coldbox" {
    
    function configurationLoad(required any config) {
        super.configurationLoad(arguments.config);
    }
}
```

Framework: ___________________________
Evidence: ___________________________

**Snippet C:**
```cfml
<cfcomponent>
    <cfset this.name = "MyApp">
    <cfinclude template="application.cfm">
</cfcomponent>
```

Framework: ___________________________
Evidence: ___________________________

### Part 3: Identify Framework by Code Patterns

For each pattern, identify the framework:

| Pattern | Framework |
|---------|-----------|
| `application.serviceLocator.getModel("UserService")` | |
| `ormReload()` | |
| `fw.action("user.save")` | |
| `new Handler(event,rc,prc)` | |
| `$.fn.myFunction()` | |
| `getPlugin("Logger")` | |

### Part 4: Create Detection Script

Write a CFML script that automatically detects frameworks:

```cfml
// Detect which framework is in use
component {
    
    public struct function detectFramework() {
        local.result = {
            framework: "none",
            confidence: 0,
            evidence: []
        };
        
        // Check for ColdBox indicators
        if (fileExistsExpandPath("/coldbox/system/Application.cfc")) {
            // Add detection logic
        }
        
        // Check for FW/1 indicators
        // ...
        
        // Check for plain CFM
        // ...
        
        return local.result;
    }
    
}
```

Complete the detection logic for:

1. ColdBox: What files or patterns to check?
2. FW/1: What files or patterns to check?
3. Plain CFM: What patterns indicate no framework?

### Part 5: Framework Compatibility Quick Reference

Create a reference table:

| Framework | Migration Difficulty | Key Indicators | Lucee Compatible? |
|-----------|---------------------|----------------|-------------------|
| FW/1 | | | |
| ColdBox | | | |
| Fusebox | | | |
| Plain CFM | | | |
| Custom MVC | | | |

## Expected Outcome

1. Completed framework identification exercises
2. Working framework detection script
3. Quick reference compatibility table

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Correct framework identification | 40 |
| Detection script logic | 25 |
| Compatibility reference accurate | 25 |
| Professional presentation | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
