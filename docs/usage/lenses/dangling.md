# :material-link-off: dangling

DNS records that may point at something the subject no longer holds, most
severe first: claimable aliases (the classic subdomain takeover), expired or
expiring alias targets and name servers, unresolved aliases, alias loops, and
stale addresses. Part of [`amass lens`](../lenses.md).

```bash
amass lens dangling -d owasp.org
amass lens dangling -org "Example Corp"
```

## What you get

Findings grouped by severity. The first group — **claimable aliases** — is the
one to act on: a CNAME pointing at a SaaS/cloud resource that no longer exists,
which an attacker could re-create to serve content under the subject's name.
Lower groups are leads of decreasing urgency.

## Example

Run against `owasp.org`:

```text
Dangling DNS of owasp.org and open web application security project:
64 name(s) checked.

Aliases to claimable service names with no stored address
(possible subdomain takeover) (1):
  oldproject.owasp.org -> owasp-oldproject.github.io: alias to a GitHub Pages name
    with no stored address; if the resource was deleted, anyone can claim the
    name and serve content as oldproject.owasp.org

Aliases to outside names with no stored address (5):
  admin.owasp.org -> 0123456789abcdef.apphost.example
  giving.owasp.org -> custom.donations.example -> edge.alias.example
  www.owasp.org -> 0123456789abcdef.apphost.example
  … 
```

## Reading it

- **Claimable aliases are the priority.** The example points `oldproject.owasp.org`
  at a GitHub Pages name with no resolving address — if that Pages site was
  deleted, someone could register it and take over the subdomain. The finding
  links to the provider's own takeover-verification docs.
- **Unresolved aliases** (to app-hosting, fundraising and mail-delivery
  targets) are weaker signals: the target may simply not be in the database
  yet, or may be inactive.
  Each is a lead to confirm with a live lookup, not a confirmed takeover.
- Everything here is derived from **stored records** — always verify a finding
  against a live lookup before acting.

## See also

- [`subdomains`](subdomains.md) — the full name list these are drawn from
- [`domains`](domains.md) — registration expiry that can also strand names

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
