# :simple-owasp: ContactRecord

The **ContactRecord** asset serves as a connective entity that maintains a reliable audit trail of where contact information was discovered during the *attack surface intelligence* collection process. It plays a critical role in ensuring both flexibility and consistency within the [Open Asset Model](https://github.com/owasp-amass/open-asset-model), as it is uniformly applied wherever contact details are identified—regardless of the specific type of contact information uncovered. Because such information is often found in varied groupings, it's important to preserve the context in which each piece was associated. The **ContactRecord** makes this possible by capturing and storing the discovered contact data alongside its source location, maintaining their relationship within the model.

## :material-contacts: ContactRecord Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `discovered_at` | string | :material-check-decagram: | Unique URL or path to the contact information |

## :material-contacts: ContactRecord Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this ContactRecord |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this ContactRecord |

## :material-contacts: ContactRecord Outgoing Relations

```mermaid
graph TD
contact["ContactRecord"]
fqdn["FQDN"]

simple1@{ shape: braces, label: "fqdn"}
contact --o simple1
simple1 --> fqdn

id["Identifier"]
simple2@{ shape: braces, label: "id"}
contact --o simple2
simple2 --> id

org["Organization"]
simple3@{ shape: braces, label: "organization"}
contact --o simple3
simple3 --> org

person["Person"]
simple4@{ shape: braces, label: "person"}
contact --o simple4
simple4 --> person

phone["Phone"]
simple5@{ shape: braces, label: "phone"}
contact --o simple5
simple5 --> phone

url["URL"]
simple6@{ shape: braces, label: "url"}
contact --o simple6
simple6 --> url
```

---

| Relation Type       | Relation Label     | Target Assets    | Description   |
| :-----------------: | :----------------: | :--------------: | :------------ |
| [`SimpleRelation`](../relations/simple_relation.md) | `fqdn` | [`FQDN`](./fqdn.md) | Represents a FQDN discovered in the contact information |
| [`SimpleRelation`](../relations/simple_relation.md) | `id` | [`Identifier`](./identifier.md) | Represents an ID (e.g. email address) in the contact information |
| [`SimpleRelation`](../relations/simple_relation.md) | `organization` | [`Organization`](./organization.md) | Represents an organization name in the contact information |
| [`SimpleRelation`](../relations/simple_relation.md) | `person` | [`Person`](./person) | Represents a person's name discovered with the contact information |
| [`SimpleRelation`](../relations/simple_relation.md) | `phone` | [`Phone`](./phone.md) | Represents a phone number in the contact information |
| [`SimpleRelation`](../relations/simple_relation.md) | `url` | [`URL`](./url.md) | Represents an URL discovered in the contact information |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
