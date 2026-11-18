# :material-eye-outline: Lenses

A **lens** is a read-only view of the [Asset Database](../asset_db/index.md).
`amass lens` answers a question about what a domain or organization controls
directly from the stored evidence, with no language model involved. Lenses
compute their answer each time and never write a conclusion back, so an
answer changes as the evidence does and nothing is left behind to clean up.

```bash
amass lens report -d example.com
amass lens network -org "Example Corp"
```

Most lenses start from a domain (`-d`) or an organization (`-org`). Lenses
only read. The scans that find records to fix and write **proposals** are a
separate subcommand, [`amass db`](db.md), reviewed with
[`amass review`](review.md).

## :material-flag: Choosing a subject

| Flag | Meaning |
| :--- | :--- |
| `-d <domain>` | The enumerated domain the lens starts from |
| `-org <name>` | The organization the lens starts from |
| `-with <domain>` / `-with-org <name>` | Second subject, for `compare` |
| `-since <when>` | Date, RFC 3339 time or age (`7d`); for `changes` |

An `-org` name is matched exactly; if it is misspelled or partial, or several
organizations share it, the lens lists the closest stored names so you can pick
the one you meant instead of failing.

## :material-cog-outline: Common options

| Flag | Meaning |
| :--- | :--- |
| `-format text\|json` | Output format (default `text`) |
| `-config <file>` / `-dir <path>` | Configuration file and data directory |
| `-max-assets <n>` | Cap the controlled assets a lens follows |
| `-max-reads <n>` | Cap the database reads of one lens run |
| `-read-stats` | Report what the run read and how long it took |
| `-vuln-data <file>` | Data file the `vulnerable` lens reads |

Reads are bounded and batched. A lens says when a result is partial, and a
large footprint is sampled across kinds of asset rather than cut off at the
first kind.

## :material-view-dashboard: Posture lenses

These read what a subject controls and report on its security posture.

### report

```bash
amass lens report -d example.com
```

The attack surface report: the key findings first, then a section from each
posture lens below. Start here.

### subdomains

```bash
amass lens subdomains -d example.com
```

The names a domain or organization controls, in order, each with its stored
IP addresses (a CNAME is followed to the addresses at the end of its chain),
and a summary of how many names fall into each autonomous system and
netblock. This replaces the former `subs` command: the name list, the names
with their addresses, and the per-AS/per-netblock counts are all here.

### family

The organizations behind an enumerated domain — its registrant, the
organizations named on its certificates, and the networks and other
registered domains that serve it — and how they relate (same institution,
parent, affiliate or vendor). A matching name alone is never treated as
strong: organizations in different jurisdictions often share a name.

### vendors / group-vendors

`vendors` lists the outside parties a domain and its organization's assets
depend on (DNS, hosting, certificates, mail, and more). `group-vendors`
does the same across a whole corporate group and shows which organization in
the group uses each vendor.

### org-group

The corporate group around an organization: its ultimate parent and every
subsidiary and unit, as an indented tree with each one's jurisdiction and
registration number. The links are stored control relationships (such as
GLEIF parent/child records), never inferred from a shared name.

### affiliation

Organizations the subject is affiliated with — tied by a shared phone, person,
funder or address — each with the signals behind the link and a confidence.
A shared name alone is never enough.

### accounts

The platform accounts the subject has (code hosts, social media and the like),
computed from the profile URLs stored for it.

### funding

The funding a domain's or organization's company has received, from stored
`FundsTransfer` records: each round or award with its amount, date and the
investor or agency behind it, and a total when the rounds share a currency.
Funding comes from keyless public sources — US federal awards and grants
(USAspending, NSF, NIH, SBIR), US nonprofit and securities filings
(ProPublica, SEC EDGAR) and public procurement in Europe (TED) and beyond
(Open Contracting / OCDS). See [Funding and procurement data](../ai/funding.md).

### group-funding

The funding above rolled up across a whole corporate group — the organization
and every parent, subsidiary and unit — merged, noting which group organization
received each round, with a group total. One institution's funding is often
split across records that different funders name differently (a university
system and one of its campuses, say); this shows the whole picture when those
records are linked in the group.

### services

The services stored for what the subject controls: where each listens, its
type, the software its response headers and banners name (`nginx 1.24.0`,
`OpenSSH 9.6p1`), the certificates it presented, and recognized web
applications. It flags services on unusual ports and weak or expiring
certificates. Software is identified from stored evidence when asked, never
written down, since a banner can be hidden or faked.

### web

The subject's web presence: its website URLs and endpoints, the host and
address each one reaches, and the web applications recognized on them.

### network

The netblocks and autonomous systems registered to the subject, where its
names are hosted (its own space or a provider's), address space none of its
names use (worth checking for forgotten assets), and other domains found in
its space. When the database supports range lookups, an address with no
stored netblock is placed in the netblock that contains it.

### cloud

The public cloud and CDN providers hosting the subject's names — by provider,
region and service — from the providers' own published IP ranges.

### dangling

DNS records that may point at something the subject no longer holds, most
severe first: claimable aliases (the classic subdomain takeover), expired or
expiring alias targets and name servers, unresolved aliases, alias loops,
and stale addresses. Each is a lead to confirm with a live lookup.

### changes { #changes }

```bash
amass lens changes -d example.com -since 2026-11-01
amass lens changes -org "Example Corp" -since 7d
```

What was first stored since a time, and what later enumerations stopped
seeing, by asset type and relationship purpose. When the database records
[collection runs](../asset_db/collection_runs.md), it compares against the
latest finished run that covered the subject and reports what that run did
not see — firmer than comparing timestamps, because the run is known to have
looked. Without `-since`, the window is the last 30 days.

### certificates

The subject's TLS certificates — expired, expiring, weak, self-issued or
overlong ones, and wildcards — and the certificate authorities it relies on.

### domains

The subject's registered domains: registrar, expiry, transfer lock, DNSSEC
status and DNS providers.

### email

The subject's mail providers and its SPF, DMARC and DKIM records, and which
of its domains can be spoofed because the records are missing or weak.

### contacts

The subject's contact details — phone numbers, email addresses, contact people
and postal addresses — from its stored contact records.

### identifiers

The registered identifiers attached to what the subject controls — LEI, tax,
company and registry numbers and handles — grouped by type.

### exposure

What the subject exposes that deserves attention: remote access, databases,
file sharing, management interfaces and login pages.

### headers

The HTTP security headers of the subject's web services — HSTS, CSP,
clickjacking and MIME-sniffing protection, and cookie flags — and which are
missing or weak.

### disclosure

How the subject invites vulnerability reports: its `security.txt` contacts,
policy and encryption links, and any of those files that have expired.

### concentration

How much the subject relies on single providers for DNS, registration,
certificates, hosting and mail — where one provider's trouble would matter
most.

### coverage

How complete the stored data is for the subject, and what collection would
fill each gap. Useful for deciding what to enumerate next.

### geography

The countries of the subject's stored addresses and of the parties hosting
its names. For an organization it also reports an inferred country — Amass's
best determination from the evidence it has (legal jurisdiction, a registration
or contact address, a registrant phone).

### compare

```bash
amass lens compare -d a.com -with b.com
amass lens compare -org "A Corp" -with-org "B Corp"
```

What two domains or organizations share: common assets and common outside
parties.

### vulnerable

```bash
amass vuln-update                      # fetch/refresh the data first
amass lens vulnerable -d example.com
```

Checks the software versions the `services` lens identifies against NVD's CVE
data and lists those with CVEs, known-exploited ones first (CISA KEV), with
each CVE's score and link. A product without a version, or a version the
data does not yet cover, is listed as not checked. See
[`vuln-update`](tools.md#vulnerability-data).

### lookalikes

Domains that resemble the subject's and could be used to impersonate it.

## :material-broom: Database hygiene

The scans that find records to fix — duplicate organizations, contradicted
identities, and organizations that are really people — are **not** lenses:
they walk the whole database and write proposals rather than viewing one
subject. They live under their own subcommand, [`amass db`](db.md).

## :material-brain: Asking in plain language

Every lens is also reachable through [`amass ai`](../ai/index.md), which uses
a language model to turn a plain-language question into the right lens and to
summarize the answer with its evidence. The lenses themselves never need a
model.
