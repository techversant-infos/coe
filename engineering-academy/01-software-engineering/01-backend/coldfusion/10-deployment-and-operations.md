# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

An API is only useful once it runs reliably for real users. This stage covers building the same server every time,
shipping it through a pipeline, changing a production database safely, and running the same code on Lucee and
Adobe ColdFusion. Back to the [roadmap](./README.md).

## Reproducible server set-up

Every environment should run the same engine, Java version and settings, built from files in the repository, not
from clicks in an administrator.

**What to learn:**

- Pinning the engine version and Java version in `server.json`, and the packages in `box.json`
- CFConfig: exporting the engine's settings, such as datasources and mail servers, to a file, with secrets read from
  environment variables. The REST template's `.cfconfig.json` turns debugging on, so production needs its own
  settings
- Server profiles, which set safe defaults for production

**Resources:**

- [Configuring your server](https://commandbox.ortusbooks.com/embedded-server/configuring-your-server) and
  [Server profiles](https://commandbox.ortusbooks.com/embedded-server/configuring-your-server/server-profiles),
  CommandBox documentation
- [CFConfig](https://cfconfig.ortusbooks.com/), Ortus documentation
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant:
  the environment management section

**Level:** Advanced · Core

## Docker images

A container image packages the engine, your code and its settings, so the API runs the same everywhere.

**What to learn:**

- Building on the `ortussolutions/commandbox` image, and warming up the engine at build time so containers start fast
- Keeping the [Stage 08 archive lab](./08-testing.md#project-pass-the-full-test-suite) outside the Docker build
  context. Copy only the files the API needs to run into the image.
- Running as a user that is not root, with no secrets in the image
- Licensing: Lucee is free to run in containers; Adobe ColdFusion needs the client's licence
- Adobe ColdFusion 2021 and later install features such as database drivers and mail as packages with its package
  manager, `cfpm`, so install the ones the API needs when you build the image

**Resources:**

- [Docker](https://commandbox.ortusbooks.com/deploying-commandbox/docker), CommandBox documentation
- [ortussolutions/commandbox](https://hub.docker.com/r/ortussolutions/commandbox), Docker Hub
- [ColdFusion package manager](https://helpx.adobe.com/coldfusion/using/coldfusion-package-manager.html), Adobe
  ColdFusion documentation
- [Containers for CFML](../../../07-consulting/coldfusion/08-cloud-containers-and-devops.md#containers-for-cfml), in
  the Senior ColdFusion Consultant roadmap

**Level:** Advanced · Core

## CI/CD pipelines

A continuous integration and continuous delivery (CI/CD) pipeline runs the checks, builds the image and deploys it
on every change, so releases are routine.

**What to learn:**

- Starting a CommandBox server in continuous integration, and running the format check, TestBox and the Hurl tests
  against it
- Building and tagging the image, and deploying it to a test environment
- Rolling back to the previous image when a release fails

**Resources:**

- [CI/CD for CFML](../../../07-consulting/coldfusion/08-cloud-containers-and-devops.md#cicd-for-cfml), in the Senior
  ColdFusion Consultant roadmap
- [Git workflow](../../../../standards/git/git-workflow.md), Techversant

**Level:** Advanced · Core

## Production database migrations

A migration that locks a large table or drops a column too early can take a production system down. Production
migrations are Red Zone work: plan them by hand, and have a senior engineer review them.

**What to learn:**

- Expand and contract: add the new column, move the data, switch the code, then remove the old column in a later
  release
- Taking a backup, testing the migration on a copy of production data, and writing the rollback
- Running migrations as a separate step in the pipeline, not when the application starts

**Resources:**
[Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
Era Coding Guidelines

**Level:** Advanced · Core

## Lucee and Adobe ColdFusion compatibility

Client applications run on both engines, and many move from one to the other. Code that works on Lucee can fail on
Adobe ColdFusion, and the reverse.

**What to learn:**

- Running the same tests on both engines with CommandBox, such as `cfengine=adobe@2025`
- Common differences: JSON key case and types, null handling, how unscoped names are looked up, built-in functions
  one engine lacks, and settings in `Application.cfc`
- Recording the differences you find and how the code handles each

**Resources:**

- [Multi-engine support](https://commandbox.ortusbooks.com/embedded-server/multi-engine-support), CommandBox
  documentation
- [Compatibility testing](../../../07-consulting/coldfusion/07-upgrades-and-migration.md#compatibility-testing), in
  the Senior ColdFusion Consultant roadmap

**Level:** Advanced · Core

## Health checks and monitoring

You need to know the API is down before your users tell you.

**What to learn:**

- A health check endpoint that checks the database, used by the load balancer or container platform
- JSON logs to standard output, and alerts on error rates and slow responses
- Watching the engine's memory and request threads, and taking a thread dump when requests hang

**Resources:**

- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection), in the
  Techversant security audit reference
- [Application monitoring](../../../07-consulting/coldfusion/02-jvm-performance-and-diagnostics.md#application-monitoring),
  in the Senior ColdFusion Consultant roadmap

**Level:** Advanced · Core

## Project: Make It Production-Ready on Both Engines

**Brief:** Package your RealWorld API as a Docker image with the scheduler running, and build a pipeline that checks,
builds and deploys it to a test environment. Run the full test suite once on Adobe ColdFusion 2025 and fix or record
every difference. Write a production migration plan for one schema change, and have a senior engineer review it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The image pins the engine and Java versions, runs as a user that is not root, and contains no secrets
- [ ] The build context excludes the Stage 08 archive lab. The reviewer inspects the built image and verifies that
  neither version of `archive.cfm` is present.
- [ ] Engine settings come from CFConfig and environment variables, with debugging output and the Robust Exception
  Information setting off
- [ ] The pipeline runs the format check, the TestBox tests and the RealWorld Hurl tests, then builds and
  deploys the image
- [ ] The health check reports healthy, and fails when the database is unreachable
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] The TestBox and Hurl tests pass on Adobe ColdFusion 2025, and the README lists each engine difference found and
  how the code handles it
- [ ] A migration plan for adding a required column to `articles` shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
