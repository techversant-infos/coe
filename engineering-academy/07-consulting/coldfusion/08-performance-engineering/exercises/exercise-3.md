# Exercise 3: Database Optimization

> Optimize slow database queries.

## Objective

Learn to analyze and optimize database performance.

## Scenario

**Application:** Reporting dashboard
**Issue:** Report generation takes 30+ seconds

## Instructions

### Part 1: Query Analysis

Analyze this reporting query:

```sql
SELECT 
    o.order_id,
    o.order_date,
    c.customer_name,
    c.customer_email,
    p.product_name,
    oi.quantity,
    oi.price,
    (oi.quantity * oi.price) as line_total,
    s.ship_date,
    s.tracking_number
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN shipments s ON o.order_id = s.order_id
WHERE o.order_date >= '2024-01-01'
ORDER BY o.order_date DESC
```

**Performance Issues:**

| Issue | Explanation |
|-------|------------|
| SELECT * | |
| Multiple JOINs | |
| No WHERE on indexed column | |
| ORDER BY on unindexed column | |
| No pagination | |

### Part 2: Create Optimized Query

```sql
-- Optimized version
SELECT 
    ___________________________________________________

FROM orders o
INNER JOIN ___________________________________________

WHERE o.order_date >= ?
___________________________________________________
```

### Part 3: Index Analysis

Current indexes on orders table:

| Column | Index Type | Unique | Purpose |
|--------|-----------|--------|---------|
| order_id | PRIMARY | Yes | PK |
| customer_id | | | |
| order_date | | | |
| status | | | |

**Missing Indexes:**

| Column(s) | Type | Purpose |
|-----------|------|---------|
| | | |

### Part 4: Query Plan Analysis

Using MSSQL:

```sql
SET SHOWPLAN_TEXT ON
GO
-- Run your query here
```

**Interpret the plan:**

| Operation | Cost | Recommendation |
|-----------|------|----------------|
| Table Scan on orders | 85% | Add index |
| | | |

---

## Expected Results

After optimization:
- Query time: 30+ seconds → < 2 seconds
- Index recommendations implemented
- Pagination added
