# :simple-owasp: PrefDNSRelation

The **PrefDNSRelation** in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) is used to represent DNS resource records that include a **preference** value, such as MX records that define mail server priority for a domain.

- **Definition:** A `PrefDNSRelation` captures the association between a DNS name and another DNS name or IP address, along with a numeric **preference** value that indicates priority. This is commonly used for records like `MX`, `SRV`, or other types where ordering or selection is influenced by a preference number.

- **Purpose:** This relation is critical for modeling DNS-based service routing and failover configurations. For example, in an `MX` record, the preference indicates which mail server should be contacted first. Accurately capturing this relationship helps model infrastructure behavior during service discovery, redundancy, and load distribution.

- **Design Choice:** `PrefDNSRelation` builds on the simpler `BasicDNSRelation` by including a structured `preference` attribute, while still avoiding full record verbosity (e.g., no TTLs, weights, ports, or target service names). This keeps the model lightweight but expressive enough for meaningful DNS prioritization use cases.

In summary, `PrefDNSRelation` extends basic DNS modeling by introducing priority-aware resolution, enabling the OAM to capture more nuanced DNS relationships where preference order matters.

## :material-relation-one-to-one: PrefDNSRelation Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `label` | string | :material-check-decagram: | The label for the relation between two assets |
| `header.rr_type` | number | :material-check-decagram: | Specifies the type of resource within the DNS record |
| `header.class` | number | :material-checkbox-blank-circle-outline: | 1, IN class (Internet), is the most commonly used |
| `header.ttl` | number | :material-checkbox-blank-circle-outline: | Specifies how long a DNS record should be cached |
| `preference` | number | :material-checkbox-blank-circle-outline: | Captures the preference or priority value for this record |

## :material-relation-one-to-one: PrefDNSRelation Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this PrefDNSRelation |
