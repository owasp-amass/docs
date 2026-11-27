# :material-cloud-outline: cloud

The public cloud and CDN providers hosting a domain or organization's names —
by provider — matched from the providers' own published IP ranges. Part of
[`amass lens`](../lenses.md).

```bash
amass lens cloud -d owasp.org
amass lens cloud -org "Example Corp"
```

## What you get

Each recognized provider, how many of the subject's names resolve into its
published ranges, and example names. Names on addresses that match no known
provider range are not listed here (see [`network`](network.md) for the full
hosting picture).

## Example

Run against `owasp.org`:

```text
Cloud and CDN hosting of owasp.org and open web application security project:
52 of 64 name(s) on a recognized provider.

  Cloudflare: 44 name(s), e.g. community.owasp.org, kerala.owasp.org, …
  Amazon Web Services: 5 name(s), e.g. training.owasp.org, …
  DigitalOcean: 2 name(s), e.g. lists.owasp.org, cloud.owasp.org
  GitHub: 1 name(s), e.g. oldproject.owasp.org
```

## Reading it

- **"52 of 64 on a recognized provider"** is the share of names Amass could
  place in a known cloud/CDN range. The remaining names are on addresses that
  match no published range (a smaller host, or space Amass has not mapped).
- **The provider mix** tells you where an outage or account compromise would
  hurt most — here, overwhelmingly Cloudflare, with pockets on AWS, DigitalOcean
  and GitHub Pages.
- Attribution comes from the providers' **published ranges**, so it reflects
  stored resolutions, not a live scan.

## See also

- [`network`](network.md) — full hosting breakdown, including non-cloud space
- [`concentration`](concentration.md) — single points of failure across
  providers

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
