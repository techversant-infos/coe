# 01. CFML and the Platform

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

The engines, versions, tools and coding habits a senior ColdFusion consultant works with every day. Back to the
[roadmap](./README.md).

## Adobe ColdFusion, Lucee and BoxLang

Three engines run CFML (ColdFusion Markup Language) today. Clients choose between them on cost, support and
compatibility, so you need to explain the differences without bias.

| Engine | Who makes it | License | Notes |
|--------|--------------|---------|-------|
| Adobe ColdFusion | Adobe | Commercial; ColdFusion 2025 is sold as a subscription only | Bundles services such as PDF generation and Solr search, some as optional add-on packages |
| Lucee | Lucee Association Switzerland | Open source (LGPL 2.1) | Paid support comes from association members |
| BoxLang | Ortus Solutions | Open source (Apache 2.0) | New JVM language, released in May 2025, that can run most CFML |

**What to learn:**

- What each engine does well and where they differ
- Which built-in Adobe features have no direct Lucee equivalent
- How licensing changes the total cost for a client

**Resources:**

- [Lucee and Adobe ColdFusion differences](./reference/lucee-vs-adobe.md)
- [ColdFusion 2021 support ending, Adobe](https://coldfusion.adobe.com/2026/03/planning-ahead-coldfusion-2021-support-ending-soon/),
  which also notes that ColdFusion 2025 is subscription only
- [BoxLang](https://boxlang.io/)

**Level:** Practitioner · Core

## Versions and support lifecycle

Clients often run versions that no longer receive security updates. Knowing the dates lets you spot risk in the first
conversation.

| Version | End of core support | End of extended support |
|---------|---------------------|-------------------------|
| Adobe ColdFusion 2018 | 13 July 2023 | 13 July 2024 |
| Adobe ColdFusion 2021 | 10 November 2025 | 10 November 2026 |
| Adobe ColdFusion 2023 | 16 May 2028 | 16 May 2029 |
| Adobe ColdFusion 2025 | 26 February 2030 | None announced |

Adobe's extended support is best-effort migration help and does not include security patches. Lucee 5.4 reached end of
life on 31 December 2025; Lucee 6.2 is the long-term support release and 7.1 is the current stable release.

**What to learn:**

- Core versus extended support, and why only core support brings security updates
- The Java version each engine release needs
- Where to check dates before you quote them to a client

**Resources:**

- [Adobe products and technical support periods](https://helpx.adobe.com/support/programs/eol-matrix.html)
- [Lucee downloads](https://download.lucee.org/), which list the current long-term support and stable releases
- [Lucee 5.4 end of life announcement](https://dev.lucee.org/t/lucee-roadmap-2025-5-4-is-eol-dec-31st-2025/14760)

**Level:** Practitioner · Core

## Modern CFML

Much client code is tag-based and written for engines from 15 years ago. You need to read that style and write the
modern one.

**What to learn:**

- Script syntax, components (CFCs), closures and member functions
- `queryExecute()` with parameters instead of string-built SQL
- Moving from `Application.cfm` to `Application.cfc`
- Error handling with `try`/`catch` and `onError`

**Resources:** [CFDocs](https://cfdocs.org/), a community reference for tags and functions

**Level:** Practitioner · Core

## Frameworks

Recognizing the framework tells you how an application is organized before you read much code.

**What to learn:**

- ColdBox and FW/1, the frameworks most common in maintained applications
- Older frameworks you will still meet: Fusebox, Mach-II and Model-Glue
- Applications with no framework: plain `.cfm` pages joined with `cfinclude`

**Resources:** [ColdBox documentation](https://coldbox.ortusbooks.com/)

**Level:** Practitioner · Core

## CommandBox and CFConfig

CommandBox starts a local CFML server from the command line. CFConfig exports and imports server settings as JSON, so
configuration can live in version control.

**What to learn:**

- Starting Adobe ColdFusion or Lucee servers with `server.json`
- Installing packages from ForgeBox
- Exporting and importing settings with CFConfig

**Resources:**

- [CommandBox documentation](https://commandbox.ortusbooks.com/)
- [CFConfig documentation](https://cfconfig.ortusbooks.com/)

**Level:** Practitioner · Core

## Testing with TestBox

TestBox is the standard testing framework for CFML. Tests are what make changes to old code safe.

**What to learn:**

- Writing unit and integration specs
- Running tests from CommandBox and in CI
- Mocking components with MockBox

**Resources:** [TestBox documentation](https://testbox.ortusbooks.com/)

**Level:** Practitioner · Core

## CFML coding standards

Techversant's own CFML standards apply to every change you make on a client project.

**What to learn:** the style guide, best practices and review checklist.

**Resources:**

- [ColdFusion Best Practices](../../../standards/coldfusion/coldfusion-best-practices.md)
- [ColdFusion Style Guide](../../../standards/coldfusion/coldfusion-style-guide.md)
- [ColdFusion Code Review Checklist](../../../standards/coldfusion/coldfusion-code-review-checklist.md)

**Level:** Practitioner · Core

## Project: Run the Practice App on Two Engines

**Brief:** Get the [practice app, BlogCFC5](./reference/practice-app-blogcfc5.md), running locally on Lucee 6.2 or 7.1
and on the free Adobe ColdFusion 2025 Developer edition, both started with CommandBox. Record every compatibility error
you hit; later projects use the list.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] A `server.json` for each engine starts the app with one `box server start` command
- [ ] Server settings, including the datasource, are exported with CFConfig and committed without passwords
- [ ] A list of every compatibility error, with the file, the engine and the cause
- [ ] At least three TestBox specs cover the home page, a single post and search, and pass on both engines
- [ ] A one-page note explains which engine you would recommend for this app and why

Back to the [roadmap](./README.md) · Next: [02. JVM, Performance and Diagnostics](./02-jvm-performance-and-diagnostics.md)
