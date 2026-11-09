# 07. Evaluation and Experimentation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

An AI feature needs a repeatable way to notice when its behaviour changes. Evaluate each part and the whole task, and
use human review to interpret failures. No single score proves a system is correct or safe. Back to the
[roadmap](./README.md).

## Building an evaluation set

An evaluation set is a fixed list of inputs with the expected behaviour for each. It is the test suite for the parts
of the feature that ordinary unit tests cannot check.

**What to learn:**

- Covering ordinary, difficult, ambiguous, unsupported and hostile cases
- Writing expected behaviour as facts, article IDs, tool calls and when to decline, not exact wording
- Versioning the cases, reviewing every label change, and keeping personal or client data out

**Resources:**
[Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests),
Claude documentation

**Level:** Practitioner · Core

## Measuring each part

A relevant passage can be retrieved while the answer still ignores it, and a correct answer can still break the tool
contract. Measure each part separately, so you know where to fix.

**What to learn:**

- Retrieval: hit rate at `k`. Answers: correct facts, supported citations and declining when the evidence is missing
- Application behaviour: valid structure, authorised tool calls, timeouts and the error states the user sees
- Grouping failures by cause, and fixing the most common cause first

**Resources:**

- [Ragas documentation](https://docs.ragas.io/en/stable/), metrics for retrieval-augmented generation (RAG)
- [Retrieval Augmented Generation Evaluation in the Era of Large Language Models](https://arxiv.org/abs/2504.14891),
  arXiv survey

**Level:** Practitioner · Core

## Model-graded evaluation

A second model can grade answers against the expected facts, which scales better than reading every answer. Model
graders have their own biases, so check them against human judgement.

**What to learn:**

- Writing a grading prompt with a clear scale and the expected facts for each case
- Known grader biases: preferring longer answers, answers in a particular position, or answers from the grader's own
  model family
- Comparing grader scores with a person's scores on a sample, and never using a model grader as the only gate

**Resources:** [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685), arXiv, on using a large language model
(LLM) as a grader

**Level:** Advanced · Core

## Regression testing

Every prompt, model, retrieval or data change can break cases that used to pass. Run the evaluation set
automatically, like any other test suite.

**What to learn:**

- One command that runs the evaluation set and writes machine-readable results
- Running it in continuous integration (CI) when prompts, models, retrieval settings or data change
- Using pass thresholds or repeated runs instead of one exact-match run, keeping the API key in CI secrets and
  capping the cost of each run
- Changing one thing at a time, and comparing results only when model, version, prompt, settings and grader match

**Resources:**

- [promptfoo documentation](https://www.promptfoo.dev/docs/intro/)
- [Inspect](https://inspect.aisi.org.uk/), UK AI Security Institute

**Level:** Practitioner · Core

## Online experiments

Offline evaluation uses a fixed set; real users ask things you did not predict. Online experiments compare versions
on live traffic, with guardrails that stop the test if harm rises.

**What to learn:**

- Shadow mode: running a new version alongside the current one without showing its answers to users
- A/B tests: splitting traffic, choosing the measure in advance and running long enough for a reliable result
- Guardrail measures that end an experiment early, such as unsupported answers or cost per request

**Resources:** [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml), Google
for Developers

**Level:** Advanced · Core

## Project: Establish and Improve the Baseline

**Brief:** Run the fixed evaluation set against the current assistant. Diagnose at least three failures by cause,
make one targeted change, and show whether it improved the intended measure without breaking guardrails.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] One command runs the fixed evaluation set and writes machine-readable results
- [ ] The report records dataset version, model identifier, prompt version, settings, date and grader version
- [ ] Results separate retrieval misses, unsupported answers, citation errors, wrong declines and tool-contract
  errors
- [ ] At least three failures have a cause and a proposed fix
- [ ] The change is tested against every case in the fixed evaluation set, not only the failure it targets
- [ ] A reviewer checks a sample of model-graded results against the expected labels
- [ ] The evaluation runs in continuous integration on every pull request that changes prompts, models or data, with
  pass thresholds that allow for run-to-run variation
- [ ] Scores from different model configurations are not compared as if they were controlled experiments

Previous: [06. Tools and Workflows](./06-tools-and-workflows.md) · Next:
[08. Data Privacy and Governance](./08-data-privacy-and-governance.md)
