# Phase 5 Assessment: Cloud Migration

> Test your cloud migration knowledge for ColdFusion.

**Time:** 1.5 hours | **Passing:** 70%

---

## Section A: AWS Architecture (25 points)

### A1: Architecture Components (15 points)

For a high-availability ColdFusion deployment, identify the correct AWS service:

| Need | AWS Service |
|------|-------------|
| DNS management | |
| Load balancing | |
| Auto-scaling | |
| Session storage | |
| File storage | |
| Database | |
| Caching | |
| CDN | |

### A2: EC2 Sizing (10 points)

ColdFusion app with these requirements:
- 500 concurrent users
- Average response time: 2 seconds
- CPU usage: 40% per instance

**What instance type would you recommend?**

_______________________________________________________

**How many instances for auto-scaling group?**

_______________________________________________________

---

## Section B: Docker & Containers (25 points)

### B1: Dockerfile Best Practices (15 points)

What security improvements would you add?

```dockerfile
# Current Dockerfile
FROM ortussolutions/commandbox:latest
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ["server", "start"]
```

**Your improvements:**

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

### B2: Session Management (10 points)

Why is Redis preferred for session management in containers?

1. _______________________________________________________
2. _______________________________________________________

---

## Section C: CI/CD Pipeline (25 points)

### C1: Pipeline Stages (15 points)

Put these CI/CD stages in the correct order:

```
a) Deploy to staging
b) Push to container registry
c) Commit code
d) Deploy to production
e) Build Docker image
f) Run tests
g) Security scan
h) Smoke test
i) Pull latest code
j) Approval gate
```

**Correct Order:**
_______________________________________________________

### C2: Rollback Strategy (10 points)

When should you trigger a rollback?

| Trigger | Yes/No | Why |
|---------|--------|-----|
| Smoke test fails | | |
| 5% of users report errors | | |
| CPU at 90% | | |
| One of five instances fails | | |
| Response time doubles | | |

---

## Section D: Azure Specifics (25 points)

### D1: Azure vs AWS (15 points)

Match AWS services to Azure equivalents:

| AWS | Azure |
|-----|-------|
| EC2 | |
| S3 | |
| RDS | |
| ElastiCache | |
| CloudFront | |
| IAM | |

### D2: Azure SQL Considerations (10 points)

What special configuration is needed for ColdFusion connecting to Azure SQL?

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

---

## Answer Key

### Section A
- A1: Route53, ALB/NLB, ASG, ElastiCache/Redis, EFS/S3, RDS, ElastiCache/Redis, CloudFront
- A2: t3.xlarge or similar; 2-3 instances minimum

### Section B
- B1: Multi-stage build, non-root user, secrets via env vars
- B2: Distributed across containers, persistence, performance

### Section C
- C1: c → i → f → g → e → b → a → h → j → d
- C2: All except single instance failure

### Section D
- D1: VMs, Blob Storage, SQL Database, Azure Cache for Redis, Azure Front Door, Azure AD
- D2: SSL/TLS required, firewall rules, connection string format

---

## Scoring

| Section | Points |
|---------|--------|
| A: AWS Architecture | 25 |
| B: Docker | 25 |
| C: CI/CD | 25 |
| D: Azure | 25 |
| **Total** | **100** |

**Passing:** 70/100
