# 07. Upgrades and Migration

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Moving an application to a supported Adobe ColdFusion version, or from Adobe ColdFusion to Lucee, is the most common
CFML project. The work is mostly finding and fixing incompatibilities, then switching over safely.
Back to the [roadmap](./README.md).

## Adobe ColdFusion upgrades

Each Adobe release removes or changes features. ColdFusion 2025 runs on Java 21 and removed several long-deprecated
features, so skipping versions needs careful checking.

**What to learn:**

- Running Adobe's Code Analyzer and reading what it can and cannot find
- Checking the list of removed and deprecated features for the target version
- Upgrading the Java runtime, JDBC (Java Database Connectivity) drivers and libraries at the same time
- Installing only the packages the application needs with the ColdFusion package manager, `cfpm`, in ColdFusion 2021
  and later
- Moving straight to a version in core support, not to one that is about to lose it

**Resources:**

- [Using the Code Analyzer, Adobe](https://helpx.adobe.com/coldfusion/developing-applications/developing-cfml-applications/debugging-and-troubleshooting-applications/using-the-code-analyzer.html)
- [ColdFusion 2025 breaking changes, Pete Freitag](https://www.petefreitag.com/blog/coldfusion-2025-breaking/)

**Level:** Practitioner · Core

## Migrating to Lucee

Lucee runs most CFML, but some Adobe features and behaviors differ.

**What to learn:**

- Finding Adobe-only tags, functions and services, such as PDF, Exchange and Solr
- Choosing replacements, for example an extension, a library or an external service
- Behavior differences in dates, nulls, queries and ORM (object-relational mapping, the engine's Hibernate layer)

**Resources:**

- [CF to Lucee Migration Playbook](./deliverables/cf-lucee-migration-playbook.md)
- [Lucee and Adobe ColdFusion differences](./reference/lucee-vs-adobe.md)
- [Lucee documentation](https://docs.lucee.org/)

**Level:** Practitioner · Core

## Lucee upgrades

Clients already on Lucee need upgrades too. Lucee 5.4 reached end of life on 31 December 2025, and Lucee 7 is a larger
change than earlier versions.

**What to learn:**

- Moving from Lucee 5.4 to the 6.2 long-term support release or the 7.1 stable release
- Lucee 7's switch from the `javax` to the `jakarta` Java namespace, which needs Tomcat 10.1 or later, a fresh install
  and Jakarta versions of extensions
- Checking every extension and container image the application uses before you upgrade

**Resources:**

- [Lucee 7 guide](https://docs.lucee.org/guides/lucee-7.html)
- [Lucee downloads](https://download.lucee.org/)

**Level:** Practitioner · Core

## Compatibility testing

Tests decide whether the migrated application really behaves the same.

**What to learn:**

- Running the same TestBox suite on the old and new engines
- Comparing page output and API responses between the two
- Testing scheduled tasks, email, PDFs and file handling, which unit tests often miss

**Resources:** [CF to Lucee Migration Playbook](./deliverables/cf-lucee-migration-playbook.md)

**Level:** Practitioner · Core

## Configuration migration

Datasources, mail servers, mappings and caches live in the engine, not the code, and are easy to miss.

**What to learn:**

- Exporting settings from the old server and importing them on the new one with CFConfig
- Reviewing every setting instead of copying blindly
- Keeping the result in version control without passwords

**Resources:**

- [CF to Lucee Migration Playbook](./deliverables/cf-lucee-migration-playbook.md)
- [CFConfig documentation](https://cfconfig.ortusbooks.com/)

**Level:** Practitioner · Core

## Data, sessions and files

The code is only part of the move.

**What to learn:**

- Database driver changes and character encoding
- What happens to logged-in users during the switch
- Uploaded files, generated documents and paths that differ between servers

**Resources:** learn on engagements, with a lead.

**Level:** Practitioner · Core

## Cutover and rollback

The switch to production should be planned, rehearsed and reversible.

**What to learn:**

- Running old and new side by side, then moving traffic in steps
- A written rollback plan with a clear trigger
- Telling users and the client what will happen and when

**Resources:** [CF to Lucee Migration Playbook](./deliverables/cf-lucee-migration-playbook.md)

**Level:** Advanced · Core

## Evaluating BoxLang

BoxLang is a JVM language from Ortus Solutions, released in May 2025, that can run CFML code. Ortus states very high
CFML compatibility; this is a vendor claim, so test it on the client's code before you recommend it.

**What to learn:**

- How BoxLang runs existing CFML
- What a proof of concept on the client's code must show before you recommend it

**Resources:**

- [BoxLang documentation](https://boxlang.ortusbooks.com/)
- [Into the Box 2025 keynote recap, Ortus Solutions](https://www.ortussolutions.com/blog/into-the-box-2025-keynote-day-1-recap)

**Level:** Advanced · Optional

## Project: Migrate the Practice App

**Brief:** Treat the practice app on the Adobe ColdFusion 2025 server from stage 01 as production, and migrate it to
the engine in your stage 06 decision record. If that record keeps Adobe ColdFusion, migrate to Lucee 7.1 for practice,
and note why the client would not. Prepare a production cutover.

**Size:** 3–5 days

**Verification**, checked by a senior engineer:

- [ ] A compatibility scan of the code, with every finding fixed or accepted with a reason
- [ ] The engine configuration exported, reviewed and imported with CFConfig, with no passwords committed
- [ ] The full TestBox suite from stage 04 passes on the target engine
- [ ] Page output for ten key pages compared between the old and new engines, and every difference explained
- [ ] A cutover plan with a rollback trigger, and a rehearsal where you roll back and record how long it took

Previous: [06. Modernization Strategy](./06-modernization-strategy.md) · Next: [08. Cloud, Containers and DevOps](./08-cloud-containers-and-devops.md)
