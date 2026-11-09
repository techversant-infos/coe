# Practice App: Synthetic Support Assistant

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Every stage extends the same small assistant for a fictional service called Northstar Desk. The data is synthetic and
fixed so learners can practise retrieval, tool use, privacy and evaluation without real customer information. Back
to the [roadmap](./README.md).

## Build Contract

Use Python for the worked examples. TypeScript is an allowed alternative if you keep the same request, data and
evaluation contracts. A simple API service with a minimal chat page or command-line interface (CLI) is enough; the
goal is the AI feature, not a particular web framework. Keep the model adapter behind an application interface. The
hosted walkthrough uses the OpenAI Responses API; any provider your project approves can sit behind the same adapter.

The service has two trusted inputs: the user's message and a workspace identity supplied by the application or the test
fixture. The model may request `get_case_status(case_id)` or `get_case_summary(case_id)`, but it never supplies the
workspace identity. The server looks up the case only within the trusted workspace context and returns a generic
not-found result for unknown or out-of-scope IDs. The summary's case description is untrusted user text. The tools
have no write operation. The workspace check is authorisation code, which is Red Zone work under the AI Era Coding
Guidelines: write it by hand, without AI generation, and have a senior engineer review it, even on synthetic data. The
practice app has no real authentication.

## Fixed Dataset

| File | Contents |
|------|----------|
| [`data/support-cases.json`](./data/support-cases.json) | Twelve synthetic support cases, each with `case_id`, `workspace_id`, `status`, `plan`, `subject` and a user-written `description` |
| [`data/knowledge-base.json`](./data/knowledge-base.json) | Nine short synthetic help articles with stable IDs and revision dates |
| [`data/evaluation-cases.json`](./data/evaluation-cases.json) | Twenty-six starter cases covering supported, unsupported, ambiguous, retrieval, tool and injection behaviour |

Do not change these files when reporting the baseline. Keep new learner or cohort cases in a separate file and record
its version. The starter cases are visible practice material, not a hidden exam.

## Comparison Protocol

Everyone uses the same dataset and expected labels. A fair score comparison also requires the same model identifier
and provider, prompt version, generation settings, retrieval configuration, grader version and code version. If
any of those differ, report the configuration and compare the system to its own baseline rather than ranking learners.
Record the model identifier and run date; provider aliases and pricing change over time.

Keep credentials in an environment variable. An
optional local exercise can use an approved open-weight model served through vLLM's OpenAI-compatible endpoint.
Check the chosen model's licence, hardware requirements and feature support. Local inference is optional; this
practice guide does not approve any model provider for real client data.

## Local Data Rules

- The cases and articles are fictional. Do not add real people, contact details, customer records or client documents.
- Do not log full prompts, answers or user feedback by default.
- The tool exercise is read-only. Never connect the practice assistant to a real ticketing system.
- Do not put credentials in source control. Use a local environment file excluded by Git.
- Follow the [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md); this practice app does
  not authorise Red Zone work.

## Evaluation Labels

Each evaluation case has these fields:

| Field | Meaning |
|-------|---------|
| `eval_id` | The case's ID, such as `EVAL-001` |
| `input` | The user's message |
| `test_workspace_id` | The trusted workspace the request runs in, supplied by the test, never by the model |
| `answerable` | Whether the assistant should answer (`true`) or decline, ask for more or escalate (`false`) |
| `expected_article_ids` | Knowledge-base articles the answer should cite; empty when none apply |
| `required_facts` | Facts the answer must contain, or rules it must follow |
| `required_tools` | Tool calls the assistant must make, as `tool_name:CASE-ID`. Other read-only calls in the same workspace are allowed, except in cases tagged `tool_scope`, where only the listed calls are allowed |
| `tags` | Labels for grouping results, such as `retrieval`, `tool` or `indirect_injection` |

Do not treat exact wording as the target;
check the required facts, citations, declines and tool calls.
