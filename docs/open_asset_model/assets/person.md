# :simple-owasp: Person

The **Person** asset type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) represents an individual human being discovered as part of intelligence collection, attribution, or enrichment processes. Persons may appear in public records, domain registrations, technical contacts, breached datasets, or OSINT sources and often serve as pivots for understanding organizational relationships or behavioral patterns.

- **Definition:** A `Person` asset encapsulates identifying attributes such as full legal name, date of birth, and gender. It may represent a registrant, technical contact, executive, threat actor, or any other discovered individual.

- **Purpose:** Modeling people as structured assets allows for attribution graphs, ownership resolution, and behavioral correlation across disparate data points. Individuals are often central to understanding the provenance, intent, or organizational structure behind assets like domains, IP ranges, or certificates.

- **Design Choice:** The `Person` structure includes multiple levels of name granularity to enable flexible matching and entity resolution. Optional fields (e.g., `birth_date`, `gender`) support deeper analysis when present, but are not required—ensuring compatibility with incomplete or privacy-preserving sources. The model avoids sensitive personal information (e.g., national IDs) unless already exposed via legitimate public data sources.

## :material-account: Person Attributes

| Attributes     | Type   | Required | Description |
|:--------------:|:------:|:--------:|:------------|
| `unique_id`    | string | :material-check-decagram: | Unique identifier for the person asset |
| `full_name`    | string | :material-check-decagram: | Complete name string (e.g., `"Jane Elizabeth Smith"`) |
| `first_name`   | string | :material-check-decagram: | Given name or forename |
| `middle_name`  | string | :material-checkbox-blank-circle-outline: | Optional middle name(s) or initials |
| `family_name`  | string | :material-check-decagram: | Surname or last name |
| `birth_date`   | string | :material-checkbox-blank-circle-outline: | Optional date of birth (ISO format) |
| `gender`       | string | :material-checkbox-blank-circle-outline: | Optional gender descriptor (e.g., `female`, `nonbinary`) |

## :material-account: Person Properties

| Property Type | Property Name | Description |
|:-------------:|:-------------:|:------------|
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this Person |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this Person |

## :material-account: Person Outgoing Relations

```mermaid
graph TD
person["Person (Jane E. Smith)"]
ident["Identifier"]
idRel@{ shape: braces; label: "id" }
person --o idRel
idRel --> ident

loc["Location (Street Address)"]
locRel@{ shape: braces; label: "address" }
person --o locRel
locRel --> loc

phone["Phone"]
phoneRel@{ shape: braces; label: "phone" }
person --o phoneRel
phoneRel --> phone

acct["Account"]
account@{ shape: braces; label: "account" }
person --o account
account --> acct
```

---

| Relation Type       | Relation Label     | Target Assets    | Description   |
| :-----------------: | :----------------: | :--------------: | :------------ |
| [`SimpleRelation`](../relations/simple_relation.md) | `id` | [`Identifier`](./identifier.md) | Links the `Person` to another `Identifier`, such as a maiden name |
| [`SimpleRelation`](../relations/simple_relation.md) | `address` | [`Location`](./location.md) | Links the `Person` to a discovered street address |
| [`SimpleRelation`](../relations/simple_relation.md) | `phone` | [`Phone`](./phone.md) | Links the `Person` to a discovered phone number, such as a cell phone |
| [`SimpleRelation`](../relations/simple_relation.md) | `account` | [`Account`](./account.md) | An account owned or used by the Person, such as an email account |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*