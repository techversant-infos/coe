# Phase 5: Cloud Migration

> Move ColdFusion applications to AWS and Azure with confidence.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Specialist Pathway |
| Best for | Cloud Specialist |
| Contribution level | Contributor → Lead |
| Take this when | You need to design a cloud architecture for CF workloads |
| Evidence of readiness | Completed cloud architecture diagram for a CF application |
| Next | [capstone/exercises/phase-5](../capstone/exercises/phase-5-cloud.md) for practice |

---

## Overview

## Overview

Cloud migration is a high-demand service. This phase covers the specifics of moving ColdFusion workloads to cloud infrastructure — from lift-and-shift to cloud-native architectures.

> **Generic Skills:** Planned: General Cloud Documentation. This phase covers ColdFusion-specific cloud considerations.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Evaluate ColdFusion applications for cloud readiness
- [ ] Plan migration strategy (lift-and-shift vs refactor)
- [ ] Deploy ColdFusion to AWS (EC2, ECS, Lambda considerations)
- [ ] Deploy ColdFusion to Azure (VMs, App Service, Container Instances)
- [ ] Configure load balancing and auto-scaling for CF
- [ ] Implement cloud-native session management
- [ ] Set up CI/CD pipelines for CF applications
- [ ] Manage secrets and configuration in cloud environments

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/)
- Basic understanding of cloud fundamentals (see Planned: `general/cloud/`)

## Topics

### 1. Cloud Readiness Assessment

- Server dependency mapping
- Session state evaluation
- Database connectivity requirements
- File system dependencies
- Third-party service dependencies
- Licensing considerations (Adobe CF cloud licensing)

### 2. AWS for ColdFusion

**EC2 Approach:**
- Windows vs Linux CF instances
- Instance sizing for CF workloads
- EBS storage configuration
- VPC setup
- Security groups

**Container Approach (ECS/EKS):**
- Dockerizing ColdFusion
- Tomcat base images
- Session affinity considerations
- Logging and monitoring

**RDS Integration:**
- Connection pooling with RDS
- SSL connections
- Performance considerations

**Services:**
- ALB/NLB for load balancing
- Auto Scaling configuration
- CloudWatch for monitoring
- S3 for file storage
- ElastiCache for sessions
- CloudFront for static assets

### 3. Azure for ColdFusion

**VM Approach:**
- Azure VM sizing
- Windows Server configuration
- Azure SQL Database
- Azure Storage

**Container Approach:**
- Azure Container Instances
- Azure Kubernetes Service
- Docker deployment

**Azure Services:**
- Azure Load Balancer
- Azure Monitor
- Azure Key Vault
- Azure Cache for Redis

### 4. ColdFusion-Specific Considerations

**Session Management:**
- Sticky sessions vs distributed sessions
- Redis for session sharing
- Application scope in cloud

**File System:**
- EFS/SMB for shared files
- S3/Azure Blob for assets
- NFS for Windows

**Performance Tuning:**
- JVM sizing for cloud instances
- Connection pool configuration
- Memory management

### 5. CI/CD for ColdFusion

- Git-based deployment
- AWS CodePipeline / Azure DevOps
- Infrastructure as Code (Terraform, CloudFormation)
- Blue-green deployments
- Rollback automation

### 6. Security in Cloud

- IAM roles and policies
- Network security (security groups, NACLs)
- Secrets management (AWS Secrets Manager, Azure Key Vault)
- Encryption (at rest and in transit)
- WAF configuration

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: AWS Deployment](./exercises/exercise-1.md) | Deploy CF to AWS EC2 | Running application |
| [Exercise 2: Docker Container](./exercises/exercise-2.md) | Containerize a CF app | Working Docker image |
| [Exercise 3: Azure Migration](./exercises/exercise-3.md) | Deploy to Azure | Running application |
| [Exercise 4: CI/CD Pipeline](./exercises/exercise-4.md) | Build deployment pipeline | Automated deployment |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Deliverable

Create a cloud migration checklist using the [CF Cloud Migration Framework](../DELIVERABLES/).

## Resources

- Planned: General Cloud Documentation
- [AWS ColdFusion Best Practices](https://aws.amazon.com/blogs/architecture/)
- [Azure ColdFusion Guidance](https://learn.microsoft.com/azure/)
- [ColdFusion Administrator](https://helpx.adobe.com/coldfusion/getting-started.html)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 12 |
| Exercises | 10 |
| Assessment | 2 |
| **Total** | **24 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Assess a ColdFusion application for cloud migration
2. Deploy ColdFusion to AWS or Azure
3. Configure cloud-native session and file management
4. Build a CI/CD pipeline for ColdFusion deployments

## Next Phase

[Phase 6: AI Integration](../06-ai-integration/) — Learn to add AI capabilities to existing ColdFusion systems.
