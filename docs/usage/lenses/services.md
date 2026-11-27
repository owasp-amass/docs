# :material-server-network: services

The services stored for what a domain or organization controls: where each
listens, its type, the software its response headers and banners name, the
certificate it presented, and anything that stands out. Part of
[`amass lens`](../lenses.md).

```bash
amass lens services -d owasp.org
amass lens services -org "Example Corp"
```

## What you get

A summary by service type and port, the software Amass identified across them,
then one line per service: host and port, the `server`/`x-powered-by` headers,
the product it runs, and the certificate it served with its expiry. These come
from stored probes (active collection), not a live scan.

## Example

Run against `owasp.org` (excerpt):

```text
Services exposed by owasp.org and open web application security project:
27 service(s) on 13 host(s).
By type: web-service 27
By port: 80/TCP 11, 443/TCP 9, 8080/TCP 5, 8443/TCP 2
Identified software: Next.js 6, Express 3, nginx 2

Services:
  web-service on owaspla.owasp.org:443; server: Vercel; x-powered-by: Next.js;
    runs Next.js; certificate owasp.org from YR1 until 2027-02-09
  web-service on securecodingdojo.owasp.org:443; server: cloudflare;
    x-powered-by: Express; runs Express; certificate owasp.org until 2027-02-01
  web-service on genai.owasp.org:80; server: nginx; runs nginx;
    certificate tls.examplehost.com from WR1 until 2026-12-21
  web-service on training.owasp.org:80; server: nginx; via: CloudFront;
    certificate labs.example.net from Amazon RSA 2048 M04 until 2027-05-10
  … 
```

## Reading it

- **The by-port summary** shows the shape of the surface: here everything is
  web, but services on 8080/8443 are worth noting — the lens flags services on
  unusual ports.
- **`runs <product>`** is identified software (Next.js, Express, nginx), taken
  from headers and banners. That product-and-version is what
  [`vulnerable`](vulnerable.md) checks against CVE data.
- **The certificate** on each line — its subject and expiry — lets you spot a
  name served under a different certificate (e.g. `genai.owasp.org` under
  `tls.examplehost.com`, `training.owasp.org` under `labs.example.net`), which
  points at the real hosting provider.
- Software is read from **stored evidence when asked**, never written back,
  since a banner can be hidden or spoofed.

## See also

- [`web`](web.md) · [`certificates`](certificates.md) ·
  [`headers`](headers.md) · [`exposure`](exposure.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
