# :material-web-box: domains

The registered domains of a domain or organization: registrar, expiry,
transfer lock, DNSSEC status and DNS providers, with those expiring soon or
unlocked first. Part of [`amass lens`](../lenses.md).

```bash
amass lens domains -d owasp.org
amass lens domains -org "Example Corp"
```

## What you get

One line per registered domain with its registration facts, and how many names
sit under it. Domains that expire soon, that are not transfer-locked, or that
lack DNSSEC are surfaced first, since those are the registration-level risks.

## Example

Run against `owasp.org`:

```text
Registered domains of owasp.org and open web application security project: 1.

Domains:
  owasp.org: 64 name(s), registrar unknown, expires 2031-09-21,
             DNSSEC not stated
             status: clientTransferProhibited, clientUpdateProhibited,
                     clientDeleteProhibited, clientRenewProhibited
```

## Reading it

- **Expiry** is the headline risk: a lapsed registration strands every name
  under it. `owasp.org` expires in 2031 — comfortable.
- **The `clientTransfer/Update/Delete/RenewProhibited` statuses** are registrar
  locks: good hygiene, they block unauthorized transfers and deletions.
- **"DNSSEC not stated"** means no DNSSEC status was stored — enabling the
  registration data sources (RDAP/WHOIS) fills registrar and DNSSEC fields
  (see [`coverage`](coverage.md)).

## See also

- [`dangling`](dangling.md) · [`email`](email.md) · [`coverage`](coverage.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
