# 05. Assessing Legacy Applications

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Most modernization engagements start with an assessment: a short, paid piece of work that tells the client what they
have, what it costs them and what to do next. Back to the [roadmap](./README.md).

## Framework detection

The framework, or the lack of one, shapes every later estimate.

**What to learn:**

- Signs of ColdBox, FW/1, Fusebox, Mach-II, Model-Glue or a custom framework
- Plain `.cfm` applications held together with `cfinclude`
- Showing your evidence: the files and patterns that prove the framework

**Resources:** [Legacy Assessment Template](./deliverables/legacy-assessment-template.md)

**Level:** Practitioner · Core

## Architecture mapping

A diagram of components, data and integrations is often the first thing the client has never had.

**What to learn:**

- Mapping pages, components, datasources and external services
- Finding the authentication and session approach
- Marking the risky parts: shared state, scheduled tasks, file system use

**Resources:**

- [CF Architecture Review Checklist](./deliverables/cf-architecture-review-checklist.md)
- [Deep expertise guide](./reference/coldfusion-deep-expertise-guide.md), for how the parts of a CFML system fit together

**Level:** Practitioner · Core

## Technical debt scoring

Consistent scoring lets you compare applications and explain priorities.

**What to learn:**

- Scoring code quality, tests, dependencies, configuration, deployment and documentation
- Backing each score with examples
- Turning scores into a short list of what to fix first

**Resources:** [Legacy Assessment Template](./deliverables/legacy-assessment-template.md)

**Level:** Practitioner · Core

## Security assessment

Old CFML applications almost always have security findings. Clients need them ranked, not just listed.

**What to learn:** applying the security review from stage 03 at assessment depth, within the time box.

**Resources:**

- [CF Security Review Checklist](./deliverables/cf-security-review-checklist.md)
- [Security review](./03-security-and-hardening.md#security-review)

**Level:** Practitioner · Core

## Performance assessment

The client usually knows the application is slow but not why.

**What to learn:** profiling with the methods from stage 02, and estimating the effect of each fix.

**Resources:**

- [Legacy Assessment Template: performance assessment](./deliverables/legacy-assessment-template.md#5-performance-assessment)
- [JVM, Performance and Diagnostics](./02-jvm-performance-and-diagnostics.md)

**Level:** Practitioner · Core

## The assessment report

The report is the product. It must work for executives and for engineers.

**What to learn:**

- A one-page executive summary: risk, cost of doing nothing and recommendation
- Technical findings with evidence, severity and effort
- Recommending next steps, often a phased modernization plan

**Resources:** [Legacy Assessment Template](./deliverables/legacy-assessment-template.md)

**Level:** Advanced · Core

## Project: Assess the Practice App

**Brief:** Assess the practice app as if for a paying client, in a time box of three days, and write the report with
the Legacy Assessment Template. Assess a fresh clone of the original repository, not the copy you fixed in stages
03 and 04.

**Size:** 3 days

**Verification**, checked by your lead:

- [ ] The framework identified, with the files and patterns that prove it
- [ ] An architecture diagram covering pages, components, the database and integrations
- [ ] Every technical debt dimension scored, each with at least one example from the code
- [ ] Security and performance findings, each with evidence, severity and effort
- [ ] A one-page executive summary a non-technical reader understands, checked by someone outside engineering
- [ ] Every compatibility error from the stage 01 project included as a finding

Previous: [04. Maintaining Legacy Applications](./04-maintaining-legacy-applications.md) · Next: [06. Modernization Strategy](./06-modernization-strategy.md)
