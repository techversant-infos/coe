# Assessor Guide

> How to conduct fair, consistent assessments across the CF Consulting CoE.

## Before You Assess

1. Read the [Competency Matrix](../competency-matrix.md) thoroughly
2. Review the developer's self-assessment (if submitted)
3. Gather evidence from recent work (code reviews, client interactions, presentations)
4. Calibrate with other assessors if possible

## Assessment Principles

### Be Evidence-Based

Don't score based on your "feeling" about someone. Score based on specific, observable evidence:

| Instead of... | Think... |
|--------------|----------|
| "They seem confident" | "I observed them lead a client call on X date" |
| "They're good at SQL" | "They optimized a query that reduced load time by 60%" |
| "They struggle with communication" | "They presented to the team but rushed through slides" |

### Use the Full Scale

The scale is 1–10 for a reason. Here's what typical looks like:

| Score | ColdFusion Example | Client Skill Example |
|-------|-------------------|---------------------|
| 1–2 | Never worked with CFML | Cannot hold a client conversation |
| 3–4 | Knows basic cfquery/cfform | Needs coaching on client calls |
| 5–6 | Can build features independently | Can handle standard client questions |
| 7–8 | Can debug complex CF issues | Can lead client discussions |
| 9–10 | Recognized CF expert | Can represent company to executives |

A score of 5–6 is **not bad**. It's "can do this job." Don't inflate scores to avoid difficult conversations.

### Separate Skills

Each row in the matrix is scored independently. Strong ColdFusion skills don't mean strong presentation skills. Don't let one area influence another.

## Technical Skills Assessment

### ColdFusion (Weight: 20%)

| Score | Indicators |
|-------|------------|
| 1–2 | No CFML experience, struggles with basic syntax |
| 3–4 | Uses basic tags, needs reference for functions |
| 5–6 | Builds components, uses frameworks, handles errors |
| 7–8 | Debug complex issues, understands lifecycle, optimizes |
| 9–10 | Teaches others, writes standards, knows internals |

**Evidence to look for:**
- Code quality in PRs
- Bug resolution speed and accuracy
- Ability to explain CF concepts to others
- Performance optimization work

### Lucee (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Never used Lucee, only Adobe CF |
| 3–4 | Basic Lucee experience, knows it's different from Adobe |
| 5–6 | Has migrated or supported Lucee applications |
| 7–8 | Knows compatibility differences, extension ecosystem |
| 9–10 | Deep Lucee internals, contributes to community |

**Evidence to look for:**
- Lucee migration project experience
- Knowledge of Railo compatibility issues
- Understanding of Enginearden licensing

### Java (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Doesn't know Java exists beyond CF |
| 3–4 | Understands CF runs on JVM, can read stack traces |
| 5–6 | Can debug JVM issues, understands heap/GC basics |
| 7–8 | Can tune JVM, uses Java debugging tools |
| 9–10 | Can extend CF with custom Java, deep JVM knowledge |

**Evidence to look for:**
- JVM tuning experience
- Stack trace analysis
- Java integration projects

### SQL (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Basic cfquery, doesn't understand indexes |
| 3–4 | Can write joins, subqueries, understands basics |
| 5–6 | Can optimize queries, design basic schemas |
| 7–8 | Advanced indexing, query plans, stored procedures |
| 9–10 | Database architecture, partitioning, replication |

**Evidence to look for:**
- Query optimization results
- Schema design work
- Index strategy implementation

### Performance (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Doesn't measure performance |
| 3–4 | Uses basic timing, knows about caching |
| 5–6 | Profiles applications, identifies bottlenecks |
| 7–8 | Implements caching strategies, JVM tuning |
| 9–10 | System-wide performance architecture |

**Evidence to look for:**
- Performance improvement projects
- Profiling tools used
- Benchmarking results

### Security (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | No security awareness |
| 3–4 | Knows about SQL injection, uses cfqueryparam |
| 5–6 | Understands OWASP, implements auth |
| 7–8 | Security audits, penetration testing |
| 9–10 | Security architecture, secure code standards |

**Evidence to look for:**
- Security-related PRs
- OWASP implementation
- Security audit participation

### Cloud (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | No cloud experience |
| 3–4 | Basic AWS/Azure概念, has used S3 or similar |
| 5–6 | Can deploy CF to cloud, understands networking |
| 7–8 | Multi-region, load balancing, containers |
| 9–10 | Cloud architecture, cost optimization |

**Evidence to look for:**
- Cloud migration projects
- Container experience
- Infrastructure as code

### Git (Weight: 5%)

| Score | Indicators |
|-------|------------|
| 1–2 | Uses GUI only, doesn't understand branching |
| 3–4 | Basic branching, commits, PRs |
| 5–6 | Resolves conflicts, code review |
| 7–8 | Advanced workflows, bisect, hooks |
| 9–10 | Git administration, contribution guidelines |

### API (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Doesn't know what an API is |
| 3–4 | Consumes third-party APIs |
| 5–6 | Builds REST APIs, understands HTTP |
| 7–8 | API design, authentication, documentation |
| 9–10 | GraphQL, gRPC, API strategy |

**Evidence to look for:**
- API design work
- Documentation authored
- Integration projects

### React (Weight: 5%)

| Score | Indicators |
|-------|------------|
| 1–2 | No frontend experience |
| 3–4 | Basic HTML/CSS, some JS |
| 5–6 | Built simple React components |
| 7–8 | Complex React apps, state management |
| 9–10 | React architecture, performance |

## Client Skills Assessment

### Communication (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Struggles to explain technical concepts |
| 3–4 | Can explain with coaching |
| 5–6 | Explains clearly to technical audiences |
| 7–8 | Tailors explanation to audience level |
| 9–10 | Can explain to executives, writes clearly |

**Observation opportunities:**
- Team presentations
- Client calls (with permission)
- Documentation quality

### Confidence (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Hesitant, defers to others constantly |
| 3–4 | Uncomfortable in new situations |
| 5–6 | Handles routine situations well |
| 7–8 | Comfortable with unknowns, researches quickly |
| 9–10 | Projects calm confidence in any situation |

**Observation opportunities:**
- Client calls
- Technical discussions
- Decision-making moments

### Requirements Gathering (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Asks unclear questions |
| 3–4 | Asks basic questions, misses context |
| 5–6 | Covers functional requirements well |
| 7–8 | Uncovers hidden requirements, constraints |
| 9–10 | Master of discovery sessions |

**Observation opportunities:**
- Requirement documentation
- Discovery session participation
- Scope change frequency

### Presentation (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Reads slides, no engagement |
| 3–4 | Basic slides, some eye contact |
| 5–6 | Clear delivery, answers questions |
| 7–8 | Engaging, handles objections well |
| 9–10 | Can present to C-suite |

**Observation opportunities:**
- Team demos
- Client presentations
- Training sessions

### English Fluency (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Difficult to understand |
| 3–4 | Some errors, needs repetition |
| 5–6 | Clear communication, minor errors |
| 7–8 | Professional, articulate |
| 9–10 | Near-native fluency |

**Observation opportunities:**
- Client calls
- Written communication
- Presentations

### Listening (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Interrupts, doesn't confirm understanding |
| 3–4 | Listends but doesn't confirm |
| 5–6 | Summarizes, confirms understanding |
| 7–8 | Paraphrases effectively, reads between lines |
| 9–10 | Masterful active listening |

### Problem Solving (Weight: 5%)

| Score | Indicators |
|-------|------------|
| 1–2 | Presents problems without solutions |
| 3–4 | Identifies problems, limited solutions |
| 5–6 | Proposes solutions with trade-offs |
| 7–8 | Complex problem solving, alternatives |
| 9–10 | Strategic thinking |

## Behaviour Assessment

### Leadership (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Waits to be told what to do |
| 3–4 | Does what's assigned, occasional initiative |
| 5–6 | Drives own work, helps others |
| 7–8 | Leads projects, mentors peers |
| 9–10 | Thought leader, organizational impact |

### Curiosity (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Doesn't ask questions |
| 3–4 | Asks basic "how" questions |
| 5–6 | Explores options, experiments |
| 7–8 | Deep dives, research |
| 9–10 | Constant learner, shares knowledge |

### Calm Under Pressure (Weight: 20%)

| Score | Indicators |
|-------|------------|
| 1–2 | Panics, makes rushed decisions |
| 3–4 | Stresses visibly, still functions |
| 5–6 | Maintains composure under normal pressure |
| 7–8 | Calm during production incidents |
| 9–10 | Stabilizes others, clear in crisis |

**Observation opportunities:**
- Production incidents
- Tight deadlines
- Client escalations

### Customer Empathy (Weight: 25%)

| Score | Indicators |
|-------|------------|
| 1–2 | Doesn't consider client perspective |
| 3–4 | Basic awareness of client needs |
| 5–6 | Understands business drivers |
| 7–8 | Anticipates client needs |
| 9–10 | Advocate for client internally |

### Professionalism (Weight: 15%)

| Score | Indicators |
|-------|------------|
| 1–2 | Misses meetings, unprepared |
| 3–4 | Meets minimum expectations |
| 5–6 | Reliable, prepared |
| 7–8 | Goes beyond, represents company well |
| 9–10 | Role model for professionalism |

### Ownership (Weight: 10%)

| Score | Indicators |
|-------|------------|
| 1–2 | Passes blame, doesn't follow through |
| 3–4 | Completes assigned work |
| 5–6 | Follows through on commitments |
| 7–8 | Owns problems, escalates appropriately |
| 9–10 | Fully accountable, no excuses |

## Common Assessment Pitfalls

| Pitfall | How to Avoid |
|---------|--------------|
| Recency bias | Consider the entire period, not just last week |
| Halo effect | Score each skill independently |
| Comparing to self | Compare to the standard, not to others |
| Being too harsh | 5 = competent. Not every needs to be 9 |
| Being too lenient | 5 = competent. Reserve 7+ for genuine excellence |
| Assuming | Use specific examples and evidence |
| Group think | Conduct individual assessments before comparing notes |

## Conducting the Assessment Conversation

### Opening (5 minutes)

1. Explain the purpose of the assessment
2. Review the developer's self-assessment
3. Set expectations for the conversation

### Skills Discussion (30 minutes)

1. Go through each competency area
2. Discuss specific evidence for each score
3. Note any discrepancies between self and manager scores
4. Focus on growth areas

### Closing (10 minutes)

1. Summarize agreed scores
2. Discuss priority development areas
3. Set goals for next period
4. Answer any questions

### After the Assessment

1. Document scores and evidence
2. Update IDP with new goals
3. Schedule follow-up if needed
