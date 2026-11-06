# 04. Data Architecture

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Data usually outlives the code that writes it. Decisions about how data is modelled, stored, changed and kept are
some of the hardest to reverse. Back to the [roadmap](./README.md).

## Data modelling

A data model describes the things the business cares about and how they relate. A good model makes common questions
easy to answer and wrong data hard to store.

**What to learn:**

- Entities, relationships and constraints, and letting the database enforce rules where it can
- Normalising to avoid duplicated data, and when to duplicate on purpose for speed
- Naming tables and fields in the business's own words

**Resources:**

- [Designing Data-Intensive Applications](https://dataintensive.net/), Martin Kleppmann, the chapter on data models and query
  languages

**Level:** Practitioner · Core

## Choosing data stores

Relational databases suit most client systems. Other stores, such as document, key-value or search engines, earn
their place only for a specific need.

**What to learn:**

- What relational databases do well, and the needs they serve poorly
- When a search engine, a cache or an object store is worth the extra system to run
- The real cost of each new store: backups, monitoring, skills and licences

**Resources:**

- [Understand data store models](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview),
  Azure Architecture Center

**Level:** Advanced · Core

## Schema migrations

The schema has to change while the system is running and old code may still be reading it. Plan each change so it
can be deployed and rolled back safely.

**What to learn:**

- Expand and contract: add the new structure, move data and code across, then remove the old structure
- Running migrations in the deployment pipeline, with a tested way back
- Large data changes that must run in batches to avoid locking tables
- Production migration scripts are Red Zone work at Techversant: written by hand, without AI generation, and
  reviewed by a senior engineer

**Resources:**

- [Rollback and database script management](../../standards/git/git-workflow.md#-rollback--database-script-management),
  in the Techversant Git workflow
- [Parallel change](https://martinfowler.com/bliki/ParallelChange.html), Danilo Sato

**Level:** Practitioner · Core

## Transactions and consistency

When several things must happen together, such as saving an article and its tags, transactions keep data correct.
Across services and stores, you have to design consistency yourself.

**What to learn:**

- Transactions and isolation levels, and the problems each level allows
- Eventual consistency, and how to explain it to a client in terms of what users will see
- Keeping data consistent across services, for example with the outbox pattern

**Resources:**

- [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), PostgreSQL documentation
- [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html), Chris Richardson

**Level:** Advanced · Core

## Retention and backups

Data must be kept as long as the business and the law require, and no longer. It must also survive mistakes and
disasters.

**What to learn:**

- Retention rules for each kind of data, and deleting data when its time is up
- Backups, point-in-time recovery and testing that a restore actually works
- Classifying data by sensitivity, so personal data gets the protection it needs

**Resources:**

- [Handling and retention](../../security/audit/security-audit-reference.md#163-handling-and-retention), in the Techversant
  security audit reference, for retention periods, backups and data classification
- [Data at rest](../../security/audit/security-audit-reference.md#62-data-at-rest), in the same reference

**Level:** Practitioner · Core

## Reporting and analytics

Running reports on the live database can slow the system for everyone. Larger clients need a separate copy of the
data shaped for analysis.

**What to learn:**

- Read replicas, data warehouses and scheduled exports, and when each fits
- Keeping personal data out of reports unless it is needed

**Resources:** learn on projects, with an architect.

**Level:** Practitioner · Optional

## Project: Plan the Data for Growth

**Brief:** Lantern's growth adds followers, notifications and ten years of imported articles. Design the data
changes, prove one migration on the running app, and set retention rules for personal data.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] An updated data model covers notifications, notification preferences and imported legacy articles
- [ ] An ADR decides whether search needs a separate store, with storage and cost estimates for 50,000 users
- [ ] One schema change is carried out on the running app with expand and contract, in at least two separate
  deployments, and the API tests pass after each step
- [ ] The same change has a tested rollback script
- [ ] A table lists each kind of personal data the system stores, its sensitivity, where it lives and how long it is
  kept
- [ ] The five most frequent queries after the change have suitable indexes, shown with query plans from the running
  app

Previous: [03. API and Integration Architecture](./03-api-and-integration-architecture.md) · Next:
[05. Reliability and Performance](./05-reliability-and-performance.md)
