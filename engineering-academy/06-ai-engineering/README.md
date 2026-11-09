# AI Engineering Roadmap

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

AI Engineering at Techversant means building and operating software features that use AI, most often a large
language model (LLM). This path covers product fit, model integration, retrieval, tool workflows, evaluation,
privacy, safety and production operations. It teaches engineering judgement that transfers across model providers.

- **Who it is for:** software engineers building AI-backed product features, and engineers moving toward AI product
  engineering.
- **Before you start:** complete [Engineering Foundations](../00-engineering-foundations/README.md), or show
  equivalent evidence. You should be able to write and test a small API-backed Python application. TypeScript is also
  supported; see the [practice app](./practice-app.md).
- **What you do:** ten stages, each with a focused guide and a project. The projects grow one synthetic support-case
  assistant into a tested, secure, production-ready service.

## How the Role Differs

| Techversant role | How AI Engineering differs |
|------------------|-----------------------------|
| Software engineer | Builds application features with predictable logic. An AI engineer decides where model behaviour adds value, then measures and limits its uncertainty. |
| Quality engineer | Validates product behaviour and release risk. An AI engineer builds evaluation datasets and diagnostics into the feature lifecycle, because outputs vary across runs and model changes. |
| Forward Deployed Engineer (FDE) | Applies AI, integration and production skills inside a client engagement. This path builds deeper AI system design and evaluation skills that an FDE can apply on that engagement. |
| Software architect | Designs system-wide structure and trade-offs. This path focuses on building, evaluating and operating an AI-enabled feature within that architecture. |

## Levels

| Academy level | What the engineer demonstrates | Evidence |
|---------------|--------------------------------|----------|
| Practitioner | Builds a bounded AI feature with review, a fixed evaluation set and the practice-data rules | Practitioner-level topics in every stage and the projects for stages 01–07 verified; can explain the model, retrieval and evaluation choices |
| Advanced | Owns an AI feature through security review, production readiness and measured improvement | All ten projects and the capstone verified, plus a production AI feature shipped or an equivalent supervised deployment |
| Expert | Improves AI engineering practice beyond one feature or team | Reusable evaluation, safety or operations patterns adopted by multiple teams; coaching evidence |

The path uses the academy-wide [learning levels](../learning-levels/README.md). Foundation is the entry
prerequisite: Engineering Foundations, or equivalent software, API, testing and security evidence. Advanced is the
target. Each topic's **Level** line shows the depth expected for that topic. Expert evidence comes from sustained
work across teams and products, not a course certificate.

## Where You Start

Everyone completes the ten stages, but experience changes where to spend time.

| Stage | Software engineer | Quality engineer | FDE | Architect |
|-------|-------------------|-----------------|-----|-----------|
| [01. Product Fit and Requirements](./01-product-fit-and-requirements.md) | Partly | Partly | Already do | Already do |
| [02. How LLMs Work](./02-how-llms-work.md) | New | New | Partly | Partly |
| [03. Model Selection and Integration](./03-model-selection-and-integration.md) | New | New | Partly | Partly |
| [04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md) | Partly | Partly | Partly | Partly |
| [05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md) | New | New | Partly | Partly |
| [06. Tools and Workflows](./06-tools-and-workflows.md) | New | New | Partly | Partly |
| [07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md) | New | Partly | Partly | Partly |
| [08. Data Privacy and Governance](./08-data-privacy-and-governance.md) | New | Partly | Partly | Partly |
| [09. AI Security and Safety](./09-ai-security-and-safety.md) | New | New | Partly | Partly |
| [10. Cost, Performance and Operations](./10-cost-performance-and-operations.md) | New | Partly | Partly | Partly |

- **Already do:** show evidence for the stage project to your reviewer and move on.
- **Partly:** review the stage, then complete the project items for the gaps you identify.
- **New:** learn the topics and complete the project with a reviewer.

## The Roadmap

![AI Engineering roadmap: ten stages from product fit to production operations](./roadmap.svg)

- Work from top to bottom. Each stage page explains every topic and ends with a project; later stages extend the
  same service. The [practice app](./practice-app.md) holds the synthetic support cases, knowledge base and fixed
  evaluation set used throughout.
- **Solid boxes** are core topics. **Dashed boxes** are optional.
- A **tick** marks a Techversant guide: a standard, checklist or academy path that covers the topic. The other
  topics link to official documentation.

## Stages and Projects

Each project has a verification checklist. A reviewer, senior engineer or lead checks every item before the project
counts.

| Stage | Project |
|-------|---------|
| [01. Product Fit and Requirements](./01-product-fit-and-requirements.md) | [Define the Support Assistant](./01-product-fit-and-requirements.md#project-define-the-support-assistant) |
| [02. How LLMs Work](./02-how-llms-work.md) | [Measure Model Behaviour](./02-how-llms-work.md#project-measure-model-behaviour) |
| [03. Model Selection and Integration](./03-model-selection-and-integration.md) | [Compare and Connect Models](./03-model-selection-and-integration.md#project-compare-and-connect-models) |
| [04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md) | [Build the First Conversation](./04-prompt-context-and-interaction-design.md#project-build-the-first-conversation) |
| [05. Knowledge and Retrieval](./05-knowledge-and-retrieval.md) | [Ground Answers in Articles](./05-knowledge-and-retrieval.md#project-ground-answers-in-articles) |
| [06. Tools and Workflows](./06-tools-and-workflows.md) | [Add a Read-Only Case Lookup](./06-tools-and-workflows.md#project-add-a-read-only-case-lookup) |
| [07. Evaluation and Experimentation](./07-evaluation-and-experimentation.md) | [Establish and Improve the Baseline](./07-evaluation-and-experimentation.md#project-establish-and-improve-the-baseline) |
| [08. Data Privacy and Governance](./08-data-privacy-and-governance.md) | [Document the Data Flow](./08-data-privacy-and-governance.md#project-document-the-data-flow) |
| [09. AI Security and Safety](./09-ai-security-and-safety.md) | [Test the Threat Model](./09-ai-security-and-safety.md#project-test-the-threat-model) |
| [10. Cost, Performance and Operations](./10-cost-performance-and-operations.md) | [Release and Operate the Assistant](./10-cost-performance-and-operations.md#project-release-and-operate-the-assistant) |

## Capstone

Present the completed support-case assistant to a reviewer. Show the product requirement and baseline, the fixed
evaluation set results, a retrieval failure and its diagnosis, a blocked injection attempt, the data-flow review, and
a production report covering latency, cost, errors and rollback. Use the same dataset and evaluation protocol for
each run. Compare scores only when model, version, prompt, settings and grader match; otherwise report the
configuration alongside the result.

## How This Fits Other Paths

- [FDE stage 04: Applied AI](../08-forward-deployed-engineering/04-applied-ai.md) teaches the working knowledge an
  FDE needs across an engagement. This path goes deeper on AI feature engineering and evaluation.
- [Architecture stage 08: AI-enabled systems](../04-architecture/08-ai-enabled-systems.md) covers system-level design
  choices. This path covers building, evaluating and operating the feature within those constraints.
- AI-assisted coding is in
  [Engineering Foundations stage 02: Working with AI Tools](../00-engineering-foundations/02-working-with-ai-tools.md).
  AI-assisted test design is in the Quality Engineering
  [AI-assisted testing practice guide](../02-quality-engineering/05-ai-assisted-testing.md). Follow the
  [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md) whenever AI tools help write code.

## References

Prefer primary technical documentation. Provider features and model availability change; check current docs and
record the model identifier and date for every evaluation run.

- [OpenAI Responses API](https://developers.openai.com/api/docs/guides/text) (hosted API worked example) and
  [Claude documentation](https://platform.claude.com/docs/en/models/overview), for comparison
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/)
  (optional open-weight deployment)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) of the AI Risk Management
  Framework, US National Institute of Standards and Technology (NIST)
