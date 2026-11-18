# :material-lan: network

The network infrastructure behind what a domain or organization controls: the
netblocks and autonomous systems registered to it, where its names are hosted
(its own space or a provider's), address space none of its names use, and
other domains found in its space. Part of [`amass lens`](../lenses.md).

```bash
amass lens network -d owasp.org
amass lens network -org "Example Corp"
```

## What you get

If the subject registers its own address space, that is listed first. Then the
hosting breakdown: each provider, how many of the subject's names it serves,
the networks involved, and example names. Names reached through a CNAME are
counted against the provider at the end of the chain.

## Example

Run against `owasp.org`:

```text
Network infrastructure of owasp.org and open web application security project,
from 1551 controlled asset(s).
No netblock or autonomous system registered to it is stored.

Where its 62 resolving name(s) are hosted (12 through an alias):
  cloudflare: 44 (71%), e.g. community.owasp.org, kerala.owasp.org, …
  amazon.com: 5 (8%), e.g. secureflag.owasp.org, support.docs.owasp.org, …
  canva: 2 (3%), e.g. www.projectsummit.owasp.org, projectsummit.owasp.org
  digitalocean: 2 (3%), e.g. lists.owasp.org, cloud.owasp.org
  sendgrid.net: 2 (3%), e.g. s1._domainkey.owasp.org, s2._domainkey.owasp.org
  … 
Names with no stored address: 2.
```

## Reading it

- **"No netblock … registered to it"** means OWASP owns no address space of its
  own — everything is on providers. An organization that runs its own network
  would list its netblocks and ASNs here.
- **The percentages** show reliance: 71% of names behind Cloudflare is a strong
  single-provider concentration. `12 through an alias` means those names are
  CNAMEs whose provider is the chain's endpoint.
- **"no recorded network owner"** flags addresses whose netblock Amass has not
  attributed yet — a gap to fill with more collection.

To put the same picture on a map of countries, use [`geography`](geography.md);
to see only the public cloud/CDN providers, use [`cloud`](cloud.md).

## See also

- [`cloud`](cloud.md) · [`concentration`](concentration.md) ·
  [`subdomains`](subdomains.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
