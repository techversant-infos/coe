# Practice App: Synthetic Support Assistant

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Every stage extends the same small assistant for a fictional service called Northstar Desk. The data is synthetic and
fixed so learners can practice retrieval, tool use, privacy and evaluation without real customer information.

## Build Contract

Use Python for the worked examples. TypeScript is an allowed alternative if the same request, data and evaluation
contracts are preserved. A simple API service and minimal chat page or CLI are enough; the goal is the AI feature,
not a particular web framework. Keep the model adapter behind an application interface and use the OpenAI Responses
API as the hosted walkthrough.

The service has two trusted inputs: the user's message and a workspace identity supplied by the application/test
fixture. The model may request `get_case_status(case_id)` or `get_case_summary(case_id)`, but it never supplies the
workspace identity. The server looks up the case only within the trusted workspace context and returns a generic
not-found result for unknown or out-of-scope IDs. The summary's case description is untrusted user text. The tools
have no write operation. This exercises authorization boundaries without implementing real authentication, which
is Red Zone work.

## Fixed Dataset

| File | Contents |
|------|----------|
| [`data/support-cases.json`](./data/support-cases.json) | Twelve synthetic support cases with case IDs, status, subject and user-written description |
| [`data/knowledge-base.json`](./data/knowledge-base.json) | Nine short synthetic help articles with stable IDs and revision dates |
| [`data/evaluation-cases.json`](./data/evaluation-cases.json) | Twenty-five starter cases covering supported, unsupported, ambiguous, retrieval, tool and injection behavior |

Do not change these files when reporting the baseline. Keep new learner or cohort cases in a separate file and record
its version. The starter cases are visible practice material, not a hidden exam.

## Comparison Protocol

Everyone uses the same dataset and expected labels. A fair score comparison also requires the same model identifier
and provider, prompt version, generation settings, retrieval configuration, evaluator version and code version. If
any of those differ, report the configuration and compare the system to its own baseline rather than ranking learners.
Record the model identifier and run date; provider aliases and pricing change over time.

Use the OpenAI Responses API for the hosted Python walkthrough. Keep credentials in an environment variable. An
optional local exercise can use an approved open-weight model served through vLLM's OpenAI-compatible endpoint.
Check the chosen model's license, hardware requirements and feature support. Local inference is optional; no model
provider is approved for real client data by this practice guide.

## Local Data Rules

- The cases and articles are fictional. Do not add real people, contact details, customer records or client documents.
- Do not log full prompts, answers or user feedback by default.
- The tool exercise is read-only. Never connect the practice assistant to a real ticketing system.
- Do not put credentials in source control. Use a local environment file excluded by Git.
- Follow the [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md); this practice app does
  not authorize Red Zone work.

## Evaluation Labels

Each evaluation case defines an expected intent, whether the assistant may answer, expected article IDs, key facts,
permitted tools and safety tags. A reviewer should check the labels before the first cohort uses them. Do not treat
exact wording as the target; assess the required facts, evidence, abstention or tool behavior.
