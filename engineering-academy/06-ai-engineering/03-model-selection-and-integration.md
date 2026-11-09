# 03. Model Selection and Integration

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Choose a model and where it runs from the product's quality, privacy, latency and cost needs. Keep provider-specific
code behind a small boundary, so the rest of the service does not change when the model does. Back to the
[roadmap](./README.md).

## Hosted and open-weight models

A hosted model runs on a provider's servers, which saves infrastructure work but sends each request to that provider.
An open-weight model can run in an environment you control, but needs hardware, operations and a licence review.

**What to learn:**

- The trade-offs: data leaving your environment, set-up and running effort, cost at your expected volume
- Licence and acceptable-use terms for open-weight models, and reading a model card
- Running an open-weight model locally for practice, with vLLM or Ollama

**Resources:**

- [Model cards](https://huggingface.co/docs/hub/model-cards), Hugging Face documentation
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/)
  and [Ollama documentation](https://docs.ollama.com/)

**Level:** Practitioner · Core

## Comparing models on your own cases

Public leaderboards measure general tasks. Your feature has its own data, risks and limits, so compare candidate
models on your own cases.

**What to learn:**

- Running each candidate on the same fixed cases, prompt and settings
- Comparing quality, context limits, structured-output support, latency, availability and cost
- Checking data processing terms, retention and region before a model is approved for client data

**Resources:**

- [Model selection](https://developers.openai.com/api/docs/guides/model-selection), OpenAI documentation
- [Models overview](https://platform.claude.com/docs/en/models/overview), Claude documentation

**Level:** Practitioner · Core

## The provider boundary

Put every model call behind one small module, an adapter, with an interface your service owns. The worked examples
use the OpenAI Python software development kit (SDK) and the Responses API. Keep the model name and credentials in
environment variables.

```python
import os
from openai import OpenAI

# The SDK reads OPENAI_API_KEY from the environment.
client = OpenAI()

response = client.responses.create(
    model=os.environ["AI_MODEL"],
    input="Reply with the single word READY.",
)
print(response.output_text)  # Expected: READY
```

For the optional local lab, point the same SDK at a vLLM server's compatible endpoint. `AI_BASE_URL` includes
`/v1`, such as `http://localhost:8000/v1`; `AI_API_KEY` matches the server's `--api-key`; and `AI_MODEL` is the
served model name. vLLM supports the Responses API, so the same `responses.create` call works:

```python
import os
from openai import OpenAI

# Point this client at the local practice server, never at a client system.
client = OpenAI(
    base_url=os.environ["AI_BASE_URL"],
    api_key=os.environ["AI_API_KEY"],
)
```

**What to learn:**

- Keeping the support workflow independent of any one provider's SDK
- Why a compatible endpoint does not mean identical behaviour or features, so the same cases must be run again
- Recording the provider, model identifier, date and settings with every evaluation run

**Resources:** [Text generation](https://developers.openai.com/api/docs/guides/text), OpenAI documentation

**Level:** Practitioner · Core

## Handling provider errors

Model APIs time out, hit rate limits and return output that does not match what you asked for. The service needs a
planned response to each.

**What to learn:**

- Timeouts, and retries with backoff for rate limits and temporary errors, with a limit on attempts
- The SDK's own defaults: the OpenAI SDK waits up to 10 minutes and retries twice, so set `timeout` and
  `max_retries` on the client and do not stack a second retry layer on top
- Treating malformed or incomplete output as an error, not as an answer
- Showing the user a clear message, and never logging prompts or responses that contain sensitive data

**Resources:**

- [Errors](https://platform.claude.com/docs/en/api/errors), Claude documentation
- [Error codes](https://developers.openai.com/api/docs/guides/error-codes), OpenAI documentation

**Level:** Practitioner · Core

## Model versions and retirement

Providers release new models and retire old ones. A model change can alter behaviour as much as a code change.

**What to learn:**

- Using a fixed model version in production instead of an alias that moves to newer models
- Following the provider's retirement dates, and planning the move before a model is switched off
- Treating every model change as a release that must pass the evaluation set first

**Resources:**

- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), Claude documentation
- [Deprecations](https://developers.openai.com/api/docs/deprecations), OpenAI documentation

**Level:** Practitioner · Core

## When to fine-tune

Fine-tuning trains a model further on your own examples. It suits a consistent style or format, but it does not keep
facts up to date, and retrieval usually solves knowledge problems more cheaply.

**What to learn:**

- When to try better prompts, retrieval or fine-tuning, in that order
- The data, evaluation and retraining work that fine-tuning adds

**Resources:**

- [Supervised fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning), OpenAI
  documentation
- [Parameter-efficient fine-tuning (PEFT)](https://huggingface.co/docs/peft/index), Hugging Face documentation

**Level:** Advanced · Optional

## Project: Compare and Connect Models

**Brief:** Build one model adapter for the hosted model used in the [practice app](./practice-app.md). If you have
suitable hardware and approved model
weights, run the same cases against an open-weight endpoint and compare the results.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] The service reads credentials and model settings from environment variables
- [ ] No credential appears in source, logs or the browser
- [ ] The adapter handles timeouts, rate limits and invalid responses, with a test for each
- [ ] Production configuration uses a fixed model version, not a moving alias
- [ ] The report records provider, model identifier, date, settings, quality, latency and estimated cost
- [ ] The model choice is justified against the product brief, not a general leaderboard
- [ ] Any model comparison uses identical cases and application code

Previous: [02. How LLMs Work](./02-how-llms-work.md) · Next:
[04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md)
