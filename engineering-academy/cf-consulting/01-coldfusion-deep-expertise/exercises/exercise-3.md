# Exercise 3: Multi-Level Caching Implementation

> Implement caching at multiple levels to achieve >80% cache hit rate.

## Objective

Learn to implement caching at different levels (query, application, distributed) and measure the impact.

## Prerequisites

- ColdFusion server
- Database with at least 10,000 rows for testing
- Redis or Memcached (optional, for distributed caching)
- Performance measurement tool

## Instructions

### Part 1: Identify Caching Opportunities

For the given application scenario, identify caching opportunities:

**Scenario:** You have a product catalog application with:
- Product list page (shows 50 products)
- Product detail page (shows single product)
- Category listing (shows products by category)
- Homepage (shows featured products)
- Header/navigation (shows categories)

Analyze each page:

| Page | Cacheable? | Cache Type | TTL | Why |
|------|-----------|------------|-----|-----|
| Product list | | | | |
| Product detail | | | | |
| Category listing | | | | |
| Homepage | | | | |
| Header/nav | | | | |

### Part 2: Implement Query Caching

1. Create a query that retrieves products
2. Measure execution time without caching
3. Implement `cachedWithin` caching:

```cfml
// Without caching
<cfquery name="products">
    SELECT * FROM products ORDER BY name
</cfquery>

// With caching (5 minute TTL)
<cfquery name="products" cachedWithin="#createTimeSpan(0,0,5,0)#">
    SELECT * FROM products ORDER BY name
</cfquery>
```

4. Measure and compare:
   - First execution time
   - Subsequent execution times
   - Cache hit behavior

### Part 3: Implement Application Scope Caching

1. Create a caching service component:

```cfml
component {
    
    public any function getCachedData(required string key, any factory) {
        // Check cache first
        if (structKeyExists(application.cache, arguments.key)) {
            return application.cache[arguments.key];
        }
        
        // Factory creates the data
        local.data = arguments.factory();
        
        // Store in cache
        application.cache[arguments.key] = local.data;
        
        return local.data;
    }
    
    public void function clearCache(required string key) {
        structDelete(application.cache, arguments.key);
    }
    
    public void function clearAllCache() {
        application.cache = {};
    }
}
```

2. Use it to cache expensive operations

3. Implement cache invalidation:
   - Time-based expiration
   - Manual invalidation
   - Event-based invalidation

### Part 4: Implement Distributed Caching (Optional)

If Redis is available:

```cfml
component {
    
    remote any function getCachedData(string key) {
        local.result = redis.get(arguments.key);
        if (isNull(local.result)) {
            return false;
        }
        return deserializeJSON(local.result);
    }
    
    remote void function setCachedData(string key, any data, numeric ttl=3600) {
        redis.setex(arguments.key, arguments.ttl, serializeJSON(arguments.data));
    }
}
```

### Part 5: Measure Cache Effectiveness

Create a measurement dashboard:

| Metric | Before Cache | After Cache | Improvement |
|--------|-------------|-------------|-------------|
| Avg Response (ms) | | | |
| P95 Response (ms) | | | |
| Database Queries/page | | | |
| Cache Hit Rate | N/A | | |

Calculate cache hit rate:

```
Cache Hit Rate = (Cache Hits) / (Cache Hits + Cache Misses) × 100
```

### Part 6: Implement Cache Warming

Create a cache warming mechanism:

```cfml
// On application start
void function onApplicationStart() {
    application.cacheService = new cacheService();
    
    // Warm critical caches
    application.cacheService.warmCache([
        { key: 'featured_products', factory: getFeaturedProducts },
        { key: 'categories', factory: getCategories },
        { key: 'config', factory: getConfig }
    ]);
}
```

## Expected Outcome

A caching implementation with:

1. **Caching Strategy Document** — What to cache where and why
2. **Working Code** — At least 3 levels of caching implemented
3. **Measurement Results** — Before/after performance comparison
4. **Cache Hit Rate** — Achieved >80% cache hit rate
5. **Invalidation Strategy** — How caches are cleared when data changes

## Caching Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Cache everything | Wasted memory | Cache expensive operations only |
| No expiration | Stale data | Set appropriate TTLs |
| No invalidation | Data inconsistency | Implement event-based clearing |
| Huge objects | Memory pressure | Cache small, frequently accessed data |
| No monitoring | Unknown cache health | Monitor hit rates |

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Caching opportunities identified | 15 |
| Query caching implemented | 20 |
| Application caching implemented | 20 |
| Cache invalidation implemented | 15 |
| Metrics measured | 20 |
| Cache hit rate achieved (>80%) | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
