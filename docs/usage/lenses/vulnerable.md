# :material-bug-outline: vulnerable

The software versions identified on what a domain or organization controls that
have known vulnerabilities, known-exploited ones (CISA KEV) first. Matched by
version against NVD CVE data. Part of [`amass lens`](../lenses.md).

```bash
amass vuln-update                      # fetch/refresh the data first
amass lens vulnerable -d owasp.org
```

## What you get

Three groups: software with CVEs (KEV first, each with score and link);
software checked and **clean**; and software **not checked** — with the reason
(no version in the banner, or a version the feed does not cover). It reads the
data file [`vuln-update`](../vuln-update.md) writes.

## Example

Run against `owasp.org` (after `amass vuln-update`):

```text
Vulnerable software of owasp.org and open web application security project:
0 identified version(s) with CVEs, 0 with known exploited ones,
from 154 service(s). Vulnerability data updated 2026-11-17.

No CVEs for: nginx 1.31.8, jQuery 3.7.1

Not checked:
  Next.js on 20 endpoint(s): its header carries no version
  nginx on 4 endpoint(s): the version is not known
  Express on 3 endpoint(s): its header carries no version
  WordPress add-ons on 1 endpoint(s): 12 found (elementor, jetpack, …);
    their versions in asset URLs are chosen by each add-on, not confirmed
```

## Reading it

- **"with known exploited ones" (CISA KEV)** is the line to act on first — a KEV
  entry means the CVE is being exploited in the wild.
- **"No CVEs for …"** is a clean result for a version the feed does cover —
  reassuring, but only as current as the last `vuln-update`.
- **"Not checked"** is not "safe": it means Amass could not get a reliable
  version (a header with no version, or add-on versions it cannot confirm). To
  check those, you need the exact version from another source.
- Software can **hide or fake its version**, so confirm a hit against the
  vendor's advisory before treating it as real.

## See also

- [`vuln-update`](../vuln-update.md) · [`services`](services.md) · [`web`](web.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
