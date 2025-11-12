**Version:** 1.0  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** November 2025  
**Contributers:** Nandu S, Aswathy S, Deepak Jose, Lajin M J  

# ColdFusion Best Practices: The Ultimate Survival Guide  
*How to write ColdFusion code that doesn’t make you want to scream into a pillow.*



## 📚 Table of Contents
- [Intro: Why Bother?](#intro-why-bother)
- [Application.cfc: Your App’s Control Panel](#applicationcfc-your-apps-control-panel)
- [Scopes: Where Stuff Lives](#scopes-where-stuff-lives)
- [Security: Lock the Doors](#security-lock-the-doors)
- [Database Queries: Don’t Be That Person](#database-queries-dont-be-that-person)
- [Performance: Need for Speed](#performance-need-for-speed)
- [Modularization & DI: Lego Mastery](#modularization--dependency-injection)
- [Error Handling: Expect Chaos](#error-handling-expect-chaos)
- [Logging: Your App’s Diary](#logging-your-apps-diary)
- [Debugging: Becoming a Code Detective](#debugging-becoming-a-code-detective)
- [Documentation & Comments](#documentation--comments)
- [Testing](#testing)
- [Environment Management](#environment-management)
- [Starting a New Project](#starting-a-new-project)
- [Joining an Existing Project](#joining-an-existing-project)
- [Deployment & CI/CD](#deployment--cicd)
- [Quick Wins](#quick-wins)
- [Conclusion: Be the Hero](#conclusion-be-the-hero)



## 🎬 Intro: Why Bother?

Writing good ColdFusion is like following a recipe — skip steps and you’ll end up with chaos instead of code.  
> “Good code is its own best documentation.”  
> — *Some Smart Developer Who Got Tired of Fixing Bad Code*

Good CFML isn’t about being clever; it’s about being **clear, consistent, and maintainable**.  
Future-you (and your teammates) will thank you.



## 🧠 Application.cfc: Your App’s Control Panel

This file is your app’s **cockpit** — mess it up, and you’re flying blind.

```coldfusion
component {
  // 1. Basic settings
  this.name = "MyApp_#hash(getCurrentTemplatePath())#";
  this.sessionManagement = true;
  this.clientManagement = false;

  // 2. App startup (pre-flight)
  function onApplicationStart() {
    application.config = configService.load();
    return true;
  }

  // 3. Request security
  function onRequestStart(string targetPage) {
    if (url.keyExists("debug") && !isLocalHost()) {
      throw("Debug mode disabled in production");
    }
  }

  // 4. Dependency Injection (manual or framework)
  function onApplicationStart() {
    application.services = {
      userService = new models.UserService(),
      logger = new models.Logger()
    };
  }
}
```

💡 *Use `onMissingTemplate()` to make your 404s user-friendly instead of “File not found!”*



## 🗺️ Scopes: Where Stuff Lives

Scopes are like rooms in your house — put things where they belong.

| Scope | Lifespan | Analogy | Use For |
|-------|-----------|----------|----------|
| `variables` | current request | junk drawer | temporary values |
| `arguments` | function call | grocery list | parameters |
| `local` | function execution | post-it notes | scoped variables |
| `this` | CFC instance | ID card | properties/methods |
| `session` | user session | backpack | user data |
| `application` | app lifetime | fridge | shared data |
| `request` | one request | takeout menu | temp data passing |
| `server` | server lifetime | foundation | rarely used |
| `cookie` | browser | loyalty card | preferences |
| `cgi` | request info | passport | headers/env vars |

🚨 **DON’T:**  
```coldfusion
application.tempData = "why is this here?";
```

✅ **DO:**  
```coldfusion
cflock(type="exclusive", scope="application") {
  application.cache = {};
}
```



## 🛡️ Security: Lock the Doors

Security is like brushing your teeth — skip it, and things get painful fast.

```cfscript
// Sanitize input
function saveComment(required string comment) {
  arguments.comment = sanitizeHTML(arguments.comment);
}

// Password hashing
function setPassword(required string password) {
  variables.password = hash(password & application.salt, "SHA-512");
}

// Validate uploads
if (!arrayContains(["jpg","pdf","png"], fileExt)) {
  throw("Invalid file type");
}
```

### Security Checklist:
✅ Use `<cfqueryparam>` in **every** query  
✅ Set `secureJSON="true"` in `Application.cfc`  
✅ Block direct CFC access via `onRequestStart()`  
✅ Escape output with `encodeForHTML()` / `encodeForJavaScript()`



## 💾 Database Queries: Don’t Be That Person

Bad queries are like leaving your car running — wasteful and dangerous.

❌ **Never Do This**
```coldfusion
queryExecute("SELECT * FROM users WHERE id = #url.id#");
```

✅ **Do This**
```coldfusion
queryExecute(
  "SELECT * FROM users WHERE id = :id",
  { id: { value: url.id, cfsqltype: "cf_sql_integer" } }
);
```

💡 **Join Instead of Loop**
```coldfusion
queryExecute("
  SELECT u.*, o.order_date
  FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  WHERE u.id IN (:ids)
", { ids: { value: listToArray(userIDs), list: true } });
```



## ⚡ Performance: Need for Speed

Slow apps are like elevators that stop at every floor.

```coldfusion
productList = cacheGet("products");
if (isNull(productList)) {
  productList = productService.list();
  cachePut("products", productList, createTimeSpan(1,0,0,0));
}
```

### Top Tips:
- Cache expensive queries
- Avoid `session` bloat
- Use `cachedWithin` wisely
- Benchmark regularly



## 🧩 Modularization & Dependency Injection

### ❌ Don’t Write God Objects
```coldfusion
component {
  function processOrder() { /* 300 lines */ }
  function sendEmail() { /* 200 lines */ }
}
```

### ✅ Do This
```
/services/
  OrderService.cfc
  EmailService.cfc
  Logger.cfc
```

### Dependency Injection
```coldfusion
component accessors="true" {
  property name="userService" inject="UserService";
  property name="logger" inject="Logger";

  function getUser(id) {
    return userService.getUserById(id);
  }
}


```

💡 *Use WireBox or DI/1 for larger apps.*



## 🚨 Error Handling: Expect Chaos

```coldfusion
try {
  payment = paymentService.process(form.amount);
} catch (PaymentFailed e) {
  logService.error(e);
  throw(type="Payment.Error", message="Payment failed. Try another card?");
} catch (any e) {
  logService.error(e);
  rethrow;
}
```

🔴 Don’t:
- Use empty catch blocks  
- Hide stack traces  
- Expose raw error messages



## 📓 Logging: Your App’s Diary

```coldfusion
cflog(
  text = "Payment failed for user #userID#. Error: #e.message# | Input: #serializeJSON(form)#",
  file = "payment",
  type = "error"
);
```

✅ **Good Logs Include:**  
- Who (User/Session ID)  
- What (Error context)  
- When (Timestamps)  
- Where (Page or module)  



## 🔍 Debugging: Becoming a Code Detective

```coldfusion
writeDump(var=local, label="LOCAL SCOPE", abort=true);
logService.search("error", date=now());
```

**Pro Tips:**
- Add checkpoints (`writeOutput("Reached X")`)
- Check logs first
- Use CF Builder or VS Code debugger
- Suspect the code you “didn’t touch”



## 📝 Documentation & Comments

```coldfusion
/**
 * Calculates discount for a user
 * @userID numeric - The user’s ID
 * @orderTotal numeric - The total
 * @return numeric - Discount percent
 */
function calculateDiscount(required numeric userID, required numeric orderTotal) {
  if (userService.isPremium(userID) && orderTotal >= 100) {
    return 10;
  }
  return 0;
}
```



## 🧪 Testing

```coldfusion
component extends="testbox.system.BaseSpec" {
  function run() {
    describe("UserService", function() {
      it("should validate emails", function() {
        expect(service.isValidEmail("test@example.com")).toBeTrue();
      });
    });
  }
}
```

**Testing Pyramid**
- 70% Unit  
- 20% Integration  
- 10% UI  



## 🌿 Environment Management

```coldfusion
// environment.properties (git ignored)
db.url=jdbc:mysql://localhost:3306/dev_db
```

```coldfusion
this.datasource = configLoader.get("db.url", detectEnvironment());
```



## 🛠️ Starting a New Project

Checklist:
- ✅ Error handling  
- ✅ Security (CSRF, CORS)  
- ✅ Logging setup  
- ✅ DI configuration  
- ✅ Environment detection  
- ✅ Base service layer



## 🔍 Joining an Existing Project

1. Find `Application.cfc`  
2. Review configs  
3. Run tests  
4. Deploy locally  
5. Identify key services  
6. Document what you learn  



## 🚀 Deployment & CI/CD

```yaml
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: ./run_tests.sh
      - if: success() && github.ref == 'refs/heads/main'
        run: ./deploy_to_prod.sh
```

✅ **Checklist**
- Automate deployments  
- Test before deploy  
- Support rollbacks  



## ⚡ Quick Wins

- Add `<cfquery timeout="30">`  
- Set `this.scriptProtect = "all";`  
- Add `/cfscripts/healthcheck.cfm`  
- Cache static data  
- Log request times  


## 🎯 Conclusion: Be the Hero

Good ColdFusion isn’t about being flashy — it’s about:
- **Clarity:** Make sense at 3 AM  
- **Humility:** Assume failure  
- **Empathy:** For your teammates & future self  

> “Always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live.”  
> — *Ancient Developer Proverb (Probably)*  

🚀 Go from **dev** to **legend**. One tag at a time.
