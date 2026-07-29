# Phase 8 Assessment: Performance Engineering

> Test your performance optimization knowledge.

**Time:** 1.5 hours | **Passing:** 70%

---

## Section A: Profiling (25 points)

### A1: Identify Bottlenecks (15 points)

Analyze this request timeline:

| Step | Duration | % of Total | Status |
|------|----------|------------|--------|
| Application init | 500ms | 10% | |
| DB Query 1 | 2000ms | 40% | |
| DB Query 2 | 1000ms | 20% | |
| External API | 1500ms | 30% | |
| **Total** | 5000ms | 100% | |

**Top bottleneck:** _______________________________________

**Recommendation:** _____________________________________

### A2: Profiling Tool Selection (10 points)

Match the tool to the use case:

| Use Case | Tool |
|----------|------|
| Database query analysis | |
| JVM memory analysis | |
| HTTP request timing | |
| CF request debugging | |
| Front-end performance | |

---

## Section B: Caching (25 points)

### B1: Cache Strategy (15 points)

For each scenario, recommend the cache type:

| Scenario | Cache Type | TTL | Why |
|----------|------------|-----|-----|
| Product list | | | |
| User profile | | | |
| Session data | | | |
| API response | | | |
| Search results | | | |

### B2: Cache Implementation (10 points)

What's wrong with this cache code?

```cfml
// Cache user data indefinitely
application.userCache = {};
application.userCache[userId] = userData;
```

**Issues:**
1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

---

## Section C: Database Optimization (25 points)

### C1: N+1 Query Detection (15 points)

How many queries does this code execute if there are 100 orders?

```cfml
<cfquery name="orders">
    SELECT * FROM orders WHERE status = 'pending'
</cfquery>

<cfloop query="orders">
    <cfquery name="customer">
        SELECT * FROM customers WHERE id = #orders.customer_id#
    </cfquery>
    <cfquery name="items">
        SELECT * FROM order_items WHERE order_id = #orders.id#
    </cfquery>
</cfloop>
```

**Query count:** _______________________________________

**How to fix:** _______________________________________

### C2: Index Recommendations (10 points)

Given this query:

```sql
SELECT * FROM orders 
WHERE customer_id = ? 
AND order_date >= ? 
ORDER BY order_date DESC
```

**What indexes do you recommend?**

| Index | Columns | Type |
|-------|---------|------|
| 1 | | |
| 2 | | |

---

## Section D: JVM Tuning (25 points)

### D1: Memory Sizing (15 points)

For a server with 32GB RAM:

| Setting | Value | Rationale |
|---------|-------|-----------|
| -Xms | | |
| -Xmx | | |
| -XX:NewRatio | | |
| -XX:MaxMetaspaceSize | | |

### D2: GC Selection (10 points)

When would you choose G1GC over ZGC?

| Factor | G1GC | ZGC |
|--------|------|-----|
| Heap size | | |
| Pause time | | |
| Throughput | | |
| Complexity | | |
| Java version | | |
