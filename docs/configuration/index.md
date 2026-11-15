
# Amass Configuration Guide

This document explains the structure and options available in Amass configuration files. Amass uses YAML files to define its scan scope, data sources, and operational options. Understanding these files will help you customize Amass for your use case.

---

## Main Configuration: `config.yaml`

The main configuration file, typically named `config.yaml`, controls the scope of your scan, scanning options, and transformation rules. Below is a breakdown of its main sections:

### `seed`

The `seed` is where an enumeration **starts**: the existing knowledge about
the target. It is the one section you really need, because every seed entry
is collected from and is automatically in scope. A simple run needs only a
seed; add a `scope` section (below) only when the boundary should be wider
than the starting points.

**Supported Fields:**

- `domains` (array of strings): registered domains to begin from, the usual
  starting point (e.g., `owasp.org`).
- `names` (array of strings): known DNS names, or *leads* — normally
  subdomains of a domain already in scope, supplied from other tooling or
  past knowledge so the enumeration does not overlook them. Each lead's
  registered domain is added to the scope. The `-nf` command-line flag adds
  names the same way.
- `names_file` (string): path to a file of leads, one name per line.
- `ips` (array of strings): IP addresses to begin from. Supports single IPs,
  dash-ranges, and full ranges.
- `cidrs` (array of strings): CIDR ranges to begin from (e.g., `192.0.2.0/24`).
- `asns` (array of ints): autonomous system numbers to begin from.
- `organizations` (array of strings): company names to begin from; the
  engine resolves each to its registered domains, networks and systems.

**Example:**

```yaml
seed:
  domains:
    - owasp.org
  names:
    - vpn.owasp.org
    - api.owasp.org
  names_file: ./known-names.txt
  cidrs:
    - 192.0.2.0/24
  asns:
    - 64496
  organizations:
    - Example Corporation
```

### `scope`

The `scope` is the **boundary** a discovered asset must fall within to be
kept. Unless the run is started with `-rigid`, the engine may widen the
scope as it finds evidence (for example, a netblock or domain registered to
an in-scope organization), so it is a starting boundary, not a hard cap.
Leave `scope` out to bound the run by the seed alone; list entries here only
to allow assets beyond the seed.

**Supported Fields:**

- `domains` (array of strings): registered domain names allowed in scope.
- `ips` (array of strings): IP addresses allowed in scope. Supports single
  IPs (e.g., `192.0.2.1`), dash-ranges (e.g., `192.168.0.3-8`), and full
  ranges (e.g., `192.168.0.10-192.168.0.20`).
- `asns` (array of ints): autonomous systems allowed in scope (their
  announced networks).
- `cidrs` (array of strings): CIDR ranges allowed in scope.
- `organizations` (array of strings): companies discovered assets must be
  attributable to.
- `ports` (array of ints): ports active enumeration may probe on in-scope
  addresses. Leave out to probe every port the probes know; list ports only
  to narrow that (ranges such as `8000-8010` also work).
- `blacklist` (array of strings): subdomains that will never be investigated.

**Example:**

```yaml
scope:
  domains:
    - owasp.org
  cidrs:
    - 192.0.2.0/24
  organizations:
    - Example Corporation
  ports:
    - 80
    - 443
  blacklist:
    - internal.owasp.org
```

### `options`

The `options` section controls data sources, brute force, alterations, engine/database connections, and default values for transforms. Each option is handled by dedicated loader functions in Amass, and must match the expected type.

**Supported Options:**

- `datasources` (string): Path to the data sources YAML file. Required for external data source integration.
  - For information about the format and fields in this file, see the [Data Sources Configuration](data_sources.md) section.
- `engine` (string): URL for the Amass engine API (e.g., `http://127.0.0.1:4000/graphql`).
- `database` (string): Database connection string (e.g., `bolt://neo4j:amass4OWASP@neo4j:7687/neo4j` or `postgres://amass:amass4OWASP@assetdb:5432/assetdb`).
- `bruteforce` (object):
  - `enabled` (bool): Enable or disable brute force subdomain enumeration.
  - `wordlists` (array of strings): List of wordlist files for brute forcing. Each file can be plain text or gzipped.
- `alterations` (object):
  - `enabled` (bool): Enable or disable name alteration techniques.
  - `wordlists` (array of strings): List of wordlist files for alterations. Each file can be plain text or gzipped.
- `default_transform_values` (object):
  - `ttl` (int): Default time-to-live for transform results (in minutes).
  - `confidence` (int): Default confidence value (percentage).
  - `priority` (int): Default priority value.
- `active` (bool): Enable active enumeration (e.g., zone transfers, certificate checks).
- `rigid_boundaries` (bool): Enforce strict scope boundaries for enumeration.

> **Notice:** Relative paths are relative to the config file location.

**Example:**

```yaml
options:
  datasources: "./datasources.yaml"
  engine: "http://127.0.0.1:4000/graphql"
  database: "bolt://neo4j:amass4OWASP@neo4j:7687/neo4j"
  bruteforce:
    enabled: false
    wordlists:
      - "./namelist.txt"
  alterations:
    enabled: false
    wordlists:
      - "./alterations.txt"
  default_transform_values:
    ttl: 1440
    confidence: 50
    priority: 5
  active: true
  rigid_boundaries: false
```

#### Environment Variables for Engine and Database

Amass supports configuring the Engine API and Database connection using environment variables as an alternative to specifying the `engine` or `database` URI in the `options` section. **If you specify a URI in the config file for either `engine` or `database`, Amass will NOT use the corresponding environment variables for that object.** There is no merging of environment variables and config values per object—it's either one or the other for each.

**Engine API Environment Variables:**

- `AMASS_ENGINE_USER`: Username for Engine API authentication
- `AMASS_ENGINE_PASSWORD`: Password for Engine API authentication
- `AMASS_ENGINE_HOST`: Host for the Engine API (default: `localhost`)
- `AMASS_ENGINE_PORT`: Port for the Engine API (default: `4000`)
- `AMASS_ENGINE_PATH`: Path for the Engine API (default: `graphql`)
- `AMASS_ENGINE_SCHEME`: Scheme for the Engine API (`http` or `https`, default: `http`)

**Database Environment Variables:**

- `AMASS_DB_USER`: Username for the database
- `AMASS_DB_PASSWORD`: Password for the database
- `AMASS_DB_HOST`: Host for the database (default: `localhost`)
- `AMASS_DB_PORT`: Port for the database (default: `5432`)
- `AMASS_DB_NAME`: Database name (default: `assetdb`)

**Important:**

- If you set the `engine` or `database` URI in the config file, Amass will use only that value and ignore the related environment variables for that object.
- You cannot mix or merge environment variable values with a URI specified in the config for either the Engine API or the Database. For now, it is one or the other, per object.

---

### `transformations`

The `transformations` section controls how assets should be proccessed, how long results from specific transforms are considered valid (TTL), and the minimum confidence level. This can be customized per entity and transform type. 

- Each transformation key is parsed as `<from>-><to>`. Amass validates these against the Open Asset Model (OAM) and ensures there are no conflicts (e.g., you can't have both `FQDN->ALL` and `FQDN->none`). You can set `ttl`, `confidence`, `priority`, and `exclude` for each transformation.
- If a transformation omits `ttl`, `confidence`, or `priority`, Amass uses the values from `default_transform_values` in `options`.
- You can add or modify transformations in Go by editing the `Config.Transformations` map and calling validation methods.

**Supported Format:**
  
- `<from>-><to>` (object):
  - `ttl` (int, optional): Time-to-live for this transformation result, in minutes.
  - `confidence` (int, optional): Confidence value for this transformation (percentage).
  - `priority` (int, optional): Priority value for this transformation.
  - `exclude` (array of strings, optional): List of transforms to exclude.
In this example, the TTL and confidence settings will only apply when the transformation is handled by the plugin named `myplugin`.

> **Tip:** Use `ALL` as the transform to apply the rule to all transforms for a given entity.

**Example:**

```yaml
transformations:
  FQDN->DNS:
    ttl: 1440
  FQDN->DomainRecord:
    ttl: 43200
  Account->ALL:
    ttl: 1080
```

**Granular Example (per plugin):**
[Amass handles plugin level granularity](https://github.com/owasp-amass/amass/blob/main/engine/plugins/support/support.go#L91C1-L105C1). You can specify transformation rules as granularly as you want—even down to a single plugin. If you use the plugin's name as the `<to>` in your `<from>-><to>` transformation key, Amass will apply that rule only for that plugin. This enables highly targeted configuration and fine-grained control over how results are handled for each plugin.

```yaml
transformations:
  FQDN->myplugin:
    ttl: 60
    confidence: 90
```

---

For more details, see the [example configuration files](https://github.com/owasp-amass/amass/tree/main/resources) and the [Amass documentation](https://github.com/owasp-amass/amass/wiki).

---

## How Amass Loads Configuration

Amass supports flexible configuration loading. allowing you to control settings via YAML files, environment variables, and programmatic overrides.

### Configuration Loading Order

1. **Explicit file**: If you specify a config file path (e.g., with `-config`), it is loaded first.
2. **Environment variable**: If the `AMASS_CONFIG` environment variable is set, its path is used.
3. **Default locations**: Amass looks for `config.yaml` in the output directory (usually `~/.config/amass/`) or `/etc/amass/config.yaml` on Linux.

### Programmatic Configuration

If you use Amass as a Go library, you can construct a `Config` object directly in code, set fields, and call methods like `LoadSettings()` or `AcquireConfig()` to merge YAML and programmatic settings.

---

## Advanced Configuration Details

Amass uses Go interfaces and flexible types in its configuration structs to allow for advanced and custom settings:

- **Flexible Options:** [The `options` section in YAML is loaded into a `map[string]interface{}`](https://github.com/owasp-amass/amass/blob/f46cda51b3e9a701a0498eafa0e9f82a0f26e864/config/config.go#L67). This means you can add arbitrary keys and values—even ones not officially documented. If Amass has a loader for your option (like `active`, `rigid_boundaries`, or future features), it will be parsed and used (e.g., check out the code for [loading the `database` option](https://github.com/owasp-amass/amass/blob/f46cda51b3e9a701a0498eafa0e9f82a0f26e864/config/graphdb.go#L40-L57)). Otherwise, you can access these values programmatically if you use Amass as a library.

- **Scope Parsing:** The `Scope` struct uses fields like `PortsRaw []interface{}` so you can specify ports as single values, lists, or ranges in YAML. Amass normalizes these internally, so you have flexibility in how you define scope.

- **Loader Functions:** After deserialization, [Amass runs a series of loader functions to process, validate, and normalize settings](https://github.com/owasp-amass/amass/blob/f46cda51b3e9a701a0498eafa0e9f82a0f26e864/config/config.go#L292-L302). This means you can experiment with new options or override behaviors by adding new keys to your YAML, as long as you handle them in your own fork or via the Go API.

- **Programmatic Access:** If you use Amass as a Go library, you can read, modify, or extend the config structs directly, including any custom or experimental options you add to your YAML.

> **Tip:** This flexibility is powerful for advanced users and developers, but be careful—unsupported or misspelled options may be silently ignored unless handled in code.
