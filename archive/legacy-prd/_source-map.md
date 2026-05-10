# Legacy PRD Source Map

This file maps legacy PRD documents to confirmed or pending knowledge-base content.

It is intentionally conservative. A legacy PRD should not be treated as current product truth unless its relevant facts have been reviewed and extracted into `knowledge-base/` or confirmed by another approved current source.

## Status meaning

- `ingested`: confirmed facts have been extracted to `knowledge-base/`.
- `partially-ingested`: only part of the legacy PRD is confirmed in `knowledge-base/`.
- `pending-review`: the legacy PRD has not been fully reviewed for current relevance.
- `legacy-only`: kept only for historical reference.
- `deprecated`: known to be outdated or removed.

## General source rule

When using a legacy PRD:

1. Check whether the relevant topic exists in `knowledge-base/`.
2. If yes, use the `knowledge-base/` file as current truth.
3. If no, treat the legacy content as historical context only.
4. If the legacy content looks useful but unconfirmed, add or reference a pending item in `knowledge-base/changelog/knowledge-gaps.md`.

## Module-level mapping

| Legacy area | Knowledge-base area | Default status | Notes |
|---|---|---:|---|
| App legacy PRDs | `knowledge-base/app/` or related module files | pending-review | Use only for app-level historical context unless confirmed. |
| Wallet legacy PRDs | `knowledge-base/wallet/` and related transaction files | pending-review | Wallet features such as asset, deposit, send, swap, and transaction logic require KB confirmation. |
| Card legacy PRDs | `knowledge-base/card/` and related transaction files | pending-review | Card flows, limits, provider behavior, and status rules require KB confirmation. |
| KYC legacy PRDs | `knowledge-base/kyc/` or compliance-related files | pending-review | KYC requirements may be compliance-sensitive and must not be inferred from old PRDs. |
| Transaction legacy PRDs | `knowledge-base/transaction/` and module-specific transaction files | pending-review | Transaction statuses, fields, and display logic must follow current KB if available. |

## File-level mapping template

When a legacy PRD is reviewed, add a row under the relevant section using this format:

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| `path/to/legacy-file.md` | `knowledge-base/module/file.md` | partially-ingested | Briefly describe what was extracted and what remains pending. |

## App

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| TBD | TBD | pending-review | Add reviewed app legacy PRDs here. |

## Wallet

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| TBD | TBD | pending-review | Add reviewed wallet legacy PRDs here. |

## Card

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| TBD | TBD | pending-review | Add reviewed card legacy PRDs here. |

## KYC

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| TBD | TBD | pending-review | Add reviewed KYC legacy PRDs here. |

## Transaction

| Legacy PRD | Knowledge-base file | Status | Notes |
|---|---|---|---|
| TBD | TBD | pending-review | Add reviewed transaction legacy PRDs here. |
