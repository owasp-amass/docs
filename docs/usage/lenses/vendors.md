# :material-truck-outline: vendors

The outside parties a domain and its organization's assets depend on — DNS,
hosting, certificates, mail and more — each with how it is used and example
assets. Part of [`amass lens`](../lenses.md).

```bash
amass lens vendors -d owasp.org
amass lens vendors -org "Example Corp"
```

## What you get

Each outside party, most widely used first, with the **kinds** of dependency
(Certificate, DNS, Network, Registration…), how many assets rely on it, and
examples. These are stored OAM relationships, not verified contracts.

## Example

Run against `owasp.org` (excerpt):

```text
Outside parties, most widely used first:
  let's encrypt: 8 asset(s), Certificate; e.g. owasp.org, prodsec.owasp.org
  google trust services: 5 asset(s), Certificate; e.g. owasp.org, genai.…
  amazon.com: 4 asset(s), Certificate, DNS: IP addresses; e.g. training.…
  atlassian.com: 3 asset(s), DNS: FQDNs, DNS: organizations; e.g. support.…
  canva: 2 asset(s), DNS: IP addresses; e.g. projectsummit.owasp.org
  digitalocean: 2 asset(s), DNS: IP addresses; e.g. lists.owasp.org
  dbhost.example: 1 asset(s), DNS: FQDNs; e.g. auth.owasp.org
  readthedocs.io: 1 asset(s), DNS: FQDNs; e.g. docs.owasp.org
  … 
```

## Reading it

- **The "kinds" tell you the nature of the dependency.** "Certificate" means
  that party issued certificates; "DNS: FQDNs" means names are CNAMEd to it;
  "Network: services" means a service runs on its infrastructure. A party with
  several kinds (Amazon here) is relied on in more than one way.
- **Asset counts rank exposure** — Let's Encrypt and Google Trust Services as
  certificate authorities touch the most assets.
- These are **stored relationships, not confirmed service use** — a historical
  CNAME still counts until re-enumeration drops it.
- **"Stated in its own documents"** lists the suppliers and products the
  domain's own documents name, read by the [document model](../../ai/documents.md),
  with how many documents say so and the first few cited. It's what the
  organization wrote, not a verified contract.

To merge this across a whole corporate group, use
[`group-vendors`](group-vendors.md).

## See also

- [`group-vendors`](group-vendors.md) · [`network`](network.md) ·
  [`concentration`](concentration.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
