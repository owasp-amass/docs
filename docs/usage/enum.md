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
| `-p <ports>` | Ports to probe (default: FTP, SSH, mail, web, mgmt) |
| `-r <ips>` / `-rf <file>` | DNS resolvers to send this enumeration's queries to |
| `-tr <ips>` | Trusted DNS resolvers: the first one tests for DNS wildcards, and they take the queries when no `-r` resolvers are given |
| `-iface <name>` | Network interface on the engine's host (a name such as `eth0`, or one of its IP addresses) to send this enumeration's traffic through |
| `-active-route <iface or URL>` | Route for this enumeration's active traffic: an interface on the engine's host, or a proxy URL such as `socks5h://tor:9050` |
| `-active-udp-route <iface>` | Interface for active UDP when the active route is a proxy |
| `-timeout <minutes>` | Minutes without progress before stopping (default 30) |

A resolver is an IP address, with an optional port (`192.0.2.53:5353`). Without
`-r` or `-tr`, the engine uses its default public resolvers. However many
enumerations share a resolver, the engine keeps the queries it sends to it
under its per-resolver limit (`-resolver-qps`, see
[How the Engine Works](../engine/index.md)).

`-iface` names an interface on the host the engine runs on, which may not be
the host you run `amass enum` from. Without it, the enumeration uses the
engine's own interface setting.

## :material-cog: Engine, data sources and output

| Flag | Meaning |
| :--- | :--- |
| `-engine <url>` | Collection engine URL (default `http://127.0.0.1:4000`) |
| `-no-join` | Start a separate enumeration even when another engine on the same database is already enumerating this scope; without it, this enumeration [joins that one](../engine/index.md#several-engines-on-one-database) and says so |
| `-list` | Print the data sources and plugins, marking those with credentials configured, and exit without enumerating |
| `-include` / `-exclude <names>` | Limit the data sources used |
| `-config <file>` / `-dir <path>` | Configuration file and data directory |
| `-oA <prefix>` | Path prefix for all output files |
| `-log <file>` | Where errors are written |
| `-v` | Verbose status and troubleshooting output |

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

# Probe only the web ports (to hold strictly to the given scope, use the
# strict expansion policy, policy-strict.yaml, in your config.yaml)
amass enum -active -p 80,443,8080,8443 -d example.com
```
