# 06. Tools and Workflows

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Give the model tools only when the product needs information or actions the model cannot provide itself. Keep
application code in charge of authorization, validation and execution. Back to the [roadmap](./README.md).

## Tool calls and deterministic workflows

A tool call is a model-proposed request, not permission to perform an action. The application validates every
argument and decides whether the current user may perform the operation.

**What to learn:**

- Define narrow tool schemas with typed, bounded inputs
- Validate IDs and arguments against trusted application state
- Prefer read-only tools for the practice assistant
- Keep deterministic rules and workflow state in ordinary application code
- Set timeouts, result-size limits and explicit error behavior

**Resources:** [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)

**Level:** Practitioner · Core

## Choosing an agent boundary

An agent loops over model decisions and tool results. That can help with open-ended tasks, but increases the number
of failure paths and makes behavior harder to predict. Start with a fixed workflow and justify every autonomous
step with evidence.

**What to learn:**

- Compare a fixed sequence, a single tool call and an agent loop for the same user task
- Set step, time and token limits
- Require a human to approve consequential or irreversible actions
- Stop safely when a tool fails, returns unexpected data or requests exceed the user's authority

**Resources:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)

**Level:** Advanced · Core

## Project: Add a Read-Only Case Lookup

**Brief:** Add read-only `get_case_status` and `get_case_summary` tools backed by the synthetic practice data. The
summary tool returns a case subject and description marked as untrusted text. The assistant may look up a supplied
case ID, but cannot create, close, refund or otherwise change a case.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] Each tool has a narrow purpose and documented input schema
- [ ] The application validates the case ID and enforces the learner's test identity boundary
- [ ] Both tools are read-only and the server, not the model, authorizes each call
- [ ] The summary labels case description as untrusted user text
- [ ] Invalid IDs, oversized output, timeout and service errors are handled safely
- [ ] The workflow has an explicit maximum number of model/tool turns
- [ ] A fixed workflow is used unless the project brief justifies an agent loop

Previous: [05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md) · Next:
[07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md)
