# Module 9-03: Presentation Skills

> Learn to deliver clear, confident presentations to technical and non-technical audiences.

## Overview

Presenting well is a multiplier for your technical expertise. This module covers presentation structure, delivery, and handling questions — skills that apply to every client engagement.

> **Generic Foundation:** Planned: General Communication Guide — this module adds CF-specific content and practice scenarios.

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Structure presentations for different audience types
- [ ] Create clear, visual slides (not walls of text)
- [ ] Present architecture diagrams to non-technical audiences
- [ ] Handle Q&A with confidence
- [ ] Manage presentation pace and time
- [ ] Project confidence without arrogance
- [ ] Use appropriate technical terminology per audience

## Audience Types

| Audience | What They Care About | How to Speak |
|----------|---------------------|--------------|
| **Executives** | Business value, ROI, risk, timeline | No code, high-level diagrams |
| **Managers** | Project impact, resources, schedule | Mix of diagrams and details |
| **Developers** | Technical details, architecture | Can use code and deep dives |
| **Mixed** | Varies | Check understanding, bridge gaps |

## Presentation Structure

### 1. Opening (10%)

- Hook: Start with the problem or opportunity
- Agenda: Set expectations
- Credibility: Brief context on why you're here

**Example opener:**
> "You mentioned that your team spends 30% of their time on deployment issues. Today, I'd like to show you how modernizing your ColdFusion stack could cut that in half while improving security and performance."

### 2. Body (80%)

- One main idea per slide
- Use visuals, not bullets
- Progress from problem → solution → benefits
- Bridge between sections

### 3. Close (10%)

- Summarize key points
- Clear next steps
- Q&A invitation

## ColdFusion Presentation Patterns

### Explaining ColdFusion to Non-Technical Audiences

| Instead of... | Say... |
|--------------|--------|
| "ColdFusion is a CFML runtime on the JVM" | "ColdFusion is a web application platform — like the engine that runs your internal tools" |
| "CF2018 is end-of-life in December" | "Your current platform will no longer receive security updates after December, which means potential vulnerabilities" |
| "JVM garbage collection tuning" | "We can make your application faster by optimizing how it uses memory" |

### Architecture Diagrams for Non-Technical Audiences

- Use boxes and arrows (no UML notation)
- Label with business terms, not technical terms
- Color-code by system ownership
- Show data flow, not implementation details

**Example:**
```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Users     │ ───→ │  ColdFusion │ ───→ │  Database   │
│  (Browser)  │      │   Server    │      │  (Data)     │
└─────────────┘      └─────────────┘      └─────────────┘
                            │
                            ↓
                     ┌─────────────┐
                     │   External  │
                     │    APIs     │
                     └─────────────┘
```

### Risk Communication

| Technical Risk | Business Impact |
|----------------|-----------------|
| CF2018 EOL | Security vulnerabilities, compliance issues |
| Single server | Downtime during updates, performance issues |
| No monitoring | Slow detection of problems, longer outages |
| Plain CFM code | Higher modernization cost, fewer developers available |
| No CI/CD | Manual deployments, human error, slower releases |

## Slide Design Principles

### DO

- One idea per slide
- Images and diagrams
- High contrast
- 6x6 rule (max 6 bullets, 6 words each)
- White space
- Consistent formatting

### DON'T

- Walls of text
- Full sentences
- More than 2 fonts
- Unnecessary animations
- Jargon without explanation
- Tiny text

## Handling Questions

### Common Question Types

| Question | How to Handle |
|----------|---------------|
| "How long will this take?" | Give a range, reference assumptions |
| "What about [specific technology]?" | "That's a great point — let me note it for the follow-up" |
| "Can you do [out of scope]?" | "That wasn't in our initial scope, but let's discuss after" |
| "What's the cost?" | "I'd need to finalize scope, but here's a ballpark..." |
| "Have you done this before?" | Share relevant experience without naming clients |
| "What if [negative scenario]?" | Acknowledge risk, explain mitigation |

### The "Bridge" Technique

When you don't know:
> "That's outside my immediate area, but here's what I'd suggest..."

> "Let me verify that and follow up with you directly."

> "That's a great question — in our experience, the answer depends on [factor]..."

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Audience Translation](./exercises/exercise-1.md) | Explain CF concepts to non-technical audience | Plain language explanations |
| [Exercise 2: Architecture Diagram](./exercises/exercise-2.md) | Create audience-appropriate diagram | Clear visual for executives |
| [Exercise 3: Full Presentation](./exercises/exercise-3.md) | Deliver 15-minute presentation | Recorded with feedback |
| [Exercise 4: Difficult Q&A](./exercises/exercise-4.md) | Handle challenging questions | Confident responses |

## Assessment

Complete all exercises and pass the module assessment with 70% or higher.

## Resources

- Planned: General Communication Guide
- [Slide Templates](./resources/slide-templates.md) — (planned)
- [Architecture Diagram Examples](./resources/architecture-diagrams.md) — (planned)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 3 |
| Exercises | 5 |
| Assessment | 1 |
| **Total** | **9 hours** |

## Success Criteria

A developer completing this module should be able to:

1. Present architecture to executives in 10 minutes
2. Create clear slides without walls of text
3. Handle Q&A without getting defensive
4. Bridge technical concepts for non-technical audiences

## Next Module

[Module 9-04: Communication](../09-04-communication/) — Master day-to-day client communication patterns.
