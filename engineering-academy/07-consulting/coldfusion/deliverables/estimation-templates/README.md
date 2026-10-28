# Estimation Templates

> Templates and benchmarks for sizing ColdFusion modernization projects.

## Files

| Template | Purpose |
|----------|---------|
| [cf-migration-benchmarks.md](./cf-migration-benchmarks.md) | Effort estimates for common CF tasks |
| [wbs-template.md](./wbs-template.md) | Work breakdown structure template |
| [estimate-sheet.md](./estimate-sheet.md) | Estimation worksheet |

---

## Quick Reference: CF Migration Benchmarks

### Hours per Task (Medium Complexity)

| Task | Hours | Notes |
|------|-------|-------|
| CF Assessment (small app, <50 files) | 20-40 | |
| CF Assessment (medium app, 50-200 files) | 40-80 | |
| CF Assessment (large app, 200+ files) | 80-160 | |
| CF Version Upgrade (minor) | 16-40 | Per major version |
| CF Version Upgrade (major) | 40-80 | |
| CF → Lucee (small app) | 40-80 | |
| CF → Lucee (medium app) | 80-200 | |
| CF → Lucee (large app) | 200-500 | |
| UI Modernization (Bootstrap, per page) | 8-24 | |
| UI Modernization (React, per page) | 16-40 | |
| Security Audit (small app) | 16-40 | |
| Security Audit (medium app) | 40-80 | |
| Performance Optimization (per page) | 4-16 | |

### Complexity Multipliers

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Code Quality | Well-structured | Some debt | High debt |
| Framework | Modern | Legacy | None/Custom |
| Documentation | Complete | Partial | None |
| Testing | Full | Partial | None |
| Team | Expert | Experienced | Learning |

**Multiply base hours by the appropriate multiplier based on complexity.**
