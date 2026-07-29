# Exercise 3: Risk and Assumption Documentation

> Practice documenting risks and assumptions for a proposal.

---

## Scenario

Write the risks and assumptions section for the BlogCFC5 modernization proposal.

---

## Risks Section Template

### Project Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Unknown dependencies | Medium | High | Discovery phase will identify |
| Compatibility issues | Medium | Medium | Buffer in compatibility phase |
| Third-party integration changes | Low | Medium | Document and test integrations early |
| Resource availability | Low | Medium | Backup resource identified |

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Custom authentication complexity | Medium | High | Use standard patterns |
| Database performance issues | Low | High | Performance testing in staging |
| Security vulnerabilities found | Medium | High | Security review in scope |

---

## Assumptions Section Template

### Project Assumptions

| Assumption | Impact if Wrong |
|------------|-----------------|
| Access to source code will be provided on Day 1 | Delay of 1-2 weeks |
| Development environment will be available | +1 week setup time |
| Client will provide feedback within 3 business days | +1 week per review cycle |
| Test environment mirrors production | Additional testing time |
| Stakeholder decision-maker is available for sign-off | Project delay |

### Technical Assumptions

| Assumption | Impact if Wrong |
|------------|-----------------|
| ColdFusion version is as reported (CF10) | Additional compatibility work |
| Database schema is documented | Discovery time increases |
| No custom extensions beyond standard CF | Additional migration work |
| Current hosting infrastructure will remain during migration | Additional coordination |
| Authentication uses standard patterns | Custom auth rewrite may be needed |

---

## Exercise: Customize the Templates

For the BlogCFC5 project:

1. Identify 3-5 specific project risks
2. Identify 3-5 specific technical risks
3. Identify 5-7 project assumptions
4. Identify 5-7 technical assumptions

---

## Deliverable

Completed risks and assumptions document for BlogCFC5 proposal
