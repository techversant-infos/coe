# 04. Maintaining Legacy Applications

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Many clients do not want a rewrite. They want their ColdFusion application kept safe, running and changeable for years.
Doing that well is the core of most CFML engagements. Back to the [roadmap](./README.md).

## Understanding inherited code

Before you change an application you did not build, map it.

**What to learn:**

- Reading the folder structure, `Application.cfc` or `Application.cfm`, datasources and scheduled tasks
- Using `git log` and `git blame` to see why code changed and who knows it
- Finding the integrations: other databases, web services, file shares and email
- Writing down what you learn so the next person starts faster

**Resources:** [CF Architecture Review Checklist](./deliverables/cf-architecture-review-checklist.md)

**Level:** Practitioner · Core

## Characterization tests

A characterization test records what the code does today, even if that behavior looks wrong. It lets you change old
code and notice what you broke.

**What to learn:**

- Writing TestBox specs around existing behavior before you change it
- Testing through HTTP when the code is too tangled to call directly
- Recording odd behavior as a question for the client, not a silent fix

**Resources:** [TestBox documentation](https://testbox.ortusbooks.com/)

**Level:** Practitioner · Core

## Applying updates safely

Engine updates, Java updates and library updates keep the application supported, but each one can change behavior.

**What to learn:**

- Keeping a test environment that matches production
- Applying an update in test, running the test suite and a smoke test, then scheduling production
- Taking a backup of the engine configuration and the application before every update
- Rolling back an update that breaks something

**Resources:** [Adobe ColdFusion security bulletins](https://helpx.adobe.com/security/products/coldfusion.html)

**Level:** Practitioner · Core

## Monitoring and alerting

You should hear about a problem from an alert, not from the client.

**What to learn:**

- Health checks for the application, the database and scheduled tasks
- Alerts for errors, slow requests, memory use and disk space
- Keeping logs long enough to investigate, and never logging personal data

**Resources:**

- [Application monitoring](./02-jvm-performance-and-diagnostics.md#application-monitoring)
- [FusionReactor](https://www.fusion-reactor.com/)

**Level:** Practitioner · Core

## Incident response

When production breaks, a calm, repeatable process restores service faster.

**What to learn:**

- Confirming the impact and telling the client early
- Restoring service first, for example by rolling back, then finding the cause
- Writing a blameless incident review with actions that prevent a repeat

**Resources:** [Google SRE book](https://sre.google/sre-book/table-of-contents/)

**Level:** Advanced · Core

## Runbooks and documentation

Legacy applications often depend on knowledge in one person's head.

**What to learn:**

- Runbooks for restarts, deployments, updates and common failures
- A one-page system overview: servers, datasources, integrations and owners
- Keeping documentation next to the code so it changes with it

**Resources:** [Handoff note structure](../../00-engineering-foundations/10-communication-and-ownership.md#handoff-notes)

**Level:** Practitioner · Core

## Support agreements

Ongoing maintenance needs clear terms: what is covered, how fast you respond and how changes are approved.

**What to learn:**

- Response and resolution targets by severity
- Separating support work from change requests
- Reporting monthly on incidents, updates applied and risks

**Resources:** [Consulting Operating Model: ongoing retainer](./deliverables/consulting-operating-model.md#23-ongoing-retainer)

**Level:** Advanced · Core

## Using AI tools on inherited code

AI coding assistants help you read and explain unfamiliar code quickly, but they can be confidently wrong about old
CFML and must not touch Red Zone code.

**What to learn:**

- Asking an assistant to explain a file or trace a request, then checking the answer against the code
- Choosing a delegation level for each task before you start
- Never pasting client code or data into a tool the client has not approved

**Resources:** [AI Era Coding Guidelines, section 2.1](../../../standards/general/ai-era-coding-guidelines.md#21-delegation-levels)

**Level:** Practitioner · Optional

## Project: Take Over the Practice App for Maintenance

**Brief:** Treat the practice app as a client system you have just inherited. Map it, protect it with tests and
monitoring, and prepare to support it.

**Size:** 3–4 days

**Verification**, checked by your lead:

- [ ] A one-page system overview: engine, datasources, scheduled tasks, integrations and configuration
- [ ] At least ten characterization specs cover the main pages and the admin login flow, and run in one command
- [ ] A test environment where you apply an engine update, run the specs, and record the result
- [ ] Alerts for errors and slow requests, shown firing during a test
- [ ] Runbooks for restart, deploy, update and rollback; a colleague follows one without help
- [ ] A simulated incident handled end to end, with a blameless incident review
- [ ] A draft support agreement with response targets by severity

Previous: [03. Security and Hardening](./03-security-and-hardening.md) · Next: [05. Assessing Legacy Applications](./05-assessing-legacy-applications.md)
