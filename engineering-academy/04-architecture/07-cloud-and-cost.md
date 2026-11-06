# 07. Cloud and Cost

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most client systems now run in the cloud, where every design choice has a monthly price. An architect has to design
for the platform and for the budget. Back to the [roadmap](./README.md).

## Cloud architecture frameworks

Each major cloud provider publishes a framework for reviewing designs. They overlap, and they make good checklists
on any platform.

**What to learn:**

- The six pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, performance
  efficiency, cost optimization and sustainability
- The five pillars of the Azure Well-Architected Framework, which cover the same ground without sustainability
- Running a lightweight review of a design against one framework

**Resources:**

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/pillars)
- [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)

**Level:** Advanced · Core

## Containers and orchestration

Containers package an application with everything it needs, so it runs the same everywhere. Orchestrators such as
Kubernetes run many containers, but add a lot to operate.

**What to learn:**

- When a managed container service is enough, and when Kubernetes is worth its cost
- Health checks, resource limits and scaling rules for containers
- Securing images and running containers without unnecessary privileges

**Resources:**

- [Containers and orchestration](../../security/audit/security-audit-reference.md#45-containers-and-orchestration),
  in the Techversant security audit reference
- [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)

**Level:** Practitioner · Core

## Infrastructure as code

Infrastructure as code describes servers, networks and services in files kept in version control. Environments can
then be rebuilt, reviewed and compared like application code.

**What to learn:**

- Declaring infrastructure with a tool such as Terraform or OpenTofu
- Reviewing infrastructure changes in pull requests, and running plans in the pipeline
- Keeping state and secrets safe

**Resources:**

- [Cloud and infrastructure as code](../../security/audit/security-audit-reference.md#44-cloud-and-infrastructure-as-code),
  in the Techversant security audit reference
- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)

**Level:** Practitioner · Core

## Cost estimation

A design the client cannot afford to run is a failed design. Estimate running costs before you commit, and design
so costs grow slower than usage.

**What to learn:**

- Estimating monthly costs with the provider's pricing calculator, line by line
- The usual cost drivers: compute, databases, data transfer, storage and managed services
- Reserved capacity, autoscaling and turning off what is not used, and reporting cost per user or per request

**Resources:**

- [AWS Pricing Calculator](https://calculator.aws/) and
  [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
- [Cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html),
  AWS Well-Architected Framework

**Level:** Advanced · Core

## Environments and deployment

How code moves from a developer's machine to production decides how safely the team can change the system.

**What to learn:**

- Environments that match production closely enough to trust, and what they cost
- Deployment strategies such as rolling, blue-green and canary releases, and rolling back
- Who approves a production release, and how that is recorded

**Resources:**

- [Environment flow](../../standards/git/git-workflow.md#-environment-flow) and
  [rollback](../../standards/git/git-workflow.md#-rollback--database-script-management), in the Techversant Git
  workflow

**Level:** Practitioner · Core

## Project: Design the Deployment and Price It

**Brief:** Design how Lantern's system runs in one cloud, describe one environment as code, and show that it fits
the USD 1,500 monthly budget at the new traffic.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] A deployment diagram shows every cloud service the design uses, in one region, with how traffic reaches it
- [ ] An ADR chooses between a managed container service and Kubernetes, with at least two options compared
- [ ] One environment is described in infrastructure as code, and a plan runs without errors in a pipeline or
  locally
- [ ] A line-by-line cost estimate from the provider's pricing calculator covers the brief's traffic, and stays under
  USD 1,500 a month
- [ ] The estimate shows how cost changes if traffic doubles
- [ ] A review against one well-architected framework lists at least three risks, each with a decision to fix,
  accept or defer it
- [ ] The release process states the deployment strategy, how to roll back and who approves production releases

Previous: [06. Security and Privacy Architecture](./06-security-and-privacy-architecture.md) · Next:
[08. AI-Enabled Systems](./08-ai-enabled-systems.md)
