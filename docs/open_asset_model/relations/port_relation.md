# :simple-owasp: PortRelation

The **PortRelation** in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) captures the association between an asset and a specific network port.

- **Definition:** A `PortRelation` denotes that a network port (identified by its number and protocol, e.g., TCP/80) is *exposed* or *served by* a given asset. It maps the fact that an asset either offers or uses a service on a designated port.

- **Purpose:** This relation is essential for modeling network-level exposure of assets. By linking an asset to its port(s), security practitioners can better understand which assets are externally accessible or internally listening, which is critical knowledge for attack surface mapping and vulnerability assessment.

- **Design Choice:** Unlike `SimpleRelation`, `PortRelation` includes the port identifier and protocol as structured metadata, giving more granularity. It avoids over-specification (e.g. connection counts or performance details) and focuses on capturing *which* port is involved and *how* (via protocol).

In essence, `PortRelation` adds precise network exposure context to the OAM, letting teams visualize and assess attack vectors related to service ports without unnecessary detail.

## :material-relation-one-to-one: PortRelation Attributes

| Attributes | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `label` | string | :material-check-decagram: | The label for the relation between two assets |
| `port_number` | number | :material-check-decagram: | The number assigned to the discovered port |
| `protocol` | string | :material-check-decagram: | The protocol stack of the specified port |

## :material-relation-one-to-one: PortRelation Properties

| Property Type | Property Name | Description |
| :--------------: | :---------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this relationship |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this PortRelation |
