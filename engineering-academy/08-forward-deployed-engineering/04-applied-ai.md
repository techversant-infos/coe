# 04. Applied AI

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

The core technical skill for most FDE work: AI features that work on the client's real data, and proof that they do.
Back to the [roadmap](./README.md).

## How LLMs work

You do not need to train models, but you need to know how they behave so you can predict where they will fail.

**What to learn:**

- Tokens, context windows and why long inputs cost more
- Why the same prompt can give different answers
- Common failures: invented facts, ignored instructions, outdated knowledge

**Resources:**

- [AI Engineering](../06-ai-engineering/README.md) (planned academy paths)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
- [Claude models overview](https://platform.claude.com/docs/en/models/overview)

**Level:** Practitioner · Core

## Prompt and context engineering

Most quality problems come from giving the model unclear instructions or the wrong context.

**What to learn:**

- Clear instructions, examples and output formats
- Giving the model the context it needs and nothing else
- Keeping prompts in version control and testing changes to them

**Resources:**

- [Claude prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- Techversant's [Prompt Library](../../ai/prompts/developer-handbook-full.md) holds prompts for development work,
  not prompts inside a product, but shows the same habits

**Level:** Practitioner · Core

## Retrieval and vector search

Retrieval lets a model answer from the client's own documents and records instead of guessing.

**What to learn:**

- Splitting documents into chunks and creating embeddings
- Vector search in PostgreSQL with pgvector, and combining it with keyword search
- Showing users where an answer came from

**Resources:** [pgvector](https://github.com/pgvector/pgvector)

**Level:** Practitioner · Core

## Tool use and MCP

Tool use lets a model call your functions, for example to look up an order. The Model Context Protocol (MCP) is a
standard way to connect models to tools and data.

**What to learn:**

- Defining tools with clear inputs and validating what the model sends
- Read-only tools first; any tool that changes data needs a check
- Building and connecting an MCP server

**Resources:** [Model Context Protocol](https://modelcontextprotocol.io/)

**Level:** Practitioner · Core

## AI agents

An agent is a model that decides its own next step and calls tools in a loop. Agents can do more on their own,
which adds risk in client systems.

**What to learn:**

- When a fixed workflow is better than an agent
- Giving an agent only the authority the task needs
- Human approval steps before anything irreversible

**Resources:** [Building effective agents](https://www.anthropic.com/research/building-effective-agents)

**Level:** Advanced · Core

## Choosing models and providers

The right model balances quality, speed, cost and where the client allows data to go.

**What to learn:**

- Comparing models on the client's own examples, not on benchmarks
- Cost per request and per month at the expected volume
- Data residency and the client's approved providers

**Resources:** [Claude models overview](https://platform.claude.com/docs/en/models/overview).
Techversant's [AI tool standard](../../ai/guides/ai-team-best-practices.md#2-tool-selection-standards) covers the
coding tools engineers use, not the models inside client products. Agree the provider with the client in the scope.

**Level:** Practitioner · Core

## Evaluations

An evaluation set is a collection of real examples with expected results. It is how you show the client that an AI
feature works, and how you notice when it stops working.

**What to learn:**

- Building an evaluation set from the client's real cases, including hard ones
- Scoring results against the success measure agreed in the scope
- Reporting failures honestly, with what they mean for the client

**Resources:** [Claude guide: define success and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)

**Level:** Practitioner · Core

## Project: Build a Standards Assistant and Prove It Works

**Brief:** Build an assistant that answers questions about Techversant's engineering standards, using the `standards/`
and `security/` folders of this repository as its knowledge base. It retrieves the relevant passages, answers with
citations, and says it does not know when the documents do not cover the question. Build it in Python or
TypeScript. Write the success measure before you build anything.

**Size:** 4–5 days

**Verification**, checked by your lead:

- [ ] A success measure agreed with your lead before building, for example "80% of answers correct and every
  out-of-scope question declined"
- [ ] An evaluation set of at least 30 questions with expected answers, including 5 the documents do not cover and 5
  hard questions written by someone else
- [ ] One command runs the evaluation and prints the score
- [ ] Every answer cites the document and section it used
- [ ] A one-page report: the score against the success measure, three failures with their cause (retrieval, prompt or
  model) and the cost per 1,000 questions
- [ ] The AI provider is named in the README and approved by your lead before you build, and no personal or client
  data goes into prompts

Previous: [03. Data](./03-data.md) · Next: [05. AI-Assisted Delivery](./05-ai-assisted-delivery.md)
