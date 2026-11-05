# 06. Modernization Strategy

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Every client eventually asks "should we migrate?" The right answer depends on their business, budget and team, not on
what is fashionable. Back to the [roadmap](./README.md).

## Modernization options

Know every realistic path and when each one fits.

| Option | Fits when |
|--------|-----------|
| Upgrade Adobe ColdFusion | The application works, the client values Adobe's features and support, and budget allows the subscription |
| Move to Lucee | Licensing cost matters and the application uses few Adobe-only features |
| Move to the cloud unchanged | Infrastructure is the main problem, not the code |
| Modernize the front end | The back end is sound but the interface is dated |
| Replace step by step (strangler fig) | The application is large and critical, and a long migration is acceptable |
| Move to BoxLang | A proof of concept on the client's code passes, and the client wants an open-source engine with vendor support |
| Rewrite | The application is small, poorly understood or blocking the business, and the client accepts the risk |
| Retire or replace with a product | The application no longer gives the business enough value, or a standard product now does the job |

**What to learn:** the strengths, costs and risks of each option, and how options combine.

**Resources:** [CF Modernization Framework](./deliverables/cf-modernization-framework.md)

**Level:** Advanced · Core

## Decision matrix

A scored comparison keeps the recommendation honest and easy to explain.

**What to learn:**

- Scoring options against complexity, business criticality, drivers and constraints
- Weighting factors with the client, not for them
- Explaining why the top score is the recommendation, or why it is not

**Resources:** [CF Modernization Framework: decision matrix](./deliverables/cf-modernization-framework.md#decision-matrix)

**Level:** Advanced · Core

## Total cost of ownership

Clients compare options on cost over several years, not on the first project.

**What to learn:**

- Licensing: Adobe ColdFusion 2025 is a yearly subscription; Lucee and BoxLang are free, with optional paid support
- Hosting, support, staff and training costs
- The cost of doing nothing: security risk, unsupported versions, slow change
- Presenting a three- to five-year comparison with clear assumptions

**Resources:** [Adobe ColdFusion product terms](https://wwwimages2.adobe.com/content/dam/cc/en/legal/servicetou/Adobe-ColdFusion-Product-Specific-Terms-en_US-20250225.pdf)

**Level:** Advanced · Core

## Strangler fig pattern

Replace an application piece by piece: put new services in front of or beside the old one, move one feature at a time,
and switch the old code off when nothing uses it.

**What to learn:**

- Choosing the first feature to move: valuable, low-risk and loosely coupled
- Routing traffic between old and new code
- Keeping data consistent while both run

**Resources:**

- [CF Modernization Framework: strangler fig option](./deliverables/cf-modernization-framework.md#option-e-strangler-fig-pattern)
- [Strangler fig application, Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)

**Level:** Advanced · Core

## Phased roadmap

A good plan delivers value early and keeps a way back at every step.

**What to learn:**

- Quick wins first: patching, security fixes, monitoring
- Foundations next: tests, CI, configuration in version control
- Larger changes last, each with a rollback plan

**Resources:** [CF Modernization Framework: implementation phases](./deliverables/cf-modernization-framework.md#implementation-phases)

**Level:** Advanced · Core

## When not to modernize

Sometimes the best advice is to keep the application as it is, or to retire it.

**What to learn:**

- Signs an application should be maintained, replaced with a product or switched off
- Saying so clearly, even when a bigger project would earn more

**Resources:** [CF Modernization Framework: quick decision guide](./deliverables/cf-modernization-framework.md#quick-decision-guide)

**Level:** Advanced · Core

## Project: Recommend a Modernization Path

**Brief:** Use Scenario 0, the BlogCFC5 media client, from the [practice clients](./reference/practice-clients.md),
so your recommendation builds on your stage 05 assessment. Using the CF Modernization Framework, recommend a path and
an engine, and defend them.

**Size:** 2–3 days

**Verification**, checked by your lead:

- [ ] At least three options compared in a decision matrix, with the weights agreed with the "client"
- [ ] A five-year cost comparison for the top two options, with every assumption written down
- [ ] A phased roadmap with quick wins in the first three months and a rollback plan for each phase
- [ ] A short decision record: the recommendation, the options rejected and why
- [ ] A 15-minute presentation to your lead playing the client, including one question you could not answer and how
  you followed up

Previous: [05. Assessing Legacy Applications](./05-assessing-legacy-applications.md) · Next: [07. Upgrades and Migration](./07-upgrades-and-migration.md)
