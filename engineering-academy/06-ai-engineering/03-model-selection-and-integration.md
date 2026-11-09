# 03. Model Selection and Integration

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Choose a model and hosting arrangement from the product's quality, privacy, latency and cost requirements. Keep
provider-specific code behind a small application boundary. Back to the [roadmap](./README.md).

## Hosted and open-weight options

Hosted APIs reduce infrastructure work but send requests to a provider. Open-weight models can run in an approved
environment, but require capacity, operations and license review. Neither choice removes the need to validate model
behavior or data handling.

**What to learn:**

- Compare model candidates on the same fixed cases and settings
- Check capability, context limits, output controls, latency, availability and cost
- Review model license and acceptable-use terms for open-weight deployments
- Check data processing terms, retention, residency and client approval for hosted providers
- Treat a model replacement as a versioned change that must pass evaluations before release

**Resources:**

- [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection)
- [OpenAI Responses API](https://developers.openai.com/api/docs/guides/text)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/)

**Level:** Practitioner · Core

## Provider boundary

Use the OpenAI Python client and Responses API for the hosted walkthrough. Keep model name and credentials in
environment configuration. For the optional open-weight lab, vLLM can expose a compatible HTTP endpoint; check
feature support because protocol compatibility does not guarantee identical model behavior or API features.

```python
import os

from openai import OpenAI

# The SDK reads OPENAI_API_KEY from the environment.
client = OpenAI()
response = client.responses.create(
    model=os.environ["AI_MODEL"],
    input="Reply with the single word READY.",
)
print(response.output_text)
```

For the optional local vLLM lab, configure the same SDK with the local endpoint and its practice API key:

```python
# Point this client at the local practice server, never a client endpoint.
client = OpenAI(
    base_url=os.environ["AI_BASE_URL"],
    api_key=os.environ["AI_API_KEY"],
)
```

Do not send the example request to a client system or add real case data. The same client interface does not imply
that hosted and open-weight models have identical behavior or feature support.

**What to learn:**

- Keep the domain workflow independent of the provider client
- Handle timeout, rate limit, malformed output and provider errors explicitly
- Avoid logging prompts or responses that contain sensitive data
- Record model identifier, provider, date and settings for evaluation reproducibility

## Project: Compare and Connect Models

**Brief:** Implement one model adapter for the hosted walkthrough. If local hardware and approved model weights are
available, run the same cases against an open-weight endpoint and compare results.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] The service reads credentials and model settings from environment variables
- [ ] No credential appears in source, logs or the browser
- [ ] The interface handles timeout, rate-limit and invalid-response cases
- [ ] The report records provider, model identifier, date, settings, quality, latency and estimated cost
- [ ] The model choice is justified against the product brief, not a general leaderboard
- [ ] If comparing models, identical evaluation cases and application code are used

Previous: [02. How LLMs Work](./02-how-llms-work.md) · Next:
[04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md)
