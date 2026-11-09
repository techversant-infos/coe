# 09. AI Security and Safety

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Treat model input, retrieved documents and tool results as untrusted. A prompt is not an authorization control.
Apply existing Techversant security standards and design the application so a model failure cannot grant extra
access. Back to the [roadmap](./README.md).

## Threat model the feature

Consider attacks through user input, knowledge articles, case text, model output, tools and dependencies. Define
what an attacker could read or change before choosing mitigations.

**What to learn:**

- Identify direct and indirect prompt injection in untrusted content
- Prevent cross-user and cross-tenant access in application code
- Validate model output and encode it for the target context
- Restrict network access, tool scope, result size and execution time
- Add human approval and a safe stop for high-impact actions

**Resources:**

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [Techversant security audit checklist](../../security/audit/security-audit-checklist.md)

**Level:** Advanced · Core

## Test defenses at the application boundary

Instructions can help a model follow policy, but the application must enforce who can read or change data. Test
whether malicious content changes tool use, disclosure or citations. Verify controls with ordinary tests and
security review.

**What to learn:**

- Put authorization in trusted application code, never in model instructions alone
- Treat retrieved text as data, not as instructions to the assistant
- Check that model output cannot execute as HTML, SQL, shell input or a tool action without validation
- Use allow-listed tools and validate every argument against the authenticated user's permissions
- Record security events without storing sensitive prompt content

## Project: Exercise the Threat Model

**Brief:** Use the synthetic injection in CASE-1012. Demonstrate that untrusted case text cannot reveal another
case, override the assistant's policy or invoke a write action.

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] A threat model names assets, trust boundaries, attacker inputs and impact
- [ ] Tests include direct user injection and injection returned by the read-only case-summary tool
- [ ] The assistant treats injected text as untrusted and cites only approved knowledge articles
- [ ] Unauthorized, invalid and out-of-scope tool calls are rejected by application checks
- [ ] The practice app has no write-capable tools
- [ ] Security behavior is included in the fixed evaluation regression run

Previous: [08. Data Privacy and Governance](./08-data-privacy-and-governance.md) · Next:
[10. Cost, Performance and Operations](./10-cost-performance-and-operations.md)
