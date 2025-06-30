# :simple-owasp: BasicDNSRelation

The **BasicDNSRelation** in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) represents a minimal DNS resource record that links a DNS name to either another DNS name or an IP address, using only standard DNS header information.

- **Definition:** A `BasicDNSRelation` captures DNS records such as A, AAAA, or CNAME that map a hostname to another hostname or IP address. It includes only the DNS header fields and the target reference, without storing extended metadata or record-specific attributes.

- **Purpose:** This relation type is designed to reflect simple DNS resolution chains within the asset model. It allows mapping how DNS names ultimately resolve to assets or addresses, which is fundamental for understanding how domain names expose infrastructure in an attack surface.

- **Design Choice:** By limiting the relation to just the DNS header and the resolved name or address, `BasicDNSRelation` avoids the complexity of modeling full DNS behavior (e.g., priorities or DNSSEC). It's intended for lightweight use cases where basic DNS resolution structure is sufficient.

In summary, `BasicDNSRelation` enables efficient modeling of essential DNS relationships, illustrating how domain names resolve in a minimal, structured format, without the overhead of full DNS record semantics.

## :material-relation-one-to-one: BasicDNSRelation Attributes

| Attributes | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `label` | string | :material-check-decagram: | The label for the relation between two assets |
| `header.rr_type` | number | :material-check-decagram: | Specifies the type of resource within the DNS record |
| `header.class` | number | :material-checkbox-blank-circle-outline: | 1, IN class (Internet), is the most commonly used |
| `header.ttl` | number | :material-checkbox-blank-circle-outline: | Specifies how long a DNS record should be cached |

## :material-relation-one-to-one: BasicDNSRelation Properties

| Property Type | Property Name | Description |
| :--------------: | :---------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this relationship |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this BasicDNSRelation |
