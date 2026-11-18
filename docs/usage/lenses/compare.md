# :material-compare: compare

What two domains or organizations share: common assets and common outside
parties. The one lens that takes a second subject. Part of
[`amass lens`](../lenses.md).

```bash
amass lens compare -d a.com     -with a-staging.com
amass lens compare -org "A Corp" -with-org "B Corp"
```

The subject is given as usual (`-d` or `-org`); the second subject is given
with `-with` (a domain) or `-with-org` (an organization).

## What you get

The assets both subjects control in common, and the outside parties
(vendors, hosting, certificate authorities) both depend on — a quick way to
tell whether two domains or organizations are run by the same team, or how far
two parts of an organization overlap.

## Example

Comparing two related domains:

```text
Comparison of a.com and a-staging.com.

Shared assets (3):
  Netblock 203.0.113.0/24   — hosts names of both
  Organization "A Corp"     — controls both
  TLSCertificate *.a.com    — covers names of both

Shared outside parties (2):
  cloudflare   — DNS and hosting for both
  let's encrypt — certificates for both
```

## Reading it

- **Shared assets are the strong tie.** A shared netblock, a shared wildcard
  certificate, or the same controlling organization is good evidence two
  subjects are operated together — far stronger than a shared vendor.
- **Shared outside parties** (both on Cloudflare, both using Let's Encrypt) are
  weak on their own — most of the web shares those — but they add up alongside
  shared assets.
- An empty comparison is meaningful: two subjects with nothing in common are
  likely genuinely separate.

## See also

- [`family`](family.md) · [`vendors`](vendors.md) ·
  [`db duplicates`](../db.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
