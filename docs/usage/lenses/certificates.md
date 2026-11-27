# :material-certificate-outline: certificates

The subject's TLS certificates — expired, expiring, weak, self-issued or
overlong ones, and wildcards — the other domains a shared certificate covers,
and the certificate authorities relied on. Part of [`amass lens`](../lenses.md).

```bash
amass lens certificates -d owasp.org
amass lens certificates -org "Example Corp"
```

## What you get

A breakdown by issuing authority, certificates that **cover other domains**
(multi-tenant certificates — a strong hint about shared hosting), and policy
findings such as domains with **no CAA record**. Expiring, expired and weak
certificates are surfaced first.

## Example

Run against `owasp.org` (bounded run; excerpt):

```text
Certificates of owasp.org and open web application security project: 4 found.

Issued by:
  google trust services: 2, e.g. owasp.org, tls.examplehost.com
  amazon: 1, e.g. labs.example.net
  let's encrypt: 1, e.g. owasp.org

Covering other domains (2):
  tls.examplehost.com (google trust services): also covers names of
    examplehost.com and other hosted customers' domains
  labs.example.net (amazon): also covers customer-a.example, customer-b.example,
    customer-c.example

No CAA policy (1):
  owasp.org publishes no CAA policy, so any certificate authority may issue
  certificates for it
```

## Reading it

- **Issuer breakdown** shows which CAs you depend on (feeds
  [`concentration`](concentration.md)).
- **"Covering other domains"** means a name is served under a certificate
  shared with unrelated domains — a signature of a multi-tenant host (a
  hosting provider's shared certificate, a training vendor's). It tells you
  the real platform behind a name.
- **"No CAA policy"** is a real hardening gap: without a CAA record, any CA may
  issue for the domain. Publishing CAA limits issuance to CAs you choose.
- **"Mark certificates (BIMI)"** lists the certificates a domain publishes in
  its BIMI record to show its logo in mail clients. A certificate authority
  issues one only after verifying the organization and, for a registered mark,
  its trademark, so each line shows the verified organization, the trademark
  registration and office, the word mark, the organization's LEI and the
  domains the certificate covers. The usual TLS validity limits are not
  applied to them.
- A run cut short by its time says so; give it a longer
  `-investigation-timeout`.

## See also

- [`services`](services.md) · [`concentration`](concentration.md) ·
  [`exposure`](exposure.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
