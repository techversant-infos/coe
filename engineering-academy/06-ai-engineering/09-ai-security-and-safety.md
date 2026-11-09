# 09. AI Security and Safety

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Treat the user's message, retrieved documents and tool results as untrusted. A prompt is not a security control.
Design the application so that a model mistake cannot grant extra access. Back to the [roadmap](./README.md).

## Threat modelling an AI feature

A threat model lists what an attacker could read or change, and how. AI features add new inputs, such as retrieved
documents and tool results, to the usual list.

**What to learn:**

- Listing assets, trust boundaries and every place untrusted text enters: user input, articles, case text, tool
  results and files
- The main risks in the OWASP Top 10 for large language model (LLM) applications
- Rating each threat by impact, and choosing controls in application code first

**Resources:**

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [MITRE ATLAS](https://atlas.mitre.org/), a knowledge base of attacks on AI systems

**Level:** Advanced · Core

## Prompt injection

Prompt injection is text that tries to give the model new instructions. Direct injection comes from the user;
indirect injection hides in content the model reads, such as a case description or a web page.

**What to learn:**

- Direct and indirect injection, with examples from the practice data
- Marking untrusted content clearly in the prompt, while knowing that this reduces risk but does not remove it
- Limiting what a successful injection can do, through tool scope and authorisation in code

**Resources:**

- [LLM prompt injection prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html),
  OWASP
- [Prompt injection prevention](../../security/ai-security/ai-security-guidelines.md#41-prompt-injection-prevention),
  in the Techversant AI security guidelines

**Level:** Practitioner · Core

## Handling model output

Model output is untrusted input to the rest of the system. It must never run as code, a query or a command without
checks.

**What to learn:**

- Encoding output for where it is shown, so it cannot run as HTML or script in the browser
- Never passing model output straight into SQL, a shell, a file path or a tool call
- Checking links and citations against known sources before showing them

**Resources:** [Output validation](../../security/ai-security/ai-security-guidelines.md#71-output-validation), in the
Techversant AI security guidelines

**Level:** Practitioner · Core

## Tool and data authority

The model should never have more access than the user it acts for. Authorisation belongs in application code, where
it can be tested.

**What to learn:**

- Allow-listed tools, each checked against the current user's rights on every call
- Preventing access across users and workspaces in code, never through prompt instructions
- Limits on network access, result size and run time for every tool

**Resources:** [Agent-SafetyBench](https://arxiv.org/abs/2412.14470), arXiv, on testing the safety of tool-using
agents

**Level:** Advanced · Core

## Red teaming and security tests

Red teaming means attacking your own feature to find weaknesses before someone else does. Turn every finding into a
test that runs with the evaluation set.

**What to learn:**

- Writing attack cases for injection, data leaks, cross-workspace access and harmful output
- Running automated attack tools, then reviewing the results by hand
- Adding each confirmed weakness to the regression cases

**Resources:**

- [Red teaming](https://www.promptfoo.dev/docs/red-team/), promptfoo documentation
- [Security testing for AI systems](../../security/ai-security/ai-security-guidelines.md#11-security-testing-for-ai-systems),
  in the Techversant AI security guidelines

**Level:** Advanced · Core

## Guardrail libraries

Guardrail libraries check inputs and outputs against rules, such as blocking off-topic requests. They add a layer of
defence, but they do not replace authorisation in code.

**What to learn:**

- What input and output checks can catch, and what they miss
- Measuring the false-positive rate, so guardrails do not block valid support questions

**Resources:** [NeMo Guardrails documentation](https://docs.nvidia.com/nemo/guardrails/latest/index.html), NVIDIA

**Level:** Advanced · Optional

## Model and dependency supply chain

Models, embedding libraries and their downloads are dependencies like any other. A model file from an unknown source
can carry harmful code.

**What to learn:**

- Using model files in the safetensors format, which cannot run code when loaded
- Pinning model and library versions, and checking where each comes from
- Never enabling `trust_remote_code` (`--trust-remote-code` in vLLM) for a model repository nobody has reviewed,
  because remote code runs whatever format the weights use

**Resources:** [Safetensors](https://huggingface.co/docs/safetensors/index), Hugging Face documentation

**Level:** Advanced · Optional

## Project: Test the Threat Model

**Brief:** Use the synthetic injection in `CASE-1012`. Show that untrusted case text cannot reveal another case,
override the assistant's rules or trigger a change to any case.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] A threat model names assets, trust boundaries, attacker inputs and impact
- [ ] Tests cover direct injection from the user and indirect injection returned by the case-summary tool
- [ ] The assistant treats injected text as untrusted and cites only knowledge-base articles
- [ ] Application checks, written by hand as Red Zone code, reject unauthorised, invalid and cross-workspace tool calls
- [ ] Model output is encoded before display, and is never used as a query, command or file path
- [ ] The practice app has no tools that can change data
- [ ] The security cases run with the fixed evaluation set on every change

Previous: [08. Data Privacy and Governance](./08-data-privacy-and-governance.md) · Next:
[10. Cost, Performance and Operations](./10-cost-performance-and-operations.md)
