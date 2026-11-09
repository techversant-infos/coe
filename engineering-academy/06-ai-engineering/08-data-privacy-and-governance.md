# 08. Data Privacy and Governance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Every model request can move data across a boundary. Decide which data is allowed before you connect a model, and
keep the practice project entirely synthetic. This stage applies the Techversant AI Era Coding Guidelines and does
not authorise Red Zone work. Back to the [roadmap](./README.md).

## Mapping data flows

Trace where data goes: the browser, the application, the database, the model provider, logs and the feedback store.
You cannot protect data you have not mapped.

**What to learn:**

- Drawing a data-flow diagram with every store, service and trust boundary
- Classifying each field, such as public, internal or personal, and recording why the feature needs it
- Recording where each copy is stored, who can read it and how long it is kept

**Resources:** [Data & IP Compliance](../../standards/general/ai-era-coding-guidelines.md#53-data--ip-compliance)
(intellectual property), in the Techversant AI Era Coding Guidelines

**Level:** Practitioner · Core

## Data minimisation and redaction

The safest data is data you never send. Reduce what reaches the model, and remove sensitive values when a request
must include text that might contain them.

**What to learn:**

- Sending only the fields the task needs
- Detecting and masking personal data in text before it leaves the service, for example with Presidio. Automated
  detection misses some personal data, so treat it as one layer; on real work this code is Red Zone (manual only)
- Using synthetic data for development, tests and evaluation sets

**Resources:**

- [Presidio documentation](https://presidio.dataprivacystack.org/)
- [Sensitive information disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/),
  OWASP GenAI Security Project

**Level:** Practitioner · Core

## Provider terms, retention and region

Each provider sets how long it keeps requests, whether it uses them for training and where it processes them. These
terms decide whether a provider can be used for a client's data at all.

**What to learn:**

- Reading a provider's data-usage, retention and regional-processing terms
- Settings that store data by default: the Responses API keeps responses unless you send `store=False`, so record
  the choice in the decision record
- The client's approval as a requirement, separate from the provider's settings
- Recording these assumptions in a decision record without claiming compliance you have not confirmed

**Resources:** [Data controls](https://developers.openai.com/api/docs/guides/your-data), OpenAI documentation

**Level:** Advanced · Core

## The Red Zone boundary

Under the AI Era Coding Guidelines, authentication and authorisation, encryption and key management, handling of
personally identifiable information (PII), payment processing and production database migrations are manual-only.

**What to learn:**

- Treating any feature that sends PII to a model as Red Zone work
- Why provider controls are not approval: the security, privacy and client owners must agree first
- Stopping and escalating on a real engagement before processing sensitive data or changing an approved data flow

**Resources:** [Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the
Techversant AI Era Coding Guidelines

**Level:** Practitioner · Core

## Logging and retention

Prompts and answers often contain the most sensitive text in the system. Logs and traces should help you debug
without becoming a second copy of user data.

**What to learn:**

- Logging request IDs, model identifiers, token counts and timings by default, not prompts or answers
- Keeping secrets and personal data out of prompts, logs, traces and evaluation examples
- Retention and deletion rules for logs, feedback and stored conversations

**Resources:**
[What must never be logged](../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
in the Techversant security audit reference

**Level:** Practitioner · Core

## AI governance and documentation

Governance means someone can see what an AI feature does, what data it uses and who is responsible for it. Keep the
records short and current.

**What to learn:**

- A short system record: purpose, model and version, data sources, known limits, evaluation results and owner
- Reviewing the record when the model, prompt or data changes
- Using a risk framework, such as the US National Institute of Standards and Technology (NIST) AI Risk
  Management Framework, to check for gaps

**Resources:**

- [Model documentation](../../security/ai-security/ai-security-guidelines.md#83-model-documentation-model-cards), in
  the Techversant AI security guidelines
- [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST

**Level:** Advanced · Core

## Project: Document the Data Flow

**Brief:** Produce a data-flow diagram and a short decision record for the synthetic support assistant. Show the
trust boundaries and what would have to change before a client could approve a production data source.

**Size:** 3–4 hours

**Verification**, checked by a reviewer:

- [ ] Every data store, model boundary, log and feedback path appears on the diagram
- [ ] All sample records are synthetic, and the service accepts only the documented practice-data fields
- [ ] The decision record states provider, retention, region and approval assumptions, and claims no compliance it
  has not confirmed
- [ ] Logs and traces use request IDs and leave out prompts, answers and sensitive data by default
- [ ] Retention, deletion and access owners are recorded
- [ ] A system record lists purpose, model version, data sources, known limits and owner
- [ ] Red Zone work is excluded and assigned to a named human owner

Previous: [07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md) · Next:
[09. AI Security and Safety](./09-ai-security-and-safety.md)
