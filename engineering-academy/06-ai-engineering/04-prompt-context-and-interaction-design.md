# 04. Prompt, Context and Interaction Design

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Prompts and interface behavior form part of the product contract. The user needs to understand what the assistant
knows, what it does not know and what happens next. Back to the [roadmap](./README.md).

## Instructions and structured output

Keep task instructions, retrieved evidence and user input clearly separated. Validate model output before the
application uses it.

**What to learn:**

- State the task, constraints, evidence policy and abstention behavior explicitly
- Use examples only when they clarify the expected behavior
- Request structured output for application decisions, then validate it against a schema
- Version prompts and test prompt changes against the fixed evaluation set

**Resources:**

- [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)

**Level:** Practitioner · Core

## Interaction design

AI product interfaces need useful intermediate states. A user should not mistake a partial answer for a final one or
have to trust a confident answer without evidence.

**What to learn:**

- Stream partial output when it improves perceived responsiveness, and label it as in progress
- Show citations next to the claims they support
- Make uncertainty, missing evidence, escalation and retry states understandable
- Collect explicit user feedback with a reason code; do not treat a thumbs-up as ground truth
- Route reviewed feedback into a proposed evaluation case, with a human checking labels before use

**Resources:** [OpenAI streaming responses](https://developers.openai.com/api/docs/guides/streaming-responses)

**Level:** Practitioner · Core

## Project: Build the First Conversation

**Brief:** Connect the support assistant to the hosted walkthrough. Implement a simple answer flow before adding
retrieval or tools. Use the product brief and show uncertainty rather than inventing a support policy.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] Prompt and output contract are versioned outside application logic
- [ ] The service validates structured output before rendering it
- [ ] The interface shows loading, streaming, failure, uncertainty and retry states
- [ ] Citations have a visible placeholder contract for stage 05
- [ ] Feedback is stored only in the synthetic practice environment and is not auto-added to the evaluation labels
- [ ] Prompt changes run through a repeatable check on the shared cases

Previous: [03. Model Selection and Integration](./03-model-selection-and-integration.md) · Next:
[05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md)
