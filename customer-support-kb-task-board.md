---
type: task-board
status: active
owner: customer-support-kb
last_updated: 2026-05-10
source_of_truth: true
---

# Customer Support KB Task Board

This file is the single source of truth for building the customer-facing intelligent support knowledge base.

Any agent continuing this work must read this file first before creating, editing, or extracting any customer support knowledge.

## 1. Project Goal

Build a Chinese draft knowledge base for a C-end intelligent customer support assistant.

The assistant should be able to answer user questions about:

1. Registration / Login
2. KYC / Identity Verification / Wallet Opening
3. Wallet Asset / Deposit / Send / Swap
4. Card Application / Manage / Transaction
5. Notification / System Email
6. Website / FAQ

The knowledge base must support:

- FAQ
- Standard customer-facing answers
- Troubleshooting flows
- Boundaries for questions that cannot be answered
- Human handoff / escalation rules
- Verification status for every major knowledge block

## 2. Key Decisions Already Confirmed

| Decision Area | Confirmed Decision |
|---|---|
| Target users | C-end users |
| Knowledge base type | Draft customer support KB, to be reviewed later |
| Language | Chinese first; English translation later |
| Repository location | Create a new top-level directory: `customer-support-kb/` |
| Visibility | Must separate user-facing content from internal agent-only content |
| Source document exposure | Do not expose source document paths or PRD/archive references in user-facing answers |
| Archive usage | `archive/` can be used as source material, but historical PRDs are not current product truth |
| Verification | First extracted version should default to `draft_pending_review` unless explicitly confirmed |

## 3. Non-Negotiable Rules

1. Do not modify `archive/` source documents for this task.
2. Do not let user-facing answers mention PRD, legacy PRD, archive paths, source files, or internal document names.
3. Do not treat historical PRD content as current product truth.
4. Do not invent unsupported product rules, fees, limits, countries, card availability, supported chains, supported assets, review time, or transaction processing time.
5. If a rule is useful but unconfirmed, put it in `customer-support-kb/unresolved/pending-confirmation.md`.
6. If a topic should not be answered by the bot, put it in `customer-support-kb/unresolved/do-not-answer.md`.
7. User-facing content must be safe, concise, and written in Chinese.
8. Internal-only information must stay under `customer-support-kb/agent-internal/`.
9. Every content file should include frontmatter with `visibility`, `language`, and `verification_status`.
10. This task board is the single source of truth for task status and continuation.

## 4. Created Directory Structure

```text
customer-support-kb/
  README.md
  _answer-policy.md
  _visibility-rules.md
  _verification-status.md
  _handoff-rules.md

  user-facing/
    registration-login.md
    kyc-wallet-opening.md
    wallet-asset.md
    wallet-deposit-send-swap.md
    card-application-manage.md
    transaction-history.md
    notification-system-email.md
    website-faq.md
    general-faq.md

  agent-internal/
    registration-login-playbook.md
    kyc-wallet-opening-playbook.md
    wallet-playbook.md
    card-playbook.md
    transaction-playbook.md
    notification-playbook.md
    escalation-playbook.md

  faq/
    faq-index.md
    registration-login-faq.md
    kyc-faq.md
    wallet-faq.md
    card-faq.md
    transaction-faq.md
    notification-faq.md
    website-faq.md

  unresolved/
    pending-confirmation.md
    do-not-answer.md
```

## 5. Source Material Mapping For Extraction

Use these archive paths only as internal source material. Do not expose these paths in user-facing answers.

| Target KB Area | Internal Source Direction | Priority | Extraction Status |
|---|---|---:|---|
| Registration / Login | `archive/legacy-prd/app/registration-login/` | P0 | archive_reviewed_draft |
| KYC / Wallet Opening | `archive/legacy-prd/kyc/wallet-opening/` | P0 | archive_reviewed_draft |
| Identity Verification | `archive/legacy-prd/security/identity-verification/` | P0 | archive_reviewed_draft |
| Wallet Asset | `archive/legacy-prd/wallet/asset/` | P0 | archive_reviewed_draft |
| Wallet Deposit / Send / Swap | `archive/legacy-prd/wallet/deposit-send-swap/` | P0 | archive_reviewed_draft |
| Card Application | `archive/legacy-prd/card/application/` | P1 | archive_reviewed_draft |
| Card Manage | `archive/legacy-prd/card/manage/` | P1 | archive_reviewed_draft |
| Card Transaction | `archive/legacy-prd/card/transaction/` | P1 | archive_reviewed_draft |
| Card Me/Profile | `archive/legacy-prd/card/me/` | P1 | archive_reviewed_draft |
| Transaction History | `archive/legacy-prd/app/transaction-history/` | P1 | archive_reviewed_draft |
| Notification / Push Inbox | `archive/legacy-prd/notification/push-inbox/` | P1 | archive_reviewed_draft |
| System Email | `archive/legacy-prd/notification/system-email/` | P1 | archive_reviewed_draft |
| App FAQ | `archive/legacy-prd/app/faq/` | P1 | archive_reviewed_draft |
| Website | `archive/legacy-prd/website/phase-1/`, `phase-2/`, `waitlist-addition/`, `waitlist-campaign/` | P2 | archive_reviewed_draft |

## 6. File Content Standards

### 6.1 User-facing content file template

Use this structure for files under `customer-support-kb/user-facing/`:

```md
---
module: module-name
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 中文标题

## 适用问题

- 用户可能会问的问题 1
- 用户可能会问的问题 2

## 标准答案

### 问题标题

面向用户的简洁中文回答。

## 排查流程

1. 第一步。
2. 第二步。
3. 如仍无法解决，建议联系人工客服。

## 转人工边界

以下情况建议转人工：

- 情况 1
- 情况 2

## 确认状态

- status: draft_pending_review
- note: 该内容为初稿，需业务审核后才能作为正式客服口径。
```

### 6.2 Internal playbook template

Use this structure for files under `customer-support-kb/agent-internal/`:

```md
---
module: module-name
audience: support-agent
visibility: internal
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 中文标题 Playbook

## 适用场景

## 客服先确认

## 可向用户询问的信息

## 建议处理步骤

## 可使用的用户回复口径

## 必须升级的情况

## 不要向用户透露
```

### 6.3 FAQ item format

Use this format for files under `customer-support-kb/faq/`:

```md
## Q: 用户问题

### 推荐回答

中文回答。

### 分类

- module: module-name
- intent: intent-name
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工的情况：

- 情况 1
- 情况 2
```

## 7. Task List

| ID | Task | Output | Status | Notes |
|---|---|---|---|---|
| CSKB-001 | Create `customer-support-kb/` skeleton | Directory and base policy files | done | Created base directory and policy files |
| CSKB-002 | Create answer policy | `customer-support-kb/_answer-policy.md` | done | Prevents source exposure and hallucinated rules |
| CSKB-003 | Create visibility rules | `customer-support-kb/_visibility-rules.md` | done | Separates user-facing vs internal |
| CSKB-004 | Create verification status definitions | `customer-support-kb/_verification-status.md` | done | Default extracted content to draft_pending_review |
| CSKB-005 | Create handoff rules | `customer-support-kb/_handoff-rules.md` | done | Includes account, KYC, wallet, card, transaction escalation |
| CSKB-006 | Create unresolved files | `pending-confirmation.md`, `do-not-answer.md` | done | Created before extraction |
| CSKB-007 | Extract Registration / Login user-facing draft | `user-facing/registration-login.md` and `faq/registration-login-faq.md` | archive_reviewed_draft | Reviewed registration and identity verification content; still needs business review |
| CSKB-008 | Extract Registration / Login internal playbook | `agent-internal/registration-login-playbook.md` | archive_reviewed_draft | Reviewed legacy PRD and refined troubleshooting |
| CSKB-009 | Extract KYC / Wallet Opening user-facing draft | `user-facing/kyc-wallet-opening.md` and `faq/kyc-faq.md` | archive_reviewed_draft | Reviewed KYC wallet-opening and identity verification content |
| CSKB-010 | Extract KYC internal playbook | `agent-internal/kyc-wallet-opening-playbook.md` | archive_reviewed_draft | Compliance details remain unresolved |
| CSKB-011 | Extract Wallet Asset user-facing draft | `user-facing/wallet-asset.md` | archive_reviewed_draft | Reviewed wallet asset PRD; supported assets unresolved |
| CSKB-012 | Extract Wallet Deposit / Send / Swap user-facing draft | `user-facing/wallet-deposit-send-swap.md` and `faq/wallet-faq.md` | archive_reviewed_draft | Reviewed key Deposit/Send/Swap content; availability and limits require confirmation |
| CSKB-013 | Extract Wallet internal playbook | `agent-internal/wallet-playbook.md` | archive_reviewed_draft | Reviewed wallet PRDs and refined playbook |
| CSKB-014 | Extract Card user-facing draft | `user-facing/card-application-manage.md` and `faq/card-faq.md` | archive_reviewed_draft | Reviewed Card Application / Manage / Transaction / Me; many commercial rules unresolved |
| CSKB-015 | Extract Card internal playbook | `agent-internal/card-playbook.md` | archive_reviewed_draft | Reviewed Card Application / Manage / Transaction / Me |
| CSKB-016 | Extract Transaction History user-facing draft | `user-facing/transaction-history.md` and `faq/transaction-faq.md` | archive_reviewed_draft | Reviewed Transaction History archive; status definitions and query scope require confirmation |
| CSKB-017 | Extract Transaction internal playbook | `agent-internal/transaction-playbook.md` | archive_reviewed_draft | Reviewed Transaction History archive and refined playbook |
| CSKB-018 | Extract Notification / System Email user-facing draft | `user-facing/notification-system-email.md` and `faq/notification-faq.md` | archive_reviewed_draft | Reviewed Push/Inbox and System Email archives; official email/domain rules unresolved |
| CSKB-019 | Extract Notification internal playbook | `agent-internal/notification-playbook.md` | archive_reviewed_draft | Reviewed Push/Inbox and System Email archives |
| CSKB-020 | Extract Website / Waitlist FAQ draft | `user-facing/website-faq.md` and `faq/website-faq.md` | archive_reviewed_draft | Reviewed Website phase 1/2 and Waitlist archives; status, rewards, links, and regions unresolved |
| CSKB-021 | Create general FAQ index | `faq/faq-index.md` and `user-facing/general-faq.md` | done | Created common-intent entry files |
| CSKB-022 | Review all files for source leakage | All user-facing and FAQ files | pending | Must still run explicit review |
| CSKB-023 | Review all files for unsupported claims | All files | pending | Must still run explicit review; many details intentionally unresolved |
| CSKB-024 | Final consistency pass | Entire `customer-support-kb/` | pending | Check status labels, visibility, language, handoff rules |

## 8. Current Status

Current phase: archive-reviewed drafts completed for P0, P1, and P2 target modules. Review phase pending.

Completed:

- Confirmed target users, scope, language, visibility split, output directory, and priority modules.
- Reviewed archive structure enough to identify relevant source directions.
- Created this task board as the single source of truth.
- Created `customer-support-kb/` directory structure and base policy files.
- Created unresolved files.
- Created initial Chinese safe-draft files under `user-facing/`, `agent-internal/`, and `faq/`.
- Reviewed and refined P0 files from archive material:
  - Registration / Login
  - Identity Verification
  - KYC / Wallet Opening
  - Wallet Asset
  - Wallet Deposit / Send / Swap
- Reviewed and refined P1 Card files from archive material:
  - Card Application
  - Card Manage
  - Card Transaction
  - Card Me/Profile
- Expanded `unresolved/pending-confirmation.md` with identity verification and Card details that require business confirmation.

Not yet completed:

- No content has been business-reviewed or confirmed.
- Source leakage review is still pending.
- Unsupported-claim review is still pending.
- Final consistency pass is still pending.

## 9. Next Agent Instructions

The next agent should proceed in this order:

1. Read this file first.
2. Treat existing `customer-support-kb/` files as draft content, not final confirmed content.
3. Run source leakage review for all `user-facing/` and `faq/` files.
4. Run unsupported-claim review for all files.
5. Run final consistency pass for the entire `customer-support-kb/` directory.
6. Keep all content as `draft_pending_review` unless there is explicit business confirmation.
7. Do not expose source paths in user-facing answers.
8. Move uncertain details into `customer-support-kb/unresolved/pending-confirmation.md`.
9. Move unsafe/non-answerable topics into `customer-support-kb/unresolved/do-not-answer.md`.
10. Update this task board after every meaningful change.

## 10. Change Log

| Date | Change |
|---|---|
| 2026-05-10 | Created task board for customer support KB buildout. |
| 2026-05-10 | Created `customer-support-kb/` skeleton, base policy files, unresolved files, safe user-facing drafts, internal playbooks, and FAQ drafts. |
| 2026-05-10 | Reviewed P0 archive material and refined Registration/Login, KYC Wallet Opening, Wallet Asset, and Wallet Deposit/Send/Swap drafts. |
| 2026-05-10 | Reviewed identity verification and P1 Card archive material; refined Registration/Login, Card user-facing FAQ, Card playbook, and pending confirmations. |
| 2026-05-10 | Reviewed P1 Transaction History, P1 Notification/System Email/App FAQ, and P2 Website/Waitlist material; refined related user-facing, FAQ, playbook, and pending-confirmation files. |
