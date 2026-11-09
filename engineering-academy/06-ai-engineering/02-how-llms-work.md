# 02. How LLMs Work

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Learn enough about language models to predict their limits, measure inputs and outputs, and design appropriate
fallbacks. You do not need to train a foundation model. Back to the [roadmap](./README.md).

## Tokens and context

Models process token sequences rather than words. Context limits, tokenization and long-input behavior affect what
the model can see, how much a request costs and how quickly it responds.

**What to learn:**

- Estimate tokens for instructions, conversation history, retrieved passages and output
- Distinguish the model's context window from the application's retained conversation history
- Understand why adding more context can add noise as well as information
- Truncate or summarize history without dropping user intent or required safety instructions

**Resources:** [OpenAI tokenizer](https://platform.openai.com/tokenizer)

**Level:** Practitioner · Core

## Sampling and variability

The same request may produce different wording or decisions across repeated runs. A low temperature does not make a
system deterministic or correct.

**What to learn:**

- Explain sampling settings such as temperature and output limits at a conceptual level
- Run the same cases more than once and measure variation
- Use schema validation and application rules for properties that must be exact
- Keep model output separate from trusted application state

**Resources:** [OpenAI text generation guide](https://developers.openai.com/api/docs/guides/text)

**Level:** Practitioner · Core

## Project: Measure Model Behavior

**Brief:** Run a small set of practice questions repeatedly. Compare token use, response time, output variation and
failures when the useful context is missing or too long.

**Size:** 2–3 hours

**Verification**, checked by a reviewer:

- [ ] Save the model identifier, date and settings with each run
- [ ] Record input and output token counts where the provider exposes them
- [ ] Compare at least three repeated runs for five cases
- [ ] Include one long-context and one missing-context case
- [ ] Explain which outputs require deterministic application checks

Previous: [01. Product Fit and Requirements](./01-product-fit-and-requirements.md) · Next:
[03. Model Selection and Integration](./03-model-selection-and-integration.md)
