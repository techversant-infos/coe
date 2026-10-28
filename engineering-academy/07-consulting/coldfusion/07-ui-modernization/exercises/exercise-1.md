# Exercise 1: Bootstrap Refresh

> Modernize a legacy CFML form using Bootstrap.

## Objective

Learn to modernize ColdFusion forms with Bootstrap.

## Scenario

**Application:** User registration form
**Current:** Legacy cfinput forms
**Goal:** Mobile-responsive Bootstrap forms

## Instructions

### Part 1: Current Code Analysis

```cfml
<!--- OLD: Legacy form --->
<cfform name="registration" action="register.cfm">
    <table>
        <tr>
            <td>Username:</td>
            <td><cfinput type="text" name="username" required="yes" message="Username required"></cfinput></td>
        </tr>
        <tr>
            <td>Email:</td>
            <td><cfinput type="text" name="email" required="yes" validate="email"></cfinput></td>
        </tr>
        <tr>
            <td>Password:</td>
            <td><cfinput type="password" name="password" required="yes"></cfinput></td>
        </tr>
        <tr>
            <td>Department:</td>
            <td>
                <cfselect name="department">
                    <option value="sales">Sales</option>
                    <option value="marketing">Marketing</option>
                    <option value="engineering">Engineering</option>
                </cfselect>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <cfinput type="submit" name="btnSubmit" value="Register">
            </td>
        </tr>
    </table>
</cfform>
```

### Part 2: Modernized Version

Create the Bootstrap version:

```html
<!--- NEW: Bootstrap form --->
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h4>User Registration</h4>
                </div>
                <div class="card-body">
                    <form method="POST" action="register.cfm">
                        
                        <!-- Username field -->
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" 
                                   class="form-control" 
                                   id="username" 
                                   name="username"
                                   required
                                   minlength="3">
                            <div class="invalid-feedback">
                                Username must be at least 3 characters
                            </div>
                        </div>
                        
                        <!-- Email field -->
                        _______________________________________________________________
                        
                        <!-- Password field -->
                        _______________________________________________________________
                        
                        <!-- Department select -->
                        _______________________________________________________________
                        
                        <!-- Submit button -->
                        _______________________________________________________________
                        
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Part 3: Client-Side Validation

Add JavaScript validation:

```javascript
// Form validation
document.querySelector('form').addEventListener('submit', function(e) {
    
    // Get form fields
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    
    // Validate username
    if (username.value.length < 3) {
        _______________________________________________________________
        _______________________________________________________________
    }
    
    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        _______________________________________________________________
        _______________________________________________________________
    }
    
    // Validate password
    if (password.value.length < 8) {
        _______________________________________________________________
        _______________________________________________________________
    }
});
```

### Part 4: Backend Validation

Add server-side validation:

```cfml
<!--- register.cfm --->

<cfif structKeyExists(form, "btnSubmit")>
    
    <!--- Validate inputs --->
    <cfset local.errors = []>
    
    <!--- Username validation --->
    <cfif NOT len(trim(form.username))>
        <cfset arrayAppend(local.errors, "Username is required")>
    <cfelseif len(form.username) LT 3>
        <cfset arrayAppend(local.errors, "Username must be at least 3 characters")>
    </cfif>
    
    <!--- Email validation --->
    <cfif NOT len(trim(form.email))>
        _______________________________________________________________
    <cfelseif NOT isValid("email", form.email)>
        _______________________________________________________________
    </cfif>
    
    <!--- Password validation --->
    _______________________________________________________________
    
    <!--- Process if no errors --->
    <cfif arrayIsEmpty(local.errors)>
        <!--- Create user --->
    <cfelse>
        <!--- Show errors --->
        <cfdump var="#local.errors#">
    </cfif>
    
</cfif>
```

## Expected Outcome

1. Complete Bootstrap form
2. Client-side validation
3. Server-side validation
4. Error display

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Bootstrap structure correct | 20 |
| All fields converted | 20 |
| Validation complete | 25 |
| Responsive design | 15 |
| Professional appearance | 15 |
| Error handling | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
