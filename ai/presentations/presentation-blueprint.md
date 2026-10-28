# AI Productivity Presentation — Blueprint v3
**Session title:** Don't let AI work for you. Work better with AI.
**Target:** 15 slides · 35–40 minutes
**Audience:** Developers · QA · Designers · Tech Leads · Delivery Managers
**Tone:** Peer-to-peer. Guiding, not teaching. "Here's what works — and what doesn't."

---

## DESIGN SYSTEM

| Element | Spec |
|---------|------|
| Background | #FFFFFF (white) |
| Primary text | #111111 (near-black) |
| Secondary text | #6B7280 (medium grey) |
| Table row fill | #F3F4F6 (light grey) |
| Borders | #E5E7EB (hairline) |
| Infographic accent | Context-specific (see each slide) |
| Headline font | Calibri Bold, 38–42pt |
| Body font | Calibri Regular, 16pt |
| Code font | Consolas, 13pt |

**Visual language:**
- Navigation pin `◉` replaces bullet points as the icon marker
- Thin horizontal route line as section divider
- Signal bars `▂▄▆█` for strength/context indicators
- Clean tables: no thick borders, light alternating rows, left-aligned text
- Infographics use colour only when it communicates meaning (green/red/amber contrast, gradients for scale)
- Slides breathe — generous white space, no crowding

---

## METAPHOR REFERENCE MAP

> GPS = AI tool | Driver = Developer | Route = Workflow | Destination = Output
> Map = CLAUDE.md / project context | Fleet = Team | Traffic rules = Governance

| GPS concept | Presentation concept |
|-------------|---------------------|
| Setting the destination | Writing a good prompt |
| Wrong address → wrong place | Bad prompt → useless output |
| Saved places & preferences | CLAUDE.md / .cursorrules |
| Recalculating | Rewind / course correction |
| Signal strength | Context awareness per tool |
| Following GPS off a cliff | Blind delegation without review |
| Everyone taking a different route | The problem — no shared workflow |
| Agreed route before you leave | The solution — shared standards |
| Override GPS when you know better | Human-led delegation |
| GPS suggests, driver decides | AI assists, human validates |
| Battery / signal management | Token optimisation |
| Road rules still apply | Governance |
| Track your journey | Sprint metrics |

---

## SLIDE STRUCTURE — 15 SLIDES

| # | Title | GPS Frame | Time |
|---|-------|-----------|------|
| 1 | Cover | The map moment | 2 min |
| 2 | The Problem | Same GPS, different routes | 3 min |
| 3 | The Solution | Agree on the route | 3 min |
| 4 | Your Navigation Stack | Know your instruments | 4 min |
| 5 | The Blind Driver | Eyes on the road | 3 min |
| 6 | The Standard Route | Plan before you drive | 4 min |
| 7 | Session Controls | Recalculating | 3 min |
| 8 | Set the Right Destination | Address in → place out | 4 min |
| 9 | Signal Management | Don't let the signal drop | 3 min |
| 10 | Your Saved Places | AI knows the route | 3 min |
| 11 | GPS Signal Strength | What your AI can see | 3 min |
| 12 | Eyes on the Road | GPS says turn right... | 3 min |
| 13 | When to Override | You still drive | 3 min |
| 14 | Road Rules | Traffic laws still apply | 3 min |
| 15 | Track Your Journey | Measure. Improve. Repeat. | 3 min |

---

## SLIDE 1 — COVER

### CONTENT
**Headline:** AI is GPS. Your team is driving.

**Subhead:** Right now, everyone's using a different map.

**Session title (bottom):** Don't let AI work for you. Work better with AI.

### INFOGRAPHIC
**Type:** Minimalist split visual
**Description:** White background. Left half: clean map interface with one clear route (single colour line, destination pinned). Right half: same map with five chaotic routes going in different directions — same starting point, wildly different paths. No label needed. Visual makes the point instantly.
**Colours:** Route lines in light grey, one highlighted in black. Destination pins in accent colour (one green, others grey).

### NOTES
Don't explain the metaphor. Open with the question. Let it sit.

"Every person in this room has Claude, Copilot, or Cursor. Same map. But right now, five different people on the same project are navigating five different ways. No shared route. No agreed destination. Some are taking the expressway. Some are still on the service road. And a few are following GPS into a field."

ENGAGEMENT (before advancing):
"Quick show of hands — used an AI tool in the last 24 hours? Keep your hand up if you think your teammate used it the same way."
(Lowered hands make the point. Move to slide 2.)

TONE NOTE: You're not here to teach. You're here because you've seen what works and what doesn't — and you want the team to get the benefit of that without going through all the wrong turns first.

---

## SLIDE 2 — THE PROBLEM

### CONTENT
**Headline:** Same tools. Same team. Completely different results.

**Two columns (no headers, visual contrast only):**

Left (clean, ordered):
◉ We use AI → we save time
◉ We review code → it's consistent
◉ Same tools → same output

Right (same layout, slight visual chaos):
◉ Everyone has their own "AI style"
◉ No shared workflow = no predictability
◉ Copy → paste → ship → debug → repeat
◉ No measurement = no improvement

**Root cause (full-width, dark band at bottom):**
> "We don't have an AI problem. We have a process problem."

### INFOGRAPHIC
**Type:** Two-column contrast card + root cause banner
**Description:** Left column: clean, spaced, ordered — feels structured. Right column: same visual weight but slightly misaligned, overlapping — feels chaotic without being cartoonish. Bottom band: dark (#111111) background, white bold text for the root cause line. Width: full slide.
**Colours:** Left column text: #111111. Right column: #6B7280. Bottom band: #111111 / #FFFFFF.

### NOTES
"One developer shipped 3 features cleanly last sprint. Another needed 4 review cycles on 1 feature. Both were using Cursor. Same GPS. Completely different routes."

HUMOUR: "Faster mistakes are still mistakes. They're just harder to debug because you forgot how you made them."

INDIAN CONTEXT: "It's like 10 people ordering from the same Zomato account — same restaurant, same menu — but nobody checked the office is veg-only. Nobody's wrong. No shared context."

ENGAGEMENT:
"If I asked 5 people in this room: 'what's our AI review process for a PR?' — do you think I'd get 5 consistent answers?"
(Don't wait for answers. Let it land. Move on.)

---

## SLIDE 3 — THE SOLUTION

### CONTENT
**Headline:** One route. Everyone follows it. Everyone arrives.

**Four pillars (2×2 icon grid):**

◉ **Shared workflow** — one process, every task, every person
◉ **Shared context** — CLAUDE.md + .cursorrules, per project
◉ **Clear tool roles** — Claude plans · Cursor builds · Copilot assists
◉ **Feedback loop** — measure what ships, learn, adjust

**Outcome row (4 metrics, icon + label):**
PR cycles ↓ · Bug rate ↓ · Onboarding time ↓ · Predictability ↑

**Punchline:** "Consistency beats individual brilliance."

### INFOGRAPHIC
**Type:** 2×2 pillar grid + outcome strip
**Description:** Four equal cards in a 2×2 grid. Each: icon (outlined, not filled) + pillar name bold + one-line description in grey. Below: thin route line divider. Outcome strip: four metric chips in a row, directional arrow + label, light grey background.
**Colours:** Cards: white with #E5E7EB border. Icons: #111111. Outcome strip: #F3F4F6.

### NOTES
CRICKET ANALOGY (if F1 vibes linger): "Rohit and Virat are brilliant individually. But they play the same game plan. A team wins on coordination, not individual improvisation."

"The four pillars are simple. Doing all four consistently, across every project — that's what today is about."

ENGAGEMENT:
"If this system had been in place for the last 3 sprints — one shared workflow, one context file — what one thing would have been different?"
(Invite 1–2 short answers. Don't turn it into a discussion.)

---

## SLIDE 4 — YOUR NAVIGATION STACK

### CONTENT
**Headline:** Right instrument. Right moment.

**Tool matrix (clean table, no thick borders):**

| Tool | Role | Best for |
|------|------|---------|
| Claude | Long-range planner | Architecture, planning, complex reasoning, long documents |
| Cursor | Turn-by-turn navigation | In-file editing, multi-file refactoring, codebase-aware changes |
| Copilot | Heads-up display | Inline autocomplete, PR summaries, fast completions |
| ChatGPT | Offline map | Quick Q&A, exploration — no project context |

**Rule (below table):**
> One instrument per task. Don't drive staring at three screens simultaneously.

### INFOGRAPHIC
**Type:** Horizontal spectrum bar below the table
**Description:** A single horizontal bar from left ("Fast, inline, low context") to right ("Deep, planned, high context"). Each tool positioned as a labelled pin on the spectrum. Copilot far left. Claude far right. Cursor centre-right. ChatGPT centre-left.
**Colours:** Bar: light grey gradient. Pins: black with tool name below. No tool brand colours.

### NOTES
"Using Claude for inline autocomplete is like using your long-range GPS planner to navigate a car park. Technically it works. Complete overkill."

COST POINT (for leads): "Claude Opus for simple completions costs 10× more than Copilot for the same output. Tool selection is cost discipline."

ENGAGEMENT:
"What are you using Claude for that Copilot could handle cheaper and faster? And what should you be using Claude for that you're not?"
(No right answer. Just awareness.)

---

## SLIDE 5 — THE BLIND DRIVER

### CONTENT
**Headline:** GPS told someone to drive into a lake. They followed it.

**Two paths (diverging route visual):**

Blind (left path):
◉ Task → open Cursor → generate → commit
◉ Compiles? Ship it.
◉ PR fails → back to start
◉ Time: 3 days

Smart (right path):
◉ Task → plan with Claude first
◉ Generate → read every line
◉ "What did AI miss?" → test it
◉ Commit what you can explain
◉ Time: 1 day

**The gap:**
> "Same AI. Same codebase. One day versus three."

### INFOGRAPHIC
**Type:** Diverging path from one starting point
**Description:** Single road splitting into two paths from "Task received." Left path (grey, dotted): winds messily, ends in a wall labelled "PR rejected / prod bug." Right path (black, clean): straight, structured, ends at "Merged ✓." Time labels at the end of each path. No dramatic colours — clean contrast between solid and dotted lines.
**Colours:** Background white. Blind path: #9CA3AF dashed. Smart path: #111111 solid. Labels: standard text.

### NOTES
"When you debug AI-generated code you don't understand, you start from zero. No mental model. That's when a 2-hour task becomes a 2-day problem."

FOR JUNIORS: "There's a career-defining difference between 'AI taught me how this works' and 'AI wrote this and I hope it works.' One builds you. The other makes you fragile."

HUMOUR: "AI gives you the confidence of a senior developer with the context of someone who joined today."

ENGAGEMENT:
"Raise your hand if you've spent more time debugging AI code than it would have taken to write it yourself."
(Almost everyone raises a hand. That's the whole slide. Move on.)

---

## SLIDE 6 — THE STANDARD ROUTE

### CONTENT
**Headline:** You don't drive without setting the destination first.

**The 7-step route (horizontal pipeline):**

```
PLAN → VALIDATE → BUILD → AI CHECK → HUMAN REVIEW → TEST → MERGE
```

**Step labels (below pipeline):**

| Step | Tool | Non-negotiable? |
|------|------|----------------|
| PLAN | Claude | ✓ Always |
| VALIDATE | You | ✓ Always |
| BUILD | Cursor / Copilot | — |
| AI CHECK | Claude / Copilot Chat | — |
| HUMAN REVIEW | Peer / Lead | ✓ Always |
| TEST | All | ✓ Always |
| MERGE | Lead / Peer | ✓ Always |

**Rule:** Never go from task to code without planning first.

### INFOGRAPHIC
**Type:** 7-node horizontal pipeline with non-negotiable markers
**Description:** Seven connected rectangular nodes in a flow. Non-negotiable nodes (PLAN, VALIDATE, HUMAN REVIEW, TEST, MERGE) have a bold black border and small lock icon ◉ below. Optional nodes (BUILD, AI CHECK) have grey border. A thin route line runs above the pipeline as the GPS visual thread.
**Colours:** Required nodes: #111111 border. Optional: #D1D5DB border. Arrow connectors: #9CA3AF.

### NOTES
"Planning with Claude before writing code takes 10 minutes. Debugging code written without a plan takes 2 hours. The maths is not complicated."

GPS TIE-IN: "You don't start the car and figure out the route as you go. You set the destination, confirm the route, then drive. Same here."

ENGAGEMENT:
"Count silently — how many of these 7 steps are you doing today? How many are you skipping?"
(No hands. Just reflection. Then move.)

---

## SLIDE 7 — SESSION CONTROLS

### CONTENT
**Headline:** Recalculating. Five ways to stay on course.

**Control table:**

| Control | When | What it does |
|---------|------|-------------|
| Continue | Claude stopped mid-task | Picks up exactly where it left off — no drift |
| Rewind | Wrong direction taken | Cuts the wrong path cleanly. Re-prompt correctly. |
| /clear | Switching tasks entirely | Removes stale context. Fresh map for new destination. |
| /compact | Context window filling | Summarises progress. Recovers ~60% context. |
| Subagent | Repeatable specialist task | Triggers a specialist — same standards, every time |

**Punchline:** "Re-prompting is not the same as recalculating."

### INFOGRAPHIC
**Type:** 5-row table with GPS icon column
**Description:** Clean table. Left column: GPS-icon per control (◉ for continue, ↩ for rewind, ✕ for clear, ⊘ for compact, ⬡ for subagent). Middle: control name bold. Right two: "When" and "What it does" in regular weight. Light alternating rows. No heavy borders.
**Colours:** Table rows alternating #FFFFFF / #F3F4F6. Control names: #111111 bold. Descriptions: #6B7280.

### NOTES
CONTINUE: "Claude paused your auth refactor across 6 files after file 3. Type continue — it picks up at file 4, same pattern, no drift. Re-prompting restarts reasoning and can drift from what was established."

REWIND: "Claude spent 3 messages rewriting your DB schema to fix a slow query. You realise it's a JOIN issue. Don't say 'ignore all that' — Claude partially carries it forward. Rewind cuts it cleanly."

/CLEAR: "After 45 minutes debugging a Node.js memory leak, you start a new React component. /clear first — otherwise Claude applies backend context to frontend output. Stale context is invisible but real."

/COMPACT: "An hour into building your API endpoint. Context filling. /compact — Claude summarises the agreed approach, you recover 60% context. Rule: compact before it fills, not after."

SUBAGENT: "/review triggers code-reviewer.md — pre-configured with your team rules. Same standards every PR. Automatically."

ENGAGEMENT:
"Raise your hand if you've ever said 'ignore all that' to Claude after it went the wrong direction."
(Hands up — then:) "That's what rewind is for. Cleaner and cheaper than correcting mid-path."

---

## SLIDE 8 — SET THE RIGHT DESTINATION

### CONTENT
**Headline:** Wrong address in. Wrong place out. Every time.

**Formula:**
> `Context + Task + Constraints + Format = Useful output`

**Two prompt examples (side by side):**

Weak:
```
Fix this function
```

Strong:
```
Node.js + Express + PostgreSQL.
/api/users/:id throws 500 when user doesn't exist.
Should return 404: { error: 'user_not_found' }
Fix error handling only. Don't change function
signature or JWT middleware. Return code only.
```

**5 rules (icon list):**
◉ Name the file/function — don't describe it
◉ State what you've already tried
◉ Specify format: "bullet list / code only / max 3 options"
◉ One task per prompt — chained prompts drift
◉ Add constraints: what NOT to change

### INFOGRAPHIC
**Type:** Side-by-side chat mockup
**Description:** Two chat interface cards. Left (weak): short vague prompt, long wandering AI response. Right (strong): structured prompt with formula components colour-labelled — Context (underlined), Task (bold), Constraints (grey highlight), Format (italic). Clean specific response below. Formula legend strip above both cards.
**Colours:** Weak card: #F3F4F6 background, no accent. Strong card: white, with light annotation colours for formula components. Label strip: #111111 background, white text.

### NOTES
"A vague question gets a vague answer. From a human. From Google. From Claude. AI is only as specific as you are."

GPS TIE-IN: "If you type 'coffee shop' into GPS, you might end up anywhere. The more specific your destination — 'Blue Tokai, Indiranagar, Bangalore' — the more useful the route."

INDIAN HUMOUR: "Like telling a chai wala 'give me something hot.' You might get green tea. Be specific: adrak wali cutting chai, thodi meethi, extra strong."

LIVE ACTIVITY (most memorable part of this slide):
Show: "Write tests for my auth module."
Ask: "What's missing? Call it out."
Get answers: language? framework? test style? edge cases?
Then reveal the strong version. More memorable than any explanation.

---

## SLIDE 9 — SIGNAL MANAGEMENT

### CONTENT
**Headline:** Don't let the signal drop mid-journey.

**What kills signal (wastes tokens):**
◉ Pasting entire files for a 3-line question
◉ Re-explaining context the AI already has
◉ Vague questions → 3 clarifying rounds
◉ No CLAUDE.md → re-explain every session

**What keeps signal strong:**
◉ `/compact` before context fills → ~60% recovered
◉ `/clear` when switching tasks
◉ Reference line numbers, not whole files
◉ One task per prompt

**Model selection (cost/signal table):**

| Model | Use for | Cost |
|-------|---------|------|
| Haiku | Repetitive tasks, test gen, summaries | Low |
| Sonnet | Most dev tasks — best ratio | Medium |
| Opus | Architecture, complex reasoning only | High |

### INFOGRAPHIC
**Type:** Signal strength split + model cost bar
**Description:** Left panel: "Low signal" — long prompt, token meter near full, sections of irrelevant content highlighted grey. Right panel: "Strong signal" — short targeted prompt, token meter at 30%, clean output. Below: three model blocks side by side (Haiku / Sonnet / Opus) with task type labels and relative cost indicator (low/mid/high bar).
**Colours:** Token meter: green (low) to red (high). Model blocks: light grey background, black text, cost bar in neutral grey gradient.

### NOTES
"If you paste a 500-line file to ask about one function, you're burning context on 490 lines Claude will never reference. It's like giving a taxi driver your entire travel history just to get to the airport."

GPS TIE-IN: "GPS uses less battery when it knows your saved places. CLAUDE.md is your saved places. Set it up once — stop burning context re-explaining every session."

ENGAGEMENT:
"Has anyone hit the context limit mid-session and lost everything they'd built up?"
(Hands up — then:) "That's a signal failure. Compact early. Not after you've lost it."

---

## SLIDE 10 — YOUR SAVED PLACES

### CONTENT
**Headline:** AI knows the route before you say a word.

**Project file structure (code tree):**
```
project/
├── CLAUDE.md              ← Claude's route preference
├── .cursorrules           ← Cursor's driving style
└── .claude/
    ├── agents/
    │   ├── code-reviewer.md    ← /review
    │   └── test-generator.md  ← /gen-tests
    └── commands/
        └── review.md
```

**What each file does (compact table):**

| File | What AI learns |
|------|---------------|
| CLAUDE.md | Stack, patterns, off-limits zones |
| .cursorrules | Coding style, framework conventions |
| agents/ | Repeatable specialist workflows |
| commands/ | One-command team standards |

**Minimum CLAUDE.md (show on slide):**
```
Stack: Node.js 20, React 18, PostgreSQL, AWS
Style: ESLint Airbnb, async/await, no raw SQL
Tests: Jest + Supertest
Off-limits: /src/auth/, /src/middleware/security.js
```

### INFOGRAPHIC
**Type:** IDE-style file tree (dark panel) + annotation callouts
**Description:** Left: dark sidebar panel (VS Code aesthetic, #1E1E1E background) showing the file tree in monospace, colour-coded by tool — Claude files in one tone, Cursor in another, shared in neutral. Right: three callout boxes pointing to key files with one-line explanations. Style: feels like opening your IDE — immediately recognisable.
**Colours:** Dark tree panel: #1E1E1E background, #D4D4D4 text, files highlighted by tool category. Callout boxes: white with light border.

### NOTES
"Without this structure, every AI session starts from zero. With it, Claude already knows your stack, your standards, and what not to touch — before you type a word."

"CLAUDE.md is onboarding documentation for your AI. Write it once. Save 10 hours per sprint."

GPS TIE-IN: "Saved places in GPS mean you don't re-enter the address every trip. CLAUDE.md is your saved places. Set it up once per project."

ENGAGEMENT:
"How many active projects in this room have a CLAUDE.md file right now?"
(Almost certainly: very few.)
"This is the single highest-leverage action from today. 2 hours of setup. Pays back every session."

---

## SLIDE 11 — GPS SIGNAL STRENGTH

### CONTENT
**Headline:** Know exactly what your AI can see — and what it's guessing.

**Context visibility table:**

| Tool | Sees clearly | Can't see | Risk |
|------|-------------|-----------|------|
| Claude | What you paste / attach | Everything else | Conflicts with your architecture |
| Cursor | Open + indexed files | Runtime state, secrets | Hallucinates imports |
| Copilot | Current file + adjacent | Your whole project | Generates wrong patterns |
| ChatGPT | This conversation only | Your codebase entirely | Always generic |

**Signs AI is guessing:**
◉ Imports a function that doesn't exist
◉ Suggests a package you already have
◉ Duplicates a file that already exists
◉ Recommends a pattern you explicitly don't use

**Fix:** CLAUDE.md + .cursorrules remove most of this.

### INFOGRAPHIC
**Type:** Signal strength grid — 2×2, one panel per tool
**Description:** Four equal panels. Each panel: tool name bold, a signal bar indicator (▂▄▆█) showing relative visibility strength, a mini file tree with "visible" files solid and "invisible" files greyed out. Below each: "Sees: X | Doesn't see: Y" in two-tone text. Style: clean, technical, like a network dashboard.
**Colours:** Visible files: #111111. Invisible files: #D1D5DB. Signal bars: filled = #111111, empty = #E5E7EB. Panel borders: #E5E7EB.

### NOTES
"Cursor with a well-indexed codebase is the most context-aware tool you have. But indexed doesn't mean understood — it means searchable. It still needs guidance on what matters."

"Claude has no memory between sessions unless you use Projects or CLAUDE.md. Every new chat is a blank slate. That's not a bug. It's why CLAUDE.md exists."

GPS TIE-IN: "GPS can't see road closures that happened 10 minutes ago. It can't see the local knowledge you have. It works with what it has. So does AI — and you need to know what 'what it has' actually means."

ENGAGEMENT:
"Has AI ever suggested you import a function or use a pattern that doesn't exist in your project?"
(Hands up — very common.)
"That's AI guessing. CLAUDE.md is the fix."

---

## SLIDE 12 — EYES ON THE ROAD

### CONTENT
**Headline:** GPS says turn right. You still look at the road.

**Two-gate review:**

| Gate | Who | Catches |
|------|-----|---------|
| Gate 1 — AI Review | Claude / Copilot Chat | Logic gaps, edge cases, test coverage |
| Gate 2 — Human Review | Developer / Lead | Business logic, security, architecture fit |

**The cost of skipping Gate 2:**
> Dev = 1× · Review = 2× · Staging = 5× · Production = 10×

**Testing rule:**
◉ Tests written alongside code — not after
◉ Never merge AI code without reading every test
◉ Never trust AI-generated tests without verifying edge cases

**Non-negotiable:** Every AI-generated PR gets human review. No exceptions.

### INFOGRAPHIC
**Type:** Two-gate funnel + cost escalation timeline
**Description:** Upper: funnel visual — "AI output" flows through Gate 1 (AI review, grey) then Gate 2 (human review, black border) → "Approved." Bypass path from Gate 1 to "Production bug" in dashed line, no dramatisation — just a clear consequence path. Lower: horizontal cost timeline with bug multipliers growing from left (1×) to right (10×). Simple, factual.
**Colours:** Gate 1: #6B7280. Gate 2: #111111. Bypass path: dashed #9CA3AF. Cost multiplier blocks: gradient from #F3F4F6 (left) to #D1D5DB (right) — no red, just visual weight increase.

### NOTES
"The biggest risk is reviewers getting lazy because 'the AI already checked it.' AI-generated code needs more scrutiny — not less."

"A spell-checker doesn't know if your email is appropriate. It checks spelling. Claude checking your code doesn't know if the logic fits your business. That's your job."

GPS TIE-IN: "GPS told you to turn right. You looked — there's a flooded road. GPS doesn't know. You do. Same with AI. It gives you the turn. You decide whether to take it."

FOR QA: "AI removes the mechanical test-writing. The 20% requiring real judgment — the user flow nobody spec'd, the thing that just 'feels wrong' — that's irreplaceable and that's yours."

---

## SLIDE 13 — WHEN TO OVERRIDE

### CONTENT
**Headline:** You still drive. GPS is not the driver.

**Delegation scale (4 levels):**

| Level | Mode | Use for | Examples |
|-------|------|---------|---------|
| GREEN — Follow GPS | Full delegate | Mechanical, verifiable, low-risk | Boilerplate, test stubs, PR descriptions |
| YELLOW — Confirm the route | Collaborate | Domain judgment needed | Business logic, integrations, refactoring |
| AMBER — You navigate | Human-led | Needs your architectural context | System design, API contracts, data models |
| RED — GPS off | Never delegate | Sensitive, irreversible, security | Auth, encryption, PII, production incidents |

**The decision test:**
◉ Can the output be verified quickly? → higher delegation
◉ Does it need context AI doesn't have? → lower delegation
◉ Could wrong output reach production silently? → never delegate

**The rule:** "Delegate the typing. Never delegate the thinking."

### INFOGRAPHIC
**Type:** Vertical scale with gradient + task pills
**Description:** Vertical bar running left (or top) to bottom — gradient from light (full delegate) to dark (never delegate). Each level sits on the bar as a labelled band: GREEN / YELLOW / AMBER / RED text labels (no emoji — clean). Right side: task example pills for each level (small rounded rectangles). Decision test below as a 3-node flow with yes/no branches.
**Colours:** Scale gradient: #F3F4F6 → #6B7280 → #374151 → #111111. Level text: white on dark, dark on light. Task pills: #F3F4F6 with #111111 text.

### NOTES
"AI is like a very fast, very capable junior developer. You'd give them repetitive CRUD tasks without a second thought. You'd review their business logic before merging. You'd write the architecture yourself and have them implement it. And you'd never let them push directly to production without sign-off. AI is exactly this — with one extra catch: it never tells you when it's guessing."

"Teams that fully delegate hard thinking start to lose architectural muscle. The moment you need to debug something novel — nobody can — because they haven't wrestled with a hard problem in months."

LIVE POLL:
"For your most recent AI-assisted task — which level? Full delegate? Collaborate? Human-led?"
(Most answers will be "full delegate" without realising it. That's the moment.)

Follow: "What's one task you're fully delegating right now that should probably be 'collaborate'?"
(Get 2–3 answers. No judgment.)

---

## SLIDE 14 — ROAD RULES

### CONTENT
**Headline:** GPS or not — road rules still apply.

**Non-negotiables (numbered, clean):**
1. All AI-generated code gets human review
2. No credentials, API keys, or client data in any prompt
3. Auth, encryption, PII: manual only
4. Can't explain it → don't commit it
5. No AI agent with write access to production systems

**Reference card (two columns, printable):**

| Do ✓ | Don't ✗ |
|-------|---------|
| Review and understand every output | Deploy because it compiles |
| Use CLAUDE.md on every project | Skip human review — "AI checked it" |
| Tag PRs: ai-assisted + tool used | Let AI make architecture decisions |
| Log AI wins and failures in retros | Paste client data into public tools |

**Escalation rule:**
> AI suggests something → you can't explain it → escalate. Don't commit.

### INFOGRAPHIC
**Type:** Reference card layout — designed to be printed
**Description:** Clean two-column card. Left (Do): green header chip, 4 items as compact one-liners. Right (Don't): grey header chip, 4 matching items. Below: dark full-width banner with non-negotiables numbered in white. Bottom: escalation rule in italic, bordered quote box. Entire slide designed as a printable/screenshottable card.
**Colours:** Do header: #111111 on #F3F4F6. Don't header: #9CA3AF on #F3F4F6. Bottom banner: #111111 background, white text. No red/green — clean, authoritative.

### NOTES
"Governance has a bad reputation because it usually means slower. Reframe it: road rules don't make you slow — they make it safe to drive fast. A car without brakes isn't faster. It's dangerous."

"This isn't about trust. AI is confident even when it's completely wrong. Human judgment is the only check on that confidence. It doesn't have impostor syndrome."

ENGAGEMENT:
"Has anyone pasted something into an AI tool that, in hindsight, shouldn't have left the company network?"
(No hands needed. Just let it sit. Then move.)

TIP: Print this slide as a physical reference card for the team.

---

## SLIDE 15 — TRACK YOUR JOURNEY

### CONTENT
**Headline:** You can't improve a route you don't measure.

**Sprint metrics (4 cards):**

| Metric | How |
|--------|-----|
| PR cycle time | Git: open → merge (hours) |
| Rework rate | PRs needing >1 review round (%) |
| AI-assist rate | Self-reported in sprint log |
| Defect escape rate | Bugs found post-merge per sprint |

**Actions (role-based, next sprint):**

| Who | Action | When |
|-----|--------|------|
| All devs | CLAUDE.md on top 2 active projects | This sprint |
| All devs | Log AI tasks in sprint notes | This sprint |
| Tech leads | Add ai-assisted tag to PR template | This week |
| Architects | Define AI off-limits zones | This week |

**Four things to remember:**
1. AI increases speed — not correctness
2. Discipline makes the difference — not the tool
3. Consistency beats individual brilliance
4. Measure it. Improve it. Don't assume it.

**Closing line:**
> "The best AI workflow is the one your whole team actually follows."

### INFOGRAPHIC
**Type:** Three-section closing layout
**Description:** Top third: 4 metric cards in a row (clean, no charts — just label + measure method). Middle third: action table with role/action/when — owner column intentionally blank, filled in live. Bottom third: dark background (#111111), white text — 4 numbered takeaways, closing line in larger italic below. Visual closure with the dark cover slide.
**Colours:** Metric cards: white, #E5E7EB border. Action table: #F3F4F6 alternating rows. Bottom dark section: #111111 / #FFFFFF.

### NOTES
"End on action, not inspiration. Teams leave motivated, then don't act because next steps were vague. Fix that right now — one commitment per table, named person, in the next 5 working days."

GPS CLOSING CALLBACK:
"GPS got you here today. You didn't follow it blindly — you knew the destination, confirmed the route, and drove. That's what we're asking for with AI. Know where you're going. Agree on the route. Stay in control."

COMMITMENT EXERCISE:
"One commitment from each table. What does your team do in the next 5 working days? Write it down."
Get verbal commitments from 3–4 people by name. Public accountability.

FINAL QUESTION:
"One word — what's the single thing you're taking from today?"
(Let 5–6 people answer. Close on the last one.)

---

## DELIVERY NOTES

**Pacing:** Don't rush slides 6 and 13 — they're the anchor content. Give them room.
**Live activities:** Slide 8 (prompt rewrite) and slide 13 (delegation poll) are the highest-engagement moments. Protect the time.
**Physical handout:** Print slide 14 (Road Rules) as a reference card. Distribute at the start, not the end.
**Tone throughout:** You're not teaching — you're sharing what works. Use "we" and "our team" wherever possible. Invite correction.
**Closing:** The commitment exercise is not optional. Named commitments > inspiration.

---

## EDITING CHECKLIST

- [ ] Slide 1: Confirm split-map visual direction
- [ ] Slide 6: Add time estimates per step (PLAN: 10 min, BUILD: varies)
- [ ] Slide 8: Replace Node.js example with Techversant stack (PHP/Laravel or ColdFusion)
- [ ] Slide 10: Add real CLAUDE.md snippet from an active project (8–10 lines)
- [ ] Slide 11: Replace generic paths with actual Techversant project file paths
- [ ] Slide 15: Fill owner column in action table before presenting
- [ ] All slides: Confirm icon set (suggested: Phosphor Icons or Heroicons — outline style)
