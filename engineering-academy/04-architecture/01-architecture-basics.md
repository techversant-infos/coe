# 01. Architecture Basics

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Architecture is the set of decisions that are expensive to change later. This stage covers how to find those
decisions, weigh them and write them down so others can follow them. Back to the [roadmap](./README.md).

## The architect's role

An architect is accountable for the technical decisions that shape a system, not for writing most of its code.
The job is to make good decisions, explain them, and stay close enough to the build to see when they stop working.

**What to learn:**

- Which decisions belong to the architect, and which the team should make
- Staying hands-on enough to keep your decisions realistic: spikes, reviews, reading the code
- Working with the lead developer, the project manager and the client's technical people

**Resources:**

- [Lead to Architect](../career-progression/04-lead-to-architect.md), Techversant's career page for the move
- [Who needs an architect?](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf), Martin Fowler

**Level:** Advanced · Core

## Quality attributes

Features say what a system does. Quality attributes say how well it must do it: how fast, how available, how
secure, how easy to change. They drive most architecture decisions, so you must find them early and make them
measurable.

**What to learn:**

- The common attributes, as named in the ISO/IEC 25010 quality model: performance efficiency, compatibility,
  reliability, security and maintainability, among others
- Turning a vague wish ("it must be fast") into a measurable scenario ("95% of article pages load in under one
  second at 500 requests a second")
- Ranking attributes with the client, because they compete with each other and with cost

**Resources:**

- [ISO/IEC 25010:2023 quality characteristics](https://quality.arc42.org/standards/iso-25010),
  on the arc42 quality model site
- [Quality requirements in arc42](https://docs.arc42.org/section-10/)

**Level:** Advanced · Core

## Trade-off analysis

Every design choice gives something up. Caching improves speed but risks stale data; splitting services allows
independent releases but adds network failures. Your job is to make the trade-off visible and choose on purpose.

**What to learn:**

- Listing at least two real options for each important decision, including "do nothing"
- Comparing options against the ranked quality attributes, cost and the team's skills
- Spotting decisions that are hard to reverse, and spending more time on those

**Resources:** learn on projects, with an architect. The decision matrix in the
[ColdFusion modernization framework](../07-consulting/coldfusion/deliverables/cf-modernization-framework.md#decision-matrix)
shows one way to compare options.

**Level:** Advanced · Core

## Architecture decision records

An architecture decision record (ADR) is a short document for one decision: the context, the decision and its
consequences. A folder of ADRs in the repository tells new team members why the system looks the way it does.

**What to learn:**

- The format Michael Nygard proposed: title, status, context, decision and consequences
- Writing an ADR in under a page, in plain language, at the time of the decision
- Superseding an old ADR with a new one instead of editing history

**Resources:**

- [Documenting architecture decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions),
  Michael Nygard
- [ADR templates and tools](https://adr.github.io/)

**Level:** Practitioner · Core

## Diagrams with the C4 model

A diagram is often the fastest way to share a design, but only if everyone reads it the same way. The C4 model
gives you four levels of zoom, so each diagram answers one question for one audience.

**What to learn:**

- The four levels: system context, containers, components and code
- Which level to show a client, a new developer or an operations team
- Keeping diagrams in the repository as code, so they change with the system

**Resources:**

- [The C4 model](https://c4model.com/), Simon Brown
- [Structurizr](https://structurizr.com/) or [Mermaid C4 diagrams](https://mermaid.js.org/syntax/c4.html), for
  diagrams as code

**Level:** Practitioner · Core

## Architecture documentation

Beyond ADRs and diagrams, larger projects need a short architecture document that pulls the picture together:
goals, constraints, structure, decisions and risks.

**What to learn:**

- A standard outline, so readers know where to look
- Writing only what the team will keep up to date

**Resources:** [arc42](https://arc42.org/), a free template for architecture documentation

**Level:** Practitioner · Optional

## Project: Document the Practice System as It Is

**Brief:** Set up the [practice system](./practice-system.md) and document the RealWorld app as it stands today,
before you change anything. Draw it, list the quality attributes that matter for Lantern's brief, and record the
decisions already built into it.

**Size:** 2–3 days

**Verification**, checked by an architect or lead:

- [ ] The app runs locally, and the API test results are recorded as the baseline
- [ ] A system context diagram shows the app, its users and every external system in the brief
- [ ] A container diagram shows the front end, back end, database and any other process, with the technology of
  each
- [ ] The diagrams are stored as code in the repository and render without errors
- [ ] Five quality attributes from the brief are ranked, each with a measurable scenario
- [ ] Three ADRs record decisions already in the app, such as the database or the sign-in method, each with at
  least one consequence the client should know about
- [ ] A reviewer who has not seen the app can explain its structure from your diagrams alone

Next: [02. System Design](./02-system-design.md)
