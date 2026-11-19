# FDE Readiness Assessment

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-19 · **Next review:** 2027-02-19

Use this assessment with the [Forward Deployed Engineer (FDE) roadmap](./README.md) to answer three questions:

1. Are you ready to start on the FDE path now?
2. Which stages can you move through quickly, and which need the most work?
3. Roughly how long will the roadmap projects take you, and what else do you need for FDE Practitioner?

It takes about 45 minutes on your own and 30 minutes with your lead. Keep your completed copy in your personal
development record, not in this repository, because it holds information about you.

## How It Works

1. Complete the [entry checks](#part-1-entry-checks). They show whether to start the roadmap now or build
   foundations first.
2. Rate yourself on the [skills](#part-2-skills) for each stage, and link evidence for every 2 or 3.
3. Tick the [ways of working](#part-3-ways-of-working) you can show with a real example.
4. Meet your lead. Your lead checks your evidence, adds their own rating, and you agree the result together.
5. Use the [result tables](#part-4-reading-your-result) to set your starting stage and a time estimate, then write
   your [gap plan](#part-5-your-gap-plan).
6. Repeat the skills rating with your lead every quarter, or sooner when your work changes.

## The Rating Scale

| Score | Meaning | Evidence needed |
|-------|---------|-----------------|
| 0 | Not started: you have not done this | None |
| 1 | Aware: you understand it, or have followed a tutorial or watched someone do it | None |
| 2 | With help: you have done it on real work, with someone reviewing the key decisions | One link |
| 3 | On your own: you have done it on real work without help, and can explain the trade-offs | One link |

Evidence is anything your lead can open: a pull request, a design note, a runbook, a demo recording or a project
from the roadmap. A 2 or 3 without evidence counts as 1. Rate what you have done, not what you could probably do.

## Part 1: Entry Checks

The FDE path is for engineers who already build and ship software. Tick each check you can support with evidence.
These five checks are the only entry checks; the [entry diagnostic](./README.md#entry-diagnostic) on the roadmap page
uses the same list.

- [ ] **Programming and debugging:** I can make and explain a small change in an unfamiliar code base without a
  walkthrough
- [ ] **Git, tests and code review:** I have submitted tested changes through pull requests and acted on review
  comments
- [ ] **APIs and data:** I have built or extended an application programming interface (API) and written SQL against
  a relational database
- [ ] **Production delivery:** I have helped deploy, monitor or fix a service that real users depend on
- [ ] **Client work:** I have taken part in a client project, such as joining client meetings, giving a demo or
  answering the client's questions

Accepted equivalents:

- **Production delivery:** work on an internal Techversant service that staff depend on counts. Following a tutorial
  or deploying a personal project does not.
- **Client work:** an internal project counts when you worked directly with a stakeholder outside your team, such as
  a product owner from another department, on scope, demos and feedback.

Your [readiness result](#readiness) depends on which checks you tick.

## Part 2: Skills

Rate each statement from 0 to 3, then work out each stage's score: add the scores and divide by the number of
statements. Leave the Lead column for your lead.

### Stage 01: Engineering Foundations

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Work with branches and pull requests following the Techversant Git workflow | | | |
| Write tests for my changes, and review other people's code | | | |
| Keep secrets out of code and validate input, following the security checklist | | | |
| Review every line of output from an AI tool before I commit it | | | |

### Stage 02: Full-Stack Delivery

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Build an API in TypeScript or Python, with validation and clear errors | | | |
| Build a web front end, such as in React or Next.js, that uses an API | | | |
| Design a PostgreSQL schema change and write a safe migration for it | | | |
| Sketch a system design for a new feature and explain the trade-offs | | | |

### Stage 03: Data

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Read an unfamiliar database schema and explain how the tables relate | | | |
| Check data for gaps, duplicates and inconsistencies before I use it | | | |
| Write SQL with joins, grouping and window functions to answer a business question | | | |
| Classify data, including personal data, and handle each class as the rules require | | | |

### Stage 04: Applied AI

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Explain how a large language model (LLM) works, including context windows and why it makes things up | | | |
| Write and test the prompt and context for a task, and improve them using failures | | | |
| Choose a model and provider for a task, weighing quality, cost, speed and the data rules | | | |
| Build retrieval over a set of documents, so a model answers from them | | | |
| Give a model tools to call, such as through the Model Context Protocol (MCP) | | | |
| Build an evaluation set and use it to measure whether an AI feature works | | | |

### Stage 05: AI-Assisted Delivery

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Use a coding agent on real work and review its output line by line | | | |
| Choose a delegation level for each task, and keep Red Zone work out of AI tools | | | |
| Set agent rules, permissions and continuous integration (CI) checks for a repository | | | |

### Stage 06: Integration Engineering

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Change a legacy system I did not build without breaking it | | | |
| Choose between a direct API call, a webhook, a queue and a batch job, and explain why | | | |
| Connect a solution to a client's single sign-on (SSO), with a senior engineer reviewing the work | | | |
| Connect to email, ticketing or enterprise resource planning (ERP) systems through their APIs | | | |
| Get system access and release approval through a client's own process | | | |

### Stage 07: Cloud and Operations

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Use the Linux shell to find out why a service is failing | | | |
| Deploy a containerised service on one cloud platform | | | |
| Build a CI and continuous delivery (CD) pipeline that tests and deploys a service | | | |
| Set up logs, metrics and alerts, and respond to an incident | | | |

### Stage 08: Production and Security

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Run evaluations of an AI feature in CI and in production | | | |
| Add guardrails and fallbacks, so an AI feature fails safely | | | |
| Measure and control the cost and response time of an AI feature | | | |
| Check an application against the OWASP (Open Worldwide Application Security Project) Top 10 for web and for LLM applications | | | |
| Explain what data protection law and the client's contract allow us to do with personal data | | | |

### Stage 09: Client Delivery

| I can… | Me | Evidence | Lead |
|--------|----|----------|------|
| Run discovery to find the real problem behind a client's request | | | |
| Learn a client's domain: map the workflow, terms and rules, and confirm assumptions with domain experts | | | |
| Scope and estimate a time-boxed piece of work, and agree how success is measured | | | |
| Keep stakeholders informed with clear written status updates | | | |
| Demo work to a non-technical audience and tie it to the business result | | | |
| Run user acceptance testing (UAT) and hand a solution over so the client's team can run it | | | |

## Part 3: Ways of Working

These habits are what most separate an FDE from an engineer who builds from an agreed backlog. Tick each one you can
show with a real example from your work, and be ready to describe it to your lead.

- [ ] Turned an unclear request into a written scope that the client or product owner agreed
- [ ] Explained a technical risk or trade-off to a non-technical person and got a decision
- [ ] Pushed back on a request and offered a better alternative
- [ ] Owned a piece of work through release and afterwards, such as fixing a production problem
- [ ] Learned a new business area quickly enough to make sound decisions in it
- [ ] Worked within someone else's rules, tools and approval process
- [ ] Delivered something useful within a short time box, instead of waiting for a complete solution
- [ ] Written documentation or a handover that let someone else run my work

Also discuss with your lead what FDE engagements can involve, such as working in the client's hours, visiting the
client's site and travelling. These are not scored; they help you both plan.

## Part 4: Reading Your Result

Use your lead's ratings where the two differ, and talk through any difference of more than one point.

### Readiness

Go down the table and stop at the first row that applies. Every combination of entry checks and ways of working
matches exactly one row.

| Order | Result | When it applies | Next step |
|-------|--------|-----------------|-----------|
| 1 | Build foundations first | Programming and debugging, Git, tests and code review, or APIs and data is not ticked | Follow the route for each missing check in the [entry diagnostic](./README.md#entry-diagnostic), then retake this assessment |
| 2 | Start with a plan | Production delivery or client work is not ticked, or you ticked fewer than five ways of working | Start the roadmap, and follow the route below for each gap |
| 3 | Ready to start | All five entry checks, and at least five ways of working | Start the roadmap at your first stage marked Partly or New |

Routes for **Start with a plan**:

- **Production delivery not ticked:** take the stages in order. During stages 07 and 08, your lead pairs you with an
  engineer who runs a production service, and you shadow at least one release and one incident review before you
  own a client deployment.
- **Client work not ticked:** pair with an experienced FDE on an engagement, in a supporting role, before you take
  independent client ownership.
- **Fewer than five ways of working:** agree with your lead which habits to build first, and practise them on your
  current work and in the stage 09 mock engagement.

### Stage status

Each stage's score gives the same labels as [Where You Start](./README.md#where-you-start) on the roadmap page.

| Stage score | Status | What to do |
|-------------|--------|------------|
| 2.5 or more, and no statement below 2 | Already do | Show your lead evidence for each check in the stage project, then move on |
| 1.5 or more, when Already do does not apply | Partly | Read the stage page, learn the topics you scored low, and complete the project |
| Below 1.5 | New | Work through the whole stage, then complete the project |

The average is for planning. A single statement below 2 is a gap your lead should see, so the stage cannot count as
Already do even when its average is high.

Already do lets you skip the learning, not the project result that a later stage builds on. If you test out of stage
02, 04, 06 or 07, you still need its result for the later stages; see
[Project Dependencies](./README.md#project-dependencies).

### Time estimate

The table gives focused working days for each stage, based on the size of each stage project. Partly uses the upper
end of the project size; New allows the same again for learning.

| Stage | Project size | Already do | Partly | New |
|-------|--------------|------------|--------|-----|
| [01. Engineering Foundations](./01-engineering-foundations.md) | 1–2 hours | 0.5 | 3 | Complete [Engineering Foundations](../00-engineering-foundations/README.md) first |
| [02. Full-Stack Delivery](./02-full-stack-delivery.md) | 4–6 days | 0.5 | 6 | 12 |
| [03. Data](./03-data.md) | 2–3 days | 0.5 | 3 | 6 |
| [04. Applied AI](./04-applied-ai.md) | 4–5 days | 0.5 | 5 | 10 |
| [05. AI-Assisted Delivery](./05-ai-assisted-delivery.md) | 1–2 days | 0.5 | 2 | 4 |
| [06. Integration Engineering](./06-integration-engineering.md) | 4–5 days | 0.5 | 5 | 10 |
| [07. Cloud and Operations](./07-cloud-and-operations.md) | 3–4 days | 0.5 | 4 | 8 |
| [08. Production and Security](./08-production-and-security.md) | 3–4 days | 0.5 | 4 | 8 |
| [09. Client Delivery](./09-client-delivery.md) | 2 weeks part-time | 0.5 | 5 | 10 |

If you test out of stage 02, 04, 06 or 07 and have no approved equivalent of its project result, plan the Partly
time for that stage.

To turn days into weeks, divide the total by the number of days a week you and your lead agree for learning. The
estimate covers the roadmap projects only. FDE Practitioner also needs a supervised placement on a real engagement
and a level sign-off, which depend on engagements being available; see
[Reaching FDE Practitioner](./README.md#reaching-fde-practitioner).

**Example:** a senior developer scores Already do for stage 01, New for stages 04 and 09, and Partly for the rest.
Stage 02 is Partly because later stages need the tracker. That is 0.5 + 6 + 3 + 10 + 2 + 5 + 4 + 4 + 10 = 44.5 days.
With two days a week for learning, the roadmap projects take about 22 weeks, or five months.

These numbers are for planning, not deadlines. Progression depends on evidence, not on time spent, so you can move
faster wherever real engagement work covers a stage.

## Part 5: Your Gap Plan

Agree two or three gaps with your lead, and close them on real work where you can. Copy this table into your
development record:

| Gap | Stage | How I will close it | Support I need | Target date |
|-----|-------|---------------------|----------------|-------------|
| Example: evaluations | 04 | Build the stage 04 project, then add an evaluation set to the assistant on my current project | An hour a week of review from an AI engineer | End of next quarter |
| | | | | |
| | | | | |

Also record:

- **Readiness result**, the routes you are following, and the date you agreed it
- **Starting stage** and **days a week** for learning
- **Time estimate** from Part 4
- **Next review date**, no more than three months away

Back to the [FDE roadmap](./README.md).
