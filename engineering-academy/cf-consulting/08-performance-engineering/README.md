# Phase 8: Performance Engineering

> Master ColdFusion performance diagnosis and optimization.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Specialist Pathway |
| Best for | Performance Specialist |
| Contribution level | Contributor → Lead |
| Take this when | You need to diagnose or optimize a slow ColdFusion application |
| Evidence of readiness | Completed performance analysis with before/after metrics |
| Next | [capstone/exercises/phase-8](../capstone/exercises/phase-8-performance.md) for practice |

---

## Overview

## Overview

Performance issues are a primary driver of modernization projects. This phase covers deep performance engineering for ColdFusion — from identifying bottlenecks to implementing solutions.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Profile ColdFusion applications to identify bottlenecks
- [ ] Analyze and optimize slow database queries
- [ ] Implement multi-level caching strategies
- [ ] Tune JVM settings for ColdFusion workloads
- [ ] Optimize memory usage and garbage collection
- [ ] Reduce HTTP overhead and latency
- [ ] Implement connection pooling
- [ ] Create performance benchmarks and monitoring

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/)
- Understanding of database performance concepts

## Topics

### 1. Performance Profiling

**Tools:**
- FusionReactor
- SeeFusion
- ColdFusion Administrator diagnostics
- Chrome DevTools (for front-end)
- Query analyzers

**Techniques:**
- Request timeline analysis
- Slow query identification
- Memory allocation tracking
- Thread analysis
- I/O profiling

### 2. Database Optimization

**Query Analysis:**
- EXPLAIN plans
- Index usage
- Query plan reading
- N+1 query detection

**Optimization Patterns:**
```cfml
// BAD: N+1 queries
for (user in users) {
    user.role = queryExecute("SELECT role FROM users WHERE id = ?", [user.id]);
}

// GOOD: Single query with JOIN
result = queryExecute("SELECT u.*, r.role 
    FROM users u 
    LEFT JOIN roles r ON u.role_id = r.id");
```

**Connection Pooling:**
- Pool sizing
- Connection validation
- Timeout configuration
- Leak prevention

### 3. Caching Strategies

**CF Caching:**
- `<cfcache>` variations
- CacheExecute
- CachePut/CacheGet
- Application variable caching

**Distributed Caching:**
- Redis
- Memcached
- Ehcache
- Hazelcast

**HTTP Caching:**
- Browser caching
- CDN configuration
- ETags and last-modified
- Cache-Control headers

### 4. JVM Tuning for ColdFusion

**Heap Sizing:**
- Young vs old generation
- Sizing guidelines
- Monitoring heap usage

**Garbage Collection:**
- GC algorithm selection
- G1GC vs ZGC
- GC logging
- Tuning parameters

**Threading:**
- Request thread pool
- Session thread pool
- Background task threads

### 5. Memory Optimization

**Common Issues:**
- Large session scope
- Application scope leaks
- Query result caching
- File upload handling

**Best Practices:**
```cfml
// Limit query results
queryExecute("SELECT * FROM large_table LIMIT 1000", {}, {maxRows=1000});

// Clear large objects
structDelete(application, 'largeData');

// Use lazy loading
```

### 6. HTTP Optimization

- Connection reuse
- Compression (gzip/deflate)
- Keep-alive settings
- SSL/TLS overhead
- External resource optimization

### 7. ColdFusion-Specific Tuning

**Request Management:**
- Request timeout configuration
- Simultaneous request limits
- Orphaned request handling

**Session Performance:**
- Session scope size
- Cluster session replication
- Session persistence

**ORM Optimization:**
- Hibernate query caching
- Lazy loading
- Batch size configuration
- Second-level cache

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Profiling](./exercises/exercise-1.md) | Profile a slow application | Bottleneck identification |
| [Exercise 2: Query Optimization](./exercises/exercise-2.md) | Optimize slow queries | Measurable improvement |
| [Exercise 3: Caching Implementation](./exercises/exercise-3.md) | Multi-level caching | 50%+ response time improvement |
| [Exercise 4: JVM Tuning](./exercises/exercise-4.md) | Tune JVM parameters | Stable memory, reduced GC |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Resources

- [FusionReactor Documentation](https://www.fusion-reactor.com/documentation/)
- [JVM Performance Tuning Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/)
- [ColdFusion Performance Guide](https://helpx.adobe.com/coldfusion/developing-applications/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 10 |
| Exercises | 8 |
| Assessment | 2 |
| **Total** | **20 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Profile any ColdFusion application and identify bottlenecks
2. Optimize queries for measurable performance gains
3. Implement caching that improves response times by 50%+
4. Tune JVM settings for stable ColdFusion performance

## Next Phase

[Phase 9: Client Consulting](../09-client-consulting/) — Master the soft skills that win projects.
