# 05. Reliability and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Every system fails sometimes. Reliability design decides how often, how badly and how fast it recovers, and sets
targets the team and the client agree on. Back to the [roadmap](./README.md).

## Service level objectives

A service level objective (SLO) is a target for how reliable a service must be, measured by a service level
indicator (SLI) such as the share of requests that succeed. It turns "the site must be up" into a number the team can
work to.

**What to learn:**

- Choosing indicators that reflect what users experience, such as successful requests and response time
- Setting objectives per user journey, because reading and writing may need different targets
- Error budgets: the unreliability an objective allows, and what the team does when it is used up

**Resources:**

- [Service level objectives](https://sre.google/sre-book/service-level-objectives/), Google's Site Reliability
  Engineering book
- [Example error budget policy](https://sre.google/workbook/error-budget-policy/), The Site Reliability Workbook

**Level:** Advanced · Core

## Failure handling

Networks drop, services slow down and providers go offline. Good designs expect this and limit the damage.

**What to learn:**

- Timeouts on every call to another system, and retries with growing delays and random jitter
- Circuit breakers that stop calling a failing service for a while
- Graceful degradation: keeping the core of the site working when an extra feature fails

**Resources:**

- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/),
  Amazon Builders' Library
- [Circuit breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker), Azure
  Architecture Center

**Level:** Practitioner · Core

## Performance and load testing

Performance claims need evidence. Load tests show how the system behaves at the traffic you expect, and where it
breaks.

**What to learn:**

- Load, stress and soak tests, and what each tells you
- Writing realistic test scenarios from production traffic or the brief
- Reading the results: percentiles, error rates and resource use, not just averages

**Resources:**

- [Performance validation](../../standards/general/ai-era-coding-guidelines.md#63-performance-validation), in the
  Techversant AI Era Coding Guidelines
- [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Practitioner · Core

## Observability

When something goes wrong in production, logs, metrics and traces are how you find out what and why. Design them in,
so the team is not guessing during an incident.

**What to learn:**

- Logs, metrics and traces, and the question each one answers
- Tracing a request across services with OpenTelemetry
- Alerts on SLOs and user impact, not on every spike in CPU

**Resources:**

- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [What must be logged](../../security/audit/security-audit-reference.md#111-what-must-be-logged) and
  [what must never be logged](../../security/audit/security-audit-reference.md#112-what-must-never-be-logged), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Disaster recovery

Disaster recovery plans how the system comes back after a major failure, such as a lost region or a deleted
database. The client's recovery time objective (RTO) and recovery point objective (RPO) decide how much it costs.

**What to learn:**

- RTO and RPO, and how they drive the choice of recovery strategy
- The common strategies, from backup and restore to a second site running all the time, and their costs
- Recovery drills, because an untested plan is only a hope

**Resources:**

- [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html),
  AWS whitepaper

**Level:** Advanced · Core

## Project: Set Service Levels and Prove Recovery

**Brief:** Lantern's brief sets availability targets and a recovery requirement. Turn them into SLOs, design how the
system handles failure, and prove you can recover within the brief's limits.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] SLIs and SLOs are defined for reading and for writing, matching the brief, with the error budget for each over
  30 days
- [ ] An error budget policy says what the team does when a budget is used up
- [ ] A failure table lists at least six ways the design can fail, the user impact of each and the response
- [ ] On the running app, a call to an external service has a timeout, retries with backoff and a fallback, and a
  test shows the site still serves articles when that service is down
- [ ] A disaster recovery strategy is chosen to meet the brief's four-hour RTO and 15-minute RPO, with its cost
- [ ] A recovery drill restores the database from backup, and the measured recovery time and data loss are within
  the brief's limits
- [ ] Dashboards or alerts are defined for each SLO

Previous: [04. Data Architecture](./04-data-architecture.md) · Next:
[06. Security and Privacy Architecture](./06-security-and-privacy-architecture.md)
