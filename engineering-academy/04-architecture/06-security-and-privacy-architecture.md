# 06. Security and Privacy Architecture

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Security flaws in the design cannot be fixed by careful coding later. This stage covers how to find threats early,
design the protections, and know when to bring in a security specialist. Back to the [roadmap](./README.md).

Authentication, authorization, encryption, key management, personal data and payment handling, and production
database migrations are Red Zone work at Techversant: the code is written by people, without AI generation, and
reviewed by a senior engineer. See
[section 2.2 of the AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only).

## Threat modelling

A threat model asks what you are building, what can go wrong, what you will do about it, and whether you did a good
enough job. Done during design, it is the cheapest security work there is.

**What to learn:**

- Drawing a data flow diagram with trust boundaries: the places where data crosses from less trusted to more trusted
- Finding threats systematically, for example with STRIDE: spoofing, tampering, repudiation, information disclosure,
  denial of service and elevation of privilege
- Recording each threat with its mitigation, owner and status

**Resources:**

- [Threat modelling](../../security/audit/security-audit-reference.md#81-threat-modeling), in the Techversant
  security audit reference
- [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html),
  OWASP
- [The four question framework](https://github.com/adamshostack/4QuestionFrame), Adam Shostack

**Level:** Advanced · Core

## Identity and access

Who can sign in, and what each person may do, is designed once and relied on everywhere. Use the client's identity
provider where one exists, and never design your own sign-in protocol.

**What to learn:**

- Single sign-on with OpenID Connect, and mapping the client's groups to roles in the system
- Checking permissions on the server for every request, including access to each record
- Service-to-service identity, so internal calls are authenticated too

**Resources:**

- [Tokens, JWT, OAuth 2.0 and OIDC](../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc)
  and [object-level access](../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in the
  Techversant security audit reference
- [How OpenID Connect works](https://openid.net/developers/how-connect-works/)

**Level:** Advanced · Core

## Secrets and key management

Passwords, API keys and encryption keys must never sit in code or configuration files. The design decides where
they live, who can read them and how they are rotated.

**What to learn:**

- Secrets managers provided by cloud platforms, and injecting secrets at run time
- Encryption in transit and at rest, and who holds the keys
- Rotating a secret without downtime

**Resources:**

- [Keys and secrets management](../../security/audit/security-audit-reference.md#63-keys-and-secrets-management), in
  the Techversant security audit reference
- [Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html),
  OWASP

**Level:** Advanced · Core

## Secure design review

Every Techversant change is checked against the security checklist. As an architect, you make sure the design gives
the team a way to pass it, and you know when a change needs a specialist.

**What to learn:**

- The OWASP Top 10:2025 categories, especially insecure design
- The Techversant minimum bar, and the triggers for a deeper security review
- Rate limits, quotas and abuse cases, such as one user posting thousands of comments

**Resources:**

- [Security Audit Checklist](../../security/audit/security-audit-checklist.md), including
  [when a change needs more](../../security/audit/security-audit-checklist.md#does-your-change-need-more-than-this-page)
- [Business logic and abuse cases](../../security/audit/security-audit-reference.md#82-business-logic-and-abuse-cases),
  in the security audit reference

**Level:** Advanced · Core

## Privacy by design

Personal data brings legal duties. Design so the system collects only what it needs, protects it and can delete it
on request.

**What to learn:**

- Collecting the minimum personal data, and recording why each item is needed
- Supporting users' rights, such as access and deletion, in the data model
- The laws that apply to the client's users, such as India's Digital Personal Data Protection Act, 2023, with the
  DPDP Rules, 2025, and the EU's GDPR, and when to ask the client's legal team

**Resources:**

- [Privacy by design](../../security/audit/security-audit-reference.md#84-privacy-by-design), in the Techversant
  security audit reference
- [Privacy and data protection law](../08-forward-deployed-engineering/08-production-and-security.md#privacy-and-data-protection-law),
  in the Techversant FDE roadmap, which covers GDPR and the DPDP Act and Rules
- [The Digital Personal Data Protection Bill, 2023: summary and status](https://prsindia.org/billtrack/digital-personal-data-protection-bill-2023),
  PRS Legislative Research

**Level:** Advanced · Core

## Supply chain security

Most of a system's code comes from open-source packages and base images. Their weaknesses become yours.

**What to learn:**

- Dependency scanning and keeping packages up to date
- Software bills of materials (SBOMs), and why clients increasingly ask for them

**Resources:**

- [Software supply chain failures](../../security/audit/security-audit-reference.md#5-a032025--software-supply-chain-failures),
  in the Techversant security audit reference

**Level:** Practitioner · Optional

## Project: Threat-Model the Growth Design

**Brief:** Lantern's growth adds staff sign-in through Microsoft Entra ID, a mobile app, notifications and readers in
India and the EU. Threat-model the design from stages 02–05 and design the protections. This is design work: do not
write authentication or permission code for this project.

**Size:** 3 days

**Verification**, checked by a senior engineer:

- [ ] A data flow diagram shows every trust boundary, including the mobile app, the identity provider and external
  providers
- [ ] At least ten threats are recorded using STRIDE, each with a mitigation, an owner and a status
- [ ] The identity design shows how staff sign in through OpenID Connect and how Entra ID groups map to editor and
  moderator roles
- [ ] The design states where every secret lives and how it is rotated, and no secret appears in the repository
- [ ] Each mitigation is mapped to an item in the Techversant security audit checklist
- [ ] A privacy table lists each item of personal data, why it is needed, and how a reader can see or delete it
- [ ] The design names which parts are Red Zone work, and who will write and review them

Previous: [05. Reliability and Performance](./05-reliability-and-performance.md) · Next:
[07. Cloud and Cost](./07-cloud-and-cost.md)
