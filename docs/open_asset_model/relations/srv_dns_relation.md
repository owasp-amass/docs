# :simple-owasp: SRVDNSRelation

The **SRVDNSRelation** in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) is used to represent DNS SRV (Service) records, which include detailed routing information for locating services such as SIP, XMPP, or LDAP.

- **Definition:** An `SRVDNSRelation` captures the mapping from a DNS service name (e.g., `_sip._tcp.example.com`) to a target host or IP address, along with structured metadata including **priority**, **weight**, and **port**. These attributes are fundamental to how SRV records guide service resolution.

- **Purpose:** This relation type is essential for modeling DNS-based service discovery mechanisms where clients need to select among multiple service endpoints based on priority and load-balancing rules. Including all SRV-specific attributes enables accurate representation of how services are discovered and accessed in real-world deployments.

- **Design Choice:** `SRVDNSRelation` is a more detailed extension of DNS relation types like `BasicDNSRelation` or `PrefDNSRelation`. It includes:
  - `priority`: Defines the order in which targets should be attempted (lower is tried first).
  - `weight`: Used for load balancing among targets with the same priority.
  - `port`: Indicates the port on which the service is running.

This richer structure allows for nuanced modeling of service behaviors and routing policies that simpler DNS relations cannot capture.

In summary, `SRVDNSRelation` brings full support for SRV record semantics into the OAM, enabling accurate modeling of service-based resolution patterns that are critical in modern, distributed infrastructure.

## :material-relation-one-to-one: SRVDNSRelation Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `label` | string | :material-check-decagram: | The label for the relation between two assets |
| `header.rr_type` | number | :material-check-decagram: | Specifies the type of resource within the DNS record |
| `header.class` | number | :material-checkbox-blank-circle-outline: | 1, IN class (Internet), is the most commonly used |
| `header.ttl` | number | :material-checkbox-blank-circle-outline: | Specifies how long a DNS record should be cached |
| `priority` | number | :material-checkbox-blank-circle-outline: | Captures the priority value for this record |
| `weight` | number | :material-checkbox-blank-circle-outline: | Captures the weight value for this record |
| `port` | number | :material-check-decagram: | Indicates the port on which the service is running |

## :material-relation-one-to-one: SRVDNSRelation Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this SRVDNSRelation |
