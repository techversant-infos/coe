# Exercise 4: Security Audit and Remediation

> Find and fix security vulnerabilities in a sample ColdFusion application.

## Objective

Identify common security vulnerabilities in ColdFusion applications and implement proper fixes.

## Prerequisites

- ColdFusion server
- Sample application with intentional vulnerabilities (provided or simulated)
- OWASP Top 10 knowledge

## Instructions

### Part 1: SQL Injection Review

Review the following code and identify vulnerabilities:

```cfml
<!--- VULNERABLE CODE --->
<cfquery name="getUser">
    SELECT * FROM users 
    WHERE username = '#form.username#' 
    AND password = '#form.password#'
</cfquery>
```

1. **Identify the vulnerability**
2. **Explain the risk**
3. **Write the fixed code**

### Part 2: XSS Prevention

Review the following code and identify vulnerabilities:

```cfml
<!--- VULNERABLE CODE --->
<cfoutput>
    Welcome, #user.name#
</cfoutput>
```

1. **Identify the vulnerability**
2. **Explain the risk**
3. **Write the fixed code**

### Part 3: Secure Authentication

Implement a secure authentication system:

Requirements:
- Password hashing (bcrypt or Argon2)
- Secure session management
- Brute force protection
- Password reset functionality

```cfml
// Password hashing example (Lucee with Bcrypt)
hashedPassword = bcrypt.hash(plainPassword);
isValid = bcrypt.check(plainPassword, hashedPassword);
```

### Part 4: CSRF Protection

Implement CSRF protection for forms:

```cfml
// Generate token on form display
<cfset session.csrfToken = hash(getTickCount(), 'SHA-256')>

// Include token in form
<input type="hidden" name="csrf_token" value="#session.csrfToken#">

// Validate on submission
if (form.csrf_token != session.csrfToken) {
    // Reject request
}
```

### Part 5: File Upload Security

Implement secure file upload:

```cfml
// Secure upload implementation checklist:
// 1. Validate file type by content, not extension
// 2. Limit file size
// 3. Generate random filenames
// 4. Store outside webroot
// 5. Set proper permissions
```

### Part 6: Full Security Audit Checklist

For a given application, complete this checklist:

| Category | Item | Status | Finding | Fix |
|----------|------|--------|---------|-----|
| SQL Injection | All queries use cfqueryparam | | | |
| XSS | All output encoded | | | |
| CSRF | Forms protected | | | |
| Auth | Passwords hashed | | | |
| Auth | Sessions secure | | | |
| Files | Uploads validated | | | |
| Config | Debug off in prod | | | |
| Config | Error handling custom | | | |
| Config | CFIDE secured | | | |

## Expected Outcome

1. **Vulnerability Analysis** — Table of found issues
2. **Fixed Code** — Corrected versions with explanations
3. **Security Checklist** — Completed checklist with findings
4. **Security Summary** — High/Medium/Low risk count

## Common CF Security Mistakes

| Mistake | Vulnerability | Fix |
|---------|--------------|-----|
| String concatenation in queries | SQL Injection | cfqueryparam |
| Unencoded user input | XSS | encodeForHTML |
| No token on forms | CSRF | Generate and validate tokens |
| MD5/SHA1 passwords | Weak hashing | bcrypt/Argon2 |
| cfabort only on errors | Information disclosure | Custom error pages |
| Debug in production | Information disclosure | Disable debug |
| File extension check only | Arbitrary upload | Content-type validation |

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| SQL injection identified and fixed | 20 |
| XSS identified and fixed | 20 |
| CSRF protection implemented | 15 |
| Secure auth implemented | 15 |
| File upload secured | 10 |
| Audit checklist completed | 10 |
| Professional documentation | 10 |
| **Total** | **100** |

**Passing Score:** 70/100
