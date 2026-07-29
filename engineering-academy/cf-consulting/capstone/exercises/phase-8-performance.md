# Phase 8 Exercise: Performance Optimization

> Profile and optimize BlogCFC5.

---

## Scenario

BlogCFC5 is running slow. Client reports:
- Homepage takes 5+ seconds to load
- Search is unresponsive
- Admin panel is sluggish

---

## Exercise 8A: Profile the Homepage

Enable request debugging and measure:

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total page time | | < 2s | |
| DB queries | | < 10 | |
| Query time | | < 500ms | |
| Template render | | < 200ms | |

---

## Exercise 8B: Identify Bottlenecks

Analyze `client/index.cfm` and `entry.cfc`:

| Bottleneck | Location | Type | Impact |
|------------|----------|------|--------|
| Slow query | | | |
| Missing index | | | |
| No caching | | | |
| Large result set | | | |
| Include overhead | | | |

---

## Exercise 8C: Implement Caching

Add application-level caching to BlogCFC5:

**Where to cache:**

| Data | Cache Type | TTL | Why |
|------|-----------|-----|-----|
| Recent posts list | | | |
| Category list | | | |
| Recent comments | | | |
| User sessions | | | |
| RSS feed | | | |

**Code pattern:**

```cfml
// Before: query every request
<cfquery name="recentPosts">
    SELECT * FROM tblblogentries 
    ORDER BY created DESC 
    LIMIT 10
</cfquery>

// After: cache the result
<cfif NOT structKeyExists(application.cache, "recentPosts")>
    <cfquery name="rs">
        SELECT * FROM tblblogentries 
        ORDER BY created DESC 
        LIMIT 10
    </cfquery>
    <cfset application.cache.recentPosts = queryToArray(rs)>
    <cfset application.cache.recentPosts_expires = now() + 15/1440>
</cfif>
```

---

## Exercise 8D: Query Optimization

Analyze and optimize the search function (`client/search.cfm`):

**Current query:**
```sql
SELECT * FROM tblblogentries 
WHERE body LIKE '%#form.search#%' 
   OR title LIKE '%#form.search#%'
```

**Issues:**
1. _______________________
2. _______________________
3. _______________________

**Optimization:**
```sql
-- Your optimized query:
SELECT * FROM tblblogentries 
WHERE ________________________________________
```

---

## Exercise 8E: Performance Results

Document before/after improvements:

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Homepage load | 5.2s | | |
| Search response | 3.1s | | |
| Query count | 45 | | |
| DB time | 2.8s | | |

---

## Deliverable

Create a performance optimization report:

1. Profiling results
2. Issues found
3. Optimizations implemented
4. Measured improvements
