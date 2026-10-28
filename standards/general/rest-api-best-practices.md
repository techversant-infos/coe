# REST API Best Practices & Style Guide  
**Version:** 3.0  
**Audience:** Backend Developers, Architects, QA  
**Scope:** Company-wide (Framework-agnostic, reusable across all teams)**



# 1. Core Principles

- **Resource-oriented:** APIs should expose nouns, not verbs.  
- **Consistency over cleverness:** Every team should follow the same naming, structure, and behavior patterns.
- **Predictable responses:** All success and error responses follow the same envelope.  
- **Stateless:** Server stores no client-specific session state.
- **Discoverability:** Endpoints should be guessable by developers.



# 2. URL Design & Naming

## 2.1 Versioning Strategy (Mandatory)
Use version prefix in every endpoint:

```
https://api.company.com/v1/
https://api.company.com/v2/
```

## 2.2 Naming Conventions
- **Plural nouns** for resources  
  `/customers`, `/orders`, `/transactions`
- **kebab-case** OR **snake_case** in URLs (choose org-wide)
- Resources never end with verbs  
  ❌ `/createCustomer`  
  ✔ `/customers`

## 2.3 Standard Resource Structure
```
GET    /customers
POST   /customers
GET    /customers/{id}
PATCH  /customers/{id}
DELETE /customers/{id}
```

## 2.4 Nested Resources (Max Depth = 2)
```
GET /customers/{id}/orders
POST /customers/{id}/addresses
```

## 2.5 Action Endpoints (Non-CRUD)
```
POST /customers/{id}/activate
POST /orders/{id}/refund
POST /auth/login
POST /auth/logout
```



# 3. HTTP Methods & Idempotency

| Method | Purpose | Idempotent |
|--------|---------|------------|
| GET    | Retrieve resources | Yes |
| POST   | Create resource / action | No |
| PUT    | Replace entire resource | Yes |
| PATCH  | Partial update | Ideally yes |
| DELETE | Remove resource | Yes |

## 3.1 Idempotency for POST  
For payment, loyalty redemption, coupon usage, etc.

```
Idempotency-Key: <uuid>
```

If duplicate POST arrives with same key → return **same response**, not duplicate action.



# 4. Request Payload Standards

## 4.1 JSON Naming Convention (Strict)
Use **camelCase** for JSON keys:

```
firstName
lastName
dateOfBirth
phoneNumber
```

Avoid mixing different conventions.

## 4.2 Boolean Naming Convention (MANDATORY)
Booleans MUST use prefixes:

```
isActive
hasSubscription
canRedeem
shouldNotify
isVerified
```

❌ Avoid ambiguous:  
```
active
enabled
verified
```

## 4.3 Date Format (ISO 8601 Only)
```
"birthDate": "1990-12-24"
"createdAt": "2025-01-20T14:30:00Z"
"updatedAt": "2025-01-20T14:30:00+05:30"
```

## 4.4 Numeric Format
```
"salary": 45000.50
"quantity": 3
```

## 4.5 Null vs Missing Fields
- Use `null` only when intentional.
- Prefer omission for optional fields.



# 5. Success & Error Responses

## 5.1 Success Response Format
```json
{
  "success": true,
  "data": {
    "id": "U123",
    "firstName": "Lajin",
    "tier": "GOLD"
  },
  "meta": {
    "traceId": "abc123"
  }
}
```

## 5.2 Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed.",
    "details": {},
    "traceId": "req-55493"
  }
}
```

## 5.3 Should we include HTTP Status Code inside JSON?
Optional for debugging:
```json
{
  "error": {
    "httpStatus": 422,
    "code": "VALIDATION_ERROR"
  }
}
```



# 6. HTTP Status Codes (Descriptive)

### 2xx Success
| Code | Meaning | Example |
|------|---------|---------|
| **200** | Successful response | GET /customers |
| **201** | Resource created | POST /customers |
| **202** | Accepted for async processing | Long-running tasks |
| **204** | No content | DELETE success |

### 4xx Client Errors
| Code | Meaning | Example |
|------|----------|---------|
| **400** | Bad request | Malformed JSON |
| **401** | Unauthorized | Invalid/expired token |
| **403** | Forbidden | Role lacks permissions |
| **404** | Not found | Unknown customer ID |
| **409** | Conflict | Duplicate record, version mismatch |
| **422** | Validation failed | Missing or invalid fields |
| **429** | Rate limit exceeded | Too many requests |

### 5xx Server Errors
| Code | Meaning |
|------|---------|
| **500** | Unexpected server failure |
| **503** | Upstream service unavailable |



# 7. Validation Error Examples

## 7.1 Single Error
```json
{
  "error": {
    "details": {
      "email": ["The email field is required."]
    }
  }
}
```

## 7.2 Multiple Errors
```json
{
  "error": {
    "details": {
      "email": ["Invalid email format."],
      "password": [
        "Must be at least 8 characters.",
        "Must contain one uppercase letter."
      ]
    }
  }
}
```

## 7.3 Nested Object Errors
```json
{
  "error": {
    "details": {
      "address.line1": ["Line1 is required."],
      "address.city": ["Invalid city."]
    }
  }
}
```

## 7.4 Array Errors
```json
{
  "error": {
    "details": {
      "items[0].productId": ["Product does not exist."],
      "items[1].quantity": ["Quantity must be > 0."]
    }
  }
}
```



# 8. Filtering, Sorting & Pagination

## 8.1 Pagination
```
GET /customers?page=1&pageSize=20
```

## 8.2 Basic Filters
```
GET /customers?tier=gold&isActive=true
```



# 8.3 Advanced Filters (Descriptive)

We use **suffix-based operator naming**, because it is:

✔ Easy to read  
✔ Easy to parse  
✔ Matches Stripe, Shopify standards  

### Supported Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `_gt` | Greater than | `filter[salary_gt]=20000` |
| `_gte` | Greater or equal | `filter[amount_gte]=5000` |
| `_lt` | Less than | `filter[age_lt]=60` |
| `_lte` | Less or equal | `filter[quantity_lte]=5` |
| `_ne` | Not equal | `filter[status_ne]=inactive` |
| `_in` | In list | `filter[tier_in]=gold,silver,platinum` |
| `_between` | Value in range | `filter[amount_between]=500,5000` |

### Examples

#### **1. Salary > 2000**
```
GET /employees?filter[salary_gt]=2000
```

#### **2. Created between 1 Jan and 31 Jan**
```
GET /transactions?filter[createdAt_gte]=2025-01-01&filter[createdAt_lte]=2025-01-31
```

#### **3. Tier in (Gold, Silver)**
```
GET /customers?filter[tier_in]=gold,silver
```

#### **4. Discount between 10% and 25%**
```
GET /products?filter[discount_between]=10,25
```

#### **5. Multiple filters combined**
```
GET /transactions?filter[amount_gt]=5000&filter[city_in]=Kochi,Bangalore&filter[isActive]=true
```



# 8.4 Sorting (Detailed Examples)

### Format:
```
sort=fieldName
sort=-fieldName  // descending
```

### Examples:

#### Sort customers by creation date (latest first)
```
GET /customers?sort=-createdAt
```

#### Sort transactions by amount ASC, then date DESC
```
GET /transactions?sort=amount,-createdAt
```

#### Sort employees by salary ASC
```
GET /employees?sort=salary
```



# 9. Security

### Authorization Header
```
Authorization: Bearer <token>
```

### Sensitive Data Never Returned
- Passwords  
- OTP  
- API keys  
- Tokens  
- Secrets  



# 10. Rate Limiting

### Response Headers
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 755
X-RateLimit-Reset: 1737480912
```

### 429 Error Example
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Retry after 60 seconds."
  }
}
```



# 11. Concurrency & ETags

### Example:
```
GET /customers/123
ETag: "v7"
```

```
PUT /customers/123
If-Match: "v7"
```

If mismatch:
```
409 Conflict
```



# 12. Versioning (Detailed)

### 12.1 URL Versioning (Preferred)
```
/v1/customers
/v2/customers
```

### 12.2 Handling Versions in Code
- Separate controllers/modules per version.
- Domain logic stays version-agnostic.
- No branching logic:  
  ❌ `if version == 1`  



# 13. Logging & Observability

Log:
- Method  
- Path  
- Status code  
- Latency  
- traceId  

Never Log:
- Password  
- OTP  
- Tokens  
- Secrets  



# 14. Testing Requirements

- Unit tests  
- Integration tests  
- Contract tests  
- Smoke tests  



# 15. Deprecation Policy

Include:
```
Deprecation: true
Sunset: 2026-01-31
```



# 16. API Review Checklist

- [ ] Naming conventions followed  
- [ ] Boolean naming correct  
- [ ] Pagination & filters implemented  
- [ ] Sorting works with multiple fields  
- [ ] Advanced filtering rules applied  
- [ ] Error envelope consistent  
- [ ] No sensitive data exposed  
- [ ] Versioning correct  
- [ ] Rate limits applied  
- [ ] OpenAPI updated  
- [ ] Tests complete  



