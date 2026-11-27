# :material-history: changes

What changed recently in what a domain or organization controls: records first
stored in a recent window, and records that later enumerations stopped seeing.
Part of [`amass lens`](../lenses.md).

```bash
amass lens changes -d owasp.org -since 2026-10-18
amass lens changes -org "Example Corp" -since 7d
```

## What you get

Two sections: assets and relationships **first stored since** the window, each
by type/purpose; and assets/relationships that went **quiet** (not seen by the
latest run). With no `-since`, the window is the last 30 days. When the database
records [collection runs](../../asset_db/collection_runs.md), "quiet" is judged
against the latest finished run that covered the subject — firmer than comparing
timestamps.

## Example

Run against `owasp.org` just after its first enumeration, everything is new:

```text
Changes to owasp.org and open web application security project since
2026-10-18, across 1551 controlled asset(s).

First stored since then (assets, by type):
  URL: 1338 new        Service: 134 new       FQDN: 64 new
  TLSCertificate: 13 new   DomainRecord: 1 new   Organization: 1 new

First stored since then (relationships, by purpose):
  web: 1340 new    dns: 214 new    certificate: 202 new
  network: 154 new    hierarchy: 63 new    identity: 2 new
  contact: 1 new    registration: 1 new
```

## Reading it

- **Group by type and purpose** tells you *what kind* of thing changed — a jump
  in `FQDN` means new names; a jump in `certificate` relationships means new or
  rotated certificates.
- **"Quiet"** means an asset was not observed again, not that it was proven
  removed — confirm before acting. On a first enumeration (like this one)
  everything is "new" and nothing is quiet.
- Run the same target over time into a persistent database to make this lens a
  monitoring tool: schedule re-enumerations and read `changes` between them.

## See also

- [`coverage`](coverage.md) · [Collection runs](../../asset_db/collection_runs.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
