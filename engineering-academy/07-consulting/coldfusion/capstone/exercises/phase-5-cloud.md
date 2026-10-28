# Phase 5 Exercise: Cloud Architecture Design

> Design a cloud architecture for BlogCFC5.

---

## Scenario

Client wants to move BlogCFC5 to AWS. Design the target architecture.

---

## Exercise 5A: Cloud Readiness Assessment

| Component | Current | Cloud Equivalent | Effort |
|-----------|---------|-----------------|--------|
| Application server | On-prem CF | EC2 / ECS | |
| Database | SQL Server on-prem | RDS SQL Server | |
| File storage | Local filesystem | S3 | |
| Sessions | In-memory | ElastiCache Redis | |
| Email | SMTP server | SES | |
| CDN | None | CloudFront | |
| Monitoring | None | CloudWatch | |

---

## Exercise 5B: Architecture Diagram

Draw the target AWS architecture:

```
┌─────────────────────────────────────────────────────────┐
│                          AWS                           │
│                                                       │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐        │
│  │ Route53 │────►│CloudFront│────►│   ALB   │        │
│  └─────────┘     └─────────┘     └────┬────┘        │
│                                       │              │
│                         ┌─────────────┼───────────┐  │
│                         │             ▼           │  │
│                         │      ┌─────────────┐    │  │
│                         │      │  ECS/Fargate│    │  │
│                         │      │  (Lucee)   │    │  │
│                         │      └─────────────┘    │  │
│                         │             │           │  │
│                         │     ┌────────┴────────┐   │  │
│                         │     ▼                 ▼   │  │
│                         │ ┌──────┐      ┌────────┐ │  │
│                         │ │ S3   │      │ RDS    │ │  │
│                         │ └──────┘      └────────┘ │  │
│                         │                       │  │
│                         └───────────────────────┘  │
│                                                       │
└───────────────────────────────────────────────────────┘
```

---

## Exercise 5C: Cost Estimate

| AWS Resource | Size | Monthly Cost Est. |
|--------------|------|-------------------|
| EC2/ECS | | |
| RDS SQL Server | | |
| S3 | | |
| CloudFront | | |
| ElastiCache | | |
| Route53 | | |
| **Total** | | |

---

## Exercise 5D: Migration Strategy

| Strategy | Pros | Cons | Best For |
|----------|------|------|----------|
| Lift-and-shift | | | |
| Re-platform | | | |
| Refactor | | | |

**Recommended strategy for BlogCFC5:** _______________

---

## Deliverable

Create a cloud migration proposal including:

1. Cloud readiness assessment
2. Target architecture diagram
3. Cost estimate (3-year TCO)
4. Migration strategy recommendation
5. Timeline
