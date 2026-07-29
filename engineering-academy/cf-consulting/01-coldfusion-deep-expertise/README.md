# Phase 1: ColdFusion Deep Expertise

> Master ColdFusion internals to diagnose issues, optimize performance, and consult with authority.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Optional Diagnostic/Reinforcement |
| Best for | All pathways — foundational knowledge |
| Contribution level | Awareness → Contributor |
| Take this when | You need to refresh deep CF knowledge or diagnose unfamiliar issues |
| Evidence of readiness | Ability to explain request lifecycle, JVM interaction, caching |

---

## Overview

## Overview

This phase builds deep technical expertise in ColdFusion — the foundation for all consulting work. Developers move beyond writing code to understanding *why* ColdFusion behaves as it does, enabling confident diagnosis and recommendation.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Trace a CFML request from HTTP to response
- [ ] Explain how ColdFusion interacts with the JVM
- [ ] Configure and tune JVM settings for ColdFusion
- [ ] Implement advanced caching strategies
- [ ] Secure ColdFusion applications against common vulnerabilities
- [ ] Optimize database interactions and connection pooling
- [ ] Use built-in diagnostics and debugging tools
- [ ] Configure session management for clustered environments
- [ ] Implement REST APIs with proper error handling
- [ ] Use cfthread for parallel processing safely

## Prerequisites

- 5+ years ColdFusion development experience
- Basic understanding of HTTP
- Familiarity with at least one CF framework

## Topics

### 1. Request Lifecycle

- How CF handles HTTP requests
- Application.cfc vs Application.cfm
- Request lifecycle events (onRequestStart, onRequest, onRequestEnd)
- Custom tag execution order
- Include processing

### 2. JVM Internals

- How CF runs on the JVM
- Understanding heap, garbage collection
- JVM arguments for CF
- Reading stack traces
- Debugging with jstack, jmap

### 3. Performance Fundamentals

- Connection pooling configuration
- Query optimization
- Caching (variable, application, server, distributed)
- Profiling tools (FusionReactor, SeeFusion, ColdFusion Administrator)
- Slow request logging

### 4. Security Basics

- CF-specific SQL injection (cfqueryparam)
- XSS prevention (encodeForHTML, encodeForURL)
- CSRF protection
- Secure session management
- Password hashing (bcrypt, Argon2)
- Datasource security

### 5. Advanced CFML

- Component inheritance and composition
- ORM fundamentals (Hibernate under the hood)
- REST web services (cfrest, API Gateway)
- PDF generation and manipulation
- Scheduled tasks best practices
- WebSocket implementation

### 6. Debugging and Diagnostics

- CF Administrator diagnostics
- Request timeout debugging
- Memory leak identification
- Thread dump analysis
- Exception handling patterns

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Request Lifecycle Tracing](./exercises/exercise-1.md) | Debug a request through the lifecycle | Document the execution path |
| [Exercise 2: JVM Tuning](./exercises/exercise-2.md) | Profile and tune JVM settings | Measurable performance improvement |
| [Exercise 3: Caching Implementation](./exercises/exercise-3.md) | Implement multi-level caching | Cache hit rate > 80% |
| [Exercise 4: Security Audit](./exercises/exercise-4.md) | Find and fix security issues | All OWASP issues resolved |
| [Exercise 5: REST API Build](./exercises/exercise-5.md) | Build a secure REST API | Proper error handling and docs |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Resources

- [Adobe ColdFusion Documentation](https://helpx.adobe.com/coldfusion.html)
- [Lucee Documentation](https://docs.lucee.org/)
- [FusionReactor](https://www.fusion-reactor.com/)
- [CFML Reference](https://cfdocs.org/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 16 |
| Exercises | 12 |
| Assessment | 2 |
| **Total** | **30 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Explain ColdFusion's architecture to a technical client
2. Diagnose a slow-performing CF application
3. Recommend JVM tuning changes with justification
4. Identify security vulnerabilities in CF code
5. Build a performant, secure REST API

## Next Phase

[Phase 2: Legacy Assessment](../02-legacy-assessment/) — Learn to assess existing ColdFusion applications.
