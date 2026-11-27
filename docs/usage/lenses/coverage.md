# :material-progress-check: coverage

How complete the stored data about a domain or organization is: assets by type,
unresolved names, missing registrations, stale assets, and what collection
would fill each gap. Part of [`amass lens`](../lenses.md).

```bash
amass lens coverage -d owasp.org
amass lens coverage -org "Example Corp"
```

## What you get

A count of controlled assets by type, then each known kind of gap with how many
assets fall into it and the collection step that would close it. Use it to
decide what to enumerate next.

## Example

Run against `owasp.org`:

```text
Data coverage of owasp.org and open web application security project:
1551 controlled asset(s).
By type: URL 1338, Service 134, FQDN 64, TLSCertificate 13,
         DomainRecord 1, Organization 1.

domains without registration: 0 of 1 (0%).
names without records: 0 of 64 (0%).
stale assets: 0 of 1551 (0%).

Coverage is of what the enumerations reached; assets they never found are
not counted.
```

## Reading it

- **The by-type counts** show the shape of what you have — here a web-heavy
  surface (1338 URLs, 134 services) over 64 names.
- **Each gap names its fix.** "names without records" would be filled by a DNS
  resolving pass; "domains without registration" by enabling the RDAP/WHOIS
  sources. A clean run like this (all 0%) means the stored data is internally
  complete — though, as the footer says, coverage can only measure what the
  enumerations actually reached.
- Pair it with [`changes`](changes.md) to see whether re-enumeration is finding
  anything new.

## See also

- [`changes`](changes.md) · [`subdomains`](subdomains.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
