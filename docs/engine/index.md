# :material-engine-outline: How the Engine Works

The Amass **collection engine** is the part of Amass that goes out and finds
things. You give it a starting point, such as a domain, a netblock or an
organization. It works outward from there, asking DNS, registries, certificate
logs, web archives and dozens of other data sources what they know. Everything
it learns goes into the [Asset Database](../asset_db/index.md) as a graph of
[Open Asset Model](../open_asset_model/index.md) assets and relations.

This page walks through the engine one piece at a time, from the big picture
down to a single event moving through a pipeline. If you want to know *why* it's
built this way, read [The Logic Behind the Engine's Design](design.md) next.

!!! tip "The one idea to keep in mind"
    **Every discovery is an asset, and every asset is a unit of work.** When the
    engine finds a new name, address, certificate or organization, it stores it
    and then asks: *"what else can this lead to?"* That loop, repeated thousands
    of times and kept inside your scope, is an enumeration.

---

## :material-map-outline: The big picture

The engine runs as a **service**. It doesn't print results itself: clients talk
to it over an HTTP API, and it writes everything it finds to the Asset Database.
Several clients, and several enumerations, can share one engine at the same
time.

```mermaid
flowchart LR
    subgraph Clients
        CLI["amass enum<br/>(command line)"]
        MCP["Amass MCP server<br/>(AI assistants)"]
        Other["Your own tools<br/>(REST API)"]
    end

    subgraph Engine["Collection engine (amass engine)"]
        API["Engine API<br/>REST + WebSocket :4000"]
        SM["Session manager"]
        DIS["Dispatcher"]
        REG["Registry of<br/>plugin handlers"]
    end

    DB[("Asset Database<br/>SQLite · PostgreSQL · Neo4j")]
    NET(("The Internet<br/>DNS · registries · cert logs<br/>archives · APIs · target hosts"))

    CLI --> API
    MCP --> API
    Other --> API
    API --> SM
    SM --> DIS
    DIS --> REG
    REG <-->|queries| NET
    REG -->|stores assets & relations| DB
    SM -->|reads & writes| DB
```

| Piece | What it does |
|:--|:--|
| **Engine API** | Accepts new sessions and seed assets, reports progress, and streams each session's log over a WebSocket. |
| **Session manager** | Creates, tracks and ends **sessions**. A session is one enumeration with its own configuration and scope. |
| **Dispatcher** | Decides which discovered asset gets worked on next, sharing the engine fairly between sessions. |
| **Registry** | Knows every **handler** each plugin offers, and builds the pipeline of handlers for each asset type. |
| **Plugins** | The collectors: DNS, RDAP and WHOIS, certificate logs, web archives, service probes, documents, roughly 35 third-party data sources, and more. |
| **Asset Database** | The system of record. Every asset, relation and property the engine finds is stored here as soon as it's found. |

---

## :material-account-switch-outline: Sessions: one enumeration each

When you run `amass enum -d example.com`, the command-line client asks the
engine for a **session**, sends the seed assets (here, the domain), then watches
the session's log and progress until the work runs out.

```mermaid
sequenceDiagram
    autonumber
    participant C as amass enum (client)
    participant A as Engine API
    participant S as Session
    participant D as Dispatcher

    C->>A: POST /api/v1/sessions (configuration)
    A->>S: create session (scope, backlog, pipelines)
    A-->>C: session token
    C->>A: GET /sessions/{token}/ws/logs (subscribe)
    C->>A: POST /sessions/{token}/assets/FQDN (seed: example.com)
    A->>S: store the seed in the Asset Database
    A->>D: dispatch the seed as the first event
    loop until no work remains
        D->>S: run discovered assets through the pipelines
        S-->>C: log messages over the WebSocket
        C->>A: GET /sessions/{token}/stats
        A-->>C: work items completed / total
    end
    C->>A: DELETE /sessions/{token}
```

Each session carries everything it needs to work on its own:

```mermaid
flowchart TB
    subgraph Session["A session"]
        CFG["Configuration<br/>(transformations, TTLs, data source keys,<br/>active or passive)"]
        SCOPE["Scope<br/>domains · addresses · netblocks · ASNs<br/>organizations · street addresses · blacklist"]
        BL[("Backlog<br/>durable queue of work")]
        PIPES["One pipeline per asset type<br/>(23 of them: FQDN, IPAddress, URL, …)"]
        NETC["Network controls<br/>connection semaphore · probe pacer<br/>HTTP clients (general, probe, crawl, bulk)"]
        LOG["Log publisher<br/>(streamed to clients)"]
        STATS["Progress<br/>work items completed / total"]
    end
    DB[("Asset Database<br/>(shared by every session)")]
    Session --- DB
```

!!! info "Sessions share the database, not their work"
    Two sessions enumerating related targets write into the **same** Asset
    Database, so one can reuse what the other already learned (see
    [freshness](#freshness-ttls-reuse-what-is-already-known)). Each still has
    its **own** scope, backlog and pipelines, so they never step on each other's
    work queue.

---

## :material-transit-connection-variant: The discovery loop

This is the heart of the engine. Each asset that enters a session becomes an
**event**. The event runs through the pipeline for its asset type, and the
handlers in that pipeline turn it into new assets. Those are stored, and each
new asset becomes an event of its own.

```mermaid
flowchart LR
    SEED(["Seed asset<br/>example.com"]) --> EV["Event"]
    EV --> PIPE["Pipeline for its<br/>asset type"]
    PIPE --> H1["Handler: DNS"]
    PIPE --> H2["Handler: certificate logs"]
    PIPE --> H3["Handler: RDAP / WHOIS"]
    PIPE --> H4["Handler: web archives"]
    H1 & H2 & H3 & H4 --> NEW["New assets & relations<br/>stored in the Asset Database"]
    NEW --> CHECK{"In scope<br/>and not seen yet?"}
    CHECK -->|yes| EV
    CHECK -->|no| STOP(["Stored, but not<br/>expanded further"])
```

Following one real thread shows how quickly this grows:

```mermaid
flowchart LR
    A["FQDN<br/>example.com"] -->|DNS| B["FQDN<br/>www.example.com"]
    A -->|cert logs| C["TLSCertificate<br/>*.example.com"]
    C -->|SAN names| D["FQDN<br/>vpn.example.com"]
    B -->|DNS A record| E["IPAddress<br/>192.0.2.10"]
    E -->|RDAP| F["Netblock<br/>192.0.2.0/24"]
    F -->|RDAP| G["AutonomousSystem<br/>AS64500"]
    F -->|registrant| H["Organization<br/>Example Corp"]
    E -->|reverse DNS| I["FQDN<br/>mail.example.com"]
    B -->|web crawl & archives| J["URL<br/>/annual-report.pdf"]
    J -->|documents| K["File<br/>annual-report.pdf"]
    K -->|names in the text| L["Phone, Person,<br/>Organization, …"]
```

Every arrow is a **transformation**: one asset type becoming another through
some source. [Transformations](../configuration/transformations.md) in your
configuration decide which of these arrows the engine may follow, and how often.

---

## :material-pipe: Pipelines: ordered stages of handlers

The engine keeps **one pipeline per asset type**. A pipeline is a series of
stages, and each stage holds the handlers registered at that **position**, from
1 (first) to 50 (last). Every event of that type passes through every stage, in
order.

Here's the `FQDN` pipeline, simplified. Cheap, authoritative work comes first;
slower or paid third-party sources come later; probes and wrap-up come last:

```mermaid
flowchart LR
    IN(["FQDN event"]) --> P2["2 · DNS CNAME"]
    P2 --> P3["3 · DNS A / AAAA"]
    P3 --> P7["7 · subdomain<br/>walk"]
    P7 --> P8["8 · DNS apex"]
    P8 --> P9["9 · DNS TXT"]
    P9 --> P10["10–15 · horizontals,<br/>known names, SRV,<br/>alterations, RDAP,<br/>WHOIS, look-alikes"]
    P10 --> P20["20–39 · third-party<br/>sources: crt.sh,<br/>CertSpotter, VirusTotal,<br/>SecurityTrails, …"]
    P20 --> P40["40 · web archives,<br/>MTA-STS, security.txt"]
    P40 --> P41["41–43 · identity,<br/>HTTP probes,<br/>storage buckets"]
    P41 --> OUT(["done"])
```

Things to know about stages:

- **Order matters, on purpose.** A later handler can rely on an earlier one's
  work. For example, the DNS A/AAAA handler (position 3) skips names the CNAME
  handler (position 2) already found to be aliases.
- **Handlers that share a position run side by side.** The event moves on when
  all of them have finished. A handler can claim a position for itself alone
  (*exclusive*).
- **Each stage handles several events at once**, up to the fewest instances any
  of its handlers allows. So a slow data source limits only its own stage, not
  the whole engine.
- **A bad handler can't crash the engine.** If a handler panics, that event gets
  an error in the session log and everything else carries on.

```mermaid
flowchart TB
    subgraph Stage["One stage (position 40 of the FQDN pipeline)"]
        direction LR
        E1["event A"] --> W["Wayback"] & CC["Common Crawl"] & M["MTA-STS"] & S["security.txt"]
        W & CC & M & S --> J{"all finished?"}
    end
    J -->|yes| NEXT["next stage"]
    E2["events B, C, … wait or run<br/>in parallel up to the<br/>stage's instance limit"] -.-> Stage
```

---

## :material-tray-full: The backlog and the dispatcher

Discovery is bursty. One certificate can name 500 hosts, and one netblock sweep
can return thousands of addresses. If every new asset went straight into a
pipeline, memory would balloon and one busy session would starve the others. So
new assets go into a **backlog** first, and the **dispatcher** feeds the
pipelines from it at a sustainable pace.

```mermaid
sequenceDiagram
    autonumber
    participant H as Handler
    participant DB as Asset Database
    participant D as Dispatcher
    participant B as Session backlog
    participant P as Pipeline (asset type)

    H->>DB: store new asset (and its relation)
    H->>D: DispatchEvent(asset)
    D->>B: already in the backlog?
    alt seen before in this session
        B-->>D: yes, drop it (no repeated work)
    else new
        D->>B: enqueue (queued)
        D->>D: wake the pump if the pipeline is running low
        D->>B: claim up to N assets of this type (leased)
        D->>P: append events to the pipeline's queue
        P->>P: stages run the handlers
        P-->>D: event finished
        D->>B: ack (done)
    end
```

With a PostgreSQL or SQLite Asset Database, the backlog is a work queue in that
database, named by the session; otherwise it is a small SQLite database in the
session's temporary directory. Each item is **queued**, **leased** while a
pipeline works on it, then **done**. In the database, a lease lasts two minutes
and the engine renews it while the session runs, so the items of an engine that
stops return to the queue. If an event can't enter a pipeline, its lease is
**released** and the item is queued again. Because the backlog remembers
everything it has ever seen in the session, the same asset is never worked twice
in one enumeration, however many sources report it.

### Fair sharing between sessions

The dispatcher's **pump** runs whenever a pipeline drops to its low-water mark,
and every 10 seconds regardless. Each time, it visits the sessions in **random
order**. From each one it claims a small burst, never letting a pipeline's queue
exceed its limit:

| Asset types | Pipeline queue limit | Wake-up (low water) | Burst per session per pump |
|:--|:--:|:--:|:--:|
| `FQDN`, `IPAddress` | 200 | 100 | 10 |
| `Service`, `TLSCertificate`, `URL` | 100 | 25 | 5 |
| Everything else | 20 | 5 | 1 |

```mermaid
flowchart LR
    PUMP(("Pump<br/>(on low water<br/>or every 10 s)")) --> SH["shuffle sessions"]
    SH --> S1["Session 1<br/>claim ≤ burst"]
    SH --> S2["Session 2<br/>claim ≤ burst"]
    SH --> S3["Session 3<br/>claim ≤ burst"]
    S1 & S2 & S3 --> Q["Pipeline queue<br/>(≤ limit)"]
    Q --> ST["Stages"]
```

A huge enumeration and a small one can share an engine: the small one keeps
getting its turn.

---

## :material-filter-check-outline: What runs: transformations, freshness, scope

Before a handler touches an event, three questions decide whether it runs, and
whether it contacts anything on the Internet.

```mermaid
flowchart TB
    EV(["Event reaches a handler"]) --> T{"Does the configuration<br/>allow this transformation?<br/>(e.g. FQDN → DNS)"}
    T -->|no, or the plugin is excluded| SKIP(["Handler skipped"])
    T -->|yes| F{"Was this asset checked<br/>by this source within<br/>its TTL?"}
    F -->|yes| REUSE["Reuse what the Asset Database<br/>already holds; no query sent"]
    F -->|no| ASK["Query the source<br/>and mark the asset monitored"]
    REUSE & ASK --> S{"Are the results<br/>in scope?"}
    S -->|yes| DISPATCH["Store and dispatch:<br/>they become new events"]
    S -->|no| KEEP["Store them as context,<br/>but don't expand them"]
```

### Transformations: which arrows the engine may follow

The `transformations` section of `config.yaml` lists which asset types may
become which, through which plugin or source, such as `FQDN->DNS`,
`IPAddress->RDAP` or `Product->ALL`. A `FROM->ALL` entry can exclude specific
plugins. A handler runs only when a transformation allows it. See
[Transformations](../configuration/transformations.md).

### Freshness: TTLs reuse what is already known

Every transformation has a **TTL** in minutes. When a source checks an asset,
the engine records when (a `last_monitored` property). If the same asset comes
up again within the TTL, in this enumeration or a later one, the handler reads
the earlier answer from the Asset Database instead of asking again. That's why a
second enumeration of the same target is much faster, and gentler on the data
sources.

### Scope: what is worth expanding

The scope holds the **domains, IP addresses, netblocks, autonomous systems,
organizations and street addresses** you asked about, plus a blacklist. Every
result is checked against it:

- **In scope** results are dispatched and expanded further.
- **Out-of-scope** results are still stored, because they're useful context (who
  hosts this name, who issued that certificate), but they don't grow the
  enumeration.
- **Association** can widen the scope. When a new asset is tied to something
  already in scope strongly enough (for example, a domain registered to your
  organization), the engine can add it, recording the evidence and a
  plain-language rationale. The expansion policy decides how far: each
  transformation's `confidence` is the evidence it needs (above 100, nothing is
  admitted), and its `reach` how far from the scope its work goes. See
  [transformations](../configuration/transformations.md).

```mermaid
flowchart LR
    R["New result:<br/>FQDN shop-example.net"] --> IS{"Matches a scope<br/>domain, netblock,<br/>ASN or organization?"}
    IS -->|"yes (with a confidence)"| IN["In scope:<br/>dispatch"]
    IS -->|no| AS{"Associated with an<br/>in-scope asset?<br/>(registrant, contact, …)"}
    AS -->|"strongly enough<br/>for the policy"| ADD["Add to scope,<br/>record rationale,<br/>dispatch"]
    AS -->|no| CTX["Store as context only"]
```

---

## :material-speedometer: Being a good neighbor on the network

An enumeration can send a lot of traffic, to data sources and in active mode to
the target's own hosts. The engine paces itself:

- **A connection semaphore per session.** The engine's network connection budget
  is divided among the running sessions, so starting a second enumeration
  doesn't double the load.
- **A limit per DNS resolver.** The engine sends at most 15 queries per second
  to any one resolver, however many enumerations use it. Change the limit with
  the engine's `-resolver-qps` flag or the `AMASS_RESOLVER_QPS` environment
  variable (`0` removes it). An enumeration can name its own resolvers (`-r`,
  `-tr`, or `resolvers` and `trusted_resolvers` in the configuration file); the
  limit still applies to each of them.
- **One network interface.** The engine's traffic leaves through the interface
  the system chooses, or the one named by the engine's `-iface` flag or the
  `AMASS_IFACE` environment variable (an interface name, such as `eth0`, or one
  of the host's IP addresses). An enumeration can name its own (`-iface`, or
  `interface` in the configuration file, or the `interface` parameter of the MCP
  `plan_enumeration` tool). An interface named by name sends IPv4 traffic from
  its IPv4 address and IPv6 traffic from its IPv6 address; one named by an IP
  address sends only that IP version. Traffic of an IP version the interface has
  no address for is not sent through another interface.
- **A separate route for active traffic.** Probes, banners, certificates, JARM
  fingerprints and zone transfers, the traffic that reaches the target's own
  hosts, can take their own route: another interface, or a SOCKS5 or HTTP
  CONNECT proxy such as Tor (`-active-route` or `AMASS_ACTIVE_ROUTE` for the
  engine, `-active-route` or `active_route` for an enumeration, for example
  `socks5h://tor:9050`). Each enumeration gets its own Tor circuits. A proxy
  carries TCP only, so active UDP leaves from `-active-udp-route`
  (`AMASS_ACTIVE_UDP_ROUTE`) when it is set and isn't sent otherwise. Active
  traffic never falls back to a direct connection, and a refusal by the proxy or
  a Tor exit isn't taken as evidence about the target.
- **A probe pacer** spaces out active probes (certificate and service probes,
  zone transfers) against the target's hosts.
- **A probe gate** bounds how many active probes are in flight at once from the
  engine's public address, shared by every enumeration it runs: at most 16 to
  one registered domain, 2 to one host name and 4 to one IP address. The
  address limit matters for names behind a CDN, which share a few edge
  addresses and are slowed or cut off when too many connections reach them at
  once. A probe waits for its turn before its own timeout starts, and a name
  is resolved through the enumeration's own DNS resolvers to find its address.
  Set the engine's limits with its `-probe-per-domain`, `-probe-per-name` and
  `-probe-per-address` flags, the `AMASS_PROBE_PER_DOMAIN`,
  `AMASS_PROBE_PER_NAME` and `AMASS_PROBE_PER_ADDRESS` environment variables,
  or `probe_per_domain`, `probe_per_name` and `probe_per_address` under
  `options:` in the configuration file the engine is started with (`-config`),
  in that order of precedence (`0` removes a limit). An enumeration's own
  configuration can set the same options lower for its probes, never higher.
- **Separate HTTP clients** for ordinary API calls, active probes, crawling, and
  slow bulk queries (such as a web archive's index of a whole domain, which can
  take minutes to start answering).
- **Passive versus active.** In passive mode the target's own hosts are
  contacted only by ordinary DNS resolution. Active mode adds certificate and
  banner probes and zone transfers, and is for systems you're authorized to
  test.

The engine's log shows what this traffic met. A data source request that fails,
times out or gets an error status is logged with its host and path (never its
query, which can carry an API key), and every few minutes and when a session
ends, its network use lists each probe plugin's probes by outcome: answered,
refused (a closed port), no answer, timed out after connecting, or failed. A
probe that timed out after connecting is logged on its own, because a burst
the target or the network can't keep up with looks like that. When the engine
logs to a syslog server (`SYSLOG_HOST`), it writes the same records to its
standard error too, so `docker logs` shows them; set `AMASS_LOG_STDERR=false`
to turn that off.

---

## :material-flag-checkered: When is an enumeration finished?

A session tracks **work items**: assets dispatched versus assets fully
processed. It also counts **background work**: jobs that run outside the backlog
but can still produce assets, such as an attribution pass that waits for the
pipelines to drain before comparing organizations.

```mermaid
stateDiagram-v2
    [*] --> Created: client requests a session
    Created --> Running: seed assets dispatched
    Running --> Running: new in-scope assets<br/>become events
    Running --> Draining: backlog empty,<br/>background work pending
    Draining --> Running: background work<br/>found new assets
    Draining --> Finished: no work and no<br/>background work left
    Running --> Terminated: client ends the session<br/>or it times out
    Finished --> [*]
    Terminated --> [*]
```

The `amass enum` client ends its session when no progress has been made for its
timeout. The MCP server, which starts enumerations for AI assistants, also waits
for any companions it runs beside the engine (such as the [document
model](../ai/documents.md)) before calling a run finished.

---

## :material-server-network: Several engines on one database

Engines that share a PostgreSQL or SQLite Asset Database can share one
enumeration. Each enumeration is a **job**, and each engine session working on
it is a **worker**:

- **Joining.** When an engine is asked to enumerate a scope that a running job
  on the database already covers, its session joins that job instead of
  starting another. It uses the job's configuration, with its own database
  connection, data source credentials, DNS resolvers, network interface and
  routes. Its log says that it joined. To start a separate enumeration of
  the same scope, set the option `join_running_jobs: false`.
- **Sharing.** The workers take assets from one queue in the database, add to
  one scope and share their admission decisions, so an asset is processed once
  and a model is asked about it once.
- **Progress.** Each worker reports the whole job's progress, including the
  other workers' background work, so `amass enum` on any of them finishes
  when the job's work is done. The engine API lists a job's workers, with the
  items each holds and has done and the requests each sent to the main model
  (`GET /sessions/{token}/workers`). The MCP `enumeration_status` tool shows
  them for a running enumeration, with the job's total model requests.
- **Ending.** The last worker to leave records the job's end and its
  collection run. A worker that stops leaves its work to the others, and the
  items it held return to the queue within two minutes. If every worker stops
  unexpectedly, the next engine to look ends the job.

Run **one engine per public IP address**. Resolvers, data sources and targets
then see one engine's traffic from each address, within the engine's own
limits. An engine finds its public address when it starts by asking OpenDNS's
name servers once (or takes it from `-egress` or `AMASS_EGRESS`). It refuses to
work with a database that another engine on the same address is already using,
and says why. On one machine with several public interfaces, give each engine
its own with `-iface`, which covers all of its traffic. An engine asked again
for a scope it is already working on gives the same session to the new client,
instead of starting a second worker in the same engine.

An engine can also be a **pool worker**, joining running jobs on its own when
it has room:

```bash
amass engine -worker -config config.yaml
```

Pool workers are for engines on other machines or other public addresses. A pool
worker joins different running jobs, one session for each, up to five at once
(`-worker-sessions` or `AMASS_WORKER_SESSIONS`), and never a job one of the
engine's sessions already works on. Data source quotas that come with an API key
are shared by every engine using the key. Every 15 seconds, while it has room,
it joins the running job with the most queued work per worker, or the older
job when two are even. It takes its database and data source credentials from
the configuration file, and leaves a job once the job has no work left. With
Neo4j as the primary database, each enumeration stays on one engine.

To keep one large enumeration from drawing in every pool worker, cap its
workers in the configuration it starts with:

```yaml
options:
  # the most engines that may work on this enumeration at once; pool workers
  # don't join it beyond this, but an engine asked for the same scope does
  max_job_workers: 3
```

The cap is kept with the job, so it applies whichever engine a pool worker
reads it from. When two pool workers check at the same moment, both may take
the last place.

---

## :material-puzzle-outline: Plugins and handlers

A **plugin** is a collector, such as DNS, crt.sh or the web archives. When the
engine starts, each plugin registers one or more **handlers** with the registry.
A handler says:

| Field | Meaning |
|:--|:--|
| **Event type** | Which asset type it works on: `FQDN`, `IPAddress`, `Organization`, … |
| **Position** | Its stage in that pipeline, 1–50. |
| **Exclusive** | Whether it must have its position to itself. |
| **Max instances** | How many events it may work on at once. |
| **Transforms** | Which asset types it can produce, matched against the configuration's transformations. |
| **Callback** | The code that does the work. |

```mermaid
flowchart LR
    subgraph Plugin["DNS plugin"]
        h1["CNAME handler<br/>FQDN · position 2"]
        h2["A/AAAA handler<br/>FQDN · position 3"]
        h3["TXT handler<br/>FQDN · position 9"]
        h4["Reverse DNS handler<br/>IPAddress · position 8"]
    end
    REG["Registry"]
    h1 & h2 & h3 & h4 -->|RegisterHandler| REG
    REG -->|at session start| P1["FQDN pipeline"]
    REG -->|at session start| P2["IPAddress pipeline"]
```

A typical handler does the same few things every time:

1. Read the event's asset (an FQDN, say).
2. Ask the configuration for the transformation's TTL, and check whether the
   asset was monitored within it.
3. Either read the earlier results from the Asset Database or query the source.
4. Store each result as an asset, with the relation that links it, and the
   source and confidence as properties.
5. Dispatch each new in-scope result as an event of its own.

Across the plugins, about 100 handlers are registered, more than 40 of them on
`FQDN` alone. Third-party sources that need an account read their keys from
`datasources.yaml`; see [Data Sources](../configuration/data_sources.md).

---

## :material-robot-outline: Where AI fits

The engine itself uses **no language model**. Its collection is deterministic
and explainable. The AI features sit beside it and on top of it:

```mermaid
flowchart TB
    subgraph Engine["Collection engine"]
        PIPE["Pipelines & handlers"]
        ATTR["Attribution plugin<br/>(last position)<br/>classifiers, duplicate and<br/>ownership proposals"]
    end
    DB[("Asset Database")]
    REVIEW["Review journal<br/>proposals · applied changes · undo"]
    MCP["MCP server &<br/>collect manager"]
    DOC["Document model companion<br/>(reads documents during a run)"]
    ASSIST["AI assistant<br/>(asks questions, plans runs)"]

    PIPE --> DB
    ATTR --> REVIEW
    ATTR --> DB
    ASSIST --> MCP
    MCP -->|starts & watches sessions| Engine
    DOC -->|leads: new assets to check| Engine
    DOC --> REVIEW
    MCP -->|lenses & questions| DB
```

- The **attribution plugin** runs at the end of the pipelines. It compares
  organizations, proposes ownership and merges, and records every decision in
  the review journal, where it can be undone.
- The **document model** reads collected documents during a run and hands the
  engine new assets as **leads**. The engine checks a lead exactly like anything
  else it finds.
- The **MCP server** lets an AI assistant plan an enumeration, start it (with
  your approval), watch it, and answer questions from the Asset Database.

See [AI (Experimental)](../ai/index.md) for details.

---

## :material-book-open-variant: Glossary

| Term | Meaning |
|:--|:--|
| **Asset** | A thing on the attack surface, typed by the Open Asset Model: an FQDN, IP address, certificate, organization, … |
| **Event** | One asset being worked on within a session. |
| **Session** | One enumeration: its configuration, scope, backlog and pipelines. |
| **Pipeline** | The ordered stages of handlers for one asset type. |
| **Handler** | One piece of a plugin that works on one asset type at one position. |
| **Transformation** | An allowed path from one asset type to another through a plugin or source, with a TTL. |
| **Backlog** | A session's durable queue of discovered assets waiting for, or finished with, a pipeline. |
| **Job** | One enumeration of one scope, shared by the engine sessions on a database that work on it. |
| **Worker** | An engine session working on a job; a pool worker joins running jobs on its own. |
| **Dispatcher** | Feeds pipelines from session backlogs, fairly and within limits. |
| **Scope** | What the session is about; only in-scope results are expanded. |
| **TTL** | How long a source's answer about an asset is reused before asking again. |

**Next:** [The Logic Behind the Engine's Design](design.md)
