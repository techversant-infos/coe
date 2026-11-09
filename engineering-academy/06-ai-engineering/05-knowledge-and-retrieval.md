# 05. Knowledge and Retrieval

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Retrieval-augmented generation (RAG) means finding relevant passages in your own documents and giving them to the
model as evidence. Treat preparing, searching and answering as separate parts, because each can fail on its own.
Back to the [roadmap](./README.md).

## Preparing the knowledge base

Good retrieval starts with current, trustworthy documents. A vector database does not make poor source material
reliable.

**What to learn:**

- Recording the source, owner, revision and date for every article
- Removing stale, duplicate or unapproved material before it is indexed
- Rebuilding the index when the source text, the embedding model or the index settings change

**Resources:** [pgvector](https://github.com/pgvector/pgvector), vector search for PostgreSQL

**Level:** Practitioner · Core

## Chunking

Documents are split into chunks, the units that search returns. Chunks that are too small lose meaning; chunks that
are too large bury the answer.

**What to learn:**

- Splitting on headings and paragraphs, so a procedure or policy stays together
- Keeping the article ID, title and section with every chunk, so citations survive
- Comparing chunk sizes on longer documents; the practice articles are short enough to index whole

**Resources:** [Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval), Anthropic

**Level:** Practitioner · Core

## Embeddings and vector search

An embedding turns text into a list of numbers, so that passages with similar meaning sit close together. Vector
search finds the chunks closest to the question.

**What to learn:**

- Creating embeddings for chunks and questions with the same model
- Storing and searching embeddings in PostgreSQL with pgvector
- Choosing an embedding model by testing it on your own cases; leaderboards are only a starting point

**Resources:**

- [Sentence Transformers documentation](https://sbert.net/)
- [Massive Text Embedding Benchmark (MTEB) leaderboard](https://huggingface.co/spaces/mteb/leaderboard), Hugging
  Face
- [pgvector](https://github.com/pgvector/pgvector)

**Level:** Practitioner · Core

## Keyword and hybrid search

Vector search misses exact terms, such as error codes and product names. Keyword search finds them. Hybrid search
combines both result lists.

**What to learn:**

- Keyword search with PostgreSQL full-text search
- Combining keyword and vector results, for example with reciprocal rank fusion
- Measuring the hit rate at `k`: how often the expected article appears in the top `k` results. On nine short
  articles the methods may differ little; the habit of measuring matters more than the result

**Resources:**

- [Full text search](https://www.postgresql.org/docs/current/textsearch.html), PostgreSQL documentation
- [Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion),
  Elastic documentation

**Level:** Practitioner · Core

## Grounding and citations

A grounded answer uses only the retrieved evidence and says where each claim came from. When the evidence is missing
or conflicting, the assistant says so instead of guessing.

**What to learn:**

- Passing article IDs through to the answer, and citing only articles that retrieval returned
- Saying "I don't know" or asking a clarifying question when evidence is missing, conflicting or out of date
- Checking that each cited article actually supports the claim next to it

**Resources:**
[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations),
Claude documentation

**Level:** Practitioner · Core

## Reranking

A reranker reads the question and each candidate passage together, then reorders the results. It is slower than
vector search, so add it only when measured retrieval errors justify it.

**What to learn:**

- Retrieving a wider set of candidates, then reranking them with a cross-encoder model
- Measuring the hit-rate gain against the added latency

**Resources:** [Cross-encoder usage](https://sbert.net/docs/cross_encoder/usage/usage.html), Sentence Transformers
documentation

**Level:** Advanced · Optional

## Project: Ground Answers in Articles

**Brief:** Index the fixed knowledge base from the [practice app](./practice-app.md). Answer supported questions with
article citations, and decline when the data does not support an answer.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] Indexing is repeatable and records article IDs and revisions
- [ ] A retrieval-only command reports the hit rate at the chosen `k` for keyword, vector and hybrid search
- [ ] At least five cases separate retrieval misses from answer errors
- [ ] Answers cite only articles that retrieval returned
- [ ] Unsupported and ambiguous cases, `EVAL-015` to `EVAL-018`, get no invented policy details
- [ ] The design shows how a superseded article is removed or re-indexed

Previous: [04. Prompt, Context and Interaction Design](./04-prompt-context-and-interaction-design.md) · Next:
[06. Tools and Workflows](./06-tools-and-workflows.md)
