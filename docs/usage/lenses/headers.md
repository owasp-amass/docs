# :material-shield-lock-outline: headers

The HTTP security headers of a domain or organization's web services — HSTS,
CSP, clickjacking and MIME-sniffing protection, and cookie flags — and which
are missing or weak. Part of [`amass lens`](../lenses.md).

```bash
amass lens headers -d owasp.org
amass lens headers -org "Example Corp"
```

## What you get

One line per web service: either "all checked hardening headers present" or the
specific headers it is missing. The checked set covers Content-Security-Policy,
Strict-Transport-Security (HSTS), X-Content-Type-Options and X-Frame-Options,
plus cookie flags.

## Example

Run against `owasp.org` (excerpt):

```text
HTTP security headers of owasp.org and open web application security project.

  admin.owasp.org: all checked hardening headers present
  auth.owasp.org:  missing Content-Security-Policy, X-Content-Type-Options
  asvs.owasp.org:  missing Content-Security-Policy, Strict-Transport-Security,
                   X-Content-Type-Options, X-Frame-Options
  … 
```

## Reading it

- **"all checked hardening headers present"** is the clean result — that
  service sets the full set.
- **A missing-list** names exactly what to add. Missing
  `Strict-Transport-Security` means no HSTS (downgrade risk); missing
  `Content-Security-Policy` weakens XSS defenses; missing `X-Frame-Options`
  allows clickjacking; missing `X-Content-Type-Options` allows MIME sniffing.
- A static site behind a CDN often misses several and that may be acceptable;
  an application or login host missing them is worth fixing. Cross-reference
  [`exposure`](exposure.md) to prioritize the sensitive hosts.

## See also

- [`services`](services.md) · [`web`](web.md) · [`exposure`](exposure.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
