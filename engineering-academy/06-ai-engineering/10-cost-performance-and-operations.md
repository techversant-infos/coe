# 10. Cost, Performance and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

A production AI feature has a predictable cost, acceptable speed, visible failures and a safe way to change or roll
back. Measure the whole request path, including retrieval and tools. Back to the [roadmap](./README.md).

## Cost per request and budgets

Model costs grow with every token and every user. Estimate them before launch and set limits that stop surprises.

**What to learn:**

- Estimating cost per request from token counts and current provider pricing, then at expected volume
- Limits on input and output tokens, retries, tool turns and retrieved passages
- Budget alerts, and what the feature does when a budget is reached

**Resources:** [Pricing](https://developers.openai.com/api/docs/pricing), OpenAI documentation, and
[Pricing](https://platform.claude.com/docs/en/about-claude/pricing), Claude documentation

**Level:** Advanced · Core

## Latency

Users feel the slowest requests, not the average. Measure each part of the request path and the whole flow.

**What to learn:**

- Measuring the 50th and 95th percentile (p50 and p95) latency for retrieval, model calls and the full flow
- Time to first token, and why streaming improves how fast the feature feels
- Choosing a smaller model, shorter prompts or fewer steps when evaluations show quality stays acceptable

**Resources:** [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), Claude documentation

**Level:** Advanced · Core

## Caching and batch processing

Caching avoids paying twice for the same work. Batch processing runs requests that do not need an instant answer at
a lower price.

**What to learn:**

- Prompt caching for a stable start to every prompt, such as instructions and tool definitions. Caching needs a
  minimum prompt length and may charge extra for cache writes; check the cached-token counts in the usage data
- Caching retrieval results or full answers, keyed by workspace and prompt version, and never shared across
  workspaces; deciding when cached answers go out of date
- Batch APIs for work such as running the evaluation set overnight

**Resources:**

- [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), Claude documentation, and
  [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching), OpenAI documentation
- [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing), Claude documentation,
  and [Batch API](https://developers.openai.com/api/docs/guides/batch), OpenAI documentation

**Level:** Advanced · Core

## Reliability and fallbacks

Providers have outages and rate limits. Decide what the user sees when the model is slow or unavailable.

**What to learn:**

- Timeouts, rate-limit handling and retries with a limit on attempts
- Fallbacks, such as a second model or search results without a generated answer, tested with the evaluation set
- A clear degraded state for the user, instead of a spinner that never ends

**Resources:** [Handling overload](https://sre.google/sre-book/handling-overload/), Google Site Reliability
Engineering (SRE) book

**Level:** Advanced · Core

## Observability

You need to see each request's path through retrieval, model calls and tools to debug failures and track cost.
Do this without copying user data into logs.

**What to learn:**

- Traces with a span for each retrieval, model call and tool call, using the OpenTelemetry generative AI conventions
- Dashboards for latency, errors, token use, cost, declines and escalations
- Leaving prompt and answer text out of traces by default

**Resources:** [Generative AI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai),
OpenTelemetry, still in development status

**Level:** Advanced · Core

## Releasing changes safely

Model, prompt, retrieval and data changes can each alter behaviour. Release them like code: tested, gradual and easy
to undo.

**What to learn:**

- Versioning the model, prompt, retrieval settings and dataset separately
- Rolling out a change gradually behind a feature flag, comparing with the previous version
- A runbook for provider outages, poor retrieval, budget alerts and rollback

**Resources:**

- [OpenFeature](https://openfeature.dev/), an open standard for feature flags
- [Git Workflow](../../standards/git/git-workflow.md), Techversant standard, for promotion and rollback

**Level:** Advanced · Core

## Project: Release and Operate the Assistant

**Brief:** Deploy the synthetic assistant to a practice environment. Run the fixed evaluation set before and after a
versioned change, watch performance and cost, and show a rollback. Never deploy with real user or client data.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Deployment uses environment configuration and keeps no secrets in source control
- [ ] A dashboard or report shows p50 and p95 latency, model latency, errors, token use and estimated cost
- [ ] Traces cover retrieval, model and tool calls, and leave out prompt and answer text by default
- [ ] Budget limits, timeouts and a provider failure are tested, and the user sees a clear degraded state
- [ ] A model, prompt or retrieval change runs the evaluation and security cases before release
- [ ] The change rolls out behind a flag, and a reviewer can roll it back using the runbook
- [ ] The final report records the evaluation configuration and any quality, latency or cost regression

Previous: [09. AI Security and Safety](./09-ai-security-and-safety.md) · Back to the [roadmap](./README.md#capstone)
for the capstone
