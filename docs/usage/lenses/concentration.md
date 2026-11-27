# :material-chart-donut: concentration

How much a domain or organization relies on single providers for certificates,
hosting and mail — where one provider's trouble would matter most. Part of
[`amass lens`](../lenses.md).

```bash
amass lens concentration -d owasp.org
amass lens concentration -org "Example Corp"
```

## What you get

For each category (certificate authorities, hosting, mail providers), whether
reliance is **spread** or **concentrated**, the share the largest outside
provider holds, and the provider breakdown.

## Example

Run against `owasp.org`:

```text
Provider concentration of owasp.org and open web application security project.

certificate authorities: spread; the largest outside provider serves 53% of
what outside providers serve (15 certificate(s) in all).
  let's encrypt: 8
  google trust services: 5
  amazon: 2

hosting: spread; the largest outside provider serves 71% of what outside
providers serve (62 name(s) in all).
  cloudflare: 44
  amazon.com: 5
  digitalocean: 2
  … 

mail providers: spread; the largest outside provider serves 50% (2 domains).
  Google Workspace: 1
```

## Reading it

- **"spread" vs "concentrated"** is the headline: a category where one provider
  holds a large majority is a single point of failure. Here hosting is 71%
  Cloudflare — still labelled spread, but clearly the dominant dependency.
- **The share is of what outside providers serve**, so self-hosted assets do
  not dilute the figure.
- Use it to decide where redundancy would help most: if Cloudflare had an
  outage, 44 of 62 names would be affected at once.

## See also

- [`network`](network.md) · [`cloud`](cloud.md) · [`certificates`](certificates.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
