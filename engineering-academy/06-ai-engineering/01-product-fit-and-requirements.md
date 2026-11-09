# 01. Product Fit and Requirements

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Start with the user's problem and the cost of getting it wrong. An LLM is one possible implementation; it is not a
product requirement. Back to the [roadmap](./README.md).

## Problem framing

Support teams need to find accurate answers and understand the status of a case. The practice app gives you a fixed
synthetic case and article set so you can test the workflow without handling real customer data.

**What to learn:**

- Identify the user, task, current workflow and measurable outcome
- Decide whether rules, search or a conventional service can solve the task more safely or cheaply
- Separate answerable questions from requests that need a human or more information
- Define error costs, latency expectations, accessibility needs and service boundaries

**Resources:** [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

**Level:** Practitioner · Core

## Project: Define the Support Assistant

**Brief:** Use the [practice app](./practice-app.md) cases to write a one-page product brief before implementing a
model call.

**Size:** 2–3 hours

**Verification**, checked by a reviewer:

- [ ] Name the user, task and current support workflow
- [ ] Compare an AI solution with a search-only or rules-based baseline
- [ ] Define one primary success measure and at least two guardrail measures
- [ ] List answerable, unanswerable and human-escalation cases
- [ ] Sketch where the user sees citations, uncertainty, loading and failure states
- [ ] Record what the assistant must never do, including changes to customer records

Next: [02. How LLMs Work](./02-how-llms-work.md)
