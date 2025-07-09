# :simple-owasp: FQDN

The **FQDN** (Fully Qualified Domain Name) asset type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) represents a fully specified domain name that uniquely identifies a resource within the DNS hierarchy. FQDNs are foundational elements in *open-source intelligence (OSINT)* and are essential to building a thorough *attack surface intelligence* profile.

- **Definition:** An `FQDN` asset contains a domain name string (e.g., `www.example.com`). It refers to the complete and unambiguous name of a host or service as resolved through DNS.

- **Purpose:** This asset type enables the modeling of DNS-resolvable names as distinct entities within an attack surface. `FQDN` assets are critical for tracing how external users and systems access internal infrastructure, through domain-based references rather than direct IP addresses.

- **Design Choice:** By treating FQDNs as first-class assets, the model supports DNS resolution chains (via relations like `BasicDNSRelation`, `PrefDNSRelation`, and `SRVDNSRelation`) and links to IP addresses, services, or other host-based assets. This allows security teams to analyze exposure, misconfigurations, or shadow assets rooted in DNS name usage.

In summary, the `FQDN` asset type provides a precise and structured way to represent domain-based identifiers in the OAM, serving as a core building block for understanding how infrastructure is referenced and accessed over the internet or internal networks.

## :material-dns: FQDN Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `name` | string | :material-check-decagram: | Unique fully qualified domain name (e.g. www.example.com) |

## :material-dns: FQDN Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this FQDN |
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

ipaddr["IPAddress"]
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

domrec["DomainRecord"]
regrel@{ shape: braces, label: "registration"}
fqdn1 --o regrel
regrel --> domrec
```

---

| Relation Type       | Relation Label     | Target Assets    | Description   |
| :-----------------: | :----------------: | :--------------: | :------------ |
| [`BasicDNSRelation`](../relations/basic_dns_relation.md) | `dns_record` | `FQDN`, [`IPAddress`](./ip_address.md) | Represents most RR types |
| [`PrefDNSRelation`](../relations/pref_dns_relation.md) | `dns_record` | `FQDN` | Utilized for RR types that have a preference attribute |
| [`SRVDNSRelation`](../relations/srv_dns_relation.md) | `dns_record` | `FQDN` | Represents the SRV Resource Record type |
| [`SimpleRelation`](../relations/simple_relation.md) | `node` | `FQDN` | Links a DNS zone apex to nodes within the zone |
| [`PortRelation`](../relations/port_relation.md) | `port` | [`Service`](./service.md) | Represents a port at the FQDN with a responding service |
| [`SimpleRelation`](../relations/simple_relation.md) | `registration` | [`DomainRecord`](./domain_record.md) | Links a root domain to its associated registration data |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
