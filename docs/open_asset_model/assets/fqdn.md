# :simple-owasp: FQDN

The **FQDN**, or **Fully Qualified Domain Name (FQDN)**, asset represents a complete and unambiguous domain name that specifies the exact location of a device or resource within a **Domain Name System (DNS)** namespace on the internet. DNS names are critical components of **open-source intelligence (OSINT)** and a comprehensive **attack surface intelligence** collection process. By organizing these assets alongside discovered attributes and relationships, the [Open Asset Model](https://github.com/owasp-amass/open-asset-model) reveals connections across diverse resources, enabling a holistic understanding of the asset landscape.

---

## :material-dns: FQDN Attributes

| Attributes | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `name` | string | :material-check-decagram: | Unique fully qualified domain name (e.g. www.example.com) |

## :material-dns: FQDN Outgoing Relations

``` mermaid
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

| Relation Label | Relation Type | Assets | Description |
| :--------------: | :--------------: | :----------: | :---------- |
| `dns_record` | [`BasicDNSRelation`](#basic_dns_relation) | [`FQDN`](#fqdn), [`IPAddress`](#ip_address) | Used for most RR types |
| `dns_record` | [`PrefDNSRelation`](#pref_dns_relation) | [`FQDN`](#fqdn) | Used for RR types that have a preference attribute |
| `dns_record` | [`SRVDNSRelation`](#srv_dns_relation) | [`FQDN`](#fqdn) | Used to support the SRV RR type |
| `node` | [`SimpleRelation`](#simple_relation) | [`FQDN`](#fqdn) | Links a DNS zone apex to nodes within the zone |
| `port` | [`PortRelation`](#port_relation) | [`Service`](#service) | Represents a port at the FQDN with a responding service |
| `registration` | [`SimpleRelation`](#simple_relation) | [`DomainRecord`](#domain_record) | Links a root domain to registration data |
