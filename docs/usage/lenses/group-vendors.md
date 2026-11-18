# :material-truck-check-outline: group-vendors

The outside parties a whole corporate group depends on — the vendors of each
organization in the group (parent, subsidiaries and units) merged — with how
many and which group organizations use each, and services one group
organization provides another set apart. Part of [`amass lens`](../lenses.md).

```bash
amass lens group-vendors -org "Example Corp"
amass lens group-vendors -d owasp.org
```

## What you get

The same vendor breakdown as [`vendors`](vendors.md), but merged across every
organization in the [group](org-group.md), with a `used by N of M` count so you
can see which dependencies are shared group-wide. A separate section lists
**internal services** — where one group organization provides another.

## Example

Run against `owasp.org` (its group is one organization here):

```text
Vendors across the corporate group of cloudflare: 1 organization in the group.

Outside parties, most widely used first:
  let's encrypt: used by 1 of 2 (owasp.org); 8 asset(s), Certificate
  google trust services: used by 1 of 2 (owasp.org); 5 asset(s), Certificate
  amazon.com: used by 1 of 2 (owasp.org); 4 asset(s), Certificate, DNS
  … 

Services one group organization provides another:
  cloudflare.com: used by 2 of 2 (cloudflare; owasp.org); 44 asset(s)
```

## Reading it

- **"used by N of M"** is the group-wide view: a vendor used by many group
  members is a shared, systemic dependency; one used by a single member is
  local to it.
- **Internal services** separate out dependencies that are really within the
  group (here Cloudflare serving owasp.org appears as internal because the
  domain's main organization resolved to the host — see [`family`](family.md)).
- With a multi-organization group, this is where you see a vendor every
  subsidiary quietly shares.

## See also

- [`vendors`](vendors.md) · [`org-group`](org-group.md) ·
  [`group-funding`](group-funding.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
