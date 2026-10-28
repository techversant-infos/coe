# Exercise 2: JVM Tuning for ColdFusion

> Profile and tune JVM settings to improve ColdFusion performance.

## Objective

Learn to analyze JVM performance and apply tuning recommendations for ColdFusion workloads.

## Prerequisites

- ColdFusion server with access to JVM configuration
- JMX monitoring tool (VisualVM, JConsole, or similar)
- A test application with some load

## Instructions

### Part 1: Baseline Measurement

Before making any changes, capture the baseline:

1. **Memory Usage**
   - Current heap size (Xms and Xmx)
   - Monitor heap usage over 10 minutes
   - Note any Full GC events

2. **Garbage Collection**
   - Enable GC logging
   - Run for 5 minutes under normal load
   - Capture GC logs

3. **Thread Analysis**
   - Current thread count
   - Blocked threads
   - Thread dump (jstack)

4. **Response Times**
   - Average response time for test pages
   - P95 and P99 response times

Document your baseline:

| Metric | Value |
|--------|-------|
| Heap Size (Xms/Xmx) | |
| GC Algorithm | |
| Avg Response Time | |
| P95 Response Time | |
| Thread Count | |
| Full GC Frequency | |

### Part 2: JVM Argument Analysis

Review current JVM arguments and categorize each:

| Argument | Current Value | Purpose | Appropriate? |
|----------|--------------|---------|--------------|
| -Xms | | | |
| -Xmx | | | |
| -XX:+UseG1GC | | | |
| (add more rows as needed) | | | |

### Part 3: Apply Recommended Tuning

Based on your analysis, apply these standard ColdFusion tuning recommendations:

1. **Heap Sizing**
   ```
   -Xms2g
   -Xmx2g
   ```
   (Adjust based on server RAM — never more than 50-75% of available RAM)

2. **G1GC Configuration**
   ```
   -XX:+UseG1GC
   -XX:MaxGCPauseMillis=200
   -XX:G1HeapRegionSize=8m
   -XX:InitiatingHeapOccupancyPercent=45
   ```

3. **Memory and GC Logging**
   ```
   -Xlog:gc*:file=gc.log:time,uptime:filecount=5,filesize=10M
   ```

4. **ColdFusion-Specific**
   - Disable debugging in production
   - Set request timeout appropriately
   - Configure session timeout

### Part 4: Re-measure and Compare

After applying changes, repeat Part 1:

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Avg Response Time | | | |
| P95 Response Time | | | |
| Full GC Frequency | | | |
| Avg GC Pause | | | |
| Max GC Pause | | | |

## Expected Outcome

A tuning report containing:

1. **Before/After Metrics Table** — Clear comparison
2. **Changes Applied** — List of JVM arguments changed
3. **Analysis** — What improved, what didn't, why
4. **Recommendations** — Next steps if further tuning needed

## Common JVM Mistakes to Avoid

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| Setting Xms = Xmx | Can cause allocation issues | Set Xms smaller, let it grow |
| Too large heap | Causes long GC pauses | Keep under 50-75% RAM |
| Wrong GC algorithm | Suboptimal for CF workloads | Use G1GC for most cases |
| Not monitoring | No visibility | Always enable GC logging |
| Too small heap | Excessive GC | Monitor and increase if needed |

## Solution Template

```markdown
# JVM Tuning Report

## Before/After Comparison

[Metrics table from Part 4]

## Changes Applied

### Arguments Changed
| Argument | Before | After | Reason |
|----------|--------|-------|--------|

### Configuration Changes
[Additional config changes]

## Analysis

### What Improved
...

### What Didn't Change
...

### Unexpected Results
...

## Recommendations

### Immediate (Next Week)
1. ...

### Medium Term (Next Month)
1. ...

### Long Term (Next Quarter)
1. ...
```

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Baseline documented | 15 |
| Analysis of current settings | 15 |
| Appropriate changes applied | 25 |
| Re-measurement complete | 15 |
| Analysis demonstrates understanding | 20 |
| Professional presentation | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
