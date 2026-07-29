# Phase 4: Lucee Migration

> Execute safe, successful migrations from Adobe ColdFusion to Lucee.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Specialist Pathway |
| Best for | Lucee Specialist |
| Contribution level | Contributor → Lead |
| Take this when | You need to plan or execute a Lucee migration |
| Evidence of readiness | Completed migration plan or compatibility analysis |
| Next | [capstone/exercises/phase-4](../capstone/exercises/phase-4-lucee.md) for practice |

---

## Overview

## Overview

Lucee migration is the most common modernization path for cost-conscious clients. This phase covers everything from initial assessment through production deployment — the playbook your team will use on real engagements.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Assess application compatibility for Lucee migration
- [ ] Identify Adobe-specific functions and extensions that need replacement
- [ ] Plan a phased migration with rollback capability
- [ ] Execute migration with zero or minimal downtime
- [ ] Replace ACF-only extensions with Lucee equivalents
- [ ] Validate application behavior post-migration
- [ ] Handle Enginearden licensing and support

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/)
- [Phase 2: Legacy Assessment](../02-legacy-assessment/)
- Understanding of [Lucee vs Adobe differences](../resources/lucee-vs-adobe.md)

## Topics

### 1. Compatibility Assessment

**Functions that need replacement:**
- `cfschedule` differences
- `cfdocument` PDF handling
- `cfexchange` (Exchange connector)
- `cfpop`/`cfsmtp` variations
- `cfpdf` capabilities
- `cfimage` operations

**Extensions that need replacement:**
- PDF services
- Solr integration
- Exchange integration
- PDF forms (Acrobat integration)
- Exchange calendar

### 2. Migration Planning

- Environment setup (Lucee Server, Tomcat, CommandBox)
- Compatibility testing strategy
- Data migration considerations
- Session handling differences
- ORM Hibernate differences

### 3. Common Issues

**Railo Compatibility Layer:**
- Functions that worked in Railo but not Lucee
- Extension incompatibilities
- Performance differences

**Lucee-Specific Bugs:**
- Known issues and workarounds
- Version-specific quirks
- Memory management differences

### 4. Deployment Options

- CommandBox
- Docker containers
- Traditional Tomcat/Jetty deployment
- Clustering with Lucee Server

### 5. Extension Ecosystem

**Free alternatives:**
- PDFtk for PDF manipulation
- LibreOffice for document conversion
- Solr alternatives (Elasticsearch, Typesense)

**Commercial alternatives:**
- Enginearden supported extensions
- Third-party PDF services
- Cloud-based document services

### 6. Rollback Planning

- Blue-green deployment
- Feature flags
- Data rollback procedures
- Communication plan

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Compatibility Scan](./exercises/exercise-1.md) | Run automated compatibility check | List of issues with fix recommendations |
| [Exercise 2: Extension Replacement](./exercises/exercise-2.md) | Replace ACF-only feature | Working Lucee equivalent |
| [Exercise 3: Docker Migration](./exercises/exercise-3.md) | Containerize a CF app | Running container with Lucee |
| [Exercise 4: Full Migration](./exercises/exercise-4.md) | Migrate sample app end-to-end | Working app on Lucee with test results |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Deliverable

Document the migration process to contribute to the [CF → Lucee Migration Playbook](../DELIVERABLES/cf-lucee-migration-playbook.md).

## Resources

- [Lucee Documentation](https://docs.lucee.org/)
- [Lucee vs Adobe Reference](../resources/lucee-vs-adobe.md)
- [CommandBox Documentation](https://commandbox.ortusbooks.com/)
- [Enginearden Lucee](https://www.lucee.org/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 12 |
| Exercises | 10 |
| Assessment | 2 |
| **Total** | **24 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Assess any CF application for Lucee compatibility in 1 day
2. Identify all migration blockers before starting
3. Execute a migration with clear rollback capability
4. Replace ACF-only extensions with suitable alternatives

## Next Phase

[Phase 5: Cloud Migration](../05-cloud-migration/) — Learn to move ColdFusion to AWS/Azure.
