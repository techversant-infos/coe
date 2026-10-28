# Exercise 5: Accessibility Audit

> Audit and fix accessibility issues in a ColdFusion form.

## Objective

Learn to implement and verify WCAG accessibility standards.

## Scenario

**Application:** Contact form
**Requirement:** WCAG 2.1 AA compliance

## Instructions

### Part 1: Current Code Analysis

Examine this form:

```cfml
<form name="contactForm" action="process.cfm">
    <table>
        <tr>
            <td>Name:</td>
            <td><input type="text" name="name"></td>
        </tr>
        <tr>
            <td>Email:</td>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <td>Message:</td>
            <td><textarea name="message"></textarea></td>
        </tr>
        <tr>
            <td colspan="2">
                <input type="submit" value="Send">
            </td>
        </tr>
    </table>
</form>
```

### Accessibility Issues Found

| Issue | WCAG Criterion | Severity |
|-------|----------------|----------|
| No labels | 1.3.1 | High |
| No error messages | 3.3.1 | High |
| | | |
| | | |

### Part 2: Fixed Accessible Version

Create an accessible version:

```html
<div class="form-group">
    <!-- What markup is needed? -->
    _______________________________________________________
    
    <input type="text" 
           id="name" 
           name="name"
           aria-describedby="name-hint"
           required>
    <span id="name-hint" class="form-hint">
        Enter your full name
    </span>
</div>

<div class="form-group">
    <!-- Add email field with validation -->
    _______________________________________________________
</div>

<div class="form-group">
    <!-- Add textarea -->
    _______________________________________________________
</div>

<div class="form-group">
    <!-- Add accessible submit button -->
    _______________________________________________________
</div>
```

### Part 3: Error Handling

Add accessible error messages:

```html
<div class="form-group" id="email-group">
    <label for="email">
        Email Address <span aria-hidden="true">*</span>
        <span class="visually-hidden">(required)</span>
    </label>
    
    <input type="email" 
           id="email" 
           name="email"
           aria-required="true"
           aria-invalid="false"
           aria-describedby="email-error email-hint">
    
    <!-- Add hint -->
    <span id="email-hint" class="form-hint">
        We'll use this for notifications
    </span>
    
    <!-- Add error message -->
    _______________________________________________________

</div>
```

### Part 4: ARIA Live Regions

Add dynamic validation feedback:

```html
<div aria-live="polite" aria-atomic="true" class="sr-only" id="form-status">
    <!-- JavaScript will update this -->
</div>

<script>
// When form submission fails:
document.getElementById('form-status').textContent = 
    'Form submission failed. Please review the errors below.';


// When form submission succeeds:
document.getElementById('form-status').textContent = 
    'Form submitted successfully.';
</script>
```

---

## Expected Outcome

An accessible form that:
- [ ] Uses proper label associations
- [ ] Provides clear hints
- [ ] Shows accessible error messages
- [ ] Uses ARIA live regions for dynamic content
- [ ] Passes automated accessibility testing (axe)
