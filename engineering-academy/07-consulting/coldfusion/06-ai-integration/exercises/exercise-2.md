# Exercise 2: Document Q&A System

> Build a document search and Q&A system using AI.

## Objective

Learn to process documents and answer questions using AI.

## Scenario

**Application:** Legal document portal
**Goal:** Allow users to ask questions about uploaded documents

## Instructions

### Part 1: Document Processing Pipeline

Design the document processing flow:

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Upload   │────►│ Extract  │────►│ Chunk    │────►│ Generate│
│ Document │     │ Text     │     │ Text     │     │ Embeddings│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                                                             │
                                                             ▼
                                                        ┌──────────┐
                                                        │ Store in │
                                                        │ Vector DB│
                                                        └──────────┘
```

### Part 2: Text Extraction

Extract text from PDF:

```cfml
// Using PDFtk or cfpdf
public string function extractText(required string filePath) {
    
    // Try Lucee PDF extension first
    try {
        local.pdf = pdf action="read" source=arguments.filePath;
        return local.pdf;
    } catch (any e) {
        // Fallback to pdftotext
        local.result = "";
        cfexecute(
            name="pdftotext",
            arguments=""#arguments.filePath#" -",
            variable="local.result",
            timeout=60
        );
        return local.result;
    }
}
```

### Part 3: Text Chunking

Implement chunking strategy:

```cfml
public array function chunkText(required string text, numeric chunkSize = 1000, numeric overlap = 100) {
    
    local.chunks = [];
    local.text = arguments.text;
    
    while (len(local.text) > 0) {
        local.chunk = left(local.text, arguments.chunkSize);
        
        // Try to break at sentence or paragraph
        local.breakPoint = reFindNoCase("[\.\!\?]\s", local.chunk);
        if (local.breakPoint > arguments.chunkSize / 2) {
            local.chunk = left(local.chunk, local.breakPoint);
        }
        
        local.chunks.append(trim(local.chunk));
        
        // Move to next chunk with overlap
        local.text = right(local.text, max(0, len(local.text) - len(local.chunk)));
        if (len(local.text) > arguments.overlap) {
            local.text = mid(local.text, arguments.overlap + 1, len(local.text) - arguments.overlap);
        }
    }
    
    return local.chunks;
}
```

**Chunking considerations:**

| Factor | Choice | Why |
|--------|--------|-----|
| Chunk size | | |
| Overlap | | |
| Split method | | |

### Part 4: Embedding Generation

Generate embeddings:

```cfml
public array function generateEmbedding(required string text) {
    
    local.payload = {
        input: text,
        model: "text-embedding-ada-002"
    };
    
    cfhttp(method="POST",
           url="https://api.openai.com/v1/embeddings",
           result="local.result") {
        cfhttpparam(type="header", name="Authorization", value="Bearer #variables.apiKey#");
        cfhttpparam(type="header", name="Content-Type", value="application/json");
        cfhttpparam(type="body", value=serializeJSON(local.payload));
    }
    
    local.response = deserializeJSON(local.result.fileContent);
    
    return local.response.data[1].embedding;
}
```

### Part 5: Store in Vector Database

Store embeddings (example with simple file-based):

```cfml
public void function storeEmbedding(required string docId, required string chunk, required array embedding) {
    
    local.record = {
        docId: arguments.docId,
        chunk: arguments.chunk,
        embedding: arguments.embedding,
        timestamp: now()
    };
    
    // Store in database
    queryExecute(
        "INSERT INTO document_embeddings (doc_id, chunk_text, embedding, created_at)
         VALUES (?, ?, ?, ?)",
        [arguments.docId, arguments.chunk, serializeJSON(arguments.embedding), now()]
    );
}
```

### Part 6: Semantic Search

Search for relevant chunks:

```cfml
public array function semanticSearch(required string query, numeric maxResults = 5) {
    
    // Generate query embedding
    local.queryEmbedding = generateEmbedding(arguments.query);
    
    // Retrieve all stored embeddings
    local.storedEmbeddings = queryExecute(
        "SELECT id, chunk_text, embedding FROM document_embeddings"
    );
    
    // Calculate similarities
    local.results = [];
    for (local.row in local.storedEmbeddings) {
        local.stored = deserializeJSON(local.row.embedding);
        local.similarity = cosineSimilarity(local.queryEmbedding, local.stored);
        local.results.append({
            id: local.row.id,
            chunk: local.row.chunk_text,
            score: local.similarity
        });
    }
    
    // Sort and return top results
    local.results.sort((a, b) => b.score - a.score);
    
    return local.results.slice(1, arguments.maxResults);
}
```

## Expected Outcome

1. Document processing pipeline
2. Text extraction and chunking
3. Embedding generation
4. Storage and retrieval system

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Pipeline design sound | 20 |
| Text extraction implemented | 20 |
| Chunking strategy appropriate | 20 |
| Embedding generation working | 20 |
| Search functional | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
