# How to Teach the Developer Excellence Curriculum

> **Audience:** the *facilitator* â€” the senior developer or tech lead who runs the pilot batch. Not a learner doc.
> **Read alongside:** [curriculum.md](./curriculum.md) (the content) + [gap-analysis.md](./gap-analysis.md) (what's deliberately skipped, for context).

---

## Why this is a separate doc

The curriculum is what the *learner* reads. This doc is what the *facilitator* reads. They're different audiences, and they ask different questions:

- **Learner:** *what do I do this week?*
- **Facilitator:** *how do I run this so it actually lands?*

Keeping them in one file means the learner skips past 30 lines of facilitator advice on every read. This doc keeps the curriculum clean for learners and gives the facilitator a focused reference.

---

## What makes the content land

**âœ” Use one simple codebase and evolve it step by step.**
Pick one codebase the team knows. Don't teach SOLID with five toy examples â€” teach SOLID by evolving *their* `PaymentProcessor`. Don't teach REST with a fresh project â€” review an existing API and refactor it.

**âœ” Refactor live during sessions.**
The "before" is a real class in the repo. The "after" is the refactor in real time. The team sees the *decisions* â€” why the developer chose to extract a service *here*, not *there*. Pre-record the refactor only if the team is remote; live is always better.

**âœ” Show before vs. after.**
Every topic has a "before" and an "after." The "before" is the smell. The "after" is the fix. The team's habit, after enough topics, is to *see the smell first* â€” to recognize the pattern in their own PRs.

**âœ” Tie every concept to:**
- **Real production bugs** â€” "this exact pattern caused incident #2143 in production. Here's the postmortem."
- **Real code review comments** â€” "this exact comment is on PR #1827. The author pushed back; here's the resolution."
- **Real maintenance pain points** â€” "this exact abstraction slowed us down in the Q3 migration. Here's why."

**âœ” Run in pairs.**
The pair format is the single biggest predictor of pilot success. A solo developer reads the topic; a pair *discusses* the topic. The discussion is where the discipline lands.

**âœ” Time-box the topics.**
One session, one topic, one mini-task. Don't combine two topics. The mini-task is the *transfer* â€” if the developer can't apply it to a real PR, the session didn't land.

**âœ” Review the mini-task.**
The mini-task is the assignment; the review is the feedback. The senior developer who runs the pilot also reviews the mini-task PRs. The review is the teaching moment, not the session.

**âœ” Document the run.**
After the pilot, write 1 page: what worked, what didn't, what to change for v0.2. Feed it back into this curriculum via a PR.

---

## How to measure pilot success (optional)

The learner-facing curriculum does not include team-level metrics â€” that's a manager concern, not a learner concern. If you're running a pilot and need to report up, the metrics to track are:

- **PR cycle time** â€” should decrease for senior developers (cleaner code lands faster on first review)
- **Defect escape rate** â€” should decrease (testable, refactored code is easier to verify)
- **Code-review comment quality** â€” should improve (objective questions, not "this is bad")
- **Tech-debt awareness** â€” should increase (developers flag the debt *they* create)
- **Mentoring hours** â€” should become a tracked activity, not an undocumented one

How to measure: tag the PRs with the topic number from the curriculum (e.g. `refactor/clean-code-1`). Review at Week 2 and Week 6.

---

## Document control

| Field | Value |
|---|---|
| Document | How to Teach the Developer Excellence Curriculum |
| Version | 0.1 (initial â€” extracted from curriculum.md v0.3) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](./curriculum.md), [README.md](./README.md), [gap-analysis.md](./gap-analysis.md) |
