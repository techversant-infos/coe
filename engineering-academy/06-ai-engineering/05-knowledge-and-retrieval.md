# 05. Knowledge and Retrieval

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Retrieval connects a model to a maintained knowledge source. Treat ingestion, access, retrieval and answer grounding
as separate parts that can fail independently. Back to the [roadmap](./README.md).

## Prepare the knowledge base

Useful retrieval starts with trustworthy, current documents and metadata. A vector database does not make poor
source material reliable.

**What to learn:**

- Track source, owner, version and effective date for each article
- Normalize documents while preserving headings and useful metadata
- Choose chunk boundaries that keep a procedure or policy together
- Generate embeddings and plan to rebuild the index when source text, embedding model or indexing settings change
- Remove stale, duplicate or unauthorized material before indexing

**Resources:** [pgvector](https://github.com/pgvector/pgvector)

**Level:** Practitioner · Core

## Retrieve and ground

Measure whether the right passages are found before judging the answer. The assistant should use only retrieved
evidence for support policy claims and cite the source article.

**What to learn:**

- Compare keyword, vector and hybrid retrieval on the supplied cases
- Measure whether expected articles appear in the top results
- Add reranking only when the measured retrieval errors justify it
- Preserve article IDs and section metadata through answer generation
- Abstain or ask a clarifying question when evidence is missing, conflicting or outdated

**Resources:** [pgvector](https://github.com/pgvector/pgvector)

**Level:** Practitioner · Core

## Project: Ground Answers in Articles

**Brief:** Ingest the fixed knowledge base from the [practice app](./practice-app.md). Answer supported questions with
article citations and abstain when the data does not support an answer.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] Ingestion is repeatable and records source IDs and article versions
- [ ] A retrieval-only command reports expected article hit rate at the chosen `k`
- [ ] At least five cases diagnose retrieval misses separately from answer-generation errors
- [ ] The answer includes only citations returned by retrieval
- [ ] Unsupported and conflicting cases do not receive fabricated policy details
- [ ] The design includes a way to remove or re-index a superseded article

Previous: [04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md) · Next:
[06. Tools and Workflows](./06-tools-and-workflows.md)
