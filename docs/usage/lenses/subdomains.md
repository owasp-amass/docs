# :material-sitemap: subdomains

The names a domain or organization controls, each with the addresses it
resolves to, plus a roll-up of how many names fall in each autonomous system
and netblock. Part of [`amass lens`](../lenses.md).

```bash
amass lens subdomains -d owasp.org          # from a domain
amass lens subdomains -org "Example Corp"   # from an organization
```

## What you get

One line per name, in order, showing its record types and — following any
CNAME chain to the end — the addresses it reaches. A CNAME that points at a
SaaS host is shown as the chain so you can see who actually serves the name.
Two summaries follow: names grouped by autonomous system, and by netblock.

## Example

Run against `owasp.org`:

```text
Subdomains of owasp.org and open web application security project: 64 name(s),
64 with DNS records, 56 resolving to an address, 0 discovered without records.

  admin.owasp.org [CNAME] -> 41e3b5a8b9f664cc.vercel-dns-016.com
  auth.owasp.org [CNAME] -> remssssfmrgmyzqnpeas.supabase.co -> 104.18.38.10, …
  cheatsheetseries.owasp.org [A, AAAA] -> 104.20.44.163, 172.66.157.115, …
  docs.owasp.org [CNAME] -> readthedocs.io -> 104.16.253.120, …
  owasp.org [A, MX, NS, TXT] -> 216.150.1.193, 216.150.16.193
  support.owasp.org [CNAME] -> support-owasp-org-….saas.atlassian.com -> …
  … (58 more)

Names by autonomous system:
  AS13335 (CLOUDFLARENET): 43 name(s), e.g. community.owasp.org, …
  (no stored autonomous system): 11 name(s), e.g. secureflag.owasp.org, …
  AS16509 (AMAZON-02): 1 name(s), e.g. owasp.org

Names by netblock:
  104.20.32.0/20 (AS13335): 42 name(s)
  (no stored netblock): 11 name(s)
  216.150.1.0/24 (AS16509): 1 name(s)
```

## Reading it

- **The record types** (`[A, AAAA]`, `[CNAME]`, `[MX, NS, TXT]`) tell you what
  each name is for. A name with only `TXT` (such as `_dmarc.owasp.org`) is a
  policy record, not a host.
- **A CNAME chain** ending at a third-party host — `supabase.co`,
  `readthedocs.io`, `saas.atlassian.com`, `vercel-dns` — shows the name is
  served by a SaaS provider. These are exactly the names to check in the
  [`dangling`](dangling.md) lens for takeover risk.
- **The autonomous-system and netblock roll-ups** show concentration at a
  glance: here 43 of 64 names sit behind Cloudflare. The
  [`concentration`](concentration.md) lens quantifies that.

Names shown are stored resolutions from past collection, not a live scan.
Every lens also takes `-format json` for machine-readable output.

## See also

- [`network`](network.md) — the netblocks and ASNs behind these names
- [`web`](web.md) — which of these names serve web applications
- [`dangling`](dangling.md) — names whose targets may be claimable

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
