# Exercise 2: Caching Strategy Implementation

> Implement multi-level caching for a product catalog.

## Objective

Learn to implement caching at query, application, and distributed levels.

## Scenario

**Application:** E-commerce product catalog
**Issue:** Database load from repeated queries
**Goal:** 90% cache hit rate

## Instructions

### Part 1: Identify Cacheable Data

| Data | Cacheable? | Cache Type | TTL | Invalidation |
|------|-----------|------------|-----|--------------|
| Product list | | | | |
| Product details | | | | |
| Categories | | | | |
| Featured products | | | | |
| User cart | | | | |
| Session data | | | | |

### Part 2: Implement Query Caching

```cfml
public array function getFeaturedProducts() {
    
    // Check if data is cached
    if (application.cacheManager.has("featuredProducts")) {
        return application.cacheManager.get("featuredProducts");
    }
    
    // Query database
    local.products = queryExecute(
        "SELECT id, name, price, image 
         FROM products 
         WHERE featured = 1 
         AND active = 1
         ORDER BY name"
    );
    
    local.result = [];
    for (local.row in local.products) {
        local.result.append(local.row);
    }
    
    // Cache for 15 minutes
    application.cacheManager.set(
        "featuredProducts",
        local.result,
        900 // 15 minutes in seconds
    );
    
    return local.result;
}
```

### Part 3: Implement Redis Caching

```cfml
public struct function getProduct(required numeric id) {
    
    local.cacheKey = "product:#arguments.id#";
    
    // Try Redis cache first
    local.cached = redis.get(local.cacheKey);
    
    if (!isNull(local.cached)) {
        return deserializeJSON(local.cached);
    }
    
    // Query database
    local.product = queryExecute(
        "SELECT * FROM products WHERE id = ?",
        [arguments.id]
    );
    
    if (local.product.recordCount == 0) {
        return {};
    }
    
    local.result = local.product.toQueryObject()[1];
    
    // Store in Redis with 1 hour TTL
    redis.setex(local.cacheKey, 3600, serializeJSON(local.result));
    
    return local.result;
}
```

### Part 4: Cache Invalidation

Design cache invalidation strategy:

```cfml
public void function invalidateProduct(required numeric id) {
    
    // Invalidate specific product
    redis.del("product:#arguments.id#");
    
    // Invalidate list caches that include this product
    redis.del("featuredProducts");
    redis.del("category:#getProduct(arguments.id).category_id#_products");
    
    // Broadcast to other instances (if clustered)
    application.messageQueue.publish("productUpdated", {id: arguments.id});
}

public void function onProductUpdate(event, productId) {
    // Handle cache invalidation from message queue
    invalidateProduct(arguments.productId);
}
```

### Part 5: Measure Results

Document cache performance:

| Metric | Before | After |
|--------|--------|-------|
| Cache hit rate | 0% | |
| Avg query time | 250ms | |
| Page load time | 2.5s | |
| DB load | 100 RPS | |
