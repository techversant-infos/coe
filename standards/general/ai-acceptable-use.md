# AI Acceptable Use Standard

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-10 · **Next review:** 2027-05-10

**Version:** 0.2 (draft)

**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** TBD — Leadership approval  
**Contributors:** CoE Team; Leadership, Legal, and Security approvals pending

> **Draft for Leadership, Legal, and Security review. This standard is not effective until approved.**

## Table of Contents

- [1. Purpose and scope](#1-purpose-and-scope)
- [2. Approved tools register](#2-approved-tools-register)
- [3. Data classification and permitted use](#3-data-classification-and-permitted-use)
- [4. Client engagements and consent](#4-client-engagements-and-consent)
- [5. Prohibited uses](#5-prohibited-uses)
- [6. Human accountability and disclosure](#6-human-accountability-and-disclosure)
- [7. Incidents](#7-incidents)
- [8. Exceptions](#8-exceptions)
- [9. Enforcement and review](#9-enforcement-and-review)
- [10. Related documents](#10-related-documents)

## 1. Purpose and scope

This standard sets the permitted use of AI tools in Techversant work. It applies to all employees and contractors,
across every client engagement and internal project, when using AI to create, transform, analyze, or review work
products or data.

This document is a draft pending Leadership, Legal, and Security review. The approved-tools register and all
approval-dependent rules must be completed before the standard is marked Active.

## 2. Approved tools register

Approval applies to the exact product, plan, tenant, configuration, and model route. A vendor name or a
Techversant-provided API key alone does not establish approval. The entries below record current practice and
proposed scope; they do not approve a tool for non-public data.

| Tool/account route | Draft permitted scope | Training and retention evidence | Required before approval |
|--------------------|-----------------------|--------------------------------|--------------------------|
| Personal Claude (including Claude Code under a personal plan) | Public, open-source, or synthetic data only (proposed) | Consumer account settings govern model improvement; personal account retention applies. See [Anthropic consumer policy](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training). | Confirm the interim restriction and whether Techversant-managed access will replace personal use. |
| Personal Codex (personal ChatGPT account) | Public, open-source, or synthetic data only (proposed) | Personal account settings govern model improvement; personal-plan retention applies. See [OpenAI privacy settings](https://openai.com/consumer-privacy/). | Confirm the interim restriction and whether Techversant-managed access will replace personal use. |
| OpusMax, provided through Techversant | Public only until route review (proposed) | Published policy says prompts/responses are not retained; usage metadata is kept while the API key exists. Requests are forwarded to upstream model providers. | Identify the contracting/operator entity, exact upstream model routes, regions, upstream terms, data-processing agreement, and settings. |
| CodeMax, provided through Techversant | Public only until route review (proposed) | Published policy says prompts/responses are not retained and usage logs are retained up to 90 days. The reviewed policy does not specify model-training or upstream retention terms. | Identify the contracting/operator entity, exact upstream model routes, regions, upstream terms, data-processing agreement, and settings. |
| Cursor, GitHub Copilot, local LLM deployments, and other routes | TBD — Leadership/Security/Legal | TBD — by plan, model, deployment, and configuration | Complete a separate evidence review for each exact route before assigning data classes. |

The OpusMax and CodeMax statements above summarize their published [privacy policies](https://www.opusmax.pro/privacy)
and [terms](https://www.opusmax.pro/terms), and [CodeMax privacy policy](https://www.codemax.pro/privacy)
and [terms](https://www.codemax.pro/terms). These are provider statements, not independent verification of the
Techversant account, upstream provider, or contract. Upstream model providers may apply separate terms and
retention. Record those terms before approving any non-public data.

The current practice reported for personal Claude and Codex is broader than this draft's proposed scope. Personal
accounts should be limited to Public, open-source, or synthetic data unless Leadership, Security, and Legal
approve a documented alternative. Turning off model-improvement settings does not by itself establish business
contract terms, retention controls, or client authorization.

Before any entry is approved, record evidence for training use, prompt/output retention, usage metadata, data
location, sub-processors/upstream providers, access controls, and applicable terms. Legal and Security review the
evidence; Leadership approves the business use and permitted data classes.

## 3. Data classification and permitted use

Use Techversant's supplied classification categories below. **External Origin** describes where information came
from; it is not a sensitivity level. Apply the source's handling instructions, then classify the information under
the internal categories. If the source gives no instructions or the classification is unclear, pause and ask the
data owner or Security to classify it before use. Apply the strictest applicable handling rule.

| Classification | Examples and handling | AI use under this draft |
|---------------|-----------------------|-------------------------|
| Public Information | Approved for unrestricted access and distribution, such as published reports and marketing materials. | Use only with an AI route that is approved for Public Information. Do not include secrets or unpublished context. |
| Internal Use Information | Internal memos, procedures, and non-sensitive project documentation; accessible to employees and stored in internal systems, with encryption where specified by the classification guidance. | Use only with a route explicitly approved for Internal Use Information. The fact that personal accounts are currently used does not make them approved for Internal data. |
| Confidential Information | Financial records, employee personal information, strategic plans, and proprietary research; access restricted to authorized personnel, with encrypted storage and transmission and secure physical storage. | Do not submit to a route unless it is explicitly approved for Confidential Information and the applicable data owner, privacy, legal, and client requirements are met. |
| External Origin Information | Client data, partner agreements, and vendor documentation. Follow external handling instructions; if none exist, classify under internal guidelines. | Follow the source terms and internal classification. Client data must also meet the contract and client-authorization rules in §4. |

Personal data and regulated information require additional privacy and legal review even when their internal
classification is known. Client ownership, personal data, and regulatory obligations may overlap with any
classification above; apply the strictest rule. Unknown, unlisted, or unverified tool approval means the data must
not be submitted. Follow the Red Zone restrictions in
[AI Era Coding Guidelines §2.2](./ai-era-coding-guidelines.md#22-red-zone-manual-only).

These category names and handling summaries reflect the classification-guideline excerpt supplied for this draft.
Security must confirm the canonical policy source and link before approval.

## 4. Client engagements and consent

Before using AI with client data, check the engagement contract and applicable client instructions for AI-related
terms. **Proposed default, pending Legal approval:** if the contract is silent or unclear, treat that as no
authorization to submit client data to an external AI route. Use synthetic or properly redacted data while the
delivery lead raises the question with Legal and the client account owner. Resume only after Legal confirms the
contract position and any required written client authorization is obtained. Do not treat client authorization as
a substitute for a separate legal basis where privacy law requires one. The delivery lead records the approval in
the official contract repository and links it from the engagement's AI/tool register; the system-of-record location
is **TBD — Legal/Leadership**.

The contract-silent default and consent-record location remain pending Legal and Leadership approval. This draft
does not provide legal advice or amend client contract terms.

## 5. Prohibited uses

- Entering passwords, API keys, tokens, private keys, or other secrets into AI prompts or tools.
- Entering client data into a tool that is not approved for that data class, or before required client approval.
- Entering production data, PII, or regulated data into a tool unless the register explicitly approves that data
  class and the engagement's legal and contractual requirements permit the use.
- Delegating Red Zone work identified in [AI Era Coding Guidelines §2.2](./ai-era-coding-guidelines.md#22-red-zone-manual-only)
  to AI, including authentication/authorization, encryption/key management, PII/payment handling, and production
  database migrations.
- Bypassing required human review, security controls, client terms, or this standard.

## 6. Human accountability and disclosure

A named human must review, understand, and own every AI-assisted change before it is shipped. AI output does not
transfer accountability to the tool or its provider. Follow the human review and delegation requirements in
[AI Era Coding Guidelines §2](./ai-era-coding-guidelines.md#2-core-principle-human-accountability) and
[§3: Code Review & Ownership Standards](./ai-era-coding-guidelines.md#3-code-review--ownership-standards).

Disclose AI-assisted commits using the repository convention `[ai-assisted: <tool>]`. Do not include prompt content,
client information, or secrets in the disclosure.

## 7. Incidents

An AI data incident includes, for example, client or restricted data submitted to a tool not approved for that
class, a secret included in a prompt, or suspected unauthorized retention or disclosure of submitted data.

Report a suspected incident to **IT Security immediately** through the internal security incident channel or
contact directory. Notify the **Privacy Officer** at the same time if personal data may be involved. Escalate
significant, ongoing, or unclear incidents to the **Chief Information Security Officer**. The current role holders'
names and direct contact details are maintained in the internal directory and are not published in this public
repository. **Canonical reporting channel or role-based contact route:** TBD — Security; publish it in the internal
directory before this standard becomes Active.

The proposed internal reporting target is immediately, and no later than one hour after discovery; **Leadership and
Security must approve this target**. This is an internal reporting target, not a statutory GDPR notification period.
The Privacy Officer and Legal assess applicable duties: under GDPR, a controller notifies the supervisory authority
without undue delay and, where feasible, within 72 hours when required; a processor notifies its controller without
undue delay. Employees must not make client, regulator, or data-subject notifications unless authorized. Follow
[AI Security Guidelines §9](../../security/ai-security/ai-security-guidelines.md#9-incident-response) for response
steps and the [GDPR, Article 33](https://eur-lex.europa.eu/eli/reg/2016/679/ojv).

## 8. Exceptions

No exception may permit secrets or credentials in prompts, unapproved client data use, or transfer of ownership
away from the named human responsible for shipped work. Any other exception must be written, limited to a defined
scope and period, and include its rationale and safeguards. The engagement owner and Security must approve it;
Legal must also approve an exception involving client terms, personal data, or regulated data.

**Exception register and process owner:** TBD — Leadership/Security. No exception is effective until its approval
and record location are confirmed. Review approved exceptions before their expiry and revoke them when their
conditions no longer hold.

## 9. Enforcement and review

- **Engyne:** detects potential policy breaches against this standard.
- **AI Scaffold:** reminds engineers to follow this standard and links to this source.
- **CoE:** maintains the standard and audits adherence.

The CoE maintains the standard. The **Privacy Officer** reviews privacy provisions; **IT Security and the Chief
Information Security Officer** review incident handling, security controls, and security exceptions; Legal approves
client-data and contract provisions. Leadership approves the standard and accepts any residual business risk.
**Named Leadership approver:** TBD — Leadership. A second independent security approval is required under the
repository's security-document review process. The standard owner reviews it every six months and updates the next
review date. Material changes require the same approval roles.

## 10. Related documents

- [AI Era Coding Guidelines](./ai-era-coding-guidelines.md)
- [AI Security Guidelines §9: Incident Response](../../security/ai-security/ai-security-guidelines.md#9-incident-response)
- [Contributing to CoE Standards](../../CONTRIBUTING.md)
