# REST API Best Practices & Style Guide
**Version:** 2.0  
**Audience:** Backend Developers, Architects, QA  
**Scope:** Company-wide (Framework-agnostic)

---

## 1. Core Principles

- **Resource-oriented:** APIs should model nouns, not verbs.  
  - Good: `/customers`, `/customers/{id}/orders`  
  - Bad: `/getCustomer`, `/createOrderNow`
- **Consistency:** Naming, HTTP semantics, and error formatting must be uniform.
- **Predictability:** Endpoints should be guessable based on domain logic.
- **Statelessness:** Each request is independent; no server-side session state.

---

## 2. URL Design & Naming

### 2.1 Base URL & Versioning
Use prefix-based versioning:
```
https://api.company.com/v1/
```

### 2.2 Naming Conventions
- Use **kebab-case** or **snake_case**.
- Use **plural nouns**.

### 2.3 Resource Structure
```
GET    /customers
POST   /customers
GET    /customers/{id}
PATCH  /customers/{id}
DELETE /customers/{id}
```

### 2.4 Sub-resources (Max depth: 2)
```
GET /customers/{id}/orders
POST /customers/{id}/addresses
```

### 2.5 Non-CRUD Actions
```
POST /customers/{id}/activate
POST /orders/{id}/cancel
POST /auth/login
```

---

## 3. HTTP Methods & Idempotency

| Method | Usage | Idempotent |
|--------|--------|------------|
| GET | Retrieve resource | Yes |
| POST | Create / Non-idempotent | No |
| PUT | Replace entire resource | Yes |
| PATCH | Partial update | Should be |
| DELETE | Remove resource | Yes |

Idempotency keys for critical POST:
```
Idempotency-Key: <uuid>
```

---

## 4. Request Payload Standards

### 4.1 JSON Naming Convention
Choose one: **camelCase** (preferred) or **snake_case**.

### 4.2 Boolean Naming Convention
Booleans MUST use prefixes:
```
isActive
hasSubscription
canRedeem
shouldNotify
```

Not recommended:
```
active
enabled
verified
```

### 4.3 Dates (ISO 8601)
```
1990-12-24
2025-01-20T14:30:00Z
2025-01-20T14:30:00+05:30
```

### 4.4 Numbers
Use numeric JSON values:
```
{ "quantity": 3, "amount": 1249.75 }
```

### 4.5 Null Handling
- Use `null` purposely.
- Omit optional fields when not required.

---

## 5. Response Structure

### Success Example
```json
{
  "success": true,
  "data": {},
  "meta": {}
}
```

### Error Example
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed.",
    "details": {},
    "traceId": "abc123"
  }
}
```

---

## 6. HTTP Status Codes (Detailed)

### 2xx Success
- 200 OK
- 201 Created
- 202 Accepted
- 204 No Content

### 4xx Client Errors
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Unprocessable Entity
- 429 Rate Limit Exceeded

### 5xx Server Errors
- 500 Internal Server Error
- 503 Service Unavailable

---

## 7. Validation Error Examples

### Single Error
```json
{
  "error": {
    "details": {
      "email": ["The email field is required."]
    }
  }
}
```

### Multiple Errors
```json
{
  "error": {
    "details": {
      "email": ["Invalid email format."],
      "password": ["Too short."]
    }
  }
}
```

### Nested Errors
```json
{
  "error": {
    "details": {
      "address.line1": ["Required"],
      "address.city": ["Invalid"]
    }
  }
}
```

### Array Errors
```json
{
  "error": {
    "details": {
      "items[0].productId": ["Invalid"],
      "items[1].quantity": ["Must be >= 1"]
    }
  }
}
```

---

## 8. Filtering, Sorting, Pagination

### Pagination
```
GET /customers?page=1&pageSize=20
```

### Basic Filtering
```
GET /customers?tier=gold&status=active
```

### Advanced Filtering
```
GET /transactions?filter[tier]=gold&filter[minAmount]=5000
```

### Sorting
```
GET /transactions?sort=-createdAt
```

---


### 8.5 Advanced Filtering Operators

Recommended operator-suffix pattern:

| Operator | Meaning | Example |
|----------|---------|---------|
| _gt | Greater than | filter[salary_gt]=2000 |
| _gte | Greater than or equal | filter[amount_gte]=500 |
| _lt | Less than | filter[age_lt]=60 |
| _lte | Less than or equal | filter[qty_lte]=10 |
| _ne | Not equal | filter[status_ne]=inactive |
| _in | In list | filter[tierIn]=gold,silver |
| _between | Range | filter[amountBetween]=500,5000 |

Examples:

```
GET /employees?filter[salary_gt]=2000
GET /transactions?filter[amount_gte]=5000&filter[tier]=gold
GET /products?filter[discountBetween]=10,25
GET /customers?filter[cityIn]=Kochi,Bangalore,Chennai
GET /transactions?filter[createdAt_gte]=2025-02-01&filter[createdAt_lte]=2025-02-28
```
## 9. Security & Rate Limiting

### Authorization Header
```
Authorization: Bearer <token>
```

### Sensitive Data Never Returned
- Passwords  
- Tokens  
- OTPs  
- Secrets  

### Rate-Limit Headers
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 755
X-RateLimit-Reset: 1737480912
```

429 Response:
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests."
  }
}
```

---

## 10. Concurrency & ETags

```
GET /tiers/123
ETag: "v5"
```

```
PUT /tiers/123
If-Match: "v5"
```

Response if mismatch:
```
409 Conflict
```

---

## 11. Versioning Strategy

### URL Versioning
```
/v1/resource
/v2/resource
```

### Handling Versions in Code
- Separate controllers/modules per version.
- Keep core domain logic version-agnostic.
- Avoid logic like `if version == ...`.

---

## 12. Logging & Observability

Log:
- HTTP method  
- Path  
- Status code  
- Execution time  
- traceId  

Never log:
- Passwords  
- Tokens  
- Sensitive PII  

---

## 13. Testing Requirements

- Unit tests  
- Integration tests  
- Contract tests  
- Smoke tests  

---

## 14. Deprecation Policy

Use headers:
```
Deprecation: true
Sunset: 2026-01-31
```

---

## 15. API Review Checklist

- [ ] Endpoint naming consistent  
- [ ] Correct HTTP method  
- [ ] JSON naming consistent  
- [ ] Boolean naming correct  
- [ ] Success & error envelope correct  
- [ ] Pagination & filtering correct  
- [ ] No sensitive data leaked  
- [ ] Versioning respected  
- [ ] OpenAPI updated  
- [ ] Tests added  

---

## End of Document
