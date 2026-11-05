# Forward Deployed Engineer Roadmap

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

A Forward Deployed Engineer (FDE) works with a client's team and takes a real problem all the way to working
software in production. FDEs write code, build AI features, connect systems they did not build, and work directly
with the client's people.

- **Who it is for:** developers, QA automation engineers, consultants and AI engineers who want to work directly
  with clients.
- **Before you start:** some client project experience. Stage 01 is the
  [Engineering Foundations](../00-engineering-foundations/README.md) course; if you have completed it, show the
  evidence and move on.
- **What you do:** nine stages, each with a short guide to every topic and one hands-on project.

## Why It Matters Now

- **The role started at Palantir.** Until around 2016, Palantir had more FDEs than regular software engineers.
  AI companies such as OpenAI now hire FDEs to get their products working inside customer organisations
  ([The Pragmatic Engineer, 2025][pragmatic]).
- **Demand has grown fast.** Job postings titled "forward deployed engineer" rose 1,165% from January to October 2025,
  compared with the same months of 2024 ([Bloomberry][bloomberry]).
- **India is following.** FDE postings in India on Indeed rose 1,807% year on year in June 2026, nearly 19 times the
  June 2025 level, then eased to about 16 times in July and 6 times in August. Roles were listed in Bengaluru,
  Hyderabad, Chennai, New Delhi, Mumbai and as remote jobs ([Indeed, reported by PTI][indeed]).
- **Enterprises expect more by 2030.** In a survey of 200 Indian enterprises, 88% expect their demand for FDEs to
  grow by 2030, while only 1% of the 1,000 engineers surveyed work in an FDE role today ([Scaler and CMR,
  2026][scaler]).
- **Deployment is the gap.** In the same survey, 77% of enterprises prioritise production deployment skills, but the
  report puts talent availability at just 19% ([Scaler and CMR, 2026][scaler]).

> **Read the numbers with care.** Job-posting counts include re-posted and unfilled jobs, and Scaler sells FDE
> training. We found no forecast from an independent analyst firm. The direction is clear across all the sources;
> the exact figures are not.

## What an FDE Does

The most common duties in FDE job postings are working directly with customers (55%), building and deploying AI
systems (37%) and integrating systems and APIs (32%) ([Bloomberry][bloomberry]). In practice, an engagement runs like
this:

1. Find the real problem behind the client's request.
2. Agree a measurable result and a short time box.
3. Map the client's systems and data, and get access.
4. Build a prototype that tests the riskiest assumption first.
5. Build the production version and prove it works with evaluations.
6. Deploy it through the client's own change process, then run it.
7. Hand it over so the client's team can run it without you.
8. Feed what you learned back into reusable components and CoE standards.

## How the Role Differs

| Role | Difference from an FDE |
|------|------------------------|
| Consultant | Gives recommendations, often one-off. An FDE builds and ships, and usually stays with the client for longer. |
| Solutions architect | At OpenAI, usually builds proofs of concept on anonymised or offline data. An FDE writes production code on the client's own systems. |
| Feature developer | Works from a defined backlog. An FDE helps define the backlog, then builds it. |
| AI engineer | Builds AI features, usually for one product. An FDE builds them inside someone else's environment, under their rules. |

The first two rows follow [The Pragmatic Engineer][pragmatic]. The same article notes that FDEs at product companies
also feed what they learn back into the core product. At Techversant, that means reusable components and CoE
standards.

## FDE Levels

| Level | What the FDE does | Evidence |
|-------|-------------------|----------|
| Practitioner | Delivers parts of an engagement, with a lead reviewing the key decisions | All stage projects verified, plus shipped work on a real engagement |
| Advanced (FDE Lead) | Leads an engagement end to end: scope, build, production, handover | An engagement record: scope, evaluation results, handover, client feedback |
| Expert | Turns field work into reusable patterns and standards, and coaches other FDEs | Patterns used by other engagements; people coached |

The levels follow the academy's [learning levels](../learning-levels/README.md). FDE is rarely a first job: of the
postings that state experience, 60% ask for three to five years and only 12% are entry-level roles asking for two
years or less ([Bloomberry][bloomberry]).

Each topic's level is the depth expected of an FDE Lead. For Practitioner, the projects plus your real engagement
work should show working knowledge of every core topic.

## From Your Role to FDE

| You are now | You probably have | Focus on |
|-------------|-------------------|----------|
| Full-stack developer | Stage 01 and most of 02 | [03 Data](./03-data.md), [04 Applied AI](./04-applied-ai.md), [09 Client Delivery](./09-client-delivery.md) |
| Consultant | Stages 06, 09 | [02 Full-Stack Delivery](./02-full-stack-delivery.md), [04 Applied AI](./04-applied-ai.md), [08 Production and Security](./08-production-and-security.md) |
| AI engineer | Stages 04–05 | [06 Integration Engineering](./06-integration-engineering.md), [07 Cloud and Operations](./07-cloud-and-operations.md), [09 Client Delivery](./09-client-delivery.md) |
| QA automation engineer | Stage 01, part of 02 | [02 Full-Stack Delivery](./02-full-stack-delivery.md), [04 Applied AI](./04-applied-ai.md), [09 Client Delivery](./09-client-delivery.md) |

## The Roadmap

![Forward Deployed Engineer roadmap: nine stages from Engineering Foundations to Client Delivery, each with its topics](./roadmap.svg)

- Work from top to bottom. Each stage page explains every topic and ends with a project.
- **Solid boxes** are core topics. **Dashed boxes** are optional and depend on the client.
- A **tick** marks a Techversant guide: a standard, checklist or academy path that covers the topic. The other
  topics link to official documentation, or are learned on engagements with a lead.

## Stages and Projects

Each project has a verification checklist. A reviewer, senior engineer or lead checks every item before the project
counts.

| Stage | Project |
|-------|---------|
| [01. Engineering Foundations](./01-engineering-foundations.md) | [Show your Foundations evidence](./01-engineering-foundations.md#project-show-your-foundations-evidence) |
| [02. Full-Stack Delivery](./02-full-stack-delivery.md) | [Build a service request tracker](./02-full-stack-delivery.md#project-build-a-service-request-tracker) |
| [03. Data](./03-data.md) | [Audit a real public dataset](./03-data.md#project-audit-a-real-public-dataset) |
| [04. Applied AI](./04-applied-ai.md) | [Build a standards assistant and prove it works](./04-applied-ai.md#project-build-a-standards-assistant-and-prove-it-works) |
| [05. AI-Assisted Delivery](./05-ai-assisted-delivery.md) | [Deliver a feature with a coding agent, safely](./05-ai-assisted-delivery.md#project-deliver-a-feature-with-a-coding-agent-safely) |
| [06. Integration Engineering](./06-integration-engineering.md) | [Connect the assistant to a ticketing workflow](./06-integration-engineering.md#project-connect-the-assistant-to-a-ticketing-workflow) |
| [07. Cloud and Operations](./07-cloud-and-operations.md) | [Deploy, break and recover](./07-cloud-and-operations.md#project-deploy-break-and-recover) |
| [08. Production and Security](./08-production-and-security.md) | [Harden the assistant for production](./08-production-and-security.md#project-harden-the-assistant-for-production) |
| [09. Client Delivery](./09-client-delivery.md) | [Run a mock engagement](./09-client-delivery.md#project-run-a-mock-engagement) |

The projects build on each other. The tracker from stage 02 is extended in stages 05 and 06 and deployed in stage 07. The
assistant from stage 04 is connected, deployed and hardened in stages 06–08. Both are used in the mock engagement.

## Capstone

The nine verified projects form your capstone portfolio. Present it to your lead in one hour:

1. Demo the deployed assistant working on a ticket, end to end.
2. Show the evaluation report and explain one failure and how you handled it.
3. Walk through the mock engagement: the scope, the result against the agreed measure and the handover.
4. Explain one thing you rejected from an AI tool and why.

Your lead signs off the capstone when every verification item is checked and all four parts are covered. Together
with shipped work on a real engagement, this is the evidence for the Practitioner level.

## How to Use It

1. Find your row in [From Your Role to FDE](#from-your-role-to-fde).
2. Rate yourself on each topic: 0 not started, 1 aware, 2 can do it with help, 3 can do it alone.
3. Agree two or three gaps with your lead, and close them on real work where possible.
4. Complete the projects for the stages you are working on.
5. Review your ratings with your lead every quarter.

## Glossary

| Term | Meaning |
|------|---------|
| Engagement | A time-boxed piece of client work with an agreed outcome |
| Discovery | Finding out what the client's problem really is, who has it and what it costs them |
| Time to value | How long until the client sees a measurable benefit |
| Evaluation set | Real examples with expected results, used to measure whether an AI feature works |
| Day 2 operations | Industry term for running a system after launch. See [Incidents and maintenance](./07-cloud-and-operations.md#incidents-and-maintenance). |
| UAT | User acceptance testing: the client's users confirm the solution does the job |
| Handover | Transferring ownership so the client's team can run, change and roll back the solution |
| Red Zone | Work Techversant never delegates to AI. See [section 2.2 of the AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only). |

## Sources

- The Pragmatic Engineer, Gergely Orosz, ["What are Forward Deployed Engineers, and why are they so in demand?"][pragmatic],
  12 August 2025
- Bloomberry, Henley Wing Chiu, ["What I learned analyzing 1K forward deployed engineer jobs"][bloomberry], last
  updated 25 January 2026. About 1,000 postings supplied by Revealera, with salaries quoted in US dollars.
- PTI, reported by People Matters, ["Demand for forward deployed engineers jumps 19-fold in India: Report"][indeed],
  15 October 2026. Indeed job-posting data for India.
- Scaler and CyberMedia Research, ["India's FDE Opportunity" report][scaler], October 2026. A survey of 1,000 software
  engineers and 200 enterprise technology decision-makers in India.

[pragmatic]: https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers
[bloomberry]: https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/
[indeed]: https://www.peoplematters.in/news/workforce-planning/demand-for-forward-deployed-engineers-jumps-19-fold-in-india-report-52770
[scaler]: https://www.scaler.com/blog/forward-deployed-engineering-indias-next-%E2%82%B91-crore-salary-opportunity-scaler-x-cmr-report/
