# Module 9-05: Proposal Support

> Learn to write proposal content that wins projects.

## Overview

Proposals are where technical expertise meets business value. This module teaches developers to contribute effective proposal content — scope, architecture, risks, timeline, and technical assumptions.

> **Generic Foundation:** [General Proposals Guide (planned)](../../../../general/proposals/) — this module adds CF-specific proposal content and boilerplates.

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Write clear scope statements for CF engagements
- [ ] Describe technical architecture in proposal format
- [ ] Document technical assumptions and risks
- [ ] Contribute to timeline and milestone sections
- [ ] Write approach sections that demonstrate expertise
- [ ] Review proposals for technical accuracy
- [ ] Respond to proposal technical questions

## Proposal Structure for CF Engagements

### Section Overview

| Section | Purpose | Who Writes It |
|---------|---------|---------------|
| Executive Summary | High-level overview for executives | Proposal lead |
| Scope | What is and isn't included | Consultant (technical) |
| Approach | How we'll do the work | Consultant (technical) |
| Architecture | Technical design | Consultant (technical) |
| Timeline | Phases and milestones | Consultant (technical) |
| Risks | Identified risks and mitigations | Consultant (technical) |
| Team | Who will do the work | Manager |
| Pricing | Cost breakdown | Manager/Sales |

### Technical Sections Checklist

**Scope Statement:**
- [ ] Specific deliverables listed
- [ ] In-scope items clear
- [ ] Out-of-scope items explicit
- [ ] Success criteria defined
- [ ] Assumptions documented

**Approach Section:**
- [ ] Methodology described
- [ ] Tools and technologies specified
- [ ] Key phases outlined
- [ ] Review points identified
- [ ] Client involvement defined

**Architecture Section:**
- [ ] Current state described
- [ ] Proposed architecture explained
- [ ] Migration strategy outlined
- [ ] Integration points identified
- [ ] Security considerations addressed

**Timeline:**
- [ ] Phases with durations
- [ ] Milestones with dates
- [ ] Dependencies identified
- [ ] Client review points marked
- [ ] Buffer time included

**Risks:**
- [ ] Technical risks identified
- [ ] Business risks identified
- [ ] Mitigation strategies provided
- [ ] Contingency plans noted
- [ ] Risk ownership assigned

## CF-Specific Proposal Content

### Scope Statement Examples

**Good (Specific):**
> "Phase 1: ColdFusion Assessment
> - Conduct technical assessment of 150 CFM files across 3 modules
> - Document current architecture, dependencies, and technical debt
> - Identify security vulnerabilities using OWASP checklist
> - Produce prioritized recommendations report
> Deliverable: Technical Assessment Report with effort estimates"

**Bad (Vague):**
> "We will assess your ColdFusion application and provide recommendations."

### Approach Section Examples

**Migration Approach:**
> "Our migration approach follows a phased methodology:
>
> 1. **Discovery (Week 1):** Automated compatibility scan + manual review
> 2. **Pilot Migration (Week 2):** Migrate authentication module as proof-of-concept
> 3. **Core Migration (Weeks 3-6):** Migrate business logic components
> 4. **UI Modernization (Weeks 7-8):** Bootstrap integration with React components
> 5. **Testing & Deployment (Weeks 9-10):** UAT, performance testing, production deployment
>
> Each phase includes client review checkpoints to validate direction."

### Risk Register Examples

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| CF extensions not compatible with Lucee | Medium | High | Identify alternatives in discovery; pilot first |
| Database schema changes needed | Low | Medium | Include DB audit in discovery; estimate contingency |
| Downtime during deployment | Low | Medium | Blue-green deployment; weekend window |
| Discovery reveals more complexity | Medium | Medium | Flexible scope with change order process |
| Client unavailable for reviews | Medium | Low | Fixed review calendar; async review option |

### Timeline Examples

```
Week 1: Discovery & Assessment
├── Client interviews
├── Automated compatibility scan
├── Manual code review
└── Risk assessment

Week 2: Pilot Migration
├── Environment setup
├── Authentication module migration
└── UAT with client

Weeks 3-6: Core Migration
├── Business logic components
├── Database layer
├── API endpoints
└── Integration points

Weeks 7-8: UI Modernization
├── Bootstrap framework
├── Component conversion
└── Responsive testing

Weeks 9-10: Testing & Deployment
├── UAT support
├── Performance testing
├── Production deployment
└── Documentation & training

Buffer: 2 weeks (flexible)
Total: 12-14 weeks
```

## Boilerplate Content

### CF Assessment Scope

> The scope of this assessment includes:
>
> - **Code Review:** Up to [X] CFM files across [Y] application modules
> - **Architecture Documentation:** Current system architecture and data flow
> - **Dependency Mapping:** External integrations, APIs, and database connections
> - **Security Assessment:** OWASP Top 10 review with CF-specific focus
> - **Performance Review:** Identification of bottlenecks and optimization opportunities
> - **Technical Debt Analysis:** Scoring across maintainability, scalability, and security
>
> Out of scope:
> - Code changes or refactoring (separate engagement)
> - Third-party vendor negotiations
> - User training

### CF Migration Approach

> **Methodology:** Agile with 2-week sprints
>
> **Sprint Structure:**
> - Sprint planning (Monday)
> - Development (Tuesday-Thursday)
> - Testing (Thursday-Friday)
> - Review with client (Friday)
>
> **Tools:**
> - Source control: Git
> - CI/CD: [Jenkins/GitHub Actions/Azure DevOps]
> - Monitoring: [FusionReactor/Other]
> - Documentation: Confluence
> - Communication: Slack + weekly calls

### Technical Assumptions

> **Technical Assumptions:**
>
> - Client will provide development, staging, and production environments
> - Source code will be provided via Git repository with appropriate access
> - Database backups will be available before major changes
> - Client IT will configure firewall/network access as needed
> - Estimated [X] hours of client participation per week for reviews and testing
>
> **Known Unknowns:**
>
> - Third-party API authentication methods require discovery
> - Legacy integration documentation may be incomplete
> - User acceptance testing timeline depends on client availability

## Proposal Review Checklist

Before submitting any proposal:

- [ ] Scope is specific and measurable
- [ ] Assumptions are documented
- [ ] Risks are identified with mitigations
- [ ] Timeline is realistic with buffer
- [ ] Pricing aligns with scope
- [ ] No technical errors or contradictions
- [ ] Format is consistent and professional
- [ ] Client-specific context incorporated

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Scope Statement](./exercises/exercise-1.md) | Write clear scope for CF assessment | Specific, measurable scope |
| [Exercise 2: Approach Section](./exercises/exercise-2.md) | Write approach for migration engagement | Clear methodology |
| [Exercise 3: Risk Register](./exercises/exercise-3.md) | Identify risks for CF migration | Complete risk register |
| [Exercise 4: Full Proposal Review](./exercises/exercise-4.md) | Review and improve sample proposal | Annotated proposal |

## Assessment

Complete all exercises and pass the module assessment with 70% or higher.

## Resources

- [General Proposals Guide](../../../../general/proposals/)
- [Proposal Boilerplates](../../DELIVERABLES/proposal-boilerplates/)
- [CF Estimation Templates](../../DELIVERABLES/estimation-templates/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 3 |
| Exercises | 4 |
| Assessment | 1 |
| **Total** | **8 hours** |

## Success Criteria

A developer completing this module should be able to:

1. Write scope statements that are specific and measurable
2. Document approach with clear phases and milestones
3. Identify and mitigate technical risks
4. Review proposals for technical accuracy

## Phase Completion

After completing all 5 modules (9-01 through 9-05), you have completed Phase 9: Client Consulting Skills.

Proceed to the [Phase 9 Assessment](../assessment.md) to test all skills together.
