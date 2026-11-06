# 07. Cloud and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

FDEs deploy into whatever the client runs, and keep it running after launch. This stage is where a working
prototype becomes something the client can rely on every day. Back to the [roadmap](./README.md).

## Linux and the shell

Client servers, containers and CI runners are usually Linux. You will often work on machines you do not own, with
limited access.

**What to learn:**

- Files, permissions, processes and services
- Reading logs with `grep`, `tail` and `less`
- SSH, environment variables and small shell scripts

**Resources:** [The Linux Command Line](https://linuxcommand.org/tlcl.php)

**Level:** Practitioner · Core

## One cloud platform

Know one cloud well rather than three a little: whichever most of your clients use.

**What to learn:**

- Compute, storage, networking and managed databases
- Identity and access management for services and people
- Reading the bill and setting budgets and alerts

**Resources:**

- [Platform Engineering](../03-platform-engineering/README.md) (planned academy path)
- [AWS documentation](https://docs.aws.amazon.com/), [Azure documentation](https://learn.microsoft.com/en-us/azure/),
  [Google Cloud documentation](https://cloud.google.com/docs)

**Level:** Practitioner · Core

## Docker

Containers make your solution run the same way on your laptop, in CI and on the client's platform.

**What to learn:**

- Writing small, secure Dockerfiles
- Docker Compose for local development
- Passing configuration and secrets without baking them into images

**Resources:** [Docker get started](https://docs.docker.com/get-started/)

**Level:** Practitioner · Core

## Kubernetes

Many larger clients run Kubernetes. You need enough to deploy, read status and debug, not to run a cluster.

**What to learn:**

- Pods, Deployments, Services, ConfigMaps and Secrets
- Reading pod logs and events
- Rolling out and rolling back a deployment

**Resources:** [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/)

**Level:** Practitioner · Optional

## Terraform

Infrastructure as code lets the client's team see, review and change the infrastructure you set up.

**What to learn:**

- Resources, variables, state and modules
- Plan, review, then apply
- Handing state and modules over to the client
- OpenTofu, the open-source fork some clients use instead

**Resources:** [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)

**Level:** Advanced · Optional

## CI/CD pipelines

Every change should be type-checked, tested and deployed the same way, with a rollback ready.

**What to learn:**

- Pipelines that build, test and deploy
- Separate environments and promotion between them
- Deploying behind feature flags and rolling back fast

**Resources:**

- [Git Workflow](../../standards/git/git-workflow.md): environments, promotion and rollback
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Feature toggles](https://martinfowler.com/articles/feature-toggles.html)

**Level:** Practitioner · Core

## Logs, metrics, traces and alerts

These tell you something is wrong before the client does, and help you find out why.

**What to learn:**

- Structured logs with a request ID, and no personal data
- Metrics and alerts for errors, latency and usage
- Distributed traces across services with OpenTelemetry

**Resources:** [OpenTelemetry documentation](https://opentelemetry.io/docs/)

**Level:** Practitioner · Core

## Incidents and maintenance

The work of running a system after launch, for as long as it exists.

**What to learn:**

- Writing runbooks so others can handle common problems
- Responding to incidents, rolling back, and writing a blameless review afterwards
- Applying patches and upgrades, testing backup restores, watching cloud and AI costs

**Resources:**

- [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- [Atlassian postmortem guide](https://www.atlassian.com/incident-management/postmortem)

**Level:** Advanced · Core

## Project: Deploy, Break and Recover

**Brief:** Deploy the service request tracker and the standards assistant to one cloud platform, then run a "game
day": a colleague breaks something on purpose and you restore the service.

**Size:** 3–4 days

**Verification**, checked by your lead:

- [ ] Each service runs in a container, and CI builds the images
- [ ] In your practice environment, pushing a version tag deploys through the pipeline with no manual steps. On a
  client project, the client's approval step comes first.
- [ ] Logs are structured and carry a request ID; a dashboard shows error rate, response time and AI cost
- [ ] An alert fires when the error rate passes a threshold, shown during the game day
- [ ] On the game day you spot the problem from the alert, follow your runbook and roll back to the previous version,
  and you record how long recovery took
- [ ] A colleague who did not build the system handles a second failure using only your runbook
- [ ] You write a blameless incident review within one working day
- [ ] Optional: the infrastructure is defined in Terraform, and `terraform plan` shows no changes after `apply`

Previous: [06. Integration Engineering](./06-integration-engineering.md) · Next: [08. Production and Security](./08-production-and-security.md)
