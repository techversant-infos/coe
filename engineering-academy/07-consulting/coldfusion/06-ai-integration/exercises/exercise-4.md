# Exercise 4: RAG Pipeline

> Build a complete RAG (Retrieval-Augmented Generation) pipeline.

## Objective

Learn to implement a full RAG system with ColdFusion.

## Scenario

**Application:** Customer support knowledge base
**Goal:** Answer customer questions using relevant documents

## Instructions

### Part 1: System Architecture

Design the RAG architecture:

```
User Question
     │
     ▼
┌─────────────┐
│  Embedding  │
│  Generation │
└─────────────┘
     │
     ▼
┌─────────────┐     ┌─────────────┐
│   Vector    │────►│  Retrieve  │
│   Database  │     │  Relevant  │
└─────────────┘     │   Chunks   │
                    └─────────────┘
                           │
                           ▼
┌─────────────┐     ┌─────────────┐
│   Generate  │◄────│   Build    │
│   Response  │     │   Prompt   │
└─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Return to  │
                    │    User     │
                    └─────────────┘
```

### Part 2: Document Ingestion Service

```cfml
component {
    
    public void function ingestDocument(required string filePath, required string metadata) {
        
        // 1. Extract text
        local.text = textExtractor.extract(arguments.filePath);
        
        // 2. Chunk text
        local.chunks = textChunker.chunk(local.text, chunkSize=1000, overlap=100);
        
        // 3. Generate embeddings and store
        for (local.i = 1; local.i <= arrayLen(local.chunks); local.i++) {
            local.chunk = local.chunks[local.i];
            local.embedding = embeddingService.generate(local.chunk);
            
            vectorStore.upsert(
                id: "#arguments.metadata.docId#_#local.i#",
                embedding: local.embedding,
                metadata: {
                    docId: arguments.metadata.docId,
                    chunkIndex: local.i,
                    text: local.chunk,
                    title: arguments.metadata.title
                }
            );
        }
    }
}
```

### Part 3: Query Service

```cfml
public struct function query(required string question) {
    
    // 1. Generate query embedding
    local.queryEmbedding = embeddingService.generate(arguments.question);
    
    // 2. Retrieve relevant chunks
    local.chunks = vectorStore.query(
        embedding: local.queryEmbedding,
        topK: 5,
        filter: {}  // Optional metadata filter
    );
    
    // 3. Build context
    local.context = "";
    for (local.chunk in local.chunks) {
        local.context &= local.chunk.metadata.text & chr(10) & chr(10);
    }
    
    // 4. Build prompt
    local.prompt = buildPrompt(question=arguments.question, context=local.context);
    
    // 5. Generate response
    local.response = llmService.complete(prompt=local.prompt);
    
    return {
        answer: local.response,
        sources: local.chunks.map(c => ({
            docId: c.metadata.docId,
            title: c.metadata.title,
            excerpt: left(c.metadata.text, 200)
        }))
    };
}

private string function buildPrompt(required string question, required string context) {
    return "You are a helpful customer support assistant. Use the following context to answer the user's question.
    
Context:
#arguments.context#

Question: #arguments.question#

Answer:";
}
```

### Part 4: Complete Implementation

Implement the full pipeline:

```cfml
// ragService.cfc
component {
    
    property name="textExtractor" inject="textExtractor";
    property name="textChunker" inject="textChunker";
    property name="embeddingService" inject="embeddingService";
    property name="vectorStore" inject="vectorStore";
    property name="llmService" inject="llmService";
    
    public void function ingest(required string filePath, struct metadata) {
        // Implement ingestion
    }
    
    public struct function query(required string question) {
        // Implement query
    }
}
```

### Part 5: Performance Optimization

| Optimization | Implementation |
|-------------|----------------|
| Batch embedding | |
| Async processing | |
| Caching | |
| Chunk optimization | |

## Expected Outcome

1. Complete RAG architecture
2. Ingestion service
3. Query service
4. Performance optimization

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Architecture sound | 20 |
| Ingestion complete | 25 |
| Query pipeline | 25 |
| Performance considered | 20 |
| Professional presentation | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
