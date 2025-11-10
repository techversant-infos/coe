# Techversant Engineering Coding Standards for the AI Era
**Issued by:** Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Prepared by:** Lajin M. J — Software Architect & Technical Account Manager  

---

## 1. Purpose

As Techversant embraces **AI-assisted development** across all stacks (ColdFusion, PHP/Laravel, React, Flutter, GoLang), our coding standards must evolve.

AI tools like **GitHub Copilot**, **Cursor**, and **ChatGPT** can accelerate development — but they also introduce new risks.  
This document ensures that every AI-assisted contribution is **secure**, **maintainable**, and **human-owned**.

> **AI can suggest — only humans decide.**

---

## 2. Core Principle: Human Accountability

Every line of code must be:
- Reviewed by a human before commit.
- Understood by the person committing.
- Owned by a Techversant engineer.

Example (bad practice):
```php
// ❌ Copilot-generated code blindly accepted
$user = DB::select("SELECT * FROM users WHERE email = '$email'");
```

Example (good practice):
```php
// ✅ Reviewed, refactored, and secured by engineer
$user = DB::table('users')->where('email', $email)->first();
```

---

## 3. Code Review & Ownership Standards

### 3.1 Human-in-the-Loop (Mandatory)
- Do **not** commit code you can’t explain.  
- Trace and verify all logic before pushing.  
- Large AI-generated chunks must be **refactored and modularized**.

Example (bad):
```php
// ❌ One giant AI-generated function
function processOrder($request) {
    // hundreds of lines...
}
```

Example (good):
```php
// ✅ Modularized and readable
function processOrder(Request $request) {
    $validated = $this->validateOrder($request);
    $order = $this->createOrder($validated);
    $this->sendNotifications($order);
}
```

### 3.2 AI Usage Disclosure
Mention AI involvement transparently in commits:

```
git commit -m "Feature: Implemented invoice generation (AI-assisted, fully reviewed)"
```

### 3.3 Refactoring for Readability
Ensure generated code matches Techversant style guides:
- Follow PSR-12.
- Indentation: 4 spaces.
- Function names: `camelCase`.
- Class names: `PascalCase`.
- Avoid “clever” shortcuts — clarity wins.

Example:
```php
// ❌ AI output (too cryptic)
if(!empty($a)&&isset($b)&&$c>10){doSomething();}

// ✅ Human-refactored
if (!empty($amount) && isset($balance) && $limit > 10) {
    $this->processTransaction();
}
```

---

## 4. Maintainability & Documentation

### 4.1 Intent-Driven Comments
AI can describe *what*, but engineers must explain *why*.

Example:
```php
/**
 * Calculates discount based on user tier.
 *
 * Why: Business rule requires premium users to get 10% off.
 */
public function calculateDiscount(User $user, float $amount): float
{
    return $user->isPremium() ? $amount * 0.9 : $amount;
}
```

### 4.2 Consistent Naming Conventions
| Element | Convention | Example |
|----------|-------------|----------|
| Classes | PascalCase | `OrderService`, `UserRepository` |
| Methods | camelCase | `getUserOrders()` |
| Variables | snake_case | `$total_amount` |
| Constants | UPPER_CASE | `MAX_DISCOUNT_PERCENT` |

### 4.3 Architectural Alignment
Generated code must match project structure.

Example (Laravel):
```
app/
  Http/
    Controllers/
  Models/
  Services/
  Repositories/
```

If AI places logic inside a controller that belongs to a service layer — refactor it.

```php
// ❌ AI-generated controller with business logic
public function store(Request $request)
{
    $discount = $request->amount * 0.1;
    $order = Order::create([...]);
}

// ✅ Corrected
public function store(Request $request, OrderService $service)
{
    $order = $service->createOrder($request->all());
}
```

---

## 5. Security & Compliance

### 5.1 Security Vetting (Non-Negotiable)
All AI-generated code handling **auth**, **encryption**, or **data I/O** must be reviewed for:
- Hardcoded secrets
- SQL Injection
- XSS / CSRF
- Unsafe file handling
- Weak cryptography

Example:
```php
// ❌ Hardcoded API key
$client = new Client(['key' => 'sk_test_abc123']);

// ✅ Use environment variables
$client = new Client(['key' => env('STRIPE_SECRET')]);
```

### 5.2 Dependency Management
Check AI-suggested packages:

| Step | Check |
|------|--------|
| ✅ | Is it well-maintained? (GitHub commits, stars, issues) |
| ✅ | Is the license compatible (MIT preferred)? |
| ✅ | Is it already used internally? |

### 5.3 Data & IP Compliance
- Use only **Techversant-approved AI tools**.  
- Don’t paste proprietary code into public models.  
- Validate AI-suggested snippets for potential license conflicts.

---

## 6. Testing & Quality Assurance

### 6.1 Test Ownership
AI-generated tests are **placeholders**, not production-ready.

Example:
```php
// ❌ AI-generated test (incomplete)
public function test_order_creation()
{
    $this->assertTrue(true);
}
```

```php
// ✅ Human-verified test
public function test_order_creation_saves_valid_data()
{
    $payload = Order::factory()->make()->toArray();
    $this->postJson('/api/orders', $payload)
         ->assertStatus(201)
         ->assertJsonStructure(['id', 'total_amount']);
}
```

### 6.2 Debugging AI Output
If a generated method is too complex, simplify or rewrite it.

Example (AI-generated mess):
```php
// ❌ Nested, unclear, no comments
return array_map(fn($x)=>$x>10?($x*2):($x/2),array_filter($arr,fn($a)=>$a!=null));
```

Refactored:
```php
// ✅ Clear and testable
$filtered = array_filter($values, fn($v) => $v !== null);
return array_map(fn($v) => $v > 10 ? $v * 2 : $v / 2, $filtered);
```

### 6.3 Performance Validation
Before merging, benchmark AI-generated queries or loops.

```php
// ❌ Inefficient
foreach (User::all() as $user) {
    $user->orders_count = $user->orders()->count();
}

// ✅ Optimized
$users = User::withCount('orders')->get();
```

---

## 7. AI Prompting & Knowledge Retention

### 7.1 Prompt Discipline
Write **clear, context-aware prompts**.

Bad:
> "Generate user login API in Laravel"

Good:
> "Generate a Laravel API controller for user login using JWTAuth, validating email and password fields, returning token in JSON response, following existing AuthService pattern."

### 7.2 Prompt Storage
Store relevant prompts in your module folder:
```
/docs/ai_prompts.md
```

Example entry:
```markdown
## LoginController.php
Prompt:
"Generate Laravel controller for user login using JWTAuth and custom response format."

Engineer Review:
Simplified error handling, added role-based access, removed unused imports.
```

---

## 8. Continuous Learning & Team Sharing

### 8.1 AI Code Review Sessions
Teams must conduct quarterly “AI Wins & Fails” sessions — share:
- Great AI use cases that saved hours.
- Common pitfalls (e.g., incorrect validation, inefficient loops).

### 8.2 CoE Oversight
The CoE maintains:
- Approved AI tools list
- AI usage best practices
- Security & compliance checklist

### 8.3 Ongoing Training
Mandatory workshops every quarter:
- “Prompt Engineering for Developers”
- “Debugging AI-Generated Code”
- “Responsible AI Usage & Licensing”

---

## 9. Summary

AI helps us move faster — but speed without control leads to chaos.  
At Techversant, we build **systems**, not just **scripts**.  
AI is a collaborator, not a substitute.

> 🧩 **AI can write code. Engineers build systems.**

---

## Appendix: AI Code Review Checklist ✅

| Area | Check | Status |
|------|--------|--------|
| Code Readability | Code refactored and PSR-compliant | ☐ |
| Ownership | Engineer reviewed and understood logic | ☐ |
| Architecture | Matches project’s pattern (MVC, service layer) | ☐ |
| Security | Secrets removed, inputs sanitized | ☐ |
| Dependencies | Approved & compatible | ☐ |
| Testing | Unit and feature tests added | ☐ |
| Documentation | Intent clearly explained | ☐ |
| AI Disclosure | Commit/PR note added | ☐ |
| Prompt Stored | Relevant prompt saved under `/docs/ai_prompts.md` | ☐ |

---

**Document Owner:**  
Lajin M. J  
Software Architect & Technical Account Manager  
Techversant InfoTech Pvt. Ltd.
