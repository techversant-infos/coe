# Exercise 4: JVM & Memory Tuning

> Tune JVM settings for a production ColdFusion server.

## Objective

Learn to analyze and tune JVM settings for ColdFusion.

## Scenario

**Server:** 16GB RAM, ColdFusion 2023
**Issue:** Slow response times, occasional OutOfMemory errors

## Instructions

### Part 1: Current Configuration Analysis

Current JVM arguments:

```bash
-Xms512m
-Xmx2048m
-XX:+UseParallelGC
-XX:MaxPermSize=256m
```

**Issues Found:**

| Argument | Issue | Impact |
|----------|-------|--------|
| -Xms512m | Too small | Frequent GC |
| -Xmx2048m | Low for 16GB server | Underutilized RAM |
| -XX:MaxPermSize | Deprecated | Ignored in Java 8+ |
| UseParallelGC | Old collector | Long pause times |

### Part 2: Calculate Appropriate Settings

**Server Resources:**
- Total RAM: 16GB
- OS + other services: 2GB
- Available for CF: 14GB

**Recommendation:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| -Xms | | |
| -Xmx | | |
| NewSize | | |
| MaxNewSize | | |

### Part 3: Create New Configuration

Write the recommended JVM arguments:

```bash
# Heap sizing (use 50% of available RAM)
-Xms____m
-Xmx____m

# G1GC (better for latency)
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:G1HeapRegionSize=8m
-XX:InitiatingHeapOccupancyPercent=45

# Metaspace (replacement for PermGen)
-XX:MaxMetaspaceSize=512m

# GC Logging
-Xlog:gc*:file=gc.log:time,uptime:filecount=5,filesize=10M

# String deduplication (reduces memory)
-XX:+UseStringDeduplication

# Other recommendations:
_______________________________________________________________
```

### Part 4: Monitoring Plan

Set up monitoring for these metrics:

| Metric | Warning | Critical | Tool |
|--------|---------|----------|------|
| Heap usage | 70% | 85% | |
| Full GC frequency | | | |
| Old gen usage | | | |
| Metaspace usage | | | |
| Thread count | | | |

### Part 5: GC Log Analysis

Analyze this GC log excerpt:

```
2024-01-15T10:23:45.123+0000: 1234.567: [GC pause (G1 Evacuation Pause) 
young
2024-01-15T10:23:45.234+0000: 1234.678: [SoftReference, 0 refs, 
0.0000000 secs]2024-01-15T10:23:45.234+0000: 1234.678: [Code 
Blobs]
```

**Interpretation:**

| Finding | Assessment |
|---------|------------|
| GC Type | |
| Duration | |
| Health Status | |
