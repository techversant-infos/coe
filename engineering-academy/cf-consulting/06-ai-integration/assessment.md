# Phase 6 Assessment: AI Integration

> Test your AI integration knowledge for ColdFusion.

**Time:** 1.5 hours | **Passing:** 70%

---

## Section A: API Integration (25 points)

### A1: CFHTTP Implementation (15 points)

Write the CFHTTP call to Claude API:

```cfml
// Complete the API call
local.result = cfhttp(method="___", 
                      url="https://api.anthropic.com/v1/messages",
                      result="local.response") {
    cfhttpparam(type="___", name="___", value="___");
    cfhttpparam(type="___", name="___", value="___");
    cfhttpparam(type="___", name="___", value=serializeJSON({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1024,
        messages: [{role: "user", content: "Hello"}]
    }));
}
```

### A2: Error Handling (10 points)

What errors could occur and how do you handle each?

| Error | Handling |
|-------|----------|
| API timeout | |
| Invalid API key | |
| Rate limit | |
| Malformed response | |

---

## Section B: RAG Pipeline (25 points)

### B1: Pipeline Components (15 points)

Order the RAG pipeline steps:

```
a) Generate embedding
b) Return response
c) Vector search
d) Generate answer
e) Chunk document
f) Extract text
g) Build prompt
h) Store vector
```

**Correct Order:**
_______________________________________________________

### B2: Chunking Strategy (10 points)

What chunk size would you recommend for:

| Document Type | Chunk Size | Rationale |
|--------------|-------------|-----------|
| Legal contracts | | |
| Support articles | | |
| Code documentation | | |

---

## Section C: Vector Databases (25 points)

### C1: Database Selection (15 points)

When would you choose each option?

| Database | When to Use |
|----------|-------------|
| Pinecone | |
| pgvector | |
| Chroma | |
| Elasticsearch | |

### C2: Query Optimization (10 points)

How do you optimize vector search for low latency?

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

---

## Section D: Security & Privacy (25 points)

### D1: Data Classification (15 points)

Classify this data for AI processing:

| Data | Sensitivity | AI Processing Allowed? |
|------|------------|----------------------|
| Public KB article | | Yes |
| Customer name | | |
| API keys | | |
| Internal policy | | |
| PII (SSN) | | |
| Code | | |

### D2: Security Best Practices (10 points)

List 5 security practices for AI integration:

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________
4. _______________________________________________________
5. _______________________________________________________

---

## Answer Key

### Section A
- A1: POST, header (x-api-key, anthropic-version, content-type), body
- A2: Timeout handling, validation, retry with backoff, JSON validation

### Section B
- B1: f → e → a → h → c → g → d → b
- B2: Legal = larger chunks, support = medium, code = function-level

### Section C
- C1: Pinecone for managed, pgvector for Postgres shops, Chroma for dev/simple, ES for search integration
- C2: Indexing, quantization, caching, batch queries

### Section D
- D1: PII never to external APIs, code may need review, internal depends
- D2: Input validation, output filtering, audit logging, key rotation, least privilege

---

## Scoring

| Section | Points |
|---------|--------|
| A: API Integration | 25 |
| B: RAG Pipeline | 25 |
| C: Vector Databases | 25 |
| D: Security | 25 |
| **Total** | **100** |

**Passing:** 70/100
