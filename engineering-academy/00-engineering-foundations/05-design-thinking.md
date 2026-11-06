# 05. Design Thinking

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

The most expensive mistakes happen before any code is written: solving the wrong problem, or picking a design
without knowing what it gives up. This stage covers thinking a change through first. Back to the
[roadmap](./README.md).

## Understanding the problem

Before designing anything, make sure you know who needs the change, what they are trying to do and how you will know
it works.

**What to learn:**

- Asking who the users are, what they do today and what problem the change solves
- Writing acceptance criteria that can be tested
- Listing what is out of scope, so the change stays small

**Resources:** learn with a reviewer, and from your project's requirements and tickets.

**Level:** Practitioner · Core

## Change scenarios

Good designs survive the changes that are likely to come. Thinking through a few likely changes shows where the
design needs to be flexible, and where it does not.

**What to learn:**

- Listing three or four realistic changes, such as a new field, ten times more users or a second client app
- Checking how much of the design each change would touch
- Not building for changes that are unlikely: flexibility has a cost too

**Resources:** *The Pragmatic Programmer*, Andrew Hunt and David Thomas, on reversibility

**Level:** Practitioner · Core

## Trade-offs

Every design choice gives something up. Writing down the options and what each costs leads to better decisions, and
helps reviewers understand yours.

**What to learn:**

- Comparing at least two options for each important decision
- Weighing simplicity, performance, cost, time and risk
- Choosing the simplest option that meets the need

**Resources:** the
[Software Architect roadmap](../04-architecture/README.md) goes deeper, for when you want to move into design work.

**Level:** Practitioner · Core

## Domain modelling

A domain model describes the things the business cares about and the rules between them. Code that uses the
business's own words is easier to discuss with clients and harder to get wrong.

**What to learn:**

- Finding the main entities and their relationships, such as article, author, comment and tag
- Using the same words in the code as the business uses
- Putting each rule next to the data it protects

**Resources:** [Ubiquitous language](https://martinfowler.com/bliki/UbiquitousLanguage.html), Martin Fowler

**Level:** Practitioner · Core

## Architecture decision records

An architecture decision record (ADR) is a short document for one decision: the context, the decision and its
consequences. ADRs stored in the repository explain to future developers why the code is the way it is.

**What to learn:**

- The format: title, status, context, decision and consequences
- Writing an ADR in under a page, at the time of the decision
- Replacing an old ADR with a new one when a decision changes

**Resources:**

- [Documenting architecture decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions),
  Michael Nygard, who proposed the format
- [ADR templates](https://adr.github.io/)

**Level:** Practitioner · Core

## Project: Design Article Bookmarks

**Brief:** Design the article bookmarks feature described in the [practice app](./practice-app.md) before building
it. Write a one-page design note and an ADR for the most important decision.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The design note states who the feature is for, the problem it solves and what is out of scope
- [ ] At least four acceptance criteria are written so each can be tested
- [ ] The note lists the data the feature stores and the API endpoints it needs, using RealWorld's existing words
  for articles and users
- [ ] Three change scenarios are listed, such as bookmark folders or sharing, with how much of the design each would
  touch
- [ ] An ADR in the repository records one decision, such as how bookmarks are stored, with at least two options
  compared
- [ ] The design is reviewed in a PR before you start building

Previous: [04. Design Principles](./04-design-principles.md) · Next:
[06. APIs and Boundaries](./06-apis-and-boundaries.md)
