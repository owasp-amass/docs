# :material-magnify-scan: Enumeration

`amass enum` runs a collection against a target and stores everything it
observes in the [Asset Database](../asset_db/index.md). It talks to the
collection engine, starting a local one when none is already running.

```bash
amass enum -d example.com
```

## :material-target: Choosing the target

| Flag | Meaning |
| :--- | :--- |
| `-d <domain>` | Root domain names, comma-separated and repeatable |
| `-df <file>` | A file of root domain names |
| `-addr <ips>` | IP addresses and ranges (`192.168.1.1-254`) |
| `-cidr <cidrs>` | CIDR ranges, comma-separated and repeatable |
| `-asn <asns>` | Autonomous system numbers, comma-separated and repeatable |
| `-bl <names>` / `-blf <file>` | Subdomains to exclude from investigation |

Giving an organization's own netblocks (`-cidr`) or autonomous systems
(`-asn`) puts that address space in scope, so active probes cover its
servers, not only the hosts its names resolve to.

## :material-radar-off: Passive vs. active collection { #active-collection }

Collection is **passive** by default — data sources and the DNS only.

```bash
amass enum -active -d example.com
```

`-active` adds collection that contacts the target directly: zone transfer
attempts, certificate name grabs, and service probes on in-scope addresses.
Amass probes every port of a service by default (`-p` narrows the list) and
covers SSH, the mail and file greetings, HTTP, and JARM.

To keep Amass from looking like a port scan to a firewall — and to avoid
being auto-blocked, which would collect nothing — active collection spaces
each host's probes a short, randomized interval apart and probes a host's
ports in a random order. Different hosts are probed in parallel, so pacing
one host does not slow an enumeration with many hosts in flight. Pacing only
ever delays a probe; it never skips one or changes a result. Two options
tune it (bounded defaults; set in `options:`):

```yaml
options:
  probe_pace_ms: 500     # minimum spacing between probes to one host
  probe_jitter_ms: 1500  # additional random spread
```

Set `probe_pace_ms: 0` to turn pacing off when you are probing hosts you
control and want maximum speed.

!!! warning "Authorized use"
    Active collection sends traffic to the target's own infrastructure.
    Only enumerate assets you own or are explicitly authorized to assess.

## :material-dns: Names and brute forcing

| Flag | Meaning |
| :--- | :--- |
| `-brute` | Brute force subdomains after the searches |
| `-w <file>` | A wordlist for brute forcing |
| `-wm <mask>` | hashcat-style masks for brute forcing |
| `-norecursive` | Turn off recursive brute forcing |
| `-min-for-recursive <n>` | Labels seen before recursing (default 1) |
| `-max-depth <n>` | Maximum label depth for brute forcing |
| `-alts` | Generate altered names |
| `-aw <file>` / `-awm <mask>` | Wordlist and masks for alterations |
| `-nf <file>` | Seed names already known from other tools |

## :material-arrow-expand: Scope and resolvers

| Flag | Meaning |
| :--- | :--- |
| `-rigid` | Disable scope expansion; collect exactly the given scope |
| `-p <ports>` | Ports to probe (default: FTP, SSH, mail, web, mgmt) |
| `-r <ips>` / `-rf <file>` | Untrusted DNS resolvers |
| `-tr <ips>` | Trusted DNS resolvers |
| `-iface <name>` | Network interface to send traffic through |
| `-timeout <minutes>` | Minutes without progress before stopping (default 30) |

## :material-cog: Engine, data sources and output

| Flag | Meaning |
| :--- | :--- |
| `-engine <url>` | Collection engine URL (default `http://127.0.0.1:4000`) |
| `-list` | Print the available data sources |
| `-include` / `-exclude <names>` | Limit the data sources used |
| `-config <file>` / `-dir <path>` | Configuration file and data directory |
| `-oA <prefix>` | Path prefix for all output files |
| `-log <file>` | Where errors are written |
| `-v` | Verbose status and troubleshooting output |
| `-demo` | Censor output for demonstrations |

## :material-history: Recording the run

Each enumeration is recorded as a
[collection run](../asset_db/collection_runs.md):
its scope, mode and session, marked finished when all of its work completed
and stopped otherwise. The [changes lens](lenses.md#changes) uses runs to
report what a later enumeration no longer found.

## Examples

```bash
# Passive discovery of a domain
amass enum -d example.com

# Active, including the organization's own network and ASN, with brute forcing
amass enum -active -brute -d example.com -cidr 192.0.2.0/24 -asn 64496

# Hold strictly to the given scope and probe only the web ports
amass enum -active -rigid -p 80,443,8080,8443 -d example.com
```
