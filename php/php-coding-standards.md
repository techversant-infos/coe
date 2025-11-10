# PHP Coding Standards
**Version:** 1.0  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Prepared by:** Vishnu Soman, Lajin M. J.



## 1. Introduction

This document defines coding conventions for all PHP applications developed at Techversant.  
It ensures **consistency, readability, and maintainability** across all projects.  
It applies to **developers, reviewers, and QA engineers** involved in code validation.



## 2. Project Structure

**Standard Folder Layout**
```
/app      - Core application/business logic (Controllers, Models, Services)
/config   - Configuration files
/public   - Publicly accessible directory (index.php, assets)
/tests    - Unit and integration tests
/vendor   - Composer dependencies (auto-managed)
```

- Maintain a clean, logical folder structure.  
- **Autoloading:** All classes must follow **PSR-4 autoloading** (via Composer).  
- **Namespaces** should reflect folder structure starting from `/app`.

### 💡 Example
```php
namespace App\Services;

class UserService
{
    // ...
}
```



## 3. Naming Conventions

### 3.1 Classes  
Use **PascalCase**  
**Example:** `UserService`, `OrderRepository`

### 3.2 Functions / Methods  
Use **camelCase**  
**Example:** `getUserData()`, `calculateTaxAmount()`

### 3.3 Variables  
Use descriptive **camelCase**  
**Example:** `$userEmail`, `$orderTotal`

### 3.4 Constants  
Use **UPPER_CASE** with underscores  
**Example:** `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`

### 3.5 Filenames  
Filename must match the class name exactly, with `.php` extension.  
**Example:** `UserController.php`

### 3.6 Interfaces & Abstract Classes  
- Interfaces: suffix with **Interface** → `PaymentGatewayInterface`  
- Abstract classes: prefix with **Abstract** → `AbstractLogger`



## 4. Formatting and Style

- Use **4 spaces** for indentation (no tabs).  
- Maximum **line length = 120 characters**.  
- **Opening braces** must be on the same line.

### 💡 Example
```php
if ($condition) {
    // ...
}
```

- One statement per line.  
- Include `declare(strict_types=1);` at the top of every file.  
- No closing `?>` tag in pure PHP files.  
- Use **short array syntax**: `$arr = ['a', 'b'];`  
- Include a single blank line between methods.  
- Use **type hints** and **return types** wherever possible.

### 💡 Example
```php
declare(strict_types=1);

class MathHelper
{
    public function add(int $a, int $b): int
    {
        return $a + $b;
    }
}
```



## 5. Commenting and Documentation

Use **PHPDoc** for classes, properties, and methods.

### 💡 Example
```php
/**
 * Get user data by ID.
 *
 * @param int $id
 * @return User|null
 */
public function getUser(int $id): ?User
{
    return $this->userRepository->find($id);
}
```

- Use inline comments (`//`) to explain **why**, not **what**.  
- Use `/** */` for multi-line comments.  
- Avoid redundant or outdated comments.



## 6. Security Best Practices

- Validate and sanitize **all user inputs**.  
- Escape **all outputs** using `htmlspecialchars()` or equivalent.  
- Always use **prepared statements** or **ORM bindings** to prevent SQL injection.  
- Store passwords using **password_hash()** and **password_verify()**.  
- Disable `display_errors` in production and enable `error_log`.

### 💡 Example
```php
// ❌ Bad
$query = "SELECT * FROM users WHERE email = '{$_POST['email']}'";

// ✅ Good
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $_POST['email']]);
```



## 7. Error Handling

- Use **exceptions** and **try-catch** blocks.  
- Never suppress errors using `@`.  
- Use **Monolog** or equivalent for error logging.  
- Avoid displaying sensitive stack traces in production.

### 💡 Example
```php
try {
    $result = $db->query($sql);
} catch (PDOException $e) {
    Log::error('Database query failed', ['error' => $e->getMessage()]);
}
```



## 8. Version Control & Branching

- Use **Git** with the following branches:
  - `main` → Production-ready code
  - `develop` → Integration branch
  - `feature/*` → Individual feature branches

- Follow **Conventional Commit** messages:
  - `feature: add user login`
  - `fix: correct email validation`
  - `refactor: optimize query performance`

- Code must **pass review** before merging to `main`.



## 9. Testing & Quality

- All code must include **unit and integration tests** (use PHPUnit).  
- Maintain **minimum 80% test coverage**.  
- Use **static analysis tools**:
  - PHPStan (level 8 recommended)
  - Psalm
- Use **PHP_CodeSniffer** with PSR-12 standard.

### 💡 Example
```bash
phpcs --standard=PSR12 app/
vendor/bin/phpstan analyse app/ --level=8
vendor/bin/phpunit --coverage-text
```

- Integrate **CI/CD pipelines** (GitHub Actions, GitLab CI) for:
  - Automated testing
  - Linting
  - Code quality enforcement



## 10. Summary

Adhering to these coding standards ensures:
- Consistent code quality across all PHP projects.  
- Reduced technical debt.  
- Better collaboration among team members.  
- Faster onboarding and smoother code reviews.

> “Readable code is reliable code — consistency is our culture.”



**Document Owner:**  
CoE, Techversant InfoTech Pvt. Ltd.
