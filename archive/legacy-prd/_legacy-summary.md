# Legacy PRD Summary

This directory contains historical AIX PRDs converted from old Word documents.

## Purpose

Legacy PRDs are used for:

- Understanding historical product design.
- Verifying where a requirement came from.
- Comparing old and new product behavior.
- Recovering missing context when `knowledge-base/` is incomplete.
- Supporting migration or clean-up of old product requirements.

## Important rule

Legacy PRDs are not current product truth.

Current product truth must come from:

- `knowledge-base/`
- approved current PRDs
- confirmed user decisions
- current reference data
- external official documents

## Recommended AI behavior

When answering product questions or writing new PRDs:

1. Read `knowledge-base/_ai-query-router.md` first.
2. Use confirmed knowledge-base files as the primary source.
3. Use legacy PRDs only after the current knowledge-base path is checked.
4. Clearly separate confirmed facts from historical references.
5. If a historical requirement is useful but unconfirmed, mark it as pending confirmation.
6. Do not silently promote historical requirements into current scope.

## Main historical areas

### App

Historical documents about app-level experience, navigation, onboarding, account, homepage, profile, and general product flows.

### Wallet

Historical documents about assets, deposit, send, swap, transaction history, and wallet-related user flows.

### Card

Historical documents about card application, card management, card transactions, card controls, and card-related flows.

### KYC

Historical documents about identity verification, onboarding compliance, verification levels, status handling, and review flows.

### Transaction

Historical documents about transaction history, transaction details, status handling, deposits, withdrawals, card transactions, and internal transfers.

## Known risks

- Some legacy features may have been removed.
- Some flows may no longer match current implementation.
- Some field names or page names may have changed.
- Some requirements may conflict with current `knowledge-base/` content.
- Some legacy PRDs may describe planned behavior that was never implemented.
- Some compliance-related details may be outdated and must be re-confirmed.

## Decision rule

If legacy content and current knowledge-base content conflict, follow current knowledge-base content.

If current knowledge-base content is missing, do not assume the legacy content is active. Treat it as historical context and create or reference a pending confirmation item.
