# Legacy PRD Module Map

This file helps AI locate relevant historical PRDs by product module.

The mappings here are navigation aids only. They do not mean the linked legacy requirements are current product facts.

## AI usage rule

- Use `knowledge-base/` as current truth.
- Use legacy PRDs only for historical reference, source verification, or comparison.
- If a legacy requirement is not confirmed in `knowledge-base/`, treat it as pending confirmation.

## App

Related legacy PRDs may include app-level experience, navigation, onboarding, account, homepage, profile, and general product flows.

Use for:

- Historical app structure and user experience reference.
- Old navigation or page behavior comparison.
- Recovering context when current knowledge-base content is incomplete.

Do not use for:

- Current information architecture unless confirmed in `knowledge-base/`.
- Current page copy or field definitions unless confirmed.

## Wallet

Related legacy PRDs may include assets, deposit, send, swap, transaction history, wallet addresses, and wallet-related flows.

Use for:

- Historical wallet feature design.
- Old deposit, send, swap, asset, and transaction logic.
- Source verification for wallet requirements.

Do not use for:

- Current active wallet scope unless confirmed in `knowledge-base/`.
- Current supported assets, chains, fees, statuses, or limits unless confirmed.

## Card

Related legacy PRDs may include card application, card management, card transactions, card controls, and card-related user flows.

Use for:

- Historical card feature design.
- Old card application and transaction flow comparison.
- Source verification for card-related requirements.

Do not use for:

- Current card provider behavior, card limits, fee rules, or compliance rules unless confirmed.

## KYC

Related legacy PRDs may include identity verification, onboarding compliance, verification levels, status handling, and review flows.

Use for:

- Historical KYC and onboarding flow reference.
- Old identity verification requirements.
- Source verification for KYC-related product decisions.

Do not use for:

- Current compliance policy, verification provider behavior, country support, or risk rules unless confirmed.

## Transaction

Related legacy PRDs may include transaction history, transaction details, status handling, deposits, withdrawals, card transactions, and internal transfers.

Use for:

- Historical transaction model comparison.
- Old status naming and record display logic.
- Source verification for transaction-related requirements.

Do not use for:

- Current transaction status model, display fields, or ledger behavior unless confirmed.

## Other modules

For modules not explicitly listed here, first check `knowledge-base/_ai-query-router.md` and the relevant `knowledge-base/` module. Only search this legacy archive when current knowledge-base content references a legacy source or when historical context is required.
