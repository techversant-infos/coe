# PHP Best Practices & Modern Development Standards  

**Version:** 1.1
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Prepared by:** Vishnu Soman, Lajin M. J.

> “A great codebase is like a well‑orchestrated symphony — every piece knows its part, no note is out of place.”  
> — Techversant CoE, 2025

---

## 1. Overview

Modern PHP development standards for all Techversant projects, aligned to **Clean Code, Security, Scalability, AI‑assisted Development, and DevSecOps automation**. Applies to **Developers, Leads, Architects, QA, and DevOps**.

> “Code is not written for machines to execute; it’s written for humans to understand.” — Martin Fowler

---

## 2. Clean Code Principles

- Follow **SOLID** and **DRY**; keep functions cohesive and short.
- Enforce **PSR‑12** style via PHP_CodeSniffer/Rector.
- Put `declare(strict_types=1);` at the top of **every** PHP file.
- Prefer **readonly properties**, **enums**, and **Value Objects/DTOs** to primitives.
- Type everything: parameters, returns, properties; annotate with PHPDoc when needed.
- Run **static analysis** (PHPStan/Psalm) in CI (no warnings allowed on `main`).

### 💡 Example

```php
<?php
declare(strict_types=1);

namespace App\Services\Order;

use DomainException;

final class OrderService
{
    public function __construct(private Notifier $notifier) {}

    public function process(Order $order): void
    {
        if (!$order->isEligible()) {
            throw new DomainException('Order not eligible for processing');
        }

        $this->notifier->sendConfirmation($order->getUser());
    }
}
```

---

## 3. Dependency Management

- Use **Composer 2.x+** with PSR‑4 autoloading. Commit `composer.lock`, never `/vendor`.
- Prefer stable semver ranges (e.g., `^2.1`). Avoid `dev-*` in production.
- Run `composer audit` in CI; fail the pipeline on critical vulnerabilities.
- Maintain private packages in an internal repository; pin versions for reproducibility.

### 💡 Example

```bash
composer install --no-dev --prefer-dist --optimize-autoloader
composer audit
```

---

## 4. Environment Configuration

- `.env` for local only; staging/prod secrets must come from **Vault/SM** (AWS Secrets Manager/Azure Key Vault).
- Apply **12‑Factor App**. Validate env at bootstrap; fail fast if required keys are missing.
- Restrict secrets via RBAC and rotate regularly.

### 💡 Example

```php
// config/app.php
return [
    'env' => env('APP_ENV', 'production'),
    'debug' => (bool) env('APP_DEBUG', false),
    'url' => env('APP_URL', 'https://example.com'),
];
```

> “An environment misconfigured is a disaster waiting to deploy.”

---

## 5. Advanced Security Practices

- Enforce **HTTPS + HSTS**. Add **CSP** headers and enable **SameSite, Secure, HttpOnly** cookies.
- Use **rate limiting** and **brute‑force** guards on auth and sensitive endpoints.
- Use **Sanctum/Passport/JWT** for APIs; rotate and revoke tokens.
- Validate and sanitize **all** inputs; escape outputs (`htmlspecialchars`) for HTML contexts.
- Prefer ORM/query builder; always use **prepared statements**.
- Validate file uploads (MIME/size/extension); store outside `/public` and generate random names.
- Encrypt PII at rest (Laravel `cast: encrypted` / database encryption).

### 💡 Examples

**Blade CSRF**

```blade
<form method="POST" action="{{ route('profile.update') }}">
  @csrf
  <input name="name">
</form>
```

**CSP Middleware Snippet**

```php
<?php
declare(strict_types=1);

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

final class AddCspHeaders
{
    public function handle(Request $request, Closure $next)
    {
        $response = $next($request);
        $response->headers->set(
            'Content-Security-Policy',
            "default-src 'self'; img-src 'self' https: data:; script-src 'self'; style-src 'self' 'unsafe-inline'"
        );
        return $response;
    }
}
```

> “Security isn’t a feature — it’s a habit that keeps you alive.”

---

## 6. Database & Data Integrity

- Use **UUIDs** for distributed systems; enforce constraints and indexes.
- Use **transactions** for multi‑step writes; adopt soft‑deletes where auditability is needed.
- Use connection pooling (PgBouncer/ProxySQL) and read/write splitting as scale grows.
- Backups are tested restores, not just snapshots.

### 💡 Example

```php
DB::transaction(function () use ($user, $order) {
    $order->save();
    $user->decrement('balance', $order->amount);
});
```

---

## 7. Performance & Scalability

- Enable **OPcache** (and JIT where beneficial). Profile with **Blackfire/New Relic**.
- Use **queues** (Redis/SQS) for background work. Keep services **stateless** for horizontal scaling.
- Prevent N+1 queries with eager loading; cache heavy reads with TTLs and cache busting.

### 💡 Example

```php
$products = Cache::remember('products.list', 300, fn () =>
    Product::with('category')->active()->get()
);
```

---

## 8. Logging, Observability & Monitoring

- Emit **structured JSON logs** with `trace_id`, `user_id`, and request metadata.
- Centralize logs (ELK/Loki/Datadog). Alert on error rates and p95 latency.
- Capture exceptions with **Sentry** (PII scrubbing enabled).

### 💡 Example

```php
use Illuminate\Support\Facades\Log;

Log::channel('stack')->info('User registration', [
    'user_id' => $user->id,
    'ip' => request()->ip(),
    'trace_id' => app()->bound('trace_id') ? app('trace_id') : null
]);
```

---

## 9. DevOps, CI/CD & Deployment Standards

- Containerize apps with **Docker**; pin PHP to **8.3+**; keep images minimal.
- Git workflow: feature → PR → `develop` → release → `main`; require approvals & green pipelines.
- Pipelines must run: install, static analysis, tests, **composer audit**, artifact build, deploy, smoke tests.
- Infrastructure as Code (Terraform/Ansible); implement **blue‑green** or **canary** deploys.

### 💡 CI Example (GitHub Actions)

```yaml
name: Laravel CI/CD
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
          coverage: none
      - run: composer install --no-interaction --no-progress
      - run: vendor/bin/phpstan analyse
      - run: vendor/bin/phpunit --coverage-text
      - run: composer audit
```

---

## 10. AI‑Assisted Development

- Use **Copilot/Cursor/ChatGPT Enterprise** for scaffolding, refactors, and test generation **with human review**.
- Never paste secrets or proprietary logic into prompts.
- Tag commits that include generated code: `[AI-Assisted]`.
- Use AI to propose **performance/security** improvements; engineers decide and document.

### 💡 Example

```bash
git commit -m "[AI-Assisted] Refactor OrderController for SRP and add missing tests"
```

> “AI is your co‑pilot, not your autopilot.”

---

## 11. Testing & Quality Assurance

- Maintain **unit/feature/integration** tests; minimum **80% coverage** on `develop`, higher on `main`.
- Use Pest/PHPUnit; integrate **InfectionPHP** for mutation testing on critical modules.
- Add **API contract tests** and **security tests** (rate limits, authz).

### 💡 Example

```php
public function test_user_cannot_access_admin_route(): void
{
    $user = User::factory()->create(['role' => 'user']);
    $this->actingAs($user)->get('/admin/dashboard')->assertForbidden();
}
```

---

## 12. Closing Thoughts
>
> “The mark of a mature engineer isn’t how much they code, but how little they need to change later.”  
> “Codebases are living ecosystems — refactor, prune, and water them often.”  
> “Code well. Test deeply. Sleep peacefully.”

**Document Owner:** Techversant CoE
