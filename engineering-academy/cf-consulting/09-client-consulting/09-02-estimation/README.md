# Module 9-02: Estimation

> Learn to size and estimate ColdFusion projects accurately.

## Overview

Accurate estimates build trust. Inaccurate estimates destroy it. This module teaches developers to estimate ColdFusion modernization projects with appropriate confidence levels and risk buffers.

> **Generic Foundation:** Planned: General Estimation Guide — this module adds CF-specific complexity factors and benchmarks.

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Break down CF modernization projects into work packages
- [ ] Apply CF-specific complexity factors
- [ ] Use three-point estimation (optimistic, likely, pessimistic)
- [ ] Add appropriate risk buffers
- [ ] Document assumptions and dependencies
- [ ] Present estimates with confidence levels
- [ ] Handle scope change gracefully

## ColdFusion Complexity Factors

### Application Factors

| Factor | Low Complexity | Medium Complexity | High Complexity |
|--------|---------------|-------------------|-----------------|
| **Size** | < 50 CFM files | 50-500 CFM files | > 500 CFM files |
| **Framework** | Modern framework (FW/1, ColdBox) | Light framework or custom MVC | Plain CFM with includes |
| **Database** | 1-10 tables | 10-50 tables | > 50 tables |
| **ORM** | No ORM or simple | Light ORM usage | Heavy ORM with relationships |
| **Custom Tags** | None | Few | Many custom tag dependencies |
| **Integrations** | None | 1-3 APIs | > 3 integrations |
| **Security** | Standard auth | Custom auth | Complex multi-tenant auth |

### Technical Factors

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| **Framework Age** | Recent (< 5 years) | Mid-age (5-10 years) | Legacy (> 10 years) |
| **CF Version** | CF2021+ | CF2018 or Lucee | CF10 or earlier |
| **Code Quality** | Well-documented, tested | Some documentation | Minimal docs, no tests |
| **Dependencies** | Standard libs | Some external libs | Many external dependencies |
| **Deployment** | CI/CD in place | Manual deploys | Complex multi-server |

### Business Factors

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| **Change Tolerance** | High flexibility | Moderate | Strict |
| **Uptime Required** | Business hours | Extended hours | 24/7 |
| **Data Sensitivity** | Public | Internal | Regulated (PCI, HIPAA) |
| **Stakeholder Support** | Strong | Moderate | Weak |

## ColdFusion Estimation Benchmarks

### Migration Effort (hours per 100 CFM files)

| Migration Type | Low | Medium | High |
|---------------|-----|--------|------|
| CF Version Upgrade | 4 | 8 | 16 |
| CF → Lucee | 8 | 16 | 32 |
| Framework Upgrade | 12 | 24 | 48 |
| Cloud Migration | 16 | 32 | 64 |
| UI Modernization | 8 | 16 | 32 |
| Full Rewrite | 40 | 80 | 160 |

### Refactoring Complexity Multipliers

| Pattern | Multiplier | Example |
|---------|------------|---------|
| Plain CFM → Component | 1.5x | More structured code |
| Custom auth → Framework auth | 2.0x | Security reimplementation |
| Include chains → Components | 2.5x | Structural refactor |
| Monolith → Services | 3.0x | Architecture change |
| No tests → Test coverage | 1.5x | Quality improvement |

### CF-Specific Effort Estimates

| Task | Hours (Typical Range) |
|------|---------------------|
| CF assessment (1 week) | 20-40 |
| CF → Lucee migration (small app, < 50 files) | 40-80 |
| CF → Lucee migration (medium app, 50-200 files) | 80-200 |
| CF → Lucee migration (large app, 200+ files) | 200-500 |
| CF upgrade (any version) | 16-80 |
| Performance optimization (per page) | 4-16 |
| Security audit (small app) | 16-40 |
| Security audit (medium app) | 40-80 |
| UI modernization (per form) | 8-24 |
| API creation (per endpoint) | 4-12 |

## Work Breakdown Structure (WBS) Template

```
CF Modernization Project
├── 1. Assessment & Discovery
│   ├── 1.1 Requirements gathering
│   ├── 1.2 Technical assessment
│   ├── 1.3 Risk analysis
│   └── 1.4 Estimation
│
├── 2. Environment Setup
│   ├── 2.1 Development environment
│   ├── 2.2 Staging environment
│   ├── 2.3 CI/CD pipeline
│   └── 2.4 Monitoring
│
├── 3. Core Migration
│   ├── 3.1 Authentication refactor
│   ├── 3.2 Database layer
│   ├── 3.3 Business logic components
│   ├── 3.4 API endpoints
│   └── 3.5 Error handling
│
├── 4. UI Modernization
│   ├── 4.1 Layout framework
│   ├── 4.2 Component conversion
│   ├── 4.3 Responsive design
│   └── 4.4 Accessibility
│
├── 5. Integration
│   ├── 5.1 External APIs
│   ├── 5.2 Background tasks
│   └── 5.3 Third-party services
│
├── 6. Testing & QA
│   ├── 6.1 Unit tests
│   ├── 6.2 Integration tests
│   ├── 6.3 UAT support
│   └── 6.4 Performance testing
│
└── 7. Deployment & Handover
    ├── 7.1 Production deployment
    ├── 7.2 Documentation
    ├── 7.3 Training
    └── 7.4 Support period
```

## Three-Point Estimation Example

```javascript
// Task: Migrate user authentication to Lucee

// Optimistic (O): Everything works, no issues
hours_optimistic = 24;

// Most Likely (M): Some compatibility issues, minor fixes
hours_likely = 40;

// Pessimistic (P): Major compatibility issues, rollback needed
hours_pessimistic = 80;

// PERT estimate
hours_pert = (O + (4 * M) + P) / 6;
// = (24 + (4 * 40) + 80) / 6 = 48 hours

// Standard deviation (confidence indicator)
std_dev = (P - O) / 6;
// = (80 - 24) / 6 = 9.3 hours

// Range: 48 ± 9 hours (39 to 57 hours likely)
```

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: WBS Creation](./exercises/exercise-1.md) | Break down a CF project | Complete WBS document |
| [Exercise 2: Three-Point Estimation](./exercises/exercise-2.md) | Apply PERT to a scenario | Estimate with confidence range |
| [Exercise 3: Client Presentation](./exercises/exercise-3.md) | Present estimate to client | Clear, confident delivery |
| [Exercise 4: Scope Change](./exercises/exercise-4.md) | Handle scope creep | Scope change impact analysis |

## Assessment

Complete all exercises and pass the module assessment with 70% or higher.

## Resources

- Planned: General Estimation Guide
- [CF Migration Benchmarks](../../DELIVERABLES/estimation-templates/cf-migration-benchmarks.md)
- [WBS Template](../../DELIVERABLES/estimation-templates/wbs-template.md)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 4 |
| Exercises | 4 |
| Assessment | 1 |
| **Total** | **9 hours** |

## Success Criteria

A developer completing this module should be able to:

1. Create a complete WBS for a CF project in 1 hour
2. Estimate a small migration with ± 20% accuracy
3. Present estimates with clear assumptions and confidence levels
4. Handle scope changes without panic

## Next Module

[Module 9-03: Presentation](../09-03-presentation/) — Learn to deliver effective presentations.
