# PHP Coding Standards  

**Status:** Needs review · **Owner:** TBD · **Last updated:** 2025-11-13 · **Next review:** 2026-05-13

**Version:** 1.1  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Prepared by:** Vishnu Soman, Lajin M. J.

> “Consistency is the soul of software — when every line speaks the same language, your system sings in harmony.”  
> — Techversant CoE, 2025

---

## 1. Introduction

Modern PHP coding conventions for clarity, consistency, security, and scalability across Techversant teams. Applies to **developers, leads, reviewers, QA, and DevOps**.

> “Code is more often read than written — write it for the next person, not just the compiler.”

---

## 2. Project Structure

```
/app       - Core business logic (Controllers, Models, Services)
/bootstrap - Application bootstrap files
/config    - Configuration settings
/database  - Migrations, seeders, factories
/public    - Web root (index.php, assets)
/resources - Views, translations, frontend assets
/routes    - Route definitions
/tests     - Unit and feature tests
/vendor    - Composer-managed dependencies
```

- Use **PSR‑4 autoloading** (Composer).  
- Keep controllers slim; move domain logic to **Services**/**Actions**.  
- Prefer feature‑oriented folders (`/app/Services/Orders`, `/app/Repositories/Users`).  
- Avoid dumping logic into `/Helpers`; create proper classes.

### 💡 Example

```php
<?php
declare(strict_types=1);

namespace App\Services\User;

use App\Models\User;

final class UserService
{
    public function getProfile(int $id): ?User
    {
        return User::find($id);
    }
}
```

---

## 3. Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Classes | PascalCase | `UserService`, `OrderRepository` |
| Methods/Functions | camelCase | `getUserOrders()`, `calculateTotal()` |
| Variables | camelCase | `$orderTotal`, `$userEmail` |
| Constants | UPPER_CASE | `MAX_RETRY_COUNT`, `CACHE_TTL_MINUTES` |
| Interfaces | Suffix `Interface` | `PaymentGatewayInterface` |
| Abstract Classes | Prefix `Abstract` | `AbstractLogger` |
| Filenames | Match class name | `UserController.php` |

> “Naming is a contract with your future self — make it one you’ll gladly sign again.”

---

## 4. Formatting & Style

- **Indentation:** 4 spaces (no tabs).  
- **Line length:** 120 chars max.  
- **Braces:** same line.  
- Add `declare(strict_types=1);` at the top of every file.  
- No closing `?>` in pure PHP files.  
- Short arrays: `['a', 'b']`.  
- One blank line between methods.  
- Type all parameters, returns, and properties. Enforce **PSR‑12** with PHP_CodeSniffer/Rector.

### 💡 Example

```php
<?php
declare(strict_types=1);

namespace App\Utils;

final class MathHelper
{
    public function add(float $a, float $b): float
    {
        return $a + $b;
    }
}
```

> “Formatting is the grammar of code — break it, and even good logic sounds wrong.”

---

## 5. Commenting & Documentation

- Document **public** classes/methods/properties with PHPDoc.  
- Explain **why**, not **what**; keep comments current.  
- Use PHPDoc for generics and complex types to help static analysis.

### 💡 Example

```php
/**
 * Retrieve a user by ID.
 *
 * @param int $id
 * @return User|null
 */
public function getUser(int $id): ?User
{
    return $this->userRepository->find($id);
}
```

---

## 6. Security Standards

- Validate & sanitize all inputs; escape HTML outputs with `htmlspecialchars($data, ENT_QUOTES, 'UTF-8')`.
- Use **prepared statements**/ORM bindings; never concatenate SQL.  
- Passwords: `password_hash()` + `password_verify()`; use modern algos (Argon2id/Bcrypt).  
- Disable `display_errors` in prod; log to file/stack (Monolog).  
- Enable **CSRF tokens**, **CSP**, **SameSite/HttpOnly/Secure** cookies, **rate limiting**.  
- Keep secrets out of code; use `.env` (local) and **Secrets Manager** (staging/prod).  
- Validate uploads (MIME/size/ext); store outside `/public` with random names.

### 💡 Example

```php
// ❌ Bad
$query = "SELECT * FROM users WHERE email = '{$_POST['email']}'";

// ✅ Good
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $_POST['email']]);
```

> “Security isn’t a checkbox — it’s a mindset you code with.”

---

## 7. Error Handling & Logging

- Use **Exceptions** and domain‑specific exception types.  
- Never suppress with `@`.  
- Log critical errors with **Monolog** (structured JSON preferred).  
- Don’t expose stack traces in prod.

### 💡 Example

```php
try {
    $orderService->process($orderId);
} catch (OrderException $e) {
    \Log::error('Order processing failed', [
        'order_id' => $orderId,
        'error' => $e->getMessage(),
    ]);
}
```

> “Logs are the black box of your application — the truth is always in there.”

---

## 8. Version Control & Branching

- Branches: `main` (prod), `develop` (integration), `feature/*` (work), `hotfix/*` (urgent).  
- **Conventional Commits**:  
  - `feat: add user login flow`  
  - `fix: correct email validation`  
  - `refactor: optimize query performance`
- Require PR reviews and green CI to merge. Tag releases (`v1.2.0`).

> “A good Git history reads like a story — clear, intentional, and complete.”

---

## 9. Testing & Quality Assurance

- Minimum **80% coverage**; unit + feature + integration tests (PHPUnit/Pest).  
- CI must run: PHP_CodeSniffer (PSR‑12), PHPStan (level 8+), Psalm (as applicable), and tests.  
- Consider **InfectionPHP** for mutation tests on critical modules.

### 💡 Example

```bash
vendor/bin/phpcs --standard=PSR12 app/
vendor/bin/phpstan analyse app/ --level=8
vendor/bin/phpunit --coverage-text
```

> “Testing is not about proving you’re right; it’s about proving you’re not wrong.”

---

## 10. AI‑Assisted Development Standards

- Use **Copilot/Cursor/ChatGPT** for scaffolding and refactors, but **always review**.  
- Never include secrets or proprietary logic in prompts.  
- Tag AI‑assisted commits `[AI-Assisted]`.

### 💡 Example

```bash
git commit -m "[AI-Assisted] Refactor CartService for SOLID compliance"
```

> “AI won’t replace developers — but developers using AI will replace those who don’t.”

---

## 11. Tooling & PHP Runtime

- PHP **8.3+** required; align local, CI, and production versions.  
- Composer 2.x; enable OPcache in production.  
- Use Docker for consistent environments; keep images minimal and pinned.

---

## 12. Summary

- 🧩 **Consistency** across teams  
- 🔒 **Security** by default  
- ⚙️ **Scalability** built‑in  
- 🧠 **AI‑assisted** productivity  
- ❤️ **Readable** and maintainable code

> “Discipline in style leads to freedom in design.”

---

**Document Owner:** Techversant CoE  

> “Code like someone will maintain it after you — because someone always will.”
