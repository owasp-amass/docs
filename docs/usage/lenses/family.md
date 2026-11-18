# :material-family-tree: family

The organizations behind an enumerated domain — its institution (name variants
and departments) and affiliates — with the evidence tying each to the domain,
the networks serving its names, and other registered domains those networks
serve. Part of [`amass lens`](../lenses.md).

```bash
amass lens family -d owasp.org
```

## What you get

The domain's **main organization**, the organizations grouped as its same
institution or affiliates (each with its evidence), and the networks serving
the domain's names. A shared name alone is never treated as strong — the
evidence is hosting, registration and contact ties.

## Example

Run against `owasp.org`:

```text
Organization family of owasp.org (64 of its names sampled).
Main organization: cloudflare [435]

Same institution:
  cloudflare [435]
    - holds 104.20.32.0/20, which serves 42 of the sampled owasp.org names
    - holds 172.66.144.0/20, which serves 42 of the sampled owasp.org names
    - the domain's main organization

Networks serving its names:
  104.20.32.0/20 (cloudflare): 42 of the sampled names
  172.66.144.0/20 (cloudflare): 42 of the sampled names
```

## Reading it

- **"Main organization" is inferred from the evidence, not assumed.** For a
  fully cloud-hosted domain like `owasp.org`, the networks serving its names
  belong to the host (Cloudflare), so the host can surface as the main
  organization. That is a true statement about the *hosting*, and a cue that
  the registrant organization is thinly tied in the stored data — enabling
  registration/identity sources would strengthen the owner's ties.
- **Evidence lines** tell you *why* each organization is in the family (which
  netblock it holds and how many names it serves), so you can weigh it.
- `family` also records findings in the review journal; confirm or reject
  identity calls with [`amass review`](../review.md).

## See also

- [`org-group`](org-group.md) · [`network`](network.md) ·
  [Organizations & geography](../../ai/organizations.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
