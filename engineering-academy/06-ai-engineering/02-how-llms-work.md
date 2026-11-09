# 02. How LLMs Work

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

You do not need to train a large language model (LLM), but you need to know how one behaves, so you can predict its
limits, measure its inputs and outputs, and plan for failure. Back to the [roadmap](./README.md).

## Tokens

Models read and write tokens, which are pieces of words. Tokens decide how much text fits in a request, how much the
request costs and how long it takes.

**What to learn:**

- How text becomes tokens, and why the same text can count differently across models
- Counting tokens for instructions, conversation history, retrieved passages and the answer
- Reading the token counts that the provider returns with each response

**Resources:**

- [Tokenizers](https://huggingface.co/learn/llm-course/chapter2/4), Hugging Face LLM course
- [tiktoken](https://github.com/openai/tiktoken), an open-source library for counting tokens

**Level:** Practitioner · Core

## Context windows

The context window is the most tokens one request can use, counting the input and the generated output,
including any reasoning tokens. It is not the same as the conversation your
application stores, and filling it does not always help.

**What to learn:**

- The difference between the model's context window and the history your application keeps
- Why extra context can add noise as well as information, and why position in a long input matters
- Shortening or summarising history without losing the user's intent or required instructions

**Resources:** [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude
documentation

**Level:** Practitioner · Core

## Sampling and variability

The same request can give different wording, and sometimes different decisions, across runs. A low temperature
reduces variation but does not make a system correct or fully repeatable.

**What to learn:**

- What temperature and output limits do, at a conceptual level
- Running the same cases several times and measuring how much the results vary
- Using schema validation and application rules for anything that must be exact
- Recording the settings the model actually accepts: some reasoning models reject temperature and `top_p`

**Resources:** [Text generation](https://developers.openai.com/api/docs/guides/text), OpenAI documentation

**Level:** Practitioner · Core

## Common failure modes

Models fail in ways that look confident. Knowing the common failures helps you design checks for them.

**What to learn:**

- Invented facts, also called hallucinations, and why they happen
- Ignored or partly followed instructions, especially in long prompts
- Out-of-date knowledge from the model's training cut-off, and why retrieval helps

**Resources:**
[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations),
Claude documentation

**Level:** Practitioner · Core

## Reasoning models

Some models spend extra tokens working through a problem before they answer. That can improve hard tasks, but costs
more and takes longer.

**What to learn:**

- When extra reasoning helps, such as multi-step questions, and when it only adds cost and delay
- Measuring the quality, latency and cost difference on your own cases before switching
- Reasoning tokens are billed as output and count toward the output limit, so a response can end incomplete with
  no visible text

**Resources:**

- [Reasoning models](https://developers.openai.com/api/docs/guides/reasoning), OpenAI documentation
- [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), Claude documentation

**Level:** Practitioner · Optional

## Project: Measure Model Behaviour

**Brief:** Run a small set of practice questions several times. Compare token use, response time, output variation
and failures when the useful context is missing or too long.

**Size:** 2–3 hours

**Verification**, checked by a reviewer:

- [ ] Each run saves the model identifier, date and settings
- [ ] The report records input and output token counts, as returned by the provider
- [ ] Five cases are each run at least three times, and the variation is described
- [ ] One case has too much context and one has none, and the report explains the effect
- [ ] The report lists which outputs need exact checks in application code

Previous: [01. Product Fit and Requirements](./01-product-fit-and-requirements.md) · Next:
[03. Model Selection and Integration](./03-model-selection-and-integration.md)
