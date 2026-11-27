# :material-shield-bug: Vulnerability data

`amass vuln-update` fetches and refreshes the vulnerability data that the
[`vulnerable`](lenses/vulnerable.md) lens matches against: the National
Vulnerability Database (NVD) CVE feed and CISA's Known Exploited
Vulnerabilities (KEV) catalog. It writes a single `vulnerabilities.json` file
into the Amass data directory; nothing else reads the network for this.

```bash
amass vuln-update
```

Run it before the `vulnerable` lens, and refresh it periodically — CVE data
changes daily. The lens tells you when the data is missing or stale.

## Keeping it fresh automatically

`-every` turns the command into a lightweight daemon that refreshes the data
whenever it is older than the given age (minimum two hours):

```bash
amass vuln-update -every 24h    # refresh once a day, then keep running
```

## Options

| Flag | Meaning |
| :--- | :--- |
| `-dir <path>` | Amass data directory that holds `vulnerabilities.json` |
| `-vuln-data <file>` | Explicit path to the vulnerability data file |
| `-timeout <dur>` | Maximum time for one update (default 30m) |
| `-every <dur>` | Keep running, refreshing when the data is older than this (≥ 2h) |

## Reading the output

The command reports how many CVE records and KEV entries it stored and where it
wrote them. After it finishes, run the lens:

```bash
amass vuln-update
amass lens vulnerable -d owasp.org
```

The lens reads `vulnerabilities.json`, matches it against the software versions
the [`services`](lenses/services.md) lens identified, and lists the affected
products — known-exploited (CISA KEV) first. A product with no version, or a
version the feed does not cover, is reported as *not checked* rather than
silently dropped. See the [`vulnerable`](lenses/vulnerable.md) lens for how to
read those results.

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
