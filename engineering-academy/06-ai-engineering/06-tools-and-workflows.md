# 06. Tools and Workflows

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Give the model tools only when the product needs information or actions the model cannot provide itself. Application
code stays in charge of checking, authorising and running every call. Back to the [roadmap](./README.md).

## Tool calling

With tool calling, the model asks your application to run a function, such as looking up a case. The model only
proposes the call; your code decides whether to run it.

**What to learn:**

- Describing a tool with a name, a purpose and an input schema
- The request-and-response loop: the model asks, the application runs the tool, the result goes back to the model
- Writing tool descriptions the model can follow, and testing that it picks the right tool

**Resources:**

- [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), Claude documentation
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling), OpenAI documentation

**Level:** Practitioner · Core

## Validating tool inputs and authority

Treat every tool call as untrusted input. The application checks the arguments and the user's rights before it runs
anything.

**What to learn:**

- Narrow tools with typed, bounded inputs, and read-only tools wherever possible
- Checking IDs against trusted application state, such as the user's workspace, never against what the model says
- Writing that check by hand: authorisation code is Red Zone work under the AI Era Coding Guidelines
- Timeouts, result-size limits and a clear error result the model can handle

**Resources:**

- [Input validation](../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/), risks in large language model (LLM)
  applications

**Level:** Practitioner · Core

## Fixed workflows

Most features work best as a fixed sequence of steps written in ordinary code, with the model doing one job in each
step. Fixed workflows are easier to test and predict than agents.

**What to learn:**

- Patterns such as chaining steps, routing a request to the right handler, and checking output before the next step
- Keeping business rules and workflow state in application code, not in the prompt
- Testing each step on its own

**Resources:** [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents),
Anthropic

**Level:** Practitioner · Core

## Agent loops

An agent lets the model choose its next step and call tools in a loop until it decides it is done. That helps with
open-ended tasks, but adds failure paths and makes behaviour harder to predict.

**What to learn:**

- Comparing a fixed workflow, a single tool call and an agent loop on the same task
- Limits on steps, time and tokens, and a safe stop when a limit is reached
- Stopping when a tool fails, returns unexpected data or the request goes beyond the user's rights

**Resources:** [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents),
Anthropic

**Level:** Advanced · Core

## Human approval

Some actions should never happen on the model's decision alone, such as closing a case, refunding money or sending
a message. A person approves them first.

**What to learn:**

- Deciding which actions need approval, based on harm and whether they can be undone
- Showing the approver exactly what will happen, with the evidence behind it
- Recording who approved what, and when

**Resources:** [Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the
Techversant AI Era Coding Guidelines

**Level:** Advanced · Core

## Model Context Protocol

The Model Context Protocol (MCP) is a standard way to connect models to tools and data. An MCP server exposes tools
that any compatible client can use.

**What to learn:**

- How MCP clients, servers and tools fit together
- The security risks of connecting servers you do not control, and the protocol's security guidance

**Resources:**

- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)

**Level:** Practitioner · Optional

## Project: Add a Read-Only Case Lookup

**Brief:** Add read-only `get_case_status` and `get_case_summary` tools backed by the practice data. The summary tool
returns the case subject and description, marked as untrusted text. The assistant can look up a case ID the user
gives, but cannot create, close, refund or otherwise change a case.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] Each tool has one purpose and a documented input schema
- [ ] The application checks the case ID against the trusted workspace from the request, not the model's arguments,
  and that check is written by hand and reviewed by a senior engineer
- [ ] Both tools are read-only, and the server decides whether each call runs
- [ ] The summary marks the case description as untrusted user text
- [ ] Invalid IDs, cases in another workspace, oversized output, timeouts and service errors are handled safely
- [ ] The workflow has a fixed maximum number of model and tool turns
- [ ] The service uses a fixed workflow, unless the pull request explains why an agent loop is needed

Previous: [05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md) · Next:
[07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md)
