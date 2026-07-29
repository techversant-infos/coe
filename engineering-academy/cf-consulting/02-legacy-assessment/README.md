# Phase 2: Legacy Application Assessment

> Learn to review, score, and report on existing ColdFusion applications for modernization engagements.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Consulting Core — Required |
| Best for | Technical Assessor, Modernization Architect, Client-Facing Lead |
| Contribution level | Contributor → Supported Lead |
| Take this when | You need to assess a legacy application for discovery or proposal |
| Evidence of readiness | Completed assessment report (sample or client) |
| Next | [03-modernization-strategy](../03-modernization-strategy/) or [capstone/exercises/phase-2](../capstone/exercises/phase-2-assessment.md) |

---

## Overview

## Overview

Every modernization engagement starts with understanding what exists. This phase teaches developers to conduct thorough assessments of legacy ColdFusion applications — the first step in any migration or upgrade project.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Identify the CF framework in use (FW/1, ColdBox, Fusebox, custom, plain CFM)
- [ ] Map the application architecture
- [ ] Assess technical debt across dimensions
- [ ] Identify security vulnerabilities
- [ ] Estimate performance bottlenecks
- [ ] Produce a professional assessment report
- [ ] Present findings to non-technical stakeholders

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/) completion
- Basic understanding of web application architecture

## Topics

### 1. Framework Detection

How to identify:
- Application.cfc vs Application.cfm
- FW/1 patterns (controllers, views, layouts)
- ColdBox patterns (wirebox, handlers, models)
- Fusebox patterns (fuseactions, circuits)
- Custom MVC implementations
- Plain CFM with includes
- Legacy frameworks (Mango, Mura, etc.)

### 2. Architecture Mapping

- Database schema analysis
- Application structure and naming conventions
- Integration points (APIs, web services, databases)
- Authentication and authorization patterns
- Session management approach
- File organization patterns

### 3. Technical Debt Assessment

Dimensions:
- Code quality (naming, complexity, documentation)
- Testing coverage
- Dependency management
- Configuration management
- Deployment automation
- Documentation completeness

### 4. Security Review

CF-specific vulnerabilities to check:
- SQL injection in cfquery
- XSS in cfoutput
- Deprecated cfform with flash
- Unsecured file uploads
- Session fixation
- Hardcoded credentials
- Exposed CFIDE
- Weak datasource configurations

### 5. Performance Profiling

- Identifying slow queries
- Missing indexes
- Inefficient cfinclude chains
- Memory-intensive operations
- External API dependencies
- Missing caching layers

### 6. Assessment Reporting

- Scoring methodology
- Risk classification
- Remediation prioritization
- Effort estimation
- Executive summary vs technical detail

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Framework Detection](./exercises/exercise-1.md) | Identify the framework in a sample app | Correct identification with evidence |
| [Exercise 2: Architecture Mapping](./exercises/exercise-2.md) | Create architecture diagram | Complete component map |
| [Exercise 3: Technical Debt Scoring](./exercises/exercise-3.md) | Score an application | Comprehensive debt report |
| [Exercise 4: Security Assessment](./exercises/exercise-4.md) | Find and document vulnerabilities | Security issues list with severity |
| [Exercise 5: Full Assessment Report](./exercises/exercise-5.md) | Complete assessment of sample app | Professional assessment document |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Deliverable

Produce a complete [Legacy Assessment Template](../DELIVERABLES/legacy-assessment-template.md) for a sample application.

## Resources

- [CF Code Review Checklist](../DELIVERABLES/cf-architecture-review-checklist.md)
- [OWASP Top 10](https://owasp.org/Top10/)
- [ColdFusion Security Guide](https://helpx.adobe.com/coldfusion/developing-applications/securing-applications.html)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 12 |
| Exercises | 8 |
| Assessment | 2 |
| **Total** | **22 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Conduct a complete application assessment in 1-2 days
2. Score technical debt consistently
3. Produce a report that drives modernization decisions
4. Present findings to technical and non-technical audiences

## Next Phase

[Phase 3: Modernization Strategy](../03-modernization-strategy/) — Learn to recommend the right modernization path.
