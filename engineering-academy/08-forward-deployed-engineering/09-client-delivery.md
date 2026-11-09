# 09. Client Delivery

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

These skills decide whether good engineering turns into a result the client values. Most of the existing Techversant
material sits in the ColdFusion consulting track, but the skills apply to any stack. Back to the [roadmap](./README.md).

## Discovery

Find the real problem behind the request before building anything.

**What to learn:**

- Interviewing the people who have the problem, not only the sponsor
- Watching the work being done
- Asking the questions that change the design, and writing down the answers

**Resources:** [Discovery Workshop Questionnaire](../07-consulting/coldfusion/deliverables/discovery-workshop-questionnaire.md)

**Level:** Practitioner · Core

## Domain learning

Learn enough about the client's industry and workflow to make sound delivery decisions. The client remains the source
of truth for domain rules; confirm assumptions with the people who do and govern the work.

**What to learn:**

- Mapping the workflow, roles, terminology, exceptions and systems involved
- Identifying domain rules, regulations and consequences of errors that affect design or rollout
- Recording which assumptions were confirmed, which remain uncertain and who can resolve them
- Explaining how domain learning changed a requirement, evaluation case or technical decision

**Resources:** learn on engagements, with a lead and the client's domain experts. Use the relevant security, privacy
and architecture standards for the client's sector.

**Level:** Practitioner · Core

## Scoping and estimation

Agree what success looks like and what is out of scope before you start.

**What to learn:**

- A measurable result with a baseline, for example "reply time from 4 hours to 30 minutes"
- What is out of scope, written down
- Estimates as ranges, and small first releases

**Resources:**

- [Estimation templates](../07-consulting/coldfusion/deliverables/estimation-templates/README.md)
- [Estimation prompts](../../ai/prompts/section-04-estimation.md)

**Level:** Practitioner · Core

## Stakeholder management

Different people at the client want different things. Know who decides, who is affected and who can block.

**What to learn:**

- Mapping stakeholders and what each one cares about
- Managing expectations and saying no to extra scope
- Escalating early when something is at risk

**Resources:** [Client Communication Guide](../07-consulting/coldfusion/deliverables/client-communication-guide.md)

**Level:** Practitioner · Core

## Status updates and technical writing

Short, regular, honest writing keeps the client informed and leaves a record for whoever comes next.

**What to learn:**

- Weekly status updates: done, next, risks, decisions needed
- Decision records and handover notes
- Sharing bad news early, with options

**Resources:** [Communication and Ownership](../00-engineering-foundations/10-communication-and-ownership.md)

**Level:** Foundation · Core

## Demos and executive reporting

Show progress on the client's terms: their data, their workflow, their success measure.

**What to learn:**

- Short demos that show working software, not slides
- Reporting results against the agreed measure, including what did not work
- Adjusting the message for executives, managers and users

**Resources:** [Client Communication Guide: explaining technical findings](../07-consulting/coldfusion/deliverables/client-communication-guide.md#explaining-technical-findings)

**Level:** Practitioner · Core

## ROI and time to value

Return on investment (ROI) and time to value are how the client judges the engagement.

**What to learn:**

- How the client's business makes and spends money
- Estimating the value of a change in time or money saved
- Choosing a first release that shows value early

**Resources:** learn on engagements, with a lead.

**Level:** Advanced · Optional

## User acceptance testing and handover

The client's users confirm the solution works, then the client's team takes ownership.

**What to learn:**

- Planning user acceptance testing (UAT) with real users and real cases
- Runbooks, training and documentation for the client's team
- Agreeing when the engagement is finished and what support follows

**Resources:** [Handoff note structure](../00-engineering-foundations/10-communication-and-ownership.md#handoff-notes).
Techversant has no user acceptance testing guide yet, so agree the test plan with the client in the scope.

**Level:** Practitioner · Core

## Reusable components and field notes

Each engagement should leave Techversant better prepared for the next one.

**What to learn:**

- Turning one-off code into reusable components where it is worth it
- Writing short field notes: what worked, what did not, what to reuse
- Removing every client-confidential detail before sharing

**Resources:** learn on engagements, with a lead. Propose changes to CoE standards through a pull request.

**Level:** Advanced · Optional

## Project: Run a Mock Engagement

**Brief:** A senior colleague plays a client who says "we want AI to help our support team". Run a two-week,
part-time engagement using what you built in the earlier projects.

**Size:** 2 weeks part-time

**Verification**, checked by the colleague playing the client and your lead:

- [ ] Discovery notes from at least two stakeholder interviews, with the real problem stated in one sentence
- [ ] A domain brief records the workflow, roles, key terms, exceptions, governing constraints and open assumptions; a client-side domain expert reviews it
- [ ] The brief identifies one design or evaluation decision changed by domain learning, with the evidence and reviewer recorded
- [ ] A one-page scope: a measurable result with a baseline, an out-of-scope list and an estimate as a range, agreed
  in writing by the "client"
- [ ] Weekly status updates covering done, next, risks and decisions needed
- [ ] A ten-minute demo that reports results against the agreed measure, including what did not work
- [ ] User acceptance testing with at least two people acting as users; every issue is fixed or accepted
- [ ] Someone who did not build the solution runs, monitors and rolls it back using only your handover pack
- [ ] A field note with lessons and reusable parts, and a reviewer confirms it holds no confidential detail

Previous: [08. Production and Security](./08-production-and-security.md) · Back to the [roadmap](./README.md)
