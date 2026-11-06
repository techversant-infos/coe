# 09. Modernization and Migration

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Many Techversant clients run older systems that still earn money. Replacing or moving them is high-risk work, and
the architect plans it so the business keeps running throughout. Back to the [roadmap](./README.md).

## Assessing legacy systems

Before recommending anything, find out what the system really does, what state it is in and what depends on it.

**What to learn:**

- Mapping the code, data, integrations and people who know the system
- Scoring technical debt and risk, so findings can be compared and ranked
- Writing an assessment the client's managers can act on

**Resources:**

- [Legacy Assessment Template](../07-consulting/coldfusion/deliverables/legacy-assessment-template.md) and
  [Assessing Legacy Applications](../07-consulting/coldfusion/05-assessing-legacy-applications.md), from the
  Techversant ColdFusion consulting track. The method applies to any stack.

**Level:** Advanced · Core

## Choosing a modernization path

The options run from leaving the system alone, through upgrading or moving it, to replacing it completely. The right
one depends on the business, not on the technology alone.

**What to learn:**

- The common options and what each costs, risks and delivers
- Comparing options with the client on value, risk and total cost of ownership
- Recognising when the best advice is not to modernize yet

**Resources:**

- [ColdFusion Modernization Framework](../07-consulting/coldfusion/deliverables/cf-modernization-framework.md) and
  [Modernization Strategy](../07-consulting/coldfusion/06-modernization-strategy.md), from the Techversant ColdFusion
  consulting track

**Level:** Advanced · Core

## Strangler fig

The strangler fig pattern replaces a system piece by piece. New features go into the new system, old features move
across one at a time, and a routing layer sends each request to the right place until the old system can be
switched off.

**What to learn:**

- Choosing the first piece to move: valuable, low-risk and loosely connected
- Routing traffic between the old and new systems, and keeping old links working
- Knowing when the old system can finally be retired

**Resources:**

- [Strangler fig application](https://martinfowler.com/bliki/StranglerFigApplication.html), Martin Fowler
- [Patterns of legacy displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), Ian
  Cartwright, Rob Horn and James Lewis

**Level:** Advanced · Core

## Data migration

Moving data is often the riskiest part of a migration. Old data is rarely as clean as the documentation says.

**What to learn:**

- Mapping old fields to new ones, and deciding what to do with data that does not fit
- Running the migration repeatedly in rehearsal, with automated checks that compare record counts and samples
- Moving data that keeps changing while the old system is still live

**Resources:** learn on projects, with an architect.

**Level:** Advanced · Core

## Cutover and rollback

Cutover is the moment users move to the new system. Plan it so that, if something goes wrong, you can go back
quickly and without losing data.

**What to learn:**

- A cutover plan with steps, owners, timings and go or no-go checks
- A rollback plan that has been tested, not just written
- Communicating the cutover to users and the client's support team

**Resources:**

- [Cutover and rollback](../07-consulting/coldfusion/07-upgrades-and-migration.md#cutover-and-rollback), in the
  Techversant ColdFusion consulting track
- [Rollback and database script management](../../standards/git/git-workflow.md#-rollback--database-script-management),
  in the Techversant Git workflow

**Level:** Advanced · Core

## Project: Plan the Legacy Blog Migration

**Brief:** Lantern's ten years of articles and comments live in its old ColdFusion blog, the
[BlogCFC5 practice app](../07-consulting/coldfusion/reference/practice-app-blogcfc5.md). Assess it, plan how its
content moves into the new system with old links still working, and rehearse the data migration.

**Size:** 4–5 days

**Verification**, checked by an architect or lead:

- [ ] A short assessment of BlogCFC5, using the Techversant legacy assessment template, lists its content, data,
  links and risks
- [ ] An ADR chooses between a one-time move and a strangler fig migration, with at least two options compared
- [ ] A field mapping shows how BlogCFC5 entries, categories and comments map to RealWorld articles, tags and
  comments, and what happens to data that does not fit
- [ ] A migration script moves a sample of at least 100 entries with their comments, and automated checks compare
  counts and spot-check content against the source
- [ ] The design keeps old BlogCFC5 article links working, for example with permanent redirects, and a test proves it
  for a sample of links
- [ ] A cutover plan has steps, owners, go or no-go checks and a tested rollback

Previous: [08. AI-Enabled Systems](./08-ai-enabled-systems.md) · Next:
[10. Architecture Practice](./10-architecture-practice.md)
