# Modern REST API Best Practices & Style Guide
**Version:** 1.0  
**Audience:** Backend Developers, Architects, QA  
**Applies to:** All REST APIs (Laravel + General)

---

## 1. Core Principles

- **Resource‑oriented:** APIs should model nouns, not verbs.  
  - **Good:** `/customers`, `/customers/{id}/orders`  
  - **Bad:** `/getCustomer`, `/createCustomerOrder`
- **Consistent:** Naming conventions, error formats, and HTTP semantics must remain uniform.
- **Predictable:** API consumers should easily guess endpoints based on domain logic.
- **Stateless:** Every request must contain all required authentication and context.

---

## 2. URL Design & Naming

### 2.1 Base Rules
- Base URL must include versioning:  
  `https://api.example.com/v1/`
- Use **kebab-case** or **snake_case** for paths & parameters. Choose one org‑wide.
- Always use **plural nouns** for resources.

### 2.2 Resource Patterns
| Type | Example |
|------|---------|
| Collection | `GET /users`, `POST /users` |
| Single item | `GET /users/{id}`, `PATCH /users/{id}` |
| Sub-resource | `GET /users/{id}/orders` |

> **Rule:** Avoid nesting deeper than 2 levels.

### 2.3 Non‑CRUD Actions
Use verbs as subordinate resources, not top‑level endpoints:
```
POST /customers/{id}/activate
POST /orders/{id}/refund
POST /auth/login
```

---

## 3. HTTP Methods & Idempotency

| Method | Meaning | Idempotent |
|--------|---------|------------|
| **GET** | Retrieve resource(s) | ✅ Yes |
| **POST** | Create resource or perform unsafe action | ❌ No |
| **PUT** | Replace entire resource | ✅ Yes |
| **PATCH** | Partial update | ⚠️ Should be |
| **DELETE** | Remove resource | ✅ Yes |

### 3.1 Idempotency Keys (for payment & critical operations)
```
Idempotency-Key: <uuid>
```

---

## 4. Request & Response Format

### 4.1 Content Types
```
Content-Type: application/json
Accept: application/json
```

### 4.2 Data Naming
Use **camelCase** or **snake_case** consistently.

### 4.3 Standard Success Response
```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Gold Tier"
  },
  "meta": {}
}
```

### 4.4 Standard Error Response
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input provided.",
    "details": {
      "email": ["The email field is required."]
    },
    "traceId": "a1b2c3d4"
  }
}
```

---

## 5. HTTP Status Codes (Detailed Guide)

### 5.1 2xx — Success
| Code | Meaning | Usage |
|------|---------|--------|
| **200 OK** | Success with response | GET, PUT, PATCH |
| **201 Created** | Resource created | POST new records |
| **202 Accepted** | Async processing started | Queued jobs |
| **204 No Content** | Success without body | DELETE, some PATCH |

---

### 5.2 4xx — Client Errors
| Code | Meaning | Description |
|------|---------|-------------|
| **400 Bad Request** | Invalid input | Missing fields, malformed JSON |
| **401 Unauthorized** | Invalid/missing credentials | Token missing/expired |
| **403 Forbidden** | Permission denied | RBAC or ownership failure |
| **404 Not Found** | Resource missing | Hidden if access denied |
| **409 Conflict** | Version conflict or duplicate | Idempotency, uniqueness |
| **422 Unprocessable Entity** | Semantic validation errors | Field validations |
| **429 Too Many Requests** | Rate limit exceeded | Throttling |

---

### 5.3 5xx — Server Errors
| Code | Meaning | Description |
|------|---------|-------------|
| **500 Internal Server Error** | Unexpected error | Should be logged with traceId |
| **503 Service Unavailable** | Downstream dependency failure | CRM/POS unavailable |

---

## 6. Pagination, Filtering, Sorting

### 6.1 Pagination
```
GET /customers?page=1&pageSize=20
```

Response:
```json
{
  "success": true,
  "data": [],
  "meta": {
    "page": 1,
    "pageSize": 20,
    "total": 145,
    "totalPages": 8
  }
}
```

### 6.2 Filtering
```
GET /transactions?status=success&tier=gold&minAmount=5000
```

### 6.3 Advanced Filtering
```
GET /transactions?filter[tier]=gold&filter[minDate]=2025-01-01
```

### 6.4 Sorting
```
GET /customers?sort=createdAt         # asc
GET /customers?sort=-createdAt        # desc
```

---

## 7. Security Best Practices

### 7.1 HTTPS Only
All public APIs must enforce TLS.

### 7.2 Authentication
Use bearer tokens:
```
Authorization: Bearer <token>
```

### 7.3 Authorization
- Enforce role permissions
- Enforce ownership (customer can only access their data)

### 7.4 Sensitive Data Masking
Never return:
- Passwords
- Tokens
- OTPs
- Secret keys

### 7.5 Rate Limiting
Return:
```
429 Too Many Requests
```

---

## 8. Concurrency & Resource Locking

### Optimistic Locking Using ETags
Request:
```
GET /tiers/123
ETag: "v5"
```

Update:
```
PUT /tiers/123
If-Match: "v5"
```

If mismatch:
```
409 Conflict
```

---

## 9. Versioning

- Use **URL versioning**:
  - `/v1/users`
  - `/v2/users`
- Increment version only when introducing breaking changes.

---

## 10. API Documentation Standards

### 10.1 OpenAPI (Swagger)
Must be maintained in the repo:
```
openapi.yaml / openapi.json
```

### 10.2 Example Payloads
Provide examples for:
- Auth
- Errors
- Pagination
- Validation failures

---

## 11. Logging & Observability

### 11.1 Required Logs
- Path  
- Method  
- Status code  
- Execution time  
- `traceId`  

### 11.2 Never Log
- Passwords  
- Tokens  
- OTPs  
- Sensitive user data

### 11.3 Error Logging
Client gets generic error;  
Server logs full stack trace.

---

## 12. Testing Requirements

### Testing Types
- **Unit tests** — business logic  
- **Integration tests** — DB + API  
- **Contract tests** — external clients  
- **Smoke tests** — before deployment  

---

## 13. Deprecation Strategy

When removing/changing endpoints:

1. Mark as deprecated in documentation  
2. Add headers:
```
Deprecation: true
Sunset: 2025-12-31
```
3. Provide migration path  
4. Remove only after deadline  

---

## 14. Developer Checklist (Before Merge)

- [ ] URL naming follows REST rules  
- [ ] Correct HTTP method used  
- [ ] Response matches standard envelope  
- [ ] Proper status codes used  
- [ ] Error structure correct  
- [ ] Pagination/filter/sort implemented  
- [ ] Input validation enforced  
- [ ] Auth + authorization checks applied  
- [ ] No sensitive data leaked  
- [ ] OpenAPI updated  
- [ ] Unit + integration tests added  

---

## End of Document
