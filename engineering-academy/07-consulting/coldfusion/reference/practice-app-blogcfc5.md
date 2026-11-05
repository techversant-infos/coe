# Practice App: BlogCFC5

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

BlogCFC5 is a real, older ColdFusion blogging application. The projects in the
[Senior ColdFusion Consultant roadmap](../README.md) use it as a stand-in for a client system: you run it, assess it,
harden it, migrate it, containerize it and extend it.

## Why This App

- It is real legacy CFML, written over many years by several people, with the habits and problems you meet on client
  systems.
- It is small enough to understand in a few days, but has an admin area, comments, search, file downloads, email and
  RSS feeds.
- It is public, so you can practice without client data or access.

## Facts

Checked against the repository on 5 November 2026.

| Detail | Value |
|--------|-------|
| Repository | [teamcfadvance/BlogCFC5](https://github.com/teamcfadvance/BlogCFC5) |
| Created | January 2012, from Raymond Camden's earlier BlogCFC |
| Last commit | 31 March 2020 |
| License | No license file at the repository root, so GitHub shows none. `install/readme.md` carries an Apache License 2.0 notice from Raymond Camden, 2008–2012. |
| Database scripts | SQL Server, MySQL and Oracle scripts, plus a Microsoft Access database, in `install/` |
| Tests | Placeholder MXUnit and TestBox tests in `tests/` |

Use it for local practice only. Do not deploy it to a public server, and do not copy its code into client work.

## What Is in the Repository

| Folder | Contents |
|--------|----------|
| `client/` | The blog itself: public pages such as `index.cfm`, `search.cfm` and `contact.cfm`, plus `Application.cfc` |
| `client/admin/` | The admin area: entries, comments, users, settings and file manager |
| `client/org/camden/blog/` | The main components, such as `blog.cfc`, and the settings file `blog.ini.cfm` |
| `blogCFC6/` | A partly finished rewrite with separate components (`entry.cfc`, `user.cfc` and others) |
| `install/` | Database scripts and upgrade notes |
| `tests/` | Test runners and placeholder tests |

Do not trust this table, or any other document, as the full picture. Mapping the app yourself is part of the stage 04
project.

## Getting It Running

You need [CommandBox](https://commandbox.ortusbooks.com/) and a database. SQL Server Developer edition and MySQL are
both free for local use.

1. Clone the repository:

   ```bash
   git clone https://github.com/teamcfadvance/BlogCFC5.git
   cd BlogCFC5
   ```

2. Create an empty database and run the matching script from `install/`, for example `install/mysql.sql`.

3. Start a server from the repository folder. Pick the engine:

   ```bash
   # Lucee
   box server start cfengine=lucee@6.2 port=8500

   # Adobe ColdFusion 2025 (free Developer edition for local use)
   box server start cfengine=adobe@2025 port=8501
   ```

4. In the engine's administrator, add a datasource whose name matches `dsn` in `client/org/camden/blog/blog.ini.cfm`,
   and set `blogDBType` and `blogURL` in the same file.

5. Open `http://localhost:8500/client/` and record every error you see.

The app was written for much older engines, so expect errors on both. Each one is a finding for your projects, not a
setup mistake. In the stage 01 project you turn these steps into a `server.json` and a CFConfig file so one command
starts the app.

## How the Projects Use It

| Stage | Project |
|-------|---------|
| 01 | [Run the practice app on two engines](../01-cfml-and-the-platform.md#project-run-the-practice-app-on-two-engines) |
| 02 | [Find and fix a performance problem](../02-jvm-performance-and-diagnostics.md#project-find-and-fix-a-performance-problem) |
| 03 | [Review and harden the practice app](../03-security-and-hardening.md#project-review-and-harden-the-practice-app) |
| 04 | [Take over the practice app for maintenance](../04-maintaining-legacy-applications.md#project-take-over-the-practice-app-for-maintenance) |
| 05 | [Assess the practice app](../05-assessing-legacy-applications.md#project-assess-the-practice-app) |
| 06 | [Recommend a modernization path](../06-modernization-strategy.md#project-recommend-a-modernization-path), for Scenario 0 of the practice clients |
| 07 | [Migrate the practice app](../07-upgrades-and-migration.md#project-migrate-the-practice-app) |
| 08 | [Containerize and ship the practice app](../08-cloud-containers-and-devops.md#project-containerize-and-ship-the-practice-app) |
| 09 | [Add an API and an AI feature](../09-modernizing-the-application.md#project-add-an-api-and-an-ai-feature) |

Stage 06 uses Scenario 0 of the [practice clients](./practice-clients.md), which puts BlogCFC5 in a business setting.
Stage 10 can use any practice client.
