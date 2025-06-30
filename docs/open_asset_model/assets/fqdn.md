# :simple-owasp: FQDN

The *Fully Qualified Domain Name* (**FQDN**) asset represents a complete and unambiguous domain name that precisely identifies the location of a device or resource within the *Domain Name System (DNS)* hierarchy. FQDNs are foundational elements in *open-source intelligence (OSINT)* and are essential to building a thorough *attack surface intelligence* profile. Within the [Open Asset Model](https://github.com/owasp-amass/open-asset-model), these assets are organized along with their associated attributes and relationships, helping to uncover connections between otherwise disparate resources. This structured representation enables a more comprehensive and contextualized view of an organization’s digital footprint.

## :material-dns: FQDN Attributes

| Attributes | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `name` | string | :material-check-decagram: | Unique fully qualified domain name (e.g. www.example.com) |

## :material-dns: FQDN Properties

| Property Type | Property Name | Description |
| :--------------: | :---------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried for this FQDN |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this FQDN |
| [`DNSRecordProperty`](../properties/dns_property.md) | `dns_record` | Represents a DNS record for this FQDN that provides only data |

## :material-dns: FQDN Outgoing Relations

```mermaid
graph TD
fqdn1["FQDN (e.g. owasp.org)"]
fqdn2["FQDN (e.g. vpn.owasp.org)"]
nodeRel@{ shape: braces, label: "node"}
fqdn1 --o nodeRel
nodeRel --> fqdn2

ipaddr["IP Address"]
basicdns1@{ shape: braces, label: "dns_record"}
basicdns2@{ shape: braces, label: "dns_record"}
fqdn1 --o basicdns1
basicdns1 --> ipaddr
fqdn2 --o basicdns2
basicdns2 --> ipaddr

fqdn3["FQDN (e.g. send.owasp.org)"]
prefdns@{ shape: braces, label: "dns_record"}
fqdn1 --o prefdns
prefdns --> fqdn3

fqdn4["FQDN (e.g. _sip._tcp.owasp.org)"]
srvdns@{ shape: braces, label: "dns_record"}
fqdn4 --o srvdns
srvdns --> fqdn1

service["Service"]
port@{ shape: braces, label: "port"}
fqdn2 --o port
port --> service

domrec["Domain Record"]
regrel@{ shape: braces, label: "registration"}
fqdn1 --o regrel
regrel --> domrec
```

---

| Relation Type | Relation Label | Target Assets | Description |
| :--------------: | :---------------: | :--------------: | :------------ |
| [`BasicDNSRelation`](../relations/basic_dns_relation.md) | `dns_record` | [`FQDN`](#fqdn), [`IPAddress`](#ip_address) | Represents most RR types |
| [`PrefDNSRelation`](../relations/pref_dns_relation.md) | `dns_record` | [`FQDN`](#fqdn) | Utilized for RR types that have a preference attribute |
| [`SRVDNSRelation`](../relations/srv_dns_relation.md) | `dns_record` | [`FQDN`](#fqdn) | Represents the SRV Resource Record type |
| [`SimpleRelation`](../relations/simple_relation.md) | `node` | [`FQDN`](#fqdn) | Links a DNS zone apex to nodes within the zone |
| [`PortRelation`](../relations/port_relation.md) | `port` | [`Service`](#service) | Represents a port at the FQDN with a responding service |
| [`SimpleRelation`](../relations/simple_relation.md) | `registration` | [`DomainRecord`](#domain_record) | Links a root domain to its associated registration data |
