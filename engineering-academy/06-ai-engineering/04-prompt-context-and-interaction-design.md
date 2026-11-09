# 04. Prompt, Context and Interaction Design

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Prompts and the way the interface behaves are part of the product. The user needs to understand what the assistant
knows, what it does not know and what happens next. Back to the [roadmap](./README.md).

## Instructions and prompt structure

Clear instructions solve most quality problems. Keep the task instructions, the evidence and the user's message in
separate, labelled parts of the prompt.

**What to learn:**

- Stating the task, the limits, the evidence rules and when to say "I don't know"
- Using examples only when they make the expected output clearer
- Keeping prompts in version control, outside application logic, and testing every change on the evaluation set

**Resources:**

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview),
  Claude documentation
- [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), OpenAI documentation

**Level:** Practitioner · Core

## Structured output

When the application acts on the model's answer, ask for a fixed structure and check it before use. Free text is for
people; structured output is for code.

**What to learn:**

- Requesting JSON that matches a schema, using the provider's structured-output feature
- Validating the result with a schema library, such as Pydantic, before the application uses it
- Handling a response that fails validation as an error, not as a partial answer

**Resources:**

- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), Claude
  documentation, and [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs), OpenAI
  documentation
- [Pydantic documentation](https://docs.pydantic.dev/latest/)

**Level:** Practitioner · Core

## Managing conversation context

A conversation grows with every turn, but the context window does not. Decide what each request must contain.

**What to learn:**

- Choosing what goes into each request: instructions, recent turns, a summary of older turns and the evidence
- Keeping instructions and safety rules in every request, even when history is shortened
- Keeping the stable part of the prompt first, which also lets providers cache it (stage 10)

**Resources:** [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude
documentation

**Level:** Practitioner · Core

## Interaction design

AI features need clear in-between states. A user should not mistake a partial answer for a final one, or have to
trust a confident answer without evidence.

**What to learn:**

- Streaming the answer when it makes the feature feel faster, and showing that it is still in progress
- Showing citations next to the claims they support
- Making uncertainty, missing evidence, escalation and retry states clear, including to screen-reader users

**Resources:**

- [People + AI Guidebook](https://pair.withgoogle.com/guidebook/), Google
- [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), Claude documentation

**Level:** Practitioner · Core

## User feedback

User feedback shows where the feature fails in real use. It is a signal to investigate, not a correct label.

**What to learn:**

- Collecting feedback with a reason, such as "wrong article" or "did not answer", not only a thumbs-up or down
- Reviewing feedback before it becomes an evaluation case, with a person checking the expected answer
- Storing feedback without personal data, and only in the practice environment for this course

**Resources:** [People + AI Guidebook](https://pair.withgoogle.com/guidebook/), Google

**Level:** Practitioner · Core

## Images and documents as input

Many models also read images and PDF documents. This helps with screenshots or scanned forms, but adds cost and new
places for hidden instructions.

**What to learn:**

- Sending an image or document with a request, and the token cost it adds
- Treating text inside an image or file as untrusted input, like any other user content

**Resources:** [Vision](https://platform.claude.com/docs/en/build-with-claude/vision), Claude documentation

**Level:** Practitioner · Optional

## Project: Build the First Conversation

**Brief:** Connect the support assistant to the hosted model through your stage 03 adapter. Build a simple answer flow
before you add
retrieval or tools. Follow the product brief, and show uncertainty instead of inventing a support policy.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] The prompt and output schema are versioned files, outside application logic
- [ ] Streamed text is shown as provisional; the final structured result, with citations and any decline or
  escalation, is validated when it completes, and the text is replaced with an error state if validation fails
- [ ] The interface shows loading, streaming, failure, uncertainty and retry states
- [ ] The answer format has a place for citations, ready for stage 05
- [ ] Feedback is stored only in the practice environment, with a reason, and is never added to the evaluation set
  automatically
- [ ] One command runs the fixed evaluation set after any prompt change

Previous: [03. Model Selection and Integration](./03-model-selection-and-integration.md) · Next:
[05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md)
