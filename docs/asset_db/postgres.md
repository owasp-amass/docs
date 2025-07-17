# Setting Up a PostgreSQL Database for OWASP Amass

The OWASP Amass framework can store collected data in a PostgreSQL database. This page walks you through the recommended setup process, including environment variables, database initialization, and configuration in your `config.yaml` file.

> **Note:** These instructions assume PostgreSQL is already installed and running on your system (e.g., `localhost:5432`). You’ll need access to a user with sufficient privileges (typically `postgres`).

## 1. Define Environment Variables

Before running the setup commands, export the following environment variables to define your database, user, and passwords. These values will be used in the setup process and your Amass configuration.

```bash
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export AMASS_DB=assetdb
export AMASS_USER=amass
export AMASS_PASSWORD=amass4OWASP
```

??? info "Secrets Management"
    Consider storing these in a `.env` file and loading them with `source .env` to avoid retyping. Never commit secrets to version control.

## 2. Create the Amass Database and User

Run the following commands in your shell to initialize the database and create a dedicated user for Amass. This uses the `psql` CLI with inline SQL for automation.

```bash
# Add single quotes around the password to handle special characters
export TEMPPASS="'$AMASS_PASSWORD'"

# Create the database and user
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    \getenv assetdb AMASS_DB
    \getenv username AMASS_USER
    \getenv password TEMPPASS

    CREATE DATABASE :assetdb;
    ALTER DATABASE :assetdb SET timezone TO 'UTC';
    CREATE USER :username WITH PASSWORD :password;
EOSQL
```

This will:

* Create the `assetdb` database
* Set its default timezone to UTC (recommended for consistency)
* Create a new user (`amass`) with the specified password

## 3. Enable Extensions and Grant Privileges

Next, connect to the new database and enable the required PostgreSQL extension and assign privileges to the Amass user.

```bash
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$AMASS_DB" <<-EOSQL
    \getenv username AMASS_USER

    CREATE EXTENSION pg_trgm SCHEMA public;

    GRANT USAGE ON SCHEMA public TO :username;
    GRANT CREATE ON SCHEMA public TO :username;
    GRANT ALL ON ALL TABLES IN SCHEMA public TO :username;
EOSQL
```

This will:

* Enable the `pg_trgm` extension (used by Amass for efficient fuzzy string matching)
* Grant the necessary privileges for Amass to create and manage data within the `public` schema

## 4. Update Your Amass Configuration

Once your database is set up, update your Amass `config.yaml` file with the connection string:

```yaml
options:
  # Be sure to replace the credentials with values matching your environment
  database: "postgres://amass:amass4OWASP@127.0.0.1:5432/assetdb"
```

??? info "Security Reminder"
    Avoid committing passwords to source control. Where possible, consider injecting the connection string using an environment variable (e.g., `${AMASS_DB_URI}`).

## 5. Test the Connection

You can test whether the Amass framework is successfully connecting to your PostgreSQL database by running a standard enumeration command:

```bash
amass enum -config config.yaml
```

If the configuration is correct, the collected data will be stored in the PostgreSQL backend you configured.

## ✅ You're Done!

Amass is now ready to store data in your PostgreSQL database. This enables you to persist, analyze, and query discovered assets using SQL or integrate with other tooling and dashboards.

## Troubleshooting Tips

* **Connection Refused?** Ensure PostgreSQL is listening on `127.0.0.1:5432` and that the database server is running.
* **Authentication Failed?** Double-check your environment variable values, especially the user and password.
* **Extension Errors?** Make sure the `pg_trgm` extension is available and installed. You can check with `\dx` in `psql`.

## See Also

* [Amass Configuration](../configuration/configuration.md)
* [PostgreSQL Documentation](https://www.postgresql.org/docs/current/index.html)
* [PostgreSQL `pg_trgm` Extension Docs](https://www.postgresql.org/docs/current/pgtrgm.html)
* [Managing Environment Variables Securely](https://direnv.net/)
