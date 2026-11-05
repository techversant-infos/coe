# 08. Production and Security

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

The FDE has to show the client that an AI feature will not break, leak data or act beyond its authority.
Back to the [roadmap](./README.md).

## Evaluation in CI and production

Run your evaluation set on every change, and sample live results, so a drop in quality is caught early.

**What to learn:**

- Running evaluations in CI and failing the build on a drop in quality
- Sampling live results for human review
- Re-running evaluations when the model or provider changes

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

**Resources:** [OpenTelemetry semantic conventions for generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

**Level:** Advanced · Optional

## Cost and latency

AI costs grow with usage. A feature that is cheap in a demo can be expensive at the client's volume.

**What to learn:**

- Estimating monthly cost from expected volume
- Prompt caching, smaller models where they are good enough, batching
- Measuring response time and setting limits

**Resources:** [Claude prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching)

**Level:** Practitioner · Core

## AI security

AI features add new risks: instructions hidden in documents or emails (prompt injection), data leaking through
tools, and agents with too much authority.

**What to learn:**

- Treating all retrieved content and user input as untrusted
- Limiting what tools can do and to which data
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
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

**Level:** Practitioner · Core

## Privacy and data protection law

Personal data laws and client contracts decide what you may collect, where it may be stored and who may process it.

**What to learn:**

- The main obligations under GDPR and India's Digital Personal Data Protection (DPDP) Act
- Data residency and the client's contract terms with AI providers
- When to involve the client's data protection officer or legal team

**Resources:**

- [GDPR full text](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [India data protection framework](https://www.meity.gov.in/data-protection-framework)

**Level:** Advanced · Core

## Project: Harden the Assistant for Production

**Brief:** Make the standards assistant safe to put in front of real users: catch quality drops, handle failures,
resist attacks and stay within budget.

**Size:** 3–4 days

**Verification**, checked by a senior engineer:

- [ ] The evaluation runs in CI, and weakening the prompt on purpose makes the build fail
- [ ] When the model times out or returns an error, the user sees a clear message and the ticket goes to a person
- [ ] Ten prompt-injection test cases, with hidden instructions inside documents and tickets: the assistant follows
  none of them and reveals no instructions or data
- [ ] Traces show the prompt, retrieved passages, tool calls, tokens and response time, and a search of the traces
  finds no email addresses or names
- [ ] A cost estimate for 10,000 requests a month, checked against the measured cost of 100 requests
- [ ] Every item in the [Security Audit Checklist](../../security/audit/security-audit-checklist.md) and the
  [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is marked done, not applicable, or open
  with an owner
- [ ] A one-page privacy note: which personal data is processed, where it is stored and which provider processes it

Previous: [07. Cloud and Operations](./07-cloud-and-operations.md) · Next: [09. Client Delivery](./09-client-delivery.md)
