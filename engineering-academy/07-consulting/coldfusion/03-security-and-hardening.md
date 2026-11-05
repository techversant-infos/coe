# 03. Security and Hardening

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

ColdFusion servers are a regular target. In July 2026, CVE-2026-48282, a ColdFusion path traversal flaw rated 10.0,
the highest score, was added to CISA's Known Exploited Vulnerabilities catalog, the US government's list of flaws
attackers are using ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48282)). Adobe fixed it in ColdFusion 2025
Update 10 and ColdFusion 2023 Update 21, in bulletin APSB26-68; ColdFusion 2021 gets no fix. A senior consultant keeps
client servers patched, locked down and reviewed. Back to the [roadmap](./README.md).

## Security updates and patching

Adobe releases ColdFusion security updates as numbered updates, rated by priority. Lucee publishes security releases
for its supported versions. An unpatched server is the easiest way in.

**What to learn:**

- Reading Adobe security bulletins and Lucee release notes, and judging how urgent an update is
- Applying updates in a test environment first, then in production, with a rollback plan
- Keeping the bundled Java runtime and JDBC (Java Database Connectivity) drivers updated as well
- Telling a client when their version no longer gets security updates at all

**Resources:**

- [Adobe ColdFusion security bulletins](https://helpx.adobe.com/security/products/coldfusion.html)
- [Versions and support lifecycle](./01-cfml-and-the-platform.md#versions-and-support-lifecycle)

**Level:** Practitioner · Core

## Server lockdown

A default installation exposes more than a production server should. Adobe publishes a lockdown guide for each
ColdFusion release.

**What to learn:**

- Removing or restricting the ColdFusion Administrator, `/CFIDE` and other default paths
- Running the service as a low-privilege user
- Disabling features the application does not use, and setting a deserialization filter
- Hardening Lucee: the server and web administrators, and production settings

**Resources:**

- [CF Security Review Checklist: ColdFusion-specific security](./deliverables/cf-security-review-checklist.md#5-coldfusion-specific-security)
- [CFDocs security page](https://cfdocs.org/security), which links the Adobe lockdown guide for each version
- [ColdFusion Security Guide, Foundeo](https://foundeo.com/security/guide/)

**Level:** Practitioner · Core

## Secure CFML coding

Most application flaws in CFML code come from a few patterns.

**What to learn:**

- Parameterized queries with `cfqueryparam` or `queryExecute()` parameters
- Output encoding with `encodeForHTML()`, `encodeForURL()` and related functions
- Safe file uploads: check type and size, store outside the web root, never trust the file name
- Cross-site request forgery (CSRF) tokens, secure session cookies and server-side authorization checks

**Resources:**

- [Deep expertise guide, section 5](./reference/coldfusion-deep-expertise-guide.md#5-secure-coldfusion-applications-against-common-vulnerabilities)
- [ColdFusion Best Practices](../../../standards/coldfusion/coldfusion-best-practices.md)

**Level:** Practitioner · Core

## Secrets and configuration

Old CFML applications often keep database passwords and API keys in code or in the administrator.

**What to learn:**

- Moving secrets into environment variables or a secrets manager
- Keeping CFConfig exports free of passwords
- Rotating a secret that has been committed to version control

**Resources:** [CFConfig documentation](https://cfconfig.ortusbooks.com/)

**Level:** Practitioner · Core

## Security review

A structured review finds what a quick look misses, and gives the client a prioritized list.

**What to learn:**

- Working through the checklist for a CFML application
- Rating each finding by severity and agreeing fix deadlines
- Writing findings a non-technical client can act on

**Resources:**

- [CF Security Review Checklist](./deliverables/cf-security-review-checklist.md)
- [Security Audit Checklist](../../../security/audit/security-audit-checklist.md)

**Level:** Advanced · Core

## Red Zone work

Techversant never delegates some work to AI tools: authentication and authorization, encryption and key management,
personal data and payment handling, and production database migrations. Legacy CFML applications often contain all
four, usually written by hand years ago.

**What to learn:**

- Recognizing Red Zone code in an inherited application
- Writing and reviewing that code by hand, with a senior engineer's review
- Stopping and escalating when a task turns into Red Zone work

**Resources:** [AI Era Coding Guidelines, section 2.2](../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)

**Level:** Practitioner · Core

## Project: Review and Harden the Practice App

**Brief:** Run a security review of the practice app with the CF Security Review Checklist, fix the most serious
findings, and lock down the server it runs on.

**Size:** 2–3 days

**Verification**, checked by a senior engineer:

- [ ] Every section of the checklist is completed, with each item marked pass, fail or not applicable with a reason
- [ ] Each finding has a severity, the file and line, and a recommended fix
- [ ] The three most serious findings are fixed, and a TestBox spec proves each fix
- [ ] The server follows the lockdown guide for its version: the administrator is not reachable from the public
  address, and default paths are removed or blocked
- [ ] No passwords or keys remain in the code or in committed configuration
- [ ] Any change to login, session or permission code was written by hand and approved by a senior engineer
- [ ] A one-page summary for a non-technical client lists the risks in order of priority

Previous: [02. JVM, Performance and Diagnostics](./02-jvm-performance-and-diagnostics.md) · Next: [04. Maintaining Legacy Applications](./04-maintaining-legacy-applications.md)
