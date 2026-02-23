# :simple-owasp: Data Sources

Data sources are plugins that query external services
to discover assets. They include API integrations, web
scrapers, and WHOIS/RDAP lookups. Each data source
registers one or more Handlers that are triggered when
specific asset types are processed by the engine.

All data sources that require credentials are configured
through a `datasources.yaml` file.

## :material-key: Configuring Credentials

Point Amass to your data sources file from
`config.yaml`:

```yaml
options:
  datasources: "./datasources.yaml"
```

Each source in `datasources.yaml` follows this format:

```yaml
datasources:
  - name: Shodan
    ttl: 10080       # optional: cache TTL (minutes)
    creds:
      account:
        apikey: YOUR_API_KEY
```

For sources requiring a username and API key:

```yaml
  - name: PassiveTotal
    creds:
      account:
        username: your@email.com
        apikey: YOUR_API_KEY
```

For sources requiring a username and password:

```yaml
  - name: CIRCL
    creds:
      account:
        username: YOUR_USERNAME
        password: YOUR_PASSWORD
```

Multiple credential accounts are supported per
source — useful for rate limit distribution:

```yaml
  - name: C99
    creds:
      account1:
        apikey: FIRST_KEY
      account2:
        apikey: SECOND_KEY
```

## :material-tune: Global Options

Set a minimum TTL floor that applies to all sources:

```yaml
global_options:
  minimum_ttl: 1440  # 1 day (minutes) — default
```

Sources without an explicit `ttl` value in their entry
use this global floor.

## :material-table: Available Data Sources

All 38 data sources require credentials. Default TTL
is 1440 minutes (1 day) unless listed otherwise. The
full template for all sources is in
[`resources/datasources.yaml`][ds-yaml].

[ds-yaml]:
  https://github.com/owasp-amass/amass/blob/main/resources/datasources.yaml

| Source | Cred Type | TTL |
| :--- | :--- | :---: |
| 360PassiveDNS | API Key | 3600 |
| ASNLookup | API Key | 1440 |
| Ahrefs | API Key | 4320 |
| AlienVault | API Key | 1440 |
| BeVigil | API Key | 1440 |
| BigDataCloud | API Key | 1440 |
| BinaryEdge | API Key | 10080 |
| BufferOver | API Key | 1440 |
| BuiltWith | API Key | 10080 |
| C99 | API Key (multi-acct) | 4320 |
| CertCentral | User + API Key | 1440 |
| Chaos | API Key | 4320 |
| CIRCL | User + Password | 1440 |
| DNSDB | API Key | 4320 |
| DNSRepo | API Key | 1440 |
| Detectify | API Key | 1440 |
| FOFA | User + API Key | 10080 |
| FullHunt | API Key | 1440 |
| GitHub | API Key | 4320 |
| GitLab | API Key | 4320 |
| HackerTarget | API Key | 1440 |
| Hunter | API Key | 1440 |
| IntelX | API Key | 1440 |
| IPdata | API Key | 1440 |
| IPinfo | API Key | 1440 |
| LeakIX | API Key | 1440 |
| Netlas | API Key | 1440 |
| PassiveTotal | User + API Key | 10080 |
| PentestTools | API Key | 10080 |
| PublicWWW | API Key | 10080 |
| SecurityTrails | API Key | 1440 |
| Shodan | API Key | 10080 |
| URLScan | API Key | 1440 |
| VirusTotal | API Key | 10080 |
| WhoisXMLAPI | API Key | 1440 |
| Yandex | User + API Key | 1440 |
| ZETAlytics | API Key | 1440 |
| ZoomEye | User + Password | 1440 |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
