# AI Acceptable Use Standard

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-05-09

**Version:** 0.1 (draft)  
**Issued by:** Techversant Center of Excellence (CoE)  
**Effective Date:** TBD — Leadership approval  
**Contributors:** CoE Team; Leadership, Legal, and Security reviewers TBD

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

Approval applies to the specific product, plan, tenant, and configuration listed below. A vendor name alone does
not establish approval. A blank or TBD entry means the tool is not approved for that data class.

| Tool and plan | Tenant/configuration | Data classes allowed | Training on Techversant/client data | Retention | Evidence/source | Approved by and date |
|--------------|----------------------|----------------------|--------------------------------------|-----------|-----------------|----------------------|
| TBD — Leadership/Legal | TBD — Security | TBD — Leadership/Legal | TBD — Legal | TBD — Legal | TBD — Legal/Security | TBD — approver |

Before an entry is approved, record the service terms and settings that establish whether submitted data is used
for model training, how long prompts and outputs are retained, and relevant processing or data location
constraints. Legal and Security review the evidence; Leadership approves the business use and permitted data
classes. Do not infer these properties from a product name or marketing statement.

## 3. Data classification and permitted use

The following working categories are used for this draft. Security must confirm that they align with Techversant's
authoritative classification scheme before approval. A dataset may belong to more than one category; apply the
most restrictive applicable rule.

| Data class | Meaning in this draft | AI use |
|------------|----------------------|--------|
| Public | Information approved for public release | May be used only with a tool approved for Public data. |
| Internal | Non-public Techversant information that is not client confidential or sensitive/regulated | May be used only with a tool approved for Internal data. |
| Client confidential | Client-provided or client-derived information subject to confidentiality obligations | Do not submit until the engagement's contract/consent requirements are met and the tool is approved for this class. |
| PII | Information that identifies or can reasonably identify a person | Do not submit unless the tool is explicitly approved for PII and the engagement, privacy, and legal requirements permit it. |
| Regulated or restricted | Information subject to legal, regulatory, contractual, or heightened security controls, including payment data | Do not submit unless the tool and use are explicitly approved for the specific data type and applicable obligations. |

No client data may be entered into a tool unless the register explicitly approves that tool configuration for the
applicable data class. Unknown, unlisted, or unverified approval means the data must not be submitted. Follow the
Red Zone restrictions in [AI Era Coding Guidelines §2.2](./ai-era-coding-guidelines.md#22-red-zone-manual-only).

## 4. Client engagements and consent

Before using AI with client data, check the engagement contract and applicable client instructions for AI-related
terms. If the contract is silent or unclear, do not submit client data until Legal confirms the default and the
client's required approval is obtained. The delivery lead is responsible for obtaining and recording written
client consent when required; the record location is **TBD — Legal/Leadership**. Link the record from the engagement's
approved client records or decision log once the authoritative location is set.

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

Report a suspected incident to the Security Lead immediately using the established security incident process.
**Reporting channel/contact details:** TBD — Security. **Formal reporting deadline:** TBD — Leadership/Security.
Until those details are approved and published, do not wait for confirmation before notifying the Security Lead.
Follow [AI Security Guidelines §9](../../security/ai-security/ai-security-guidelines.md#9-incident-response) for
incident response steps.

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

Leadership approves the standard; Legal approves the client-data and contract provisions; Security reviews the
security and data-handling provisions. **Named Leadership approver:** TBD — Leadership. The standard owner reviews
it every six months and updates the next review date. Material changes require the same approval roles.

## 10. Related documents

- [AI Era Coding Guidelines](./ai-era-coding-guidelines.md)
- [AI Security Guidelines §9: Incident Response](../../security/ai-security/ai-security-guidelines.md#9-incident-response)
- [Contributing to CoE Standards](../../CONTRIBUTING.md)
