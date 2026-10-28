# Exercise 3: Roadmap Creation

> Create a phased modernization roadmap.

## Objective

Learn to plan and sequence modernization activities realistically.

## Scenario

**Client:** Metro Logistics
**Decision:** Migrate to Lucee + Cloud + UI Modernization
**Timeline:** 12-month project
**Team:** 3 CF developers + 1 Cloud engineer (shared)

## Instructions

### Part 1: Define Phases

Design a phased approach:

| Phase | Name | Duration | Goal |
|-------|------|----------|------|
| 0 | Discovery | 2 weeks | |
| 1 | Foundation | 4 weeks | |
| 2 | Core Migration | 8 weeks | |
| 3 | Cloud Migration | 6 weeks | |
| 4 | UI Modernization | 8 weeks | |
| 5 | Testing & Launch | 4 weeks | |
| | **Buffer** | 4 weeks | |
| | **Total** | **36 weeks** | |

### Part 2: Phase Details

**Phase 0: Discovery (Weeks 1-2)**

Activities:
- [ ] Automated compatibility scan
- [ ] Manual code review
- [ ] Database analysis
- [ ] Integration mapping
- [ ] Risk assessment

Deliverables:
- Compatibility report
- Risk register
- Baseline metrics

**Phase 1: Foundation (Weeks 3-6)**

Activities:
- [ ] Set up Lucee dev environment
- [ ] Configure CI/CD pipeline
- [ ] Set up monitoring
- [ ] Database replication to cloud
- [ ] Team training on Lucee

Deliverables:
- Working dev environment
- CI/CD pipeline
- Training complete

**Phase 2: Core Migration (Weeks 7-14)**

Activities:
- [ ] Migrate authentication
- [ ] Migrate business logic
- [ ] Migrate database layer
- [ ] Migrate integrations
- [ ] Regression testing

Deliverables:
- Core application on Lucee
- All tests passing
- Performance baseline

**Phase 3: Cloud Migration (Weeks 15-20)**

Activities:
- [ ] Provision cloud infrastructure
- [ ] Deploy to staging
- [ ] Configure load balancing
- [ ] Set up monitoring
- [ ] Security hardening

Deliverables:
- Cloud staging environment
- Performance optimized
- Security configured

### Part 3: Milestone Mapping

Create a milestone timeline:

| Milestone | Target Date | Dependencies | Owner |
|-----------|-------------|--------------|-------|
| M1: Discovery Complete | Week 2 | None | |
| M2: Dev Environment Ready | Week 4 | M1 | |
| M3: CI/CD Ready | Week 6 | M2 | |
| M4: Auth Migration | Week 8 | M3 | |
| M5: Core Logic Migrated | Week 12 | M4 | |
| M6: Cloud Staging Ready | Week 16 | M3 | |
| M7: UAT Start | Week 20 | M5, M6 | |
| M8: Go-Live | Week 32 | M7 | |

### Part 4: Resource Planning

| Role | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|------|---------|---------|---------|---------|---------|
| CF Dev 1 | 100% | 100% | 80% | 100% | 80% |
| CF Dev 2 | 50% | 100% | 80% | 100% | 80% |
| CF Dev 3 | 50% | 100% | 50% | 50% | 50% |
| Cloud Eng | 50% | 20% | 100% | 30% | 50% |
| QA | | 20% | 50% | 80% | 100% |

### Part 5: Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Compatibility issues found | Medium | High | 2-week buffer in Phase 2 |
| Team capacity issues | Medium | Medium | |
| Cloud cost overrun | Low | Medium | |
| Performance issues | Medium | High | Performance testing in Phase 3 |
| | | | |

### Part 6: Communication Plan

| Audience | Frequency | Content | Owner |
|----------|-----------|---------|-------|
| Steering Committee | Monthly | Milestone status, risks | PM |
| Technical Team | Weekly | Sprint review, blockers | Tech Lead |
| Business Users | Bi-weekly | Demo, feedback | BA |
| Executive | Monthly | Executive dashboard | PM |

## Expected Outcome

1. Complete phased roadmap
2. Milestone timeline
3. Resource allocation
4. Risk register
5. Communication plan

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Phases logically sequenced | 20 |
| Milestones realistic | 20 |
| Dependencies identified | 15 |
| Risks addressed | 15 |
| Resources allocated | 15 |
| Professional presentation | 15 |
| **Total** | **100** |

**Passing Score:** 70/100
