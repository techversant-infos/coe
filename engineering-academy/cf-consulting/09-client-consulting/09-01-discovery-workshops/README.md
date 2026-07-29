# Module 9-01: Discovery Workshops

> Learn to lead effective discovery sessions that uncover what clients really need.

## Overview

Discovery is where trust is built and projects are won. This module teaches developers to lead structured discovery workshops that surface requirements, constraints, and opportunities.

> **Generic Foundation:** Planned: General Requirements Gathering — this module adds CF-specific questions and scenarios.

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Plan and structure a 2-hour discovery workshop
- [ ] Lead whiteboarding and process mapping exercises
- [ ] Ask probing questions that uncover hidden requirements
- [ ] Facilitate architecture discussions
- [ ] Capture and document findings accurately
- [ ] Identify technical risks early
- [ ] Uncover business drivers and success criteria

## ColdFusion-Specific Discovery Questions

### Current Environment

| Question | Why It Matters |
|-----------|----------------|
| What version of ColdFusion are you running? | Determines upgrade/migration path |
| Is it Adobe ColdFusion or Lucee? | Affects licensing and compatibility |
| Are you using a framework? (FW/1, ColdBox, Fusebox?) | Shows modernization complexity |
| How many CF servers in the cluster? | Indicates scale and architecture |
| What's the database? (MSSQL, MySQL, Oracle?) | Integration considerations |
| Where is it hosted? (On-prem, AWS, Azure?) | Migration relevance |
| Do you have FusionReactor or similar monitoring? | Performance baseline |

### Pain Points

| Question | Follow-up |
|-----------|-----------|
| What breaks most often? | How often? What's the impact? |
| What takes longest to deploy? | Why? |
| Where do you feel stuck technically? | What have you tried? |
| What's the biggest user complaint? | How is it measured? |

### Modernization Interest

| Question | Why It Matters |
|-----------|----------------|
| Have you considered moving to Lucee? | Opens modernization conversation |
| Is cloud migration on your roadmap? | Cloud opportunity |
| Do you see AI helping any processes? | AI opportunity |
| What's your tolerance for downtime during changes? | Risk appetite |

## Workshop Structure

### Opening (15 min)

1. Welcome and introductions
2. Set the agenda
3. Establish ground rules (no wrong answers, etc.)
4. Confirm desired outcomes

### Current State (45 min)

1. Application overview (whiteboard)
2. Pain points and issues
3. Technical constraints
4. Integration dependencies

### Future Vision (30 min)

1. Business goals
2. Success criteria
3. Timeline expectations
4. Budget framework

### Solution Exploration (20 min)

1. Possible approaches
2. Trade-offs discussion
3. Risk identification
4. Questions and concerns

### Close (10 min)

1. Summarize findings
2. Confirm understanding
3. Next steps
4. Thank you

## ColdFusion Workshop Red Flags

Watch for these indicators:

| Red Flag | What It Signals |
|----------|----------------|
| CF 10 or earlier | Urgent upgrade needed |
| No monitoring in place | Performance blind spots |
| Single server, no cluster | Availability risk |
| Plain CFM with includes | High modernization effort |
| Custom authentication | Security risk |
| No CI/CD | Deployment risk |
| No test coverage | Technical debt |
| Third-party API dependencies on CF server | Integration complexity |

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Question Preparation](./exercises/exercise-1.md) | Prepare discovery questions for a scenario | Question list with rationale |
| [Exercise 2: Whiteboard Facilitation](./exercises/exercise-2.md) | Map an application architecture | Architecture diagram |
| [Exercise 3: Mock Discovery Session](./exercises/exercise-3.md) | Lead a 2-hour workshop | Recorded session with feedback |
| [Exercise 4: Finding Documentation](./exercises/exercise-4.md) | Document findings from a session | Professional discovery report |

## Assessment

Complete all exercises and pass the module assessment with 70% or higher.

## Resources

- Planned: General Workshop Guide
- [Discovery Workshop Questionnaire Template](../../DELIVERABLES/discovery-workshop-questionnaire.md)
- ColdFusion Discovery Questions — covered in [capstone exercises](../../../capstone/exercises/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 4 |
| Exercises | 4 |
| Assessment | 1 |
| **Total** | **9 hours** |

## Success Criteria

A developer completing this module should be able to:

1. Prepare a complete discovery question list in 30 minutes
2. Lead a 2-hour workshop without prompting
3. Identify 5+ technical risks from discovery
4. Produce a clear discovery report
