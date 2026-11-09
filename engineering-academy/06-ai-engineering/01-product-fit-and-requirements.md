# 01. Product Fit and Requirements

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Start with the user's problem and the cost of getting it wrong. A large language model (LLM) is one possible way to
solve a problem, not a requirement in itself. Back to the [roadmap](./README.md).

## Problem framing

An AI feature starts as an ordinary product problem: who the user is, what they are trying to do, and how you will
know it worked. The practice app gives you a fixed set of synthetic support cases, so you can study the workflow
without real customer data.

**What to learn:**

- Describing the user, the task, the current workflow and where time or quality is lost
- Writing one measurable outcome, such as "support agents find the right help article in under a minute"
- Setting service boundaries: which questions the feature answers, and which it hands to a person

**Resources:** [People + AI Guidebook](https://pair.withgoogle.com/guidebook/), Google

**Level:** Practitioner · Core

## Choosing between AI and simpler solutions

Many problems that look like AI problems are solved more cheaply and reliably with rules, search or a form. Compare
the AI option with a simpler baseline before you build it.

**What to learn:**

- Tasks that suit an LLM, such as summarising or answering from varied text, and tasks that do not, such as exact
  calculations or fixed business rules
- Building a non-AI baseline, such as keyword search over help articles, to compare against
- The extra work an AI feature brings: evaluation, monitoring, cost per request and changing model versions

**Resources:** [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml), Google
for Developers

**Level:** Practitioner · Core

## Error costs and human oversight

An AI feature will sometimes be wrong. Decide early what a wrong answer costs, who can catch it, and what the feature
must never do.

**What to learn:**

- Listing the ways the feature can fail, such as a wrong answer, a missing citation or an action on the wrong case
- Rating each failure by harm and by how likely a user is to notice it
- Deciding where a person reviews, approves or takes over, and how the user reaches that person

**Resources:** [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), US National
Institute of Standards and Technology (NIST)

**Level:** Practitioner · Core

## Success and guardrail measures

A success measure shows whether the feature helps. Guardrail measures show whether it causes harm while doing so.
Both need numbers you can measure on the evaluation set and, later, in production.

**What to learn:**

- Choosing one primary success measure, such as the share of supported questions answered with the right article
- Choosing guardrail measures, such as unsupported answers, wrong-case lookups, latency and cost per request
- Setting targets before you build, so results are judged against a plan and not adjusted to fit

**Resources:**
[Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests),
Claude documentation

**Level:** Practitioner · Core

## Project: Define the Support Assistant

**Brief:** Use the [practice app](./practice-app.md) cases to write a one-page product brief before you write any
model call.

**Size:** 2–3 hours

**Verification**, checked by a reviewer:

- [ ] The brief names the user, the task and the current support workflow
- [ ] It compares the AI option with a search-only or rules-based baseline
- [ ] It defines one primary success measure and at least two guardrail measures, each with a target
- [ ] It lists answerable, unanswerable and escalation cases, using examples from the practice data
- [ ] It sketches where the user sees citations, uncertainty, loading and failure states
- [ ] It records what the assistant must never do, including changing customer records

Next: [02. How LLMs Work](./02-how-llms-work.md)
