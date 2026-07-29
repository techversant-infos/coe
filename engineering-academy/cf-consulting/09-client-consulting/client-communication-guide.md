# Client Communication Guide

> Practical guidance for ColdFusion consulting interactions.

---

## Before a Client Meeting

### Preparation Checklist

- [ ] Confirmed purpose and expected decision
- [ ] Confirmed attendees and their roles
- [ ] Prepared agenda (sent 24 hours in advance)
- [ ] Reviewed client background and previous interactions
- [ ] Prepared key questions for this meeting
- [ ] Identified who owns what decisions

### Sample Agenda Template

```
Meeting: [Topic]
Attendees: [Names and roles]
Purpose: [What we want to achieve]
Decision: [What we need to decide]

Agenda:
1. [Topic] — 10 min — [Owner]
2. [Topic] — 15 min — [Owner]
3. [Topic] — 15 min — [Owner]
4. Decisions and next steps — 10 min
```

---

## During Discovery Sessions

### Listen First

> "Tell me about the problem you're trying to solve."

### Paraphrase and Clarify

> "So what I'm hearing is... Is that right?"

### Distinguish Facts from Hypotheses

| Client Says | Ask |
|------------|-----|
| "The system is slow" | "When did you first notice? What changed?" |
| "We need to migrate" | "What prompted this now?" |
| "It's not secure" | "What specific concerns do you have?" |

### Summarize and Confirm

Before closing:
> "Let me confirm what I heard: [summary]. Did I get that right? What did I miss?"

---

## Explaining Technical Findings

### Business Impact First

**Instead of:** "Your database has N+1 query problems."

**Say:** "We found queries running repeatedly for the same data. This adds 2-3 seconds to every page load. For your peak traffic, that means users are waiting — and some are leaving before the page loads."

### Offer Options with Trade-offs

> "We have three approaches:
> 1. Quick fix — addresses the symptom, lower cost, temporary
> 2. Structural fix — addresses the root cause, higher cost, permanent
> 3. Full modernization — reduces future maintenance, highest investment
> 
> Each has different implications for timeline and budget."

---

## When Uncertain

### State What You Know

> "What I can tell you is..."

### State What Must Be Verified

> "I'll need to verify a few things before I can give you a complete picture."

### Give a Response Date

> "I'll research this and come back to you by [specific date] with a recommendation."

### Avoid

- ❌ "I don't know"
- ❌ "I need to check"
- ❌ Silence followed by speculation

---

## Reporting Risks, Delays, and Scope Changes

### Raise Risks Early

> "I want to flag something early: [risk]. It affects [impact]. Options are [solutions]."

### Report Delays Promptly

> "I want to update you on timeline. [Original estimate] is now [revised estimate]. The reason is [brief explanation]. To get back on track, we're [recovery plan]."

### Scope Change Protocol

1. Identify the gap
2. Quantify impact (time, cost, risk)
3. Present options
4. Get explicit decision
5. Document in writing

---

## After Meetings: Follow-Up

### Within 24 Hours

Send a summary email:

```
Subject: [Meeting Title] — Decisions and Actions

Decisions made:
1. [Decision 1]
2. [Decision 2]

Open questions:
1. [Question] — [Owner] — [Date]

Next steps:
1. [Action] — [Owner] — [Date]
2. [Action] — [Owner] — [Date]

Next meeting: [Date and topic]
```

---

## Escalation Boundaries

### What a Consultant Can Commit To

| Decision | Can Commit? |
|----------|-------------|
| Technical approach | ✅ Yes |
| Timeline estimate | ✅ Yes (with caveats) |
| Scope within agreed envelope | ✅ Yes |
| Pricing/contract terms | ❌ No — escalate to sales |
| Security/legal requirements | ❌ No — escalate to security/legal |
| Executive commitments | ❌ No — escalate to leadership |

### Escalation Template

> "That's an important point that involves [pricing/contracts/legal/executive]. I want to make sure you get the right answer from [the right person]. Let me connect you with [appropriate contact]."

---

## Quick Reference: Key Phrases

| Situation | Use This |
|----------|---------|
| Clarifying | "Can you help me understand why that matters to you?" |
| Estimating | "Based on what you've described, my estimate is... with a buffer for unknowns." |
| Raising risk | "I want to raise something early while we have options." |
| Deferring | "I'll verify that and come back with a recommendation by [date]." |
| Confirming | "So the decision is to proceed with [option]?" |
| Ending on next steps | "Next steps are: [1], [2], [3]. Talk next [date]." |

---

## Related Resources

- [Discovery Workshops Module](09-01-discovery-workshops/)
- [Communication Exercises](09-04-communication/exercises/)
- [Presentation Exercises](09-03-presentation/exercises/)
- [Proposal Support Module](09-05-proposal-support/)
- [Operating Model](../10-consulting-operating-model/)
