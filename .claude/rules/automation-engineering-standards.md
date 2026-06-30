# Automation Engineering Standards

Technical standards for automation engineering content, ensuring best practices and industry standards are taught consistently.

## Code Standards

### Naming Conventions
- Use descriptive, self-documenting names
- Prefer clarity over brevity
- Use camelCase for JavaScript/TypeScript
- Use snake_case for Python
- Use PascalCase for class names
- Use UPPER_SNAKE_CASE for constants

### Examples
```javascript
// GOOD: Self-documenting names
const loginButton = await page.locator('[data-testid="login"]');
const userProfile = await fetchUserProfile(userId);

// BAD: Cryptic names
const btn = await page.locator('[data-testid="login"]');
const d = await fetchUserProfile(id);
```

### Function Design
- Single responsibility: One function, one purpose
- Pure functions when possible: No side effects, same output for same input
- Small functions: 20-30 lines maximum
- Clear inputs and outputs
- Document purpose and return values

```javascript
// GOOD: Single responsibility
async function login(page, username, password) {
  await page.fill('#username', username);
  await page.fill('#password', password);
  await page.click('#submit');
}

// BAD: Multiple responsibilities
async function loginAndNavigateAndCheck(page, username, password) {
  // ...does too many things
}
```

### Error Handling
- Always handle errors explicitly
- Use try/catch for async operations
- Provide meaningful error messages
- Log errors with context
- Never silently ignore errors

```javascript
// GOOD: Proper error handling
async function login(page, username, password) {
  try {
    await page.fill('#username', username);
    await page.fill('#password', password);
    await page.click('#submit');
  } catch (error) {
    console.error('Login failed:', error.message);
    throw new Error(`Failed to login: ${error.message}`);
  }
}

// BAD: Silent failures
async function login(page, username, password) {
  try {
    await page.fill('#username', username);
    await page.fill('#password', password);
    await page.click('#submit');
  } catch (e) {
    // Nothing - error is lost
  }
}
```

## Test Automation Standards

### Test Structure
- Arrange-Act-Assert (AAA) pattern
- One assertion per test where possible
- Descriptive test names (should... when...)
- Independent tests: No dependencies between tests

```javascript
// GOOD: Clear AAA structure
test('should display error message when login with invalid credentials', async () => {
  // Arrange
  const username = 'invalid_user';
  const password = 'wrong_password';

  // Act
  await login(username, password);

  // Assert
  await expect(page.locator('.error')).toHaveText('Invalid credentials');
});

// BAD: Unclear structure
test('login test', async () => {
  await login('invalid_user', 'wrong_password');
  await expect(page.locator('.error')).toBeVisible();
});
```

### Selectors
- Prefer data-testid attributes for stability
- Avoid CSS classes (change frequently)
- Avoid XPath when possible
- Use semantic locators when available

```javascript
// GOOD: Stable selector
await page.getByTestId('login-button').click();

// BAD: Unstable selector
await page.locator('.btn.btn-primary.submit').click();
await page.locator('//button[contains(text(), "Submit")]').click();
```

### Wait Strategies
- Prefer auto-waiting locators
- Use explicit waits when necessary
- Avoid hardcoded timeouts
- Wait for specific conditions

```javascript
// GOOD: Auto-waiting
await page.getByTestId('login-button').click();

// ACCEPTABLE: Explicit wait with condition
await page.waitForSelector('.success-message', { state: 'visible' });

// BAD: Hardcoded timeout
await page.waitForTimeout(5000);  // Always wait 5 seconds
```

## Documentation Standards

### Code Comments
- Explain WHY, not WHAT
- Avoid redundant comments
- Use TODO comments for known issues
- Document complex algorithms

```javascript
// GOOD: Explains why
// Use session storage for auth token to persist across tabs
const token = sessionStorage.getItem('authToken');

// BAD: States the obvious
// Get the token from session storage
const token = sessionStorage.getItem('authToken');
```

### README Files
- Include purpose and usage
- Provide installation/setup instructions
- List prerequisites
- Include examples
- Note known limitations

## Version Control Practices

### Commit Messages
- Use clear, descriptive messages
- Follow format: "type: description"
- Types: feat, fix, refactor, test, docs, chore
- Reference issue numbers when applicable

```
feat: add login validation test
fix: resolve flaky test in checkout flow
refactor: extract page object for dashboard
test: add tests for user registration
docs: update setup instructions
```

### Branch Naming
- feature/feature-name
- fix/bug-description
- refactor/refactor-description

## Security Considerations

### Sensitive Data
- Never commit credentials or secrets
- Use environment variables for configuration
- Never log sensitive information
- Sanitize test data

### Input Validation
- Validate all inputs
- Handle edge cases
- Use parameterized queries (avoid SQL injection)
- Sanitize user-generated content in tests

## Performance Standards

### Efficient Selectors
- Use specific selectors
- Avoid complex CSS selectors
- Prefer locators over selectors

### Parallel Execution
- Run tests in parallel where possible
- Use worker threads appropriately
- Monitor resource usage

### Cleanup
- Always clean up test data
- Close browser sessions properly
- Release resources after tests

## Code Quality Checklist

- [ ] Follows naming conventions
- [ ] Single responsibility principle applied
- [ ] Errors are handled explicitly
- [ ] Tests follow AAA pattern
- [ ] Selectors are stable and semantic
- [ ] No hardcoded timeouts
- [ ] Code is documented where necessary
- [ ] No sensitive data in code
- [ ] Commits are atomic and well-messaged