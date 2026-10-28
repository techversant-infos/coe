# CF Migration Effort Benchmarks

> Reference data for estimating ColdFusion modernization projects.

## Purpose

These benchmarks provide baseline estimates for common ColdFusion tasks. Adjust based on specific project context.

## Complexity Levels

| Level | Criteria |
|-------|----------|
| **Low** | Well-structured code, modern framework, good docs, tests present, expert team |
| **Medium** | Some technical debt, legacy framework, partial docs, no tests, experienced team |
| **High** | Poor code quality, no framework, no docs, no tests, learning team |

---

## Assessment Phase

### Application Assessment

| App Size | Low Complexity | Medium Complexity | High Complexity |
|----------|---------------|-------------------|-----------------|
| Small (< 50 files) | 16 hours | 24 hours | 40 hours |
| Medium (50-200 files) | 32 hours | 48 hours | 80 hours |
| Large (200-500 files) | 64 hours | 96 hours | 160 hours |
| Enterprise (500+ files) | 120 hours | 180 hours | 300 hours |

**Includes:**
- Code review
- Architecture documentation
- Dependency mapping
- Risk identification
- Initial recommendations

---

## Migration Phase

### CF Version Upgrade

| From → To | Low | Medium | High |
|-----------|-----|--------|------|
| CF10 → CF2018 | 40 | 64 | 96 |
| CF10 → CF2021 | 56 | 88 | 128 |
| CF10 → CF2023 | 72 | 112 | 160 |
| CF2018 → CF2021 | 24 | 40 | 64 |
| CF2018 → CF2023 | 40 | 64 | 96 |
| CF2021 → CF2023 | 16 | 24 | 40 |

### CF → Lucee Migration

| App Size | Low | Medium | High |
|----------|---------------|-------------------|-----------------|
| Small (< 50 files) | 32 hours | 48 hours | 80 hours |
| Medium (50-200 files) | 80 hours | 120 hours | 200 hours |
| Large (200-500 files) | 160 hours | 240 hours | 400 hours |
| Enterprise (500+ files) | 320 hours | 480 hours | 800 hours |

**Includes:**
- Compatibility scanning
- Function replacement
- Extension migration
- Testing and validation

### Framework Migration

| Migration Type | Low | Medium | High |
|---------------|-----|--------|------|
| Plain CFM → FW/1 | 80 | 160 | 320 |
| Plain CFM → ColdBox | 120 | 240 | 480 |
| FW/1 → FW/1 (modern) | 40 | 80 | 120 |
| FW/1 → ColdBox | 80 | 160 | 240 |
| Fusebox → Modern | 80 | 160 | 320 |
| Custom MVC → Modern | 160 | 320 | 640 |

---

## UI Modernization

### Bootstrap Refresh

| Per Page | Low | Medium | High |
|----------|-----|--------|------|
| Simple form | 4 hours | 8 hours | 16 hours |
| Complex form | 8 hours | 16 hours | 24 hours |
| Data table | 8 hours | 16 hours | 32 hours |
| Dashboard | 16 hours | 24 hours | 40 hours |

### React/Vue Integration

| Per Page | Low | Medium | High |
|----------|-----|--------|------|
| Simple form | 12 hours | 20 hours | 32 hours |
| Complex form | 20 hours | 32 hours | 48 hours |
| Data table | 24 hours | 40 hours | 64 hours |
| Dashboard | 32 hours | 48 hours | 80 hours |

---

## Security Hardening

### Security Audit

| App Size | Low | Medium | High |
|----------|---------------|-------------------|-----------------|
| Small (< 50 files) | 16 hours | 24 hours | 40 hours |
| Medium (50-200 files) | 32 hours | 48 hours | 80 hours |
| Large (200-500 files) | 64 hours | 96 hours | 160 hours |

### Security Remediation

| Task | Hours |
|------|-------|
| SQL injection fixes (per query) | 1-2 |
| XSS fixes (per page) | 1-2 |
| Auth system refactor | 40-80 |
| Session hardening | 16-24 |
| CSRF implementation | 8-16 |
| Complete rewrite | 80-160 |

---

## Performance Optimization

### Per Page Optimization

| Optimization Type | Hours |
|-------------------|-------|
| Query optimization | 4-8 |
| Caching implementation | 8-16 |
| JVM tuning | 16-24 |
| Full page rebuild | 16-32 |

### System-Wide Optimization

| Task | Hours |
|------|-------|
| Connection pool tuning | 8-16 |
| Application caching strategy | 24-40 |
| CDN integration | 16-32 |
| Monitoring setup | 8-16 |

---

## API Development

### Per Endpoint

| Endpoint Type | Hours |
|---------------|-------|
| Simple GET | 2-4 |
| CRUD operations | 4-8 |
| Complex business logic | 8-16 |
| Third-party integration | 8-24 |

---

## Testing

### Test Coverage

| Type | Coverage Target | Hours per 100 files |
|------|-----------------|---------------------|
| Unit tests | 70% | 16-24 |
| Integration tests | 50% | 24-40 |
| E2E tests | 30% | 32-48 |

---

## Buffer Recommendations

| Phase | Buffer |
|-------|--------|
| Assessment | 10-15% |
| Migration | 15-25% |
| UI Modernization | 20-30% |
| Security | 15-25% |
| Performance | 20-30% |

---

## Example Estimate

**Project:** Medium app (100 files), Plain CFM → Lucee, Bootstrap UI

```
Assessment:              48 hours × 1.0    =   48 hours
Lucee Migration:       120 hours × 1.25  =  150 hours
Bootstrap UI (20 pages): 16 hours × 20 × 1.2 =  384 hours
Testing (partial):       16 hours × 1.0    =   32 hours
Deployment:               24 hours × 1.0    =   24 hours
                                    ─────────────
Total (rounded):                        =  640 hours

Range: 540-740 hours
```

---

## Notes for Use

1. **Start with benchmarks** — use these as starting points
2. **Adjust for context** — every project is different
3. **Add buffers** — unexpected issues always arise
4. **Document assumptions** — what you assumed in the estimate
5. **Validate with discovery** — adjust after client discovery
6. **Track actuals** — improve benchmarks with real data
