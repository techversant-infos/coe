# 08. Production and Security

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

The FDE has to show the client that an AI feature will not break, leak data or act beyond its authority.
Back to the [roadmap](./README.md).

## Evaluation in CI and production

Run your evaluation set on every change, and sample live results, so a drop in quality is caught early.

**What to learn:**

- Running evaluations in CI and failing the build on a drop in quality
- Sampling live results for human review, using an approved and privacy-safe process
- Watching for changes in quality, latency, cost and failure patterns after launch
- Re-running evaluations when the model, provider, prompt, tools, data or workflow changes
- Updating the evaluation set with reviewed production failures and representative edge cases
- Agreeing release thresholds and who can pause, roll back or route work to a person

**Resources:** builds on [Evaluations](./04-applied-ai.md#evaluations).

**Level:** Practitioner · Core

## Guardrails and fallbacks

Plan for the model being wrong, slow or unavailable.

**What to learn:**

- Validating model output before acting on it
- Timeouts, retries and a fallback, such as handing the case to a person
- Telling users clearly when an answer comes from AI

**Resources:** learn on engagements, with a lead.

**Level:** Practitioner · Core

## Tracing AI requests

Record each AI request so you can explain a bad answer: the prompt, the retrieved context, the tool calls, tokens and
time.

**What to learn:**

- Tracing model and tool calls alongside normal application traces
- Keeping personal data out of traces
- Using traces to find whether a failure came from retrieval, the prompt or the model

**Resources:** [OpenTelemetry semantic conventions for generative AI](https://github.com/open-telemetry/semantic-conventions-genai).
These conventions are still changing, so check the current version before you build.

**Level:** Advanced · Optional

## Cost and latency

AI costs grow with usage. A feature that is cheap in a demo can be expensive at the client's volume.

**What to learn:**

- Estimating monthly cost from expected volume
- Prompt caching, smaller models where they are good enough, batching
- Measuring response time and setting limits

**Resources:** [Claude prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

**Level:** Practitioner · Core

## AI security

AI features add new risks: instructions hidden in documents or emails (prompt injection), data leaking through
tools, and agents with too much authority.

**What to learn:**

- Treating all retrieved content and user input as untrusted
- Limiting what tools can do and to which data
- Connecting only MCP servers you trust, because they run with your permissions
- Testing your feature against the common AI attack patterns

**Resources:**

- [AI Security Guidelines](../../security/ai-security/ai-security-guidelines.md)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)

**Level:** Practitioner · Core

## Application security

The normal web security checks still apply to everything you build.

**What to learn:**

- Input validation, injection, access control and secrets handling
- Dependency updates and vulnerability scanning
- Running the Techversant security checklist on every pull request

**Resources:**

- [Security Audit Checklist](../../security/audit/security-audit-checklist.md)
- [OWASP Top 10:2025](https://top10.owasp.org/2025/)

**Level:** Practitioner · Core

## Privacy and data protection law

Personal data laws and client contracts decide what you may collect, where it may be stored and who may process it.

**What to learn:**

- The main obligations under GDPR, and under India's Digital Personal Data Protection (DPDP) Act 2023 and DPDP
  Rules 2025. The Rules were notified on 13 November 2025; most duties, including notice and consent, apply from
  13 May 2027
- Data residency and the client's contract terms with AI providers
- When to involve the client's data protection officer or legal team

**Resources:**

- [GDPR full text](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [DPDP Rules 2025 phased timeline, AZB & Partners](https://www.azbpartners.com/bank/update-indias-digital-personal-data-protection-framework-comes-into-effect/)

**Level:** Advanced · Core

## Project: Harden the Assistant for Production

**Brief:** Make the standards assistant safe to put in front of real users: catch quality drops, handle failures,
resist attacks and stay within budget.

**Size:** 3–4 days

**Verification**, checked by a senior engineer:

- [ ] The evaluation runs in CI, and weakening the prompt on purpose makes the build fail
- [ ] Written release thresholds cover quality, safety, latency and cost; a reviewer can identify who approves a release and who can pause or roll it back
- [ ] A post-launch review uses a small stream of synthetic or approved, privacy-safe cases to find failures; each finding is triaged, and at least one reviewed failure or edge case is added to the evaluation set
- [ ] A model, provider, prompt, tool, data or workflow change triggers the evaluation; the report records what
  changed and the decision to release, hold or roll back
- [ ] When the model times out or returns an error, the user sees a clear message and the ticket goes to a person
- [ ] Ten prompt-injection test cases, with hidden instructions inside documents and tickets: the assistant follows
  none of them and reveals no instructions or data
- [ ] Traces show the prompt, retrieved passages, tool calls, tokens and response time. Test tickets contain seeded
  synthetic names and email addresses, and searching the traces for those exact values finds nothing
- [ ] A cost estimate for 10,000 requests a month, checked against the measured cost of 100 requests
- [ ] Every release-blocking **(B)** item in the [Security Audit Checklist](../../security/audit/security-audit-checklist.md)
  is done, or not applicable with a written reason. Other items and the
  [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) are done, not applicable with a reason,
  or open with an owner
- [ ] A one-page privacy note: which personal data is processed, where it is stored and which provider processes it

Previous: [07. Cloud and Operations](./07-cloud-and-operations.md) · Next: [09. Client Delivery](./09-client-delivery.md)
