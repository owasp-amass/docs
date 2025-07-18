# Amass Data Sources Configuration

This document explains how to configure external data sources for Amass using the `datasources.yaml` file. Data sources provide additional information for enumeration and require credentials for access.

> **Note:** Some data sources require a paid subscription or API key to access advanced features. Using paid or premium data sources can unlock extra capabilities and may provide a better experience for the Amass engine, including more comprehensive results and faster queries.

---

## Data Sources Configuration: `datasources.yaml`

This file defines which external data sources Amass will use and their credentials.

### `global_options`

Set global defaults for all data sources.

- `minimum_ttl`: Default TTL for data source results (in minutes).

**Format:**

```yaml
# these are the global options related to data sources.
global_options:
# minimum_ttl is the default used when datasources don't specify a larger ttl value.
  minimum_ttl: 1440 #one day
```

### `datasources`

The `datasources` section is a list of external data sources Amass will use. Each entry can specify credentials, TTL, and multiple accounts. All fields are optional except for `name`.

**Supported Fields:**

- `name` (string, required): The name of the data source (e.g., `Shodan`, `CIRCL`).
- `ttl` (int, optional): Time-to-live for results from this data source, in minutes. If omitted, the global minimum TTL is used.
- `creds` (object, optional): A map of account names to credential sets. You can name the account key anything (e.g., `account`, `personal`, `work`, `default`), which helps organize multiple credential sets for the same data source. Amass will accept any key name here.
  - `<account>` (object): The account name (arbitrary string) for this credential set.
    - `apikey` (string, optional): API key for the data source.
    - `username` (string, optional): Username for authentication.
    - `password` (string, optional): Password for authentication.
    - `secret` (string, optional): Secret value for authentication (used by some APIs).

**Format:**

```yaml
datasources:
  - name: <DataSourceName>
    ttl: <minutes> # optional
    creds:
      <account>: # You can name this key anything (e.g., 'account', 'personal', 'work')
        apikey: <your_api_key>
        username: <your_username>
        password: <your_password>
        secret: <your_secret>
```

**Example:**

```yaml
datasources:
  - name: Shodan
    ttl: 10080
    creds:
      account:
        apikey: YOUR_SHODAN_API_KEY
  - name: CIRCL
    creds:
      account:
        username: YOUR_USERNAME
        password: YOUR_PASSWORD
```

---

## Tips

- Comment or uncomment sections in YAML to enable/disable features.
- Use relative paths for wordlists and data source files for portability.
- Always keep your API keys and credentials secure.

For more details, see the [example configuration files](https://github.com/owasp-amass/amass/tree/main/resources) and the [Amass documentation](https://github.com/owasp-amass/amass/wiki).

---

## Advanced Configuration Details

- **Custom Data Source Credentials:** In the data source config, [credentials are stored as a map](https://github.com/owasp-amass/amass/blob/f46cda51b3e9a701a0498eafa0e9f82a0f26e864/config/datasrcs.go#L16-L29) (`map[string]*Credentials`). This allows you to define multiple credential sets per data source in YAML, and Amass will deserialize them into Go structs. You can add new credential types as needed for custom integrations.

**Tip:** This flexibility is powerful for advanced users and developers, but be careful—unsupported or misspelled options may be silently ignored unless handled in code.
