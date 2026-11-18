# :material-web: web

The web presence of a domain or organization: its website URLs and endpoints,
the host each reaches, and the web applications recognized on them. Part of
[`amass lens`](../lenses.md).

```bash
amass lens web -d owasp.org
amass lens web -org "Example Corp"
```

## What you get

The URLs stored for the subject, split into endpoints on its own domains and
off-domain URLs (links out to social profiles or third-party pages), followed
by any web applications Amass recognized from the pages' markup and scripts —
with product, vendor and version where it could tell.

## Example

Run against `owasp.org` (1347 URLs stored; excerpt):

```text
Web presence of owasp.org and open web application security project:
1347 URL(s) — 50 on its own domains, 8 off-domain.

Endpoints on its own domains:
  https://20thanniversary.owasp.org/
  https://aghast.owasp.org/
  https://aivss.owasp.org/calculator/
  https://asvs.owasp.org/
  https://board.owasp.org/
  … 

Off-domain URLs (social profiles, third-party pages):
  http://crt.r2m04.amazontrust.com/r2m04.cer
  http://i.pki.goog/we1.crt
  http://ye1.i.lencr.org/
  … 

Web applications recognized:
  https://genai.owasp.org: WordPress (WordPress Foundation),
    jQuery 3.7.1, plugins: elementor 4.4.0, jetpack 16.5, download-monitor 5.3.5
```

## Reading it

- **On-domain endpoints** are the subject's own pages — the live surface a
  visitor (or an attacker) sees. Deep paths (such as historical board-meeting
  pages) show how much of a site is indexed in the database.
- **Off-domain URLs** are links the pages make outward: here they are
  certificate-authority OCSP/CRL endpoints (`amazontrust`, `pki.goog`,
  `lencr.org`), not social profiles — a reminder to read them before assuming
  intent.
- **Recognized applications** are the highest-value part: a named product and
  version (`WordPress`, `jQuery 3.7.1`, specific plugin versions) is what the
  [`vulnerable`](vulnerable.md) lens matches against CVE data. Software is
  identified from stored evidence, never written back, since markup can be
  faked.

## See also

- [`services`](services.md) — listeners, ports and certificates
- [`headers`](headers.md) — HTTP security headers on these sites
- [`vulnerable`](vulnerable.md) — CVEs for the identified software

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
