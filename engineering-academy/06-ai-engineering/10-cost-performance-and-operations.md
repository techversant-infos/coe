# 10. Cost, Performance and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Production readiness includes predictable cost, acceptable latency, observable failures and a safe way to change or
roll back model behavior. Measure the whole request path, including retrieval and tools. Back to the
[roadmap](./README.md).

## Cost, latency and reliability

Set budgets from expected use and the product's requirements. Measure under representative conditions rather than
assuming a model choice will meet the target.

**What to learn:**

- Estimate cost per request and at expected volume using current provider pricing
- Measure p50 and p95 latency for retrieval, model calls and the complete user flow
- Bound input/output tokens, retries, tool turns and retrieval result sizes
- Use caching, smaller models or asynchronous work only when evaluations show quality remains acceptable
- Define timeouts, rate-limit handling, fallbacks and user-visible degraded behavior

**Resources:**

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

**Level:** Advanced · Core

## Operate and change the feature

Model, prompt, retrieval and source-data changes can alter behavior. Treat each as a release that must pass the
evaluation and security checks for the service.

**What to learn:**

- Version model, prompt, retrieval configuration and dataset separately
- Monitor quality indicators, refusal/escalation rates, errors, latency and cost without logging private payloads
- Collect user feedback and route reviewed examples into the evaluation process
- Roll out changes gradually, compare against the prior version and keep a rollback path
- Write a runbook for provider outage, degraded retrieval, budget alerts and rollback

**Resources:**

- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Google SRE book](https://sre.google/sre-book/table-of-contents/)

**Level:** Advanced · Core

## Project: Release and Operate the Assistant

**Brief:** Deploy the synthetic assistant to a practice environment. Run the fixed evaluation before and after a
versioned change, observe performance and cost, and demonstrate rollback. Do not deploy with real user or client
data.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Deployment uses environment configuration and stores no secrets in source control
- [ ] A dashboard or report shows total request latency, model latency, errors, token use and estimated cost
- [ ] Logs and traces omit prompt and answer payloads by default
- [ ] Budget, timeout and provider-failure behavior are exercised
- [ ] A model, prompt or retrieval change runs the evaluation and security regression cases
- [ ] A reviewer can roll back to the previous known-good configuration using the runbook
- [ ] The final report records the evaluation configuration and any quality, latency or cost regression

Previous: [09. AI Security and Safety](./09-ai-security-and-safety.md)
