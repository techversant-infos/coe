# Exercise 5: Secure REST API Build

> Build a performant, secure REST API with proper error handling.

## Objective

Create a complete REST API for a resource (users, products, orders) with proper security, documentation, and error handling.

## Prerequisites

- ColdFusion 2018+ or Lucee 5+
- Understanding of HTTP methods and status codes
- Basic database knowledge

## Instructions

### Part 1: API Design

Design a REST API for a "tasks" resource:

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/tasks | GET | List all tasks |
| /api/tasks/:id | GET | Get single task |
| /api/tasks | POST | Create task |
| /api/tasks/:id | PUT | Update task |
| /api/tasks/:id | DELETE | Delete task |

Document the request/response format:

```json
// GET /api/tasks
{
    "data": [...],
    "meta": {
        "total": 100,
        "page": 1,
        "perPage": 20
    }
}

// GET /api/tasks/:id
{
    "data": {
        "id": 1,
        "title": "Task title",
        "status": "pending",
        "createdAt": "2024-01-01T00:00:00Z"
    }
}

// Error response
{
    "error": {
        "code": "NOT_FOUND",
        "message": "Task not found"
    }
}
```

### Part 2: Component Structure

Create the API component:

```cfml
component {

    remote any function GET(string id = "") returnformat="json" {
        try {
            if (len(arguments.id)) {
                return getTask(arguments.id);
            }
            return listTasks();
        } catch (any e) {
            return errorResponse(500, "INTERNAL_ERROR", e.message);
        }
    }

    remote any function POST(required struct data) returnformat="json" {
        try {
            validateInput(arguments.data);
            return createTask(arguments.data);
        } catch (any e) {
            return errorResponse(400, "VALIDATION_ERROR", e.message);
        }
    }

    // ... PUT and DELETE methods

}
```

### Part 3: Error Handling

Implement consistent error responses:

```cfml
private struct function errorResponse(required numeric status, required string code, required string message) {
    return {
        status = arguments.status,
        error = {
            code = arguments.code,
            message = arguments.message
        }
    };
}
```

Define standard error codes:

| Code | Status | When |
|------|--------|------|
| VALIDATION_ERROR | 400 | Invalid input |
| UNAUTHORIZED | 401 | Not authenticated |
| FORBIDDEN | 403 | Not authorized |
| NOT_FOUND | 404 | Resource not found |
| CONFLICT | 409 | Resource conflict |
| INTERNAL_ERROR | 500 | Server error |

### Part 4: Security

Implement security measures:

1. **Authentication** (choose one):
   - API Key authentication
   - JWT tokens
   - Basic auth

2. **Input Validation**:
```cfml
private void function validateTask(required struct data) {
    if (not structKeyExists(data, 'title') or not len(trim(data.title))) {
        throw(type="ValidationException", message="Title is required");
    }
    if (structKeyExists(data, 'title') and len(data.title) > 255) {
        throw(type="ValidationException", message="Title too long");
    }
}
```

3. **Rate Limiting**:
```cfml
// Implement rate limiting in onRequestStart
private boolean function checkRateLimit(required string clientId) {
    local.key = "rate:#arguments.clientId#";
    local.count = cacheGet(local.key) ?: 0;
    
    if (local.count >= 100) {
        return false; // Rate limited
    }
    
    cachePut(local.key, local.count + 1, createTimeSpan(0, 0, 1, 0));
    return true;
}
```

### Part 5: Documentation

Create API documentation:

```markdown
# Tasks API

## Authentication

All requests require an API key in the header:
```
X-API-Key: your-api-key
```

## Endpoints

### List Tasks
```
GET /api/tasks
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| perPage | int | No | Items per page (default: 20, max: 100) |

**Response:** 200 OK
```json
{
    "data": [...],
    "meta": { "total": 100, "page": 1, "perPage": 20 }
}
```

### Create Task
```
POST /api/tasks
Content-Type: application/json

{
    "title": "Task title",
    "description": "Optional description"
}
```

**Response:** 201 Created
```

## Expected Outcome

1. **Working API** — All CRUD operations functional
2. **Error Handling** — Consistent error responses
3. **Security** — Authentication and input validation
4. **Documentation** — Complete API docs
5. **Testing** — API calls demonstrating functionality

## REST API Checklist

- [ ] Proper HTTP methods used
- [ ] Appropriate status codes returned
- [ ] JSON format consistent
- [ ] Input validation on all endpoints
- [ ] Error responses consistent
- [ ] Authentication implemented
- [ ] Rate limiting considered
- [ ] CORS configured if needed
- [ ] Documentation complete

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| All CRUD endpoints functional | 25 |
| Consistent error handling | 20 |
| Input validation | 15 |
| Security implemented | 15 |
| API documentation | 15 |
| Professional code quality | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
