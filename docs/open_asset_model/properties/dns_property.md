# :simple-owasp: DNSRecordProperty

The `DNSRecordProperty` is a structured property type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) used to represent observed Domain Name System (DNS) record data associated with an asset. Unlike a `SimpleProperty`, which encapsulate a single key-value pair, the `DNSRecordProperty` captures a richer snapshot of a specific DNS lookup result, including the record type, value, and TTL.

DNS information is central to many asset discovery and enumeration processes, and the `DNSRecordProperty` provides a consistent way to describe these findings in the model. It supports representing common record types such as TXT, SOA, HINFO, and others, while also enabling timestamped tracking of when the record was resolved.

Each `DNSRecordProperty` includes the following components:

- **Property Name** – The name of the property, which should be `dns_record`.
- **Record Type** – The type of DNS record (e.g., `TXT`, `SOA`, `HINFO`).
- **Record Data** – The result of the DNS resolution (e.g., text string).
- **TTL** – The time-to-live value from the DNS response, indicating how long the result should be considered valid.

By modeling DNS data with a dedicated property type, `DNSRecordProperty` enables more precise tracking and temporal reasoning around changes in DNS infrastructure. It supports threat hunting, infrastructure correlation, asset ownership validation, and detection of transient or ephemeral DNS configurations.

## :fontawesome-solid-tags: DNSRecordProperty Attributes

| Attributes       | Type   | Required | Description |
| :------------------: | :--------: | :----------: | :------------- |
| `property_name`    | string | :material-check-decagram: | The name of the property that should be `dns_record` |
| `header.rr_type` | number | :material-check-decagram: | Specifies the type of resource within the DNS record |
| `header.class` | number | :material-checkbox-blank-circle-outline: | 1, IN class (Internet), is the most commonly used |
| `header.ttl` | number | :material-checkbox-blank-circle-outline: | Specifies how long a DNS record should be cached |
| `data`         | string | :material-check-decagram: | The value from the data field of the DNS resource record |
