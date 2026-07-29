# Exercise 3: Vector Search Implementation

> Implement semantic search with vector databases.

## Objective

Learn to integrate vector databases for semantic search.

## Scenario

**Application:** Knowledge base
**Goal:** Allow natural language search across articles

## Instructions

### Part 1: Vector Database Options

Compare options:

| Database | Pros | Cons | Best For |
|----------|------|------|----------|
| Pinecone | | | |
| Weaviate | | | |
| Chroma | | | |
| pgvector | | | |
| Elasticsearch | | | |

### Part 2: Pinecone Integration

Implement Pinecone search:

```cfml
component {
    
    variables.pineconeApiKey = serverSystem.ENV.PINECONE_API_KEY;
    variables.indexUrl = "https://YOUR-INDEX.svc.pinecone.io";
    
    public struct function upsertVector(required string id, required array embedding, required struct metadata) {
        
        local.payload = {
            vectors: [{
                id: arguments.id,
                values: arguments.embedding,
                metadata: arguments.metadata
            }]
        };
        
        cfhttp(method="POST",
               url="#variables.indexUrl#/vectors/upsert",
               result="local.result") {
            cfhttpparam(type="header", name="Api-Key", value=variables.pineconeApiKey);
            cfhttpparam(type="header", name="Content-Type", value="application/json");
            cfhttpparam(type="body", value=serializeJSON(local.payload));
        }
        
        return deserializeJSON(local.result.fileContent);
    }
    
    public array function query(required array queryEmbedding, numeric topK = 10) {
        
        local.payload = {
            topK: arguments.topK,
            vector: arguments.queryEmbedding,
            includeMetadata: true
        };
        
        cfhttp(method="POST",
               url="#variables.indexUrl#/query",
               result="local.result") {
            cfhttpparam(type="header", name="Api-Key", value=variables.pineconeApiKey);
            cfhttpparam(type="header", name="Content-Type", value="application/json");
            cfhttpparam(type="body", value=serializeJSON(local.payload));
        }
        
        local.response = deserializeJSON(local.result.fileContent);
        return local.response.matches;
    }
}
```

### Part 3: Hybrid Search

Combine keyword and vector search:

```cfml
public struct function hybridSearch(required string query, numeric topK = 10) {
    
    // Step 1: Generate query embedding
    local.embedding = generateEmbedding(arguments.query);
    
    // Step 2: Vector search
    local.vectorResults = vectorSearch(embedding=local.embedding, topK=topK * 2);
    
    // Step 3: Keyword search (Elasticsearch or database)
    local.keywordResults = keywordSearch(query=arguments.query, limit=topK * 2);
    
    // Step 4: RRF fusion (Reciprocal Rank Fusion)
    local.fused = reciprocalRankFusion(vectorResults=local.vectorResults, 
                                       keywordResults=local.keywordResults,
                                       k=60);
    
    return local.fused;
}

private array function reciprocalRankFusion(required array vectorResults, 
                                            required array keywordResults,
                                            numeric k = 60) {
    
    local.scores = {};
    
    // Score vector results
    for (local.i = 1; local.i <= arrayLen(arguments.vectorResults); local.i++) {
        local.id = arguments.vectorResults[local.i].id;
        local.scores[local.id] = 1 / (k + local.i);
    }
    
    // Add keyword scores
    for (local.i = 1; local.i <= arrayLen(arguments.keywordResults); local.i++) {
        local.id = arguments.keywordResults[local.i].id;
        if (structKeyExists(local.scores, local.id)) {
            local.scores[local.id] += 1 / (k + local.i);
        } else {
            local.scores[local.id] = 1 / (k + local.i);
        }
    }
    
    // Sort and return
    local.sorted = structSort(local.scores, "numeric", "desc");
    return local.sorted;
}
```

### Part 4: Performance Optimization

Address performance concerns:

| Concern | Solution |
|---------|----------|
| Slow embedding generation | |
| Large vector storage | |
| Query latency | |
| Index updates | |

## Expected Outcome

1. Vector DB integration
2. Hybrid search implementation
3. Performance optimization

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Vector DB integration | 30 |
| Hybrid search implementation | 30 |
| Performance considered | 25 |
| Professional presentation | 15 |
| **Total** | **100** |

**Passing Score:** 70/100
