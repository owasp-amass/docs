# :simple-owasp: FundsTransfer

The **FundsTransfer** asset type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) represents the movement of funds between two financial accounts. These transfers may occur via wire, ACH, cryptocurrency, internal bank movement, or other mechanisms that involve the exchange of currency between accounts or organizations.

- **Definition:** A `FundsTransfer` asset models a single financial transaction involving a specific amount of money, a method of transfer, a currency type, and optionally, reference and exchange data.

- **Purpose:** Including `FundsTransfer` in the asset model enables reasoning about **financial flows**, which can assist in analyzing operational patterns, detecting anomalies, or tracing value exchanges between entities. When connected to `Account` assets, it supports graph-based queries that explore supply chains, fraud trails, and inter-organizational dependencies.

- **Design Choice:** This type focuses on capturing the *structure* of a transfer (e.g., amount, method, and timing) rather than sensitive or regulated content (like full account numbers). Optional fields like `exchange_rate` allow the model to support cross-currency scenarios and future integration with financial intelligence tooling, while keeping the core schema minimal and auditable.

## :material-cash-multiple: FundsTransfer Attributes

| Attributes         | Type     | Required | Description |
|:------------------:|:--------:|:--------:|:------------|
| `unique_id`        | string   | :material-check-decagram: | Unique identifier for the transaction |
| `amount`           | float    | :material-check-decagram: | Monetary value of the transfer |
| `reference_number` | string   | :material-checkbox-blank-circle-outline: | Transaction reference code (e.g., SWIFT, internal ID) |
| `currency`         | string   | :material-checkbox-blank-circle-outline: | ISO 4217 currency code (e.g., `USD`, `EUR`, `BTC`) |
| `transfer_method`  | string   | :material-checkbox-blank-circle-outline: | Method used (e.g., `wire`, `ACH`, `crypto`) |
| `exchange_date`    | string   | :material-checkbox-blank-circle-outline: | Date when currency exchange (if any) occurred |
| `exchange_rate`    | float    | :material-checkbox-blank-circle-outline: | Rate used for currency conversion, if applicable |

## :material-cash-multiple: FundsTransfer Properties

| Property Type | Property Name | Description |
|:-------------:|:-------------:|:------------|
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this FundsTransfer |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this FundsTransfer |

## :material-cash-multiple: FundsTransfer Outgoing Relations

```mermaid
graph TD
transfer["FundsTransfer ($5,000 USD)"]
ident["Identifer"]
idRel@{ shape, braces; label: "id" }
transfer --o idRel
idRel --> ident

acct1["Account (acct-123)"]
fromRel@{ shape: braces; label: "sender" }
transfer --o fromRel
fromRel --> acct1

acct2["Account (acct-456)"]
toRel@{ shape: braces; label: "recipient" }
transfer --o toRel
toRel --> acct2

org["Organization"]
third@{ shape: braces; label: "third_party" }
transfer --o third
third --> org
```

---

| Relation Type       | Relation Label     | Target Assets    | Description   |
| :-----------------: | :----------------: | :--------------: | :------------ |
| [`SimpleRelation`](../relations/simple_relation.md) | `id` | [`Identifier`](./identifier.md) | Links the FundsTransfer to `Identifier` assets, such as confirmation numbers |
| [`SimpleRelation`](../relations/simple_relation.md) | `sender` | [`Account`](./account.md) | Links the FundsTransfer to the `Account` that sent the funds |
| [`SimpleRelation`](../relations/simple_relation.md) | `recipient` | [`Account`](./account.md) | Links the FundsTransfer to the `Account` that received the funds |
| [`SimpleRelation`](../relations/simple_relation.md) | `third_party` | [`Organization`](./organization.md) | A third-party sender that initiates a funds transfer on behalf of another party |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*