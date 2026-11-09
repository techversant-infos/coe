# 07. Evaluation and Experimentation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

An AI feature needs a repeatable way to detect behavior changes. Evaluate components and the user task, then use
human review to interpret failures. No single score proves a system is safe or correct. Back to the
[roadmap](./README.md).

## Build a useful evaluation set

The practice app provides a fixed starter set. Keep the expected labels separate from model prompts and application
code. Add learner-created cases in a separate file so the baseline remains comparable.

**What to learn:**

- Cover ordinary, difficult, ambiguous, unsupported and adversarial cases
- Define expected facts, relevant article IDs, abstention behavior and permitted tool behavior
- Keep examples representative without putting personal or client data into the dataset
- Version the cases and labels; review every label change

**Resources:** [OpenAI evaluation guide](https://developers.openai.com/api/docs/guides/evaluation-getting-started)

**Level:** Practitioner · Core

## Measure components and diagnose failures

Track retrieval, answer generation and application behavior separately. A retrieved passage can be relevant while
the answer is unsupported, and a correct answer can still violate the interface or tool contract.

**What to learn:**

- Measure expected-article retrieval at `k`, answer correctness, citation support and appropriate abstention
- Test schema validity, tool authorization, timeout behavior and user-visible error states
- Compare automated metrics with human review on a representative sample
- Do not use an LLM judge as the only quality gate
- Change one component at a time and run regression cases after each prompt, model or data change
- Compare results only when the model, version, prompt, settings and evaluator match

**Resources:**

- [RAG evaluation survey](https://arxiv.org/abs/2504.14891)
- [MIRAGE RAG evaluation benchmark](https://arxiv.org/abs/2504.17137)
- [RAGBench](https://arxiv.org/abs/2407.11005)
- [BRIGHT: reasoning-intensive retrieval benchmark](https://arxiv.org/abs/2407.12883)
- [RAGChecker](https://arxiv.org/abs/2408.08067)
- [Agent-SafetyBench](https://arxiv.org/abs/2412.14470)

**Level:** Advanced · Core

## Project: Establish and Improve the Baseline

**Brief:** Run the fixed evaluation cases against the current assistant. Diagnose at least three failures by layer,
make one targeted change and show whether it improved the intended measure without breaking guardrails.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] One command runs the fixed evaluation set and writes machine-readable results
- [ ] The report records dataset version, model ID, prompt version, settings, date and evaluator version
- [ ] Results separate retrieval misses, unsupported answers, citation errors, abstention errors and tool-contract errors
- [ ] At least three failures include a cause and a proposed fix
- [ ] One change is tested against all starter cases, not just the failure it targeted
- [ ] A reviewer checks a sample of automated judgments against the expected labels
- [ ] Scores are not compared across different model configurations as if they were controlled experiments

Previous: [06. Tools and Workflows](./06-tools-and-workflows.md) · Next:
[08. Data Privacy and Governance](./08-data-privacy-and-governance.md)
