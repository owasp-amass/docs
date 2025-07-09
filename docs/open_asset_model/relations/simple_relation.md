# :simple-owasp: SimpleRelation

The **SimpleRelation** in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) is the most straightforward way to express a connection between two assets.

- **Definition:** A `SimpleRelation` signifies a directed relationship from one asset to another, capturing things like `dns_record`, `contains`, or `announces`, without added complexity or metadata. It links one asset (the subject) to another (the object).

- **Purpose:** It models basic asset interdependencies or associations that are essential for understanding attack surface connectivity. By mapping these simple links, organizations can trace how one asset might depend on or enable another from a security standpoint.

- **Design Choice:** The model intentionally avoids over-engineering by excluding rich semantics or additional fields like roles, weights, or descriptions in a `SimpleRelation`. For more detailed modeling, other specialized relation types can be used.

In essence, the `SimpleRelation` is a clean, minimal tool used within the OAM to express direct and uncomplicated connections between assets, helping maintain clarity while capturing essential connectivity information.

## :material-relation-one-to-one: SimpleRelation Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `label` | string | :material-check-decagram: | The label for the relation between two assets |

## :material-relation-one-to-one: SimpleRelation Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this SimpleRelation |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
