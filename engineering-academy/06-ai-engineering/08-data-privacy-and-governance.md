# 08. Data Privacy and Governance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Model requests can move data across a system boundary. Decide what data is allowed before connecting a model, and
keep the practice project entirely synthetic. This stage applies the Techversant AI Era Coding Guidelines;
it does not authorize Red Zone work. Back to the [roadmap](./README.md).

## Map and minimize data

Trace what enters the browser, application, database, model provider, logs and feedback store. Reduce the data the
feature needs and document the reason for each field.

**What to learn:**

- Classify data and map its processing path, storage location, retention and access
- Minimize, redact or avoid data before model submission
- Check provider terms, retention controls, regional processing and client approval
- Keep secrets and personal/client data out of prompts, logs, traces and evaluation examples
- Design deletion, retention and incident escalation with the service owner

**Resources:**

- [Techversant AI Era Coding Guidelines, Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data)

**Level:** Advanced · Core

## Red Zone boundary

Under Techversant's current guidelines, authentication and authorization, encryption and key management, PII
handling, payment processing and production database migrations are manual-only. Treat sending PII to a model as
Red Zone work: do not do it in this course or treat provider controls as approval. Do not send personal or client
data to a model in this course. For real engagements, stop and involve the designated security, privacy and client
owners before processing sensitive data or changing the approved data flow.

## Project: Document the Data Flow

**Brief:** Produce a data-flow diagram and a short decision record for the synthetic support assistant. Identify the
trust boundaries and show what would have to change before a client could approve a production data source.

**Size:** 3–4 hours

**Verification**, checked by a reviewer:

- [ ] Every data store, model boundary, log and feedback path is shown
- [ ] All sample records are synthetic and the service accepts only the documented practice-data schema
- [ ] The record states provider, retention, region and approval assumptions without inventing compliance guarantees
- [ ] Logs and traces use synthetic request IDs and omit prompts, answers and sensitive payloads by default
- [ ] Retention, deletion and access ownership are documented
- [ ] Red Zone implementation is excluded and escalated to the appropriate human owner

Previous: [07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md) · Next:
[09. AI Security and Safety](./09-ai-security-and-safety.md)
