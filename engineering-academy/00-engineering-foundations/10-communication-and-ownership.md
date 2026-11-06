# 10. Communication and Ownership

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A correct change can still fail if nobody understands its purpose, risks or next steps. This stage covers writing
about your work and owning it after it ships. Back to the [roadmap](./README.md).

## PR descriptions

A PR description is the first thing a reviewer reads, and often the only record of why a change was made.

**What to learn:**

- Explaining what changed, why, how you verified it and what could go wrong
- Adding screenshots, logs or example requests when they help the reviewer
- Linking the ticket and any design note or ADR

Use this structure:

```text
## Summary
## Why
## Verification
## Risks and rollback
## Notes for reviewers
```

**Resources:** [Technical writing courses](https://developers.google.com/tech-writing), Google

**Level:** Foundation · Core

## Status and blocker updates

Short, specific updates let your lead act early. A blocker raised on day one costs far less than one found at the
deadline.

**What to learn:**

- Writing updates with dates, owners, links and the next action
- Raising a blocker as soon as you are stuck, with what you tried and the decision you need
- Keeping updates short enough to read in a minute

Use this structure for a blocker:

```text
Current state:
What I tried:
What I learned:
Decision needed:
Owner:
Needed by:
```

**Resources:** learn with your lead, from your project's stand-ups and status reports.

**Level:** Foundation · Core

## Handoff notes

When you hand work to someone else, because you are moving project, taking leave or passing a task on, a handoff
note lets them continue without guessing.

**What to learn:**

- Writing down the context, where things are, how to check they work and what is left to do
- Naming the known risks and anything only you know
- Walking the new owner through the note, not only sending it

Use this structure:

```text
Context:
Files and links:
How to verify:
Known risks:
Next action:
```

**Resources:**

- [Handover and knowledge transfer](../07-consulting/coldfusion/10-client-consulting-and-delivery.md#handover-and-knowledge-transfer),
  in the Techversant ColdFusion consulting roadmap, for handing a whole system to a client

**Level:** Foundation · Core

## Technical debt

Technical debt is a shortcut, usually taken on purpose, that will cost time later. It is not a failure, as long as
it is visible and tracked.

**What to learn:**

- Recording each shortcut with the reason, the cost and the plan to fix it
- Using your project's issue tracker or debt register, not a forgotten comment in the code
- Raising debt you find, even when you did not create it

**Resources:** [Technical debt quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html), Martin Fowler

**Level:** Practitioner · Core

## Ownership

Owning your work means caring about it after it merges: fixing what you broke, flagging risks early and leaving code
better than you found it.

**What to learn:**

- Following your change into production, and fixing your own bugs first
- Flagging risks and shortcuts when you make them, not when someone else finds them
- Leaving the codebase easier to understand than you found it
- Documenting in the cheapest place that works: a clear name in the code, the reason in the commit message, or an
  ADR for a decision

**Resources:**

- [Ownership](../career-progression/02-junior-to-senior.md#ownership), in the Techversant Junior to Senior guide

**Level:** Practitioner · Core

## Project: Hand Over Your Feature

**Brief:** Imagine you are moving to another project tomorrow. Hand over your bookmarks feature to another engineer
so they can carry on without you.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] The bookmarks PR description follows the structure above, and links the design note and ADR
- [ ] A handoff note covers context, files and links, how to verify, known risks and the next action
- [ ] Another engineer follows the handoff note alone, runs the feature and its tests, and confirms nothing was
  missing
- [ ] At least one piece of technical debt from the feature is recorded as an issue with a reason and a plan
- [ ] You walked the other engineer through the note in a short call, and recorded their questions and answers in
  the note
- [ ] A one-paragraph status update summarizes the feature's state for your lead

Previous: [09. Code Review](./09-code-review.md) · Back to the [roadmap](./README.md#capstone) for the capstone
