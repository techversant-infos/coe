# Exercise 3: Authentication System

> Implement JWT authentication between React and ColdFusion.

## Objective

Learn to handle authentication across React frontend and CF backend.

## Scenario

**Application:** Dashboard with protected routes
**Goal:** Secure API access with JWT tokens

## Instructions

### Part 1: CF Authentication Service

```cfml
component {
    
    variables.jwtSecret = serverSystem.ENV.JWT_SECRET;
    variables.tokenExpiry = 86400; // 24 hours
    
    public struct function login(required string username, required string password) {
        
        // Verify credentials
        local.user = queryExecute(
            "SELECT id, username, role, password_hash 
             FROM users 
             WHERE username = ?",
            [arguments.username]
        );
        
        if (local.user.recordCount == 0 || !bcrypt.verify(arguments.password, local.user.password_hash)) {
            return { success: false, error: "Invalid credentials" };
        }
        
        // Generate JWT
        local.token = generateToken(local.user);
        
        return {
            success: true,
            token: local.token,
            user: {
                id: local.user.id,
                username: local.user.username,
                role: local.user.role
            }
        };
    }
    
    private string function generateToken(required struct user) {
        local.payload = {
            sub: arguments.user.id,
            username: arguments.user.username,
            role: arguments.user.role,
            iat: now().getTime() / 1000,
            exp: (now().getTime() / 1000) + variables.tokenExpiry
        };
        
        // Create JWT header
        local.header = toBase64('{"alg":"HS256","typ":"JWT"}');
        
        // Create JWT payload
        local.payloadEncoded = toBase64(serializeJSON(local.payload));
        
        // Create signature
        local.signature = hmac(
            local.header & "." & local.payloadEncoded,
            variables.jwtSecret,
            "HMACSHA256"
        );
        
        return local.header & "." & local.payloadEncoded & "." & local.signature;
    }
    
    public struct function verifyToken(required string token) {
        try {
            local.parts = listToArray(arguments.token, ".");
            
            if (arrayLen(local.parts) != 3) {
                return { valid: false, error: "Invalid token format" };
            }
            
            local.header = local.parts[1];
            local.payload = local.parts[2];
            local.signature = local.parts[3];
            
            // Verify signature
            local.expectedSig = hmac(local.header & "." & local.payload, variables.jwtSecret, "HMACSHA256");
            if (local.signature != local.expectedSig) {
                return { valid: false, error: "Invalid signature" };
            }
            
            // Check expiration
            local.decodedPayload = deserializeJSON(toString(toBinary(local.payload)));
            if (local.decodedPayload.exp < (now().getTime() / 1000)) {
                return { valid: false, error: "Token expired" };
            }
            
            return { valid: true, user: local.decodedPayload };
            
        } catch (any e) {
            return { valid: false, error: "Token verification failed" };
        }
    }
}
```

### Part 2: React API Service

Create the React API service:

```javascript
// api.js
const API_BASE = process.env.REACT_APP_API_URL;

class ApiService {
  constructor() {
    this.token = localStorage.getItem('token');
  }
  
  setToken(token) {
    this.token = token;
    localStorage.setItem('token', token);
  }
  
  clearToken() {
    this.token = null;
    localStorage.removeItem('token');
  }
  
  async login(username, password) {
    const response = await fetch(`${API_BASE}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    
    const data = await response.json();
    
    if (data.success) {
      this.setToken(data.token);
    }
    
    return data;
  }
  
  async request(endpoint, options = {}) {
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers
    };
    
    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }
    
    const response = await fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers
    });
    
    if (response.status === 401) {
      this.clearToken();
      window.location.href = '/login';
      throw new Error('Unauthorized');
    }
    
    return response;
  }
  
  async get(endpoint) {
    return this.request(endpoint, { method: 'GET' });
  }
  
  async post(endpoint, data) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }
}

export const api = new ApiService();
```

### Part 3: Protected Route Component

```javascript
// ProtectedRoute.jsx
import { Navigate } from 'react-router-dom';
import { api } from './api';

export function ProtectedRoute({ children }) {
  const isAuthenticated = !!api.token;
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  
  return children;
}
```

**Usage in App.js:**
```javascript
<Routes>
  <Route path="/login" element={<Login />} />
  <Route
    path="/dashboard"
    element={
      <ProtectedRoute>
        <Dashboard />
      </ProtectedRoute>
    }
  />
</Routes>
```

## Deliverables

1. Working CF authentication service
2. React API service with token handling
3. Protected route component
