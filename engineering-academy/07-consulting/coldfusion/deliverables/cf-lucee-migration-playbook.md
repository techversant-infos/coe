# ColdFusion to Lucee Migration Playbook

> Step-by-step guide for migrating Adobe ColdFusion applications to Lucee.

## Purpose

This playbook provides a systematic approach to migrating ColdFusion applications from Adobe ColdFusion to Lucee. Follow the phases in order.

## Metadata

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | |
| Author | |
| Client | |
| Application | |

---

## Phase 1: Pre-Migration Assessment

### 1.1 Current Environment Documentation

Before starting migration, document:

- [ ] ColdFusion version
- [ ] Operating system
- [ ] JVM version
- [ ] Database type and version
- [ ] All installed extensions
- [ ] Scheduled tasks configuration
- [ ] Datasource configurations
- [ ] Mail server configuration
- [ ] Custom JVM arguments

### 1.2 Code Compatibility Scan

Use tools to identify potential issues:

**Automated Scanning:**
```bash
# CommandBox Lucee migrator
boxlucee migrate --source=/path/to/app --report
```

**Common Issues to Look For:**

| Issue | Adobe CF Usage | Lucee Alternative |
|-------|---------------|-------------------|
| PDF Services | `cfpdf>` | PDFtk, iText, or external service |
| Exchange | `cfexchange_*` | REST API integration |
| Solr | `<cfsearch>` | Elasticsearch, Typesense |
| PowerPoint | `cfpresentation` | External generation |
| Charts | `<cfchart>` | ChartJS, Highcharts |
| Flash Forms | `<cfform>` with `format="flash">` | HTML5 forms |

### 1.3 Extension Audit

Document all ACF extensions in use:

| Extension | Purpose | Replacement Needed? | Alternative |
|-----------|---------|-------------------|-------------|
| | | | |
| | | | |
| | | | |

---

## Phase 2: Environment Setup

### 2.1 Lucee Installation

**Option A: CommandBox (Recommended)**
```bash
# Install CommandBox
brew install commandbox

# Create new Lucee server
box server create name=myapp engine=lucee@5
```

**Option B: Docker**
```dockerfile
FROM ortussolutions/commandbox:latest
COPY . /app
WORKDIR /app
CMD ["server", "start"]
```

**Option C: Traditional**
Download from https://lucee.org/downloads.html

### 2.2 Configuration Mapping

Map Adobe CF settings to Lucee equivalents:

| Adobe CF Setting | Lucee Equivalent | Notes |
|-----------------|------------------|-------|
| Administrator URL | Server Administrator | Different URL pattern |
| Request timeout | `requesttimeout` in Application.cfc | |
| Session timeout | `applicationtimeout`, `sessiontimeout` | Same syntax |
| Datasource | RDS/RAM setting | Same concept |
| Error handling | `onError` in Application.cfc | |

### 2.3 Development Environment

1. Set up Lucee instance matching production config
2. Point to cloned/staged codebase
3. Configure datasources
4. Test basic functionality

---

## Phase 3: Compatibility Fixes

### 3.1 Function Replacement

Common function differences:

```cfml
<!-- Adobe CF -->
#createObject("java", "java.util.ArrayList")#
#serverlist#
#getTemplatePath()#

<!-- Lucee Equivalent -->
createObject("java", "java.util.ArrayList")  // Remove #
serverList                                           // camelCase
getBaseTemplatePath()                               // Different function
```

### 3.2 Tag Compatibility

```cfml
<!-- Adobe CF: cfschedule -->
<cfschedule action="update" ...>

<!-- Lucee: Same syntax, may need adjustments -->
<cfschedule action="update" ...>
```

### 3.3 ORM Differences

| Feature | Adobe CF | Lucee |
|---------|----------|-------|
| ORMEnable | Same | Same |
| ormSettings | Same | Same |
| EntityLoad | Same | Same |
| EntitySave | Same | Same |
| Transaction | Same | Same |

### 3.4 Session Management

```cfml
<!-- Adobe CF cluster session -->
<cfapplication sessionmanagement="true" 
               sessionstorage="mysql">

<!-- Lucee: Use Redis for distributed sessions -->
<cfset this.sessioncluster = true>
<cfset this.storage = "redis">
```

---

## Phase 4: Testing

### 4.1 Unit Testing

Set up TestBox for unit tests:
```bash
box install testbox
```

### 4.2 Functional Testing Checklist

| Test Area | Test Cases | Status |
|-----------|-----------|--------|
| Database operations | | |
| File operations | | |
| Session management | | |
| Authentication | | |
| Authorization | | |
| API endpoints | | |
| Scheduled tasks | | |
| Email functionality | | |
| File uploads | | |
| PDF generation | | |

### 4.3 Regression Testing

1. Create test accounts
2. Run full workflow tests
3. Document any differences
4. Compare output to Adobe CF

### 4.4 Performance Benchmarking

| Metric | Adobe CF | Lucee | Difference |
|--------|----------|-------|------------|
| Avg response time | | | |
| Peak memory usage | | | |
| CPU utilization | | | |
| Concurrent users | | | |

---

## Phase 5: Production Migration

### 5.1 Pre-Migration Checklist

- [ ] All tests passing
- [ ] Performance acceptable
- [ ] Extensions replaced
- [ ] Documentation updated
- [ ] Rollback plan tested
- [ ] Team trained on Lucee
- [ ] Support plan in place

### 5.2 Migration Strategy

**Option A: Blue-Green Deployment**
1. Set up new Lucee environment (green)
2. Test thoroughly
3. Switch load balancer
4. Keep blue environment running for rollback

**Option B: Phased Cutover**
1. Migrate non-critical apps first
2. Validate
3. Proceed to critical apps

**Option C: Big Bang**
1. Migrate all at once
2. Higher risk
3. Faster completion

### 5.3 Rollback Plan

| Step | Action | Time Needed |
|------|--------|-------------|
| 1 | Switch load balancer | |
| 2 | Revert DNS | |
| 3 | Restore Adobe CF | |
| | **Total** | |

### 5.4 Post-Migration Verification

1. Monitor error logs
2. Check performance metrics
3. Validate critical workflows
4. Confirm scheduled tasks running
5. Verify backups working

---

## Phase 6: Post-Migration

### 6.1 Documentation Updates

- [ ] Update architecture diagrams
- [ ] Update deployment procedures
- [ ] Document any code changes
- [ ] Update monitoring configurations

### 6.2 Team Training

| Topic | Audience | Status |
|-------|----------|--------|
| Lucee admin | DevOps | |
| Lucee differences | Developers | |
| New extension usage | Developers | |
| Troubleshooting | Support | |

### 6.3 Ongoing Monitoring

Monitor for:
- [ ] Performance regressions
- [ ] Memory leaks
- [ ] Extension issues
- [ ] Compatibility bugs

---

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Forms not submitting | CSRF differences | Check `this.csrfglobalscope` |
| PDF generation fails | Extension missing | Install PDF extension or use external service |
| Session loss | Session storage | Configure Redis session storage |
| Slow startup | Large application | Enable compilation caching |
| Database errors | Driver differences | Update datasource settings |

---

## Appendix A: Quick Reference

### Lucee-Specific Settings

```cfml
// Application.cfc settings unique to Lucee
this.compilation = "development";  // or "production"
this.csrfglobalscope = true;
this.sessioncluster = true;
this.filebrowserEnabled = false;
```

### Useful Lucee Functions

```cfml
// Lucee-specific functions
imageBlur()
imageSharpen()
sessionRotate()

// Improved JSON functions
serializeJSON(data, false);  // Struct ordered
```

### Docker Compose Example

```yaml
version: '3.8'
services:
  lucee:
    image: ortussolutions/commandbox
    ports:
      - "8080:8080"
    volumes:
      - ./app:/app
    environment:
      - JAVA_HEAP_SIZE=2g
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | | | Initial version |
