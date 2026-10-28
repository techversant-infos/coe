# ColdFusion System Architecture

> Technical reference for ColdFusion internals — request lifecycle, JVM interaction, memory management, threading, and performance tuning.

---

## 1. Request Lifecycle

### ColdFusion Request Flow

```
HTTP Request
    ↓
Web Server (IIS, Apache)
    ↓
Servlet Container (Tomcat, JBoss, WildFly)
    ↓
ColdFusion Engine
    ↓
Application.cfc (onApplicationStart, onRequestStart)
    ↓
Page Compilation (CFM → Java)
    ↓
Execution
    ↓
Output
    ↓
Application.cfc (onRequestEnd)
    ↓
HTTP Response
```

### Application.cfc Events

| Event | When It Runs | Common Uses |
|-------|--------------|-------------|
| `onApplicationStart()` | First request or after timeout | Initialize application scope |
| `onApplicationEnd()` | Application times out | Cleanup |
| `onSessionStart()` | New session created | Session initialization |
| `onSessionEnd()` | Session times out | Session cleanup |
| `onRequestStart()` | Every request | Authentication checks |
| `onRequest()` | When `request` is called | Request routing |
| `onRequestEnd()` | After page execution | Logging |
| `onError()` | When exception occurs | Error handling |
| `onMissingTemplate()` | Template not found | URL routing |

---

## 2. JVM Interaction

### ColdFusion on the JVM

ColdFusion runs as a Java application on the JVM:

```
┌─────────────────────────────────────┐
│         ColdFusion Server           │
├─────────────────────────────────────┤
│  CFML Engine (JVM Application)      │
│  ├── CFML Compiler                  │
│  ├── Tag Processor                  │
│  ├── Function Library               │
│  └── ORM (Hibernate)               │
├─────────────────────────────────────┤
│           JVM                       │
│  ├── Heap Memory                    │
│  ├── Garbage Collection             │
��  ├── Thread Management              │
│  └── Class Loading                  │
├─────────────────────────────────────┤
│      Operating System               │
└─────────────────────────────────────┘
```

### Key JVM Settings for ColdFusion

| Setting | Recommended | Purpose |
|---------|-------------|---------|
| `-Xms` | Same as `-Xmx` | Avoid heap resizing |
| `-Xmx` | 4GB-8GB | Max heap (adjust per server) |
| `-XX:MaxMetaspaceSize` | 512MB | Metaspace for class definitions |
| `-XX:+UseG1GC` | Enabled | G1 garbage collector |
| `-XX:MaxGCPauseMillis` | 500 | Target GC pause time |

---

## 3. Memory Management

### ColdFusion Scopes and Memory

| Scope | Lifetime | Storage | Memory Consideration |
|-------|----------|---------|---------------------|
| `variables` | Request | Heap | Request-scoped, auto-cleanup |
| `request` | Request | Heap | Per-request data |
| `session` | Session timeout | Heap/Session storage | Size per user |
| `application` | Server restart | Heap | Shared across users |
| `server` | Server restart | Heap | JVM-level shared |
| `client` | Client timeout | Registry/DB/Cookie | Persistent across sessions |

### Memory Leak Patterns

**Common causes:**

1. **Unbounded caching**
   ```cfm
   <!--- BAD: Cached indefinitely --->
   <cfset application.cache = queryData>
   
   <!--- GOOD: With TTL --->
   <cfset cachePut('data', queryData, 3600)>
   ```

2. **Session accumulation**
   ```cfm
   <!--- BAD: Storing large objects --->
   <cfset session.largeFile = fileRead(fullPath)>
   
   <!--- GOOD: Reference only --->
   <cfset session.filePath = fullPath>
   ```

3. **Circular references**
   ```cfm
   <!--- BAD: Circular component references --->
   <cfset this.parent = parentComponent>
   <cfset parentComponent.child = this>
   ```

---

## 4. Threading and Concurrency

### ColdFusion Threading Model

ColdFusion uses Java threads for request handling:

```
Request Thread Pool
    ├── Thread-1 (Request 1)
    ├── Thread-2 (Request 2)
    ├── Thread-3 (Request 3)
    └── ... (configurable size)

Scheduled Task Threads
    └── Separate pool for <cfschedule>
```

### Thread-Safe Code Patterns

**Shared scope access:**
```cfm
<!--- Use locks for shared resources --->
<cflock name="application.counter" type="exclusive" timeout="5">
    <cfset application.counter = application.counter + 1>
</cflock>

<!--- Read-only access --->
<cflock name="application.counter" type="readonly" timeout="5">
    <cfset currentCount = application.counter>
</cflock>
```

**cfthread for parallel processing:**
```cfm
<!--- Spawn parallel threads --->
<cfthread name="task1,task2,task3" action="run">
    <cfset result = someHeavyOperation()>
</cfthread>

<!--- Wait for completion --->
<cfthread action="join" />

<!--- Get results --->
<cfset result1 = cfthread["task1"].output>
<cfset result2 = cfthread["task2"].output>
```

### Thread Safety Checklist

- [ ] Shared scope writes protected with `<cflock>`
- [ ] No mutable static variables in CFCs
- [ ] Session scope doesn't store complex objects unnecessarily
- [ ] Application scope initialization in `onApplicationStart()`
- [ ] Thread-local storage used where appropriate

---

## 5. Session Management

### Session Configuration

**In Application.cfc:**
```cfm
component {
    this.name = "MyApp_v1";
    this.sessionManagement = true;
    this.sessionTimeout = createTimeSpan(0, 2, 0, 0); // 2 hours
    this.setClientCookies = true;
    this.setDomainCookies = false;
    
    // Clustered session storage
    this.sessionStorage = "redis"; // or "memory"
}
```

### Session Storage Options

| Storage | Pros | Cons |
|---------|------|------|
| Memory | Fast | Lost on restart, no clustering |
| Redis | Fast, clustered, persistent | External dependency |
| Database | Persistent, clustered | Slower |
| J2EE Session | Container-managed | Vendor-specific |

### Session Security

```cfm
// Regenerate session ID on login
onCFCRequest = function(string targetPage) {
    if (isAuthenticated() && !session.regenerated) {
        this.regenerateSessionID();
        session.regenerated = true;
    }
    include arguments.targetPage;
}
```

---

## 6. Database Connection Management

### Connection Pooling

ColdFusion manages database connections via connection pools:

```
┌────────────────────────────────────┐
│       ColdFusion Server            │
├────────────────────────────────────┤
│  Connection Pool Manager           │
│  ├── Min Connections: 5           │
│  ├── Max Connections: 100          │
│  ├── Idle Timeout: 300s           │
│  └── Connection Timeout: 30s       │
├────────────────────────────────────┤
│  DataSource 1 (DB1)                │
│  └── Pool of 20 connections       │
├────────────────────────────────────┤
│  DataSource 2 (DB2)                │
│  └── Pool of 10 connections       │
└────────────────────────────────────┘
```

### Best Practices

```cfm
<!--- Good: Use cfqueryparam for security and performance --->
<cfquery datasource="myDSN">
    SELECT * FROM users 
    WHERE user_id = <cfqueryparam value="#userId#" cfsqltype="cf_sql_integer">
</cfquery>

<!--- Good: Query timeout for long-running queries --->
<cfquery name="data" datasource="myDSN" querytimeout="30">
    SELECT * FROM large_table
</cfquery>

<!--- Good: Close result sets explicitly when done --->
<cfquery name="tempResult" ...>
    ...
</cfquery>
<cfset tempResult = "">
```

---

## 7. Caching Architecture

### Cache Levels in ColdFusion

```
┌─────────────────────────────────────────────┐
│              Browser Cache                   │
│         (Expires headers, ETag)              │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│              CDN / Proxy                     │
│          (CloudFront, CloudFlare)            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          Application Cache                    │
│     (CacheNew, CachePut, CacheGet)          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│           Query Cache                        │
│     (CachedWithin, cached query results)     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│             Database                         │
└─────────────────────────────────────────────┘
```

### Cache Implementation

```cfm
<!--- Function result caching --->
<cffunction name="getUserData" output="false">
    <cfargument name="userId" required="true">
    
    <!--- Cache function result for 5 minutes --->
    <cfset cached = cacheGet("user_#arguments.userId#")>
    <cfif isNull(cached)>
        <cfquery name="local.data" datasource="myDSN">
            SELECT * FROM users WHERE user_id = <cfqueryparam value="#arguments.userId#">
        </cfquery>
        <cfset cachePut("user_#arguments.userId#", local.data, 600)>
        <cfreturn local.data>
    <cfelse>
        <cfreturn cached>
    </cfif>
</cffunction>

<!--- Query caching --->
<cfquery name="data" datasource="myDSN" cachedwithin="#createTimeSpan(0,1,0,0)#">
    SELECT * FROM categories
</cfquery>
```

---

## 8. Performance Monitoring

### Built-in Diagnostics

| Tool | Access | Purpose |
|------|--------|---------|
| CF Administrator | `/cfide/administrator` | Server config, datasources |
| Server Monitoring | CF Admin → Monitoring | Real-time metrics |
| Request Profiling | CF Admin → Debugging | Slow request analysis |
| Log Files | `{cfroot}/logs` | Error and request logs |

### FusionReactor Metrics

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Response Time | < 200ms | 200-500ms | > 500ms |
| Heap Usage | < 70% | 70-85% | > 85% |
| Thread Count | < 50 | 50-100 | > 100 |
| Request Queue | < 10 | 10-50 | > 50 |

### Key Logs to Monitor

| Log | Location | Contents |
|-----|----------|----------|
| exception.log | `{cfroot}/logs` | Application errors |
| application.log | `{cfroot}/logs` | Application events |
| scheduler.log | `{cfroot}/logs` | Scheduled task events |
| jvm.log | `{cfroot}/logs` | JVM metrics |

---

## Related Resources

- [01-coldfusion-deep-expertise](../01-coldfusion-deep-expertise/) — Full CF expertise module
- [cf-architecture-review-checklist](./cf-architecture-review-checklist.md) — Architecture review
- [cf-performance-tuning-guide](./cf-performance-tuning-guide.md) — Performance optimization
