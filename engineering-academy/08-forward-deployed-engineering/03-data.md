# 03. Data

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Much FDE work starts with the client's data. If you cannot understand it and judge its quality, you cannot build on
it or promise results. Back to the [roadmap](./README.md).

## Reading an unfamiliar schema

Client databases are rarely documented. You need to find the tables that matter without breaking anything.

**What to learn:**

- Listing tables, columns and keys from the database catalogue
- Finding relationships that exist in the data but not in the schema
- Asking who owns each data set and who may change it

**Resources:** [PostgreSQL information schema](https://www.postgresql.org/docs/current/information-schema.html)

**Level:** Practitioner · Core

## Checking data quality

Check the data before you promise anything that depends on it. A short data audit at the start saves weeks later.

**What to learn:**

- Counting missing values, duplicates and odd formats
- Checking how far back the history goes and whether it changed shape
- Writing up what the data can and cannot support

**Resources:** [Great Expectations documentation](https://docs.greatexpectations.io/docs/home/) shows the kinds of
checks worth automating. Write the audit up as part of the scope, and practise it in the project below.

**Level:** Practitioner · Core

## SQL for analysis

Answering the client's questions from their own data builds trust fast, and gives you the baseline for measuring
your result.

**What to learn:**

- Joins, grouping and filtering
- Window functions for trends and rankings
- Running heavy queries on a copy, not on the live database

**Resources:** [PostgreSQL window functions](https://www.postgresql.org/docs/current/tutorial-window.html)

**Level:** Practitioner · Core

## Data pipelines and scheduled jobs

Moving and transforming data on a schedule: nightly imports, syncing to a search index, refreshing embeddings.

**What to learn:**

- Scheduled jobs, queues and retries
- Making jobs safe to run twice (idempotent)
- When a workflow tool such as Airflow is worth it, and when a scheduled job is enough

**Resources:** [Apache Airflow documentation](https://airflow.apache.org/docs/)

**Level:** Advanced · Optional

## Data classification

Knowing what counts as personal or confidential data decides what you may store, log or send to an AI provider.

**What to learn:**

- Techversant's four classes, Public, Internal, Confidential and Restricted, plus whether data is personal
- The client's own categories, which may differ
- What must never go into the AI tools you use to write code
- Masking and synthetic data for development and testing
- Code that handles personal data is Red Zone: written by hand and reviewed by a senior engineer

The AI tool rules cover the tools engineers use to write code. An AI feature you build for a client may process
client data only through the provider and terms agreed in the client's contract.

**Resources:**

- [AI Team Best Practices: data classification](../../ai/guides/ai-team-best-practices.md#data-classification--what-must-not-enter-ai-tools)
- [Security Audit Reference: data classification](../../security/audit/security-audit-reference.md#62-data-at-rest)
- [Security Audit Checklist](../../security/audit/security-audit-checklist.md)

**Level:** Practitioner · Core

## Project: Audit a Real Public Dataset

**Brief:** Download one month of [New York City 311 service requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9),
a public open dataset, and load it into PostgreSQL with a Python script. Treat the address and location columns as personal data, and
do not paste rows into AI tools. Write a two-page data audit for an imaginary client who wants to
predict how long requests take to resolve.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] A Python script loads the extract into PostgreSQL and reports how many rows it loaded and rejected
- [ ] Every number in the audit has the SQL query that produced it, saved in the repository
- [ ] The audit covers missing values, duplicates, inconsistent formats, the date range and changes over time
- [ ] At least five analysis queries, including one window function such as weekly request volume
- [ ] Every column is classified as Public, Internal, Confidential or Restricted, marked personal or not, and given a
  handling rule
- [ ] A clear verdict: what the data can and cannot support for the client's goal, and why
- [ ] A second engineer reruns the queries on the same extract and gets the same numbers

Previous: [02. Full-Stack Delivery](./02-full-stack-delivery.md) · Next: [04. Applied AI](./04-applied-ai.md)
