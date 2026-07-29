# Phase 6: AI Integration

> Add modern AI capabilities to existing ColdFusion systems.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Specialist Pathway |
| Best for | AI Integration Advisor |
| Contribution level | Contributor → Supported Lead |
| Take this when | You need to identify or scope AI opportunities for a CF application |
| Evidence of readiness | Completed AI use case analysis for a client or sample application |
| Next | [capstone/exercises/phase-6](../capstone/exercises/phase-6-ai.md) for practice |

---

## Overview

## Overview

AI integration is a high-value differentiator. This phase covers practical ways to add AI to legacy ColdFusion applications — from chatbots to document processing to code assistance.

> **Note:** AI fundamentals are covered in this module. External AI documentation available at Planned: `../../ai/`

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Identify AI use cases for ColdFusion applications
- [ ] Integrate external AI services (Claude, OpenAI) via CFHTTP
- [ ] Build chatbots and virtual assistants
- [ ] Implement document processing pipelines (OCR, summarization)
- [ ] Create semantic search with vector databases
- [ ] Use RAG (Retrieval-Augmented Generation) patterns
- [ ] Implement AI-powered workflow automation
- [ ] Evaluate local LLM options for sensitive data

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/)
- Basic understanding of AI concepts (see Planned: AI fundamentals)

## Topics

### 1. AI Use Cases for ColdFusion

**High-Value Quick Wins:**
- Customer support chatbot
- Document search and Q&A
- Email generation and summarization
- Ticket classification
- Code comment generation

**Medium-Effort Projects:**
- Intelligent search
- Content recommendation
- Anomaly detection
- Workflow automation

**Advanced:**
- Custom training
- Fine-tuned models
- Agentic workflows
- Multi-modal processing

### 2. Integration Architecture

**HTTP-Based Integration:**
- CFHTTP for API calls
- JSON parsing with DeserializeJSON
- Streaming responses
- Error handling patterns

**API Providers:**
- Claude API (Anthropic)
- OpenAI API (GPT-4, Assistants)
- Azure OpenAI
- Local models (Ollama)

### 3. Common Patterns

**Chatbot Implementation:**
- Session management for conversations
- Context preservation
- Multi-turn dialogs
- Fallback strategies

**Document Processing:**
- PDF text extraction (cfpdf + AI)
- Chunking strategies
- Summarization
- Classification

**Semantic Search:**
- Embedding generation
- Vector database integration
- Pinecone, Weaviate, Chroma
- Hybrid search (keyword + vector)

**RAG Pipeline:**
- Document ingestion
- Chunking and embedding
- Vector storage
- Query processing
- Response generation

### 4. CF-Specific Implementation

**CfHttp Patterns:**
```cfml
// Basic Claude integration
result = cfhttp(method="POST", url="#variables.apiEndpoint#", result="result") {
    cfhttpparam(type="header", name="x-api-key", value="#variables.apiKey#");
    cfhttpparam(type="header", name="Content-Type", value="application/json");
    cfhttpparam(type="body", value=serializeJSON(payload));
}
```

**Error Handling:**
- Rate limiting (cfthread + sleep)
- Timeout handling
- Retry logic
- Graceful degradation

### 5. MCP (Model Context Protocol)

- What is MCP
- When to use MCP
- CF integration points

### 6. Security and Privacy

- Data sensitivity classification
- PII handling
- API key management
- Local vs cloud models
- Audit logging

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Basic Chatbot](./exercises/exercise-1.md) | CFHTTP + Claude API | Working chatbot |
| [Exercise 2: Document Q&A](./exercises/exercise-2.md) | PDF + AI search | Document Q&A system |
| [Exercise 3: Vector Search](./exercises/exercise-3.md) | Embeddings + vector DB | Semantic search prototype |
| [Exercise 4: RAG Pipeline](./exercises/exercise-4.md) | End-to-end RAG | Full RAG implementation |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Deliverable

Contribute to the [CF AI Integration Playbook](../DELIVERABLES/cf-ai-integration-playbook.md) with implementation patterns.

## Resources

- Planned: AI fundamentals documentation
- [Claude API Documentation](https://docs.anthropic.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [RAG Patterns](https://arxiv.org/abs/2005.11401)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 10 |
| Exercises | 8 |
| Assessment | 2 |
| **Total** | **20 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Identify 3+ AI use cases for any ColdFusion application
2. Integrate Claude or OpenAI via CFHTTP
3. Build a working chatbot prototype
4. Design a RAG pipeline for document search

## Next Phase

[Phase 7: UI Modernization](../07-ui-modernization/) — Learn to modernize the front end of ColdFusion applications.
