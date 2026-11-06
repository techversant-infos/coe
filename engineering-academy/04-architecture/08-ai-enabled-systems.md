# 08. AI-Enabled Systems

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

More client systems now include features built on large language models (LLMs). An architect decides where AI fits,
how it is fed data, how its quality is measured and what it costs. Back to the [roadmap](./README.md).

## Where AI fits in a system

An LLM is one component among many: slow, costly per call and sometimes wrong. Design around those facts, and use AI
only where it beats a simpler solution.

**What to learn:**

- Treating the model as an external service behind your own interface, so it can be swapped
- Running AI work in the background where users do not need the answer straight away
- Choosing between providers and models on quality, cost, speed and where data is processed

**Resources:**

- [How LLMs work](../08-forward-deployed-engineering/04-applied-ai.md#how-llms-work) and
  [choosing models and providers](../08-forward-deployed-engineering/04-applied-ai.md#choosing-models-and-providers),
  in the Techversant FDE roadmap

**Level:** Advanced · Core

## Retrieval and data access

Models only know what they were trained on and what you send them. Retrieval finds the right client data for each
request, within the user's permissions.

**What to learn:**

- Retrieval-augmented generation: searching for relevant content and adding it to the request
- Keeping retrieval inside the user's access rights, so the model never sees data the user could not
- Which data may be sent to an external provider, and which must stay inside the client's systems

**Resources:**

- [Retrieval and vector search](../08-forward-deployed-engineering/04-applied-ai.md#retrieval-and-vector-search),
  in the Techversant FDE roadmap
- [Handling and retention](../../security/audit/security-audit-reference.md#163-handling-and-retention), in the
  Techversant security audit reference, including where data may be transferred

**Level:** Advanced · Core

## Evaluations and guardrails

You cannot test an AI feature by reading a few answers. Evaluations measure quality on a fixed set of examples, and
guardrails catch bad output before users see it.

**What to learn:**

- Building an evaluation set from real examples, and running it on every change to prompts or models
- Guardrails on input and output, and a fallback when the model fails or refuses
- Monitoring quality in production, not only at launch

**Resources:**

- [Evaluations](../08-forward-deployed-engineering/04-applied-ai.md#evaluations) and
  [guardrails and fallbacks](../08-forward-deployed-engineering/08-production-and-security.md#guardrails-and-fallbacks),
  in the Techversant FDE roadmap

**Level:** Advanced · Core

## AI cost and latency

AI providers charge by the amount of text sent and received, and large models can take seconds to answer. Both must
fit the budget and the user experience.

**What to learn:**

- Estimating cost per request and per month from expected volumes and text sizes
- Caching results, using smaller models where they are good enough, and batching background work
- Streaming answers, or moving work to the background, when users would otherwise wait

**Resources:**

- [Cost and latency](../08-forward-deployed-engineering/08-production-and-security.md#cost-and-latency), in the
  Techversant FDE roadmap

**Level:** Practitioner · Core

## AI security and governance

AI features bring new risks, such as prompt injection and leaked data, and clients increasingly ask how AI use is
governed.

**What to learn:**

- The OWASP Top 10 for LLM applications, especially prompt injection and sensitive information disclosure
- Techversant's rules for using AI, and how they apply to features you build for clients
- Recording what each AI feature does, which data it uses and who is accountable for it

**Resources:**

- [AI Security Guidelines](../../security/ai-security/ai-security-guidelines.md), Techversant
- [OWASP Top 10 for LLM applications](https://genai.owasp.org/llm-top-10/)
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST

**Level:** Advanced · Core

## Project: Design the Article Summary Feature

**Brief:** Lantern wants AI summaries at the top of long articles and suggestions for related articles. Design both
features, build a small prototype of the summary to measure quality and cost, and show how they fit the budget.
Use an AI provider approved by Techversant, with an API key agreed with your lead.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] An updated container diagram shows where the AI components sit, behind an interface of your own
- [ ] An ADR records the choice of provider and model, with at least two options compared on quality, cost, speed
  and where data is processed
- [ ] The design states which data is sent to the provider, and confirms no personal data from readers is sent
- [ ] An evaluation set of at least 30 long, openly licensed articles, such as public-domain texts or Wikipedia
  articles loaded into the practice app, each with a checked summary, is run against the prototype, and the results are recorded
- [ ] The design states what readers see when the provider is slow, fails or returns an unsafe summary
- [ ] A monthly cost estimate for summaries and suggestions at the brief's volumes fits inside the overall budget
  from stage 07
- [ ] All ten items in the OWASP Top 10 for LLM applications are listed, each marked relevant or not with a reason,
  and each relevant item has a mitigation

Previous: [07. Cloud and Cost](./07-cloud-and-cost.md) · Next:
[09. Modernization and Migration](./09-modernization-and-migration.md)
