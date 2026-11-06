# 10. Architecture Practice

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Good designs only matter if people understand them, trust them and keep following them. This stage covers the
working habits of an architect: reviews, communication, estimates, standards and mentoring. Back to the
[roadmap](./README.md).

## Architecture reviews

An architecture review checks a design against its goals before it is expensive to change. Run well, it helps the
team; run badly, it becomes a gate everyone tries to avoid.

**What to learn:**

- When to hold a review: before major decisions, before build and before go-live
- Preparing a review pack, and running the meeting so it ends with clear decisions and actions
- Reviewing other people's designs with questions and evidence, not personal preference

**Resources:**

- [ColdFusion Architecture Review Checklist](../07-consulting/coldfusion/deliverables/cf-architecture-review-checklist.md),
  from the Techversant ColdFusion consulting track. Most sections apply to any stack.

**Level:** Advanced · Core

## Explaining decisions to stakeholders

Clients and managers decide on cost, risk and time, not on technology. Explain each decision in those terms, at the
level of detail the audience needs.

**What to learn:**

- Presenting options and a recommendation on one page
- Choosing the right C4 level and vocabulary for each audience
- Saying "I don't know yet" and coming back with evidence

**Resources:** learn on projects, with an architect.

**Level:** Advanced · Core

## Estimates and proposals

Architects shape proposals: the solution, the estimate and the risks. A design that cannot be delivered for the
agreed price helps nobody.

**What to learn:**

- Breaking a solution into work packages that can be estimated
- Estimating with ranges and stating the assumptions and risks behind them
- Reviewing a proposal's scope for gaps before it reaches the client

**Resources:**

- [Estimation templates](../07-consulting/coldfusion/deliverables/estimation-templates/README.md), from the
  Techversant ColdFusion consulting track

**Level:** Advanced · Core

## Reference architectures and standards

When the same kind of system appears on several projects, a proven reference saves each team from starting at zero.
Standards keep projects consistent where it matters.

**What to learn:**

- Spotting patterns that have worked on more than one project
- Writing a reference architecture: when to use it, the design, the decisions and the known limits
- Proposing a new or changed CoE standard

**Resources:**

- [CoE standards](../../standards/README.md), Techversant's existing standards
- [Contributing to CoE Standards](../../CONTRIBUTING.md)

**Level:** Expert · Core

## Mentoring

Architects grow other architects. Mentoring lead developers and senior developers through design decisions is how
the practice scales.

**What to learn:**

- Letting others make design decisions, with you reviewing, instead of making them all yourself
- Giving design feedback that teaches the reasoning, not only the answer
- Agreeing growth goals and evidence with the people you mentor

**Resources:**

- [Career Progression](../career-progression/01-transition-overview.md), Techversant's transition guides

**Level:** Advanced · Core

## Fitness functions

A fitness function is an automated check that a design rule still holds, such as "the web layer never calls the
database directly". It keeps the architecture from drifting as the code grows.

**What to learn:**

- Turning an architecture rule into an automated test that runs in the pipeline
- Choosing the few rules that matter most

**Resources:**

- [Fitness function-driven development](https://www.thoughtworks.com/insights/articles/fitness-function-driven-development),
  Thoughtworks

**Level:** Advanced · Optional

## Project: Review a Peer's Design and Propose a Reference

**Brief:** Swap designs with another engineer on this roadmap, or review a real project's design chosen with your
lead. Run a formal architecture review of it, then turn one part of your own design into a reference architecture
that other Techversant teams could reuse.

**Size:** 3 days

**Verification**, checked by an architect or lead:

- [ ] A review pack is sent at least two working days before the review meeting
- [ ] The review meeting is held with the design's author and at least one other reviewer
- [ ] A review record lists each finding with evidence, its severity, and a decision and owner for each action
- [ ] The design's author confirms in writing that the findings were clear and fair
- [ ] A reference architecture, for example for notifications or AI summaries, states when to use it, the design,
  the key decisions and its known limits
- [ ] The reference is proposed to the CoE Team following the contributing guide

Previous: [09. Modernization and Migration](./09-modernization-and-migration.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
