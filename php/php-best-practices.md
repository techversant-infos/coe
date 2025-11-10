# PHP Best Practices
**Version:** 1.0  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Prepared by:** Vishnu Soman, Lajin M. J.


## 1. Overview

This document outlines **recommended best practices for all PHP-based applications** at Techversant to ensure maintainability, security, and scalability.  
All **developers, leads, and DevOps engineers** are expected to adhere to these guidelines across all PHP and Laravel projects.


## 2. Clean Code Principles

### ✅ Guidelines
- Follow the **Single Responsibility Principle (SRP)** — each function or class should have one purpose.
- Use **descriptive, meaningful names** for functions, variables, and classes.
- Avoid **long functions** — refactor into smaller reusable methods.
- Maintain consistent naming conventions:
  - **Classes** → PascalCase (e.g., `UserService`)
  - **Methods & Variables** → camelCase (e.g., `getUserOrders()`)
- Avoid deep nesting — use **early returns** for better readability.

### 💡 Example

```php
// ❌ Bad
function process($user) {
    if ($user) {
        if ($user->isActive()) {
            if ($user->hasOrders()) {
                $this->sendNotification($user);
            }
        }
    }
}

// ✅ Good
function process($user) {
    if (!$user || !$user->isActive() || !$user->hasOrders()) {
        return;
    }
    $this->sendNotification($user);
}
```


## 3. Dependency Management

- Use **Composer** to manage dependencies.
- **Never commit `/vendor`** directory to Git.
- Always commit **`composer.lock`** to ensure reproducible builds.
- Prefer **stable releases** over dev versions.
- Run dependency updates periodically but test carefully.

### 💡 Example

```bash
# Install dependencies
composer install

# Add a new dependency
composer require guzzlehttp/guzzle

# Update specific dependency
composer update guzzlehttp/guzzle
```


## 4. Environment Configuration

- Use **`.env`** files or **environment variables** for config values (DB credentials, API keys, etc.).
- **Never hard-code secrets** in code.
- Use libraries like `vlucas/phpdotenv` for environment handling.
- Add `.env` to `.gitignore`.

### 💡 Example

**.env**
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=app_db
DB_USERNAME=root
DB_PASSWORD=secret
```

**config/database.php**
```php
'connections' => [
    'mysql' => [
        'driver' => 'mysql',
        'host' => env('DB_HOST', '127.0.0.1'),
        'database' => env('DB_DATABASE', 'forge'),
        'username' => env('DB_USERNAME', 'forge'),
        'password' => env('DB_PASSWORD', ''),
    ],
],
```


## 5. Secure Development

- Avoid functions like `eval()`, `exec()`, `shell_exec()`, `system()`.
- Always use **HTTPS** in production.
- Use **secure, HTTP-only, SameSite cookies** for sessions.
- Implement **CSRF protection** for forms.
- **Validate & sanitize** all user input.
- Escape output with `htmlspecialchars()` for HTML output.

### 💡 Example

```php
// ❌ Bad - vulnerable to XSS
echo $_GET['name'];

// ✅ Good
echo htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');
```


## 6. Database Best Practices

- Use **migrations** for schema versioning (`php artisan migrate`).
- Avoid raw SQL — prefer **Eloquent ORM** or **query builder**.
- Always use **prepared statements** or bindings.
- Add **indexes** for frequently queried fields.
- Implement **pagination** for large datasets.

### 💡 Example

```php
// ❌ Bad (SQL Injection risk)
$users = DB::select("SELECT * FROM users WHERE role = '{$_GET['role']}'");

// ✅ Good (parameter binding)
$users = DB::table('users')->where('role', $_GET['role'])->get();
```

```php
// Pagination Example
$users = User::paginate(25);
```


## 7. Performance Optimization

- Enable **OPcache** in production.
- Use **Redis/Memcached** for caching.
- Avoid **N+1 queries** — use `with()` for eager loading.
- Profile slow queries using **Laravel Telescope**, **Blackfire**, or **Xdebug**.

### 💡 Example

```php
// ❌ Bad (N+1 Query)
$users = User::all();
foreach ($users as $user) {
    echo $user->profile->bio;
}

// ✅ Good (Eager Loading)
$users = User::with('profile')->get();
foreach ($users as $user) {
    echo $user->profile->bio;
}
```


## 8. Logging & Monitoring

- Use **Monolog** (default in Laravel) for structured logging.
- Log messages in **JSON format** for easy parsing.
- Include **context** like user ID, request ID, and IP address.
- Set up **real-time monitoring** (e.g., Sentry, Datadog, Prometheus).

### 💡 Example

```php
// Logging example
Log::info('Order processed', [
    'order_id' => $order->id,
    'user_id' => $user->id,
    'amount' => $order->total
]);
```


## 9. DevOps & CI/CD

- Use CI/CD pipelines (GitHub Actions, GitLab CI) to automate:
  - Testing
  - Linting
  - Deployment
- Use **rollback strategies** (blue-green/canary deploys).
- Staging must mirror production (PHP version, DB schema, cache config).
- Enforce **PR reviews** and **quality gates**.

### 💡 Example

**.github/workflows/ci.yml**
```yaml
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup PHP
        uses: shivammathur/setup-php@v2
        with:
          php-version: '8.2'
      - name: Install Dependencies
        run: composer install --no-progress --no-suggest --prefer-dist
      - name: Run Tests
        run: php artisan test
```


## 10. Summary

By following these best practices, we ensure that every PHP project at Techversant remains:  
- **Maintainable** — clean, readable, and modular.  
- **Secure** — protected against common vulnerabilities.  
- **Scalable** — optimized for growth and performance.

> **Quality is not an act, but a habit — especially in code.**


**Document Owner:**  
CoE, Techversant InfoTech Pvt. Ltd.
