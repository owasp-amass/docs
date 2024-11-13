# :simple-owasp: Amass Docs 

**OWASP Amass** is an open-source, versatile Attack Surface Intelligence platform designed to comprehensively map an organization’s footprint. Built for flexibility and depth, Amass combines advanced data collection, network mapping, and OSINT capabilities to deliver detailed insights into physical and digital assets. 

## Overview

Amass extends far beyond basic subdomain enumeration, offering a comprehensive, automated approach to information gathering that reveals the full scope of an organization's infrastructure.


!!! info "Open Asset Model (OAM)"
    The `Open Asset Model` expands traditional asset specifications by covering physical and digital assets, providing a comprehensive view of an organization's attack surface.
    It defines assets and their relationships, capturing their real-world interconnectedness. The `OAM` allows for concurrent data collection and querying, automating the asset collection, analysis, and visualization process.

---

:fontawesome-brands-youtube:{ .youtube } 
__[Unlocking the Power of OWASP Amass]__ by [@jeff_foley](https://x.com/jeff_foley) - DEFCON 31 Recon Village :octicons-clock-24: 33m  

  [Unlocking the Power of OWASP Amass]: https://www.youtube.com/watch?v=IgxPsv8MXMw

- **Automated Deployment and Enumeration:** Easily deploy Amass with [Docker Compose](https://docs.docker.com/compose/) for quick, automated asset discovery across multiple domains with minimal configuration.

- **Centralized Asset Management with Asset DB:** Use the Asset DB for storing, managing, and retrieving discovered assets, with support for long-term tracking and consistent data collection through the Open Asset Model.

- **Scalable and Flexible Infrastructure:** Designed for enterprise environments, [Docker](https://www.docker.com/products/docker-desktop/) enables scalable deployments of Amass, ensuring consistent attack surface management for organizations of any size.

- **Advanced Collection and Monitoring:** The Collections Engine refines the data collection process, while open-source tools like [syslog-ng](https://github.com/syslog-ng/syslog-ng) provide centralized logging, enabling real-time monitoring and diagnostics.

- **Visualization and Data-Driven Insights:** The latest release features a fully integrated [Grafana](https://grafana.com/oss/grafana/) dashboard, providing dynamic visualization and analysis for deeper attack surface intelligence.

---

## :octicons-tools-16: Getting Started 

Follow these steps to set up the OWASP Amass Project using [Docker Compose](https://docs.docker.com/compose/):

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Docker:** Up-to-date intallation running on your system. You can download it from [Docker's Official Website](https://www.docker.com/products/docker-desktop/).
  
- **Docker Compose:** Typically, Docker Compose is bundled with Docker Desktop, but you can verify the installation or install it seperately from
    [Docker Compose Installation](https://docs.docker.com/compose/).

- **Git:** To clone the Amass repository. Download it from [Git's Official Website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Step 1: Clone the Amass Docker Compose Directory

Start by cloning the OWASP Amass repository, which contains the Docker Compose setup files.

```bash
git clone https://github.com/owasp-amass/amass-docker-compose.git
mv amass-docker-compose amass   # Optional: Rename the directory to something shorter (e.g., amass)
cd amass   # Navigate to local directory
```

### Step 2: Configure the Compose Environment

**> Open the `assetdb.env` File:**

Navigate to the `config` directory and open the `assetdb.env` file in a text editor to set the database passwords.

```bash
cd config
nano assetdb.env # (1)!
```

1.   You can replace `nano` with your preferred text editor, like `vim` or `code` for Visual Studio Code.


**> Set the Passwords:** 

In the `assetdb.env` file, locate the lines for `POSTGRES_PASSWORD` and `AMASS_PASSWORD`. Update them to assign new values. 

For example:

```bash
POSTGRES_PASSWORD= your_new_postgres_password
AMASS_PASSWORD= your_new_amass_password
```

!!! Warning
    This cannot be performed after you start the Docker Compose and the database has been created.

**> Save Changes:** 

After editing, save the file:

- If you're using **nano**: Press `Ctrl + O` (then hit `Enter`) to save and `Ctrl + X` to exit.

- If you're using **vim**: Press `Esc`, then type `:wq` and hit `Enter`.


**> Modify the `config.yaml` File:**

Open the `config.yaml` file to set the database password to the one you just assigned as `AMASS_PASSWORD`.

```bash
nano ../config.yaml
```

**> Update the Database Password:** 

Find the section in the `config.yaml` file that specifies the database settings. Change the password to match the `AMASS_PASSWORD` you set earlier.

For example:

```yaml
options:
  ...
  database: "postgres://amass:password@assetdb:5432/assetdb"
```

**> Save Changes:**

As before, save the changes using your preferred text editor.


!!! info "Update the Data Sources"
    If you want to configure data sources, you can modify the `datasources.yaml` file. Open it with:
    ```bash
    nano datasources.yaml
    ```
    Uncomment the lines you need, and provide any necessary credentials.

### Step 3: Building the Docker Images

Your **Amass** framework is now configured and ready to be built. [Docker Compose](https://docs.docker.com/compose/) will build the required images and start them correctly when you perform your first Amass command execution.

**> Type the following to get started:**

```bash
docker compose run --rm amass enum -active -d example.org # (1)!
```

1.   If the build process times out, simply execute the command again to resume.


**> Accessing the Web UI:**

You can obtain information about your asset discoveries by accessing the web UI at `http://127.0.0.1:3000`

> All persistent data used exists on your host in the local repo root directory.

> The `assetdb` is a [PostgreSQL](https://www.postgresql.org/) database reachable from your localhost on `port 55432`.

> The `config` files in the local repo are automatically mapped to where components expect to find them in the Docker environment.

!!! tip "Utilize the IP2Location Database" 
    - **Sign up** for a free [IP2Location LITE](https://lite.ip2location.com/) account.
    - **Download Database File:** Download the `IP2LOCATION-LITE-DB11.CSV` and `IP2LOCATION-LITE-DB11.IPV6.CSV` files.  
    - **Copy Files to the Compose Directory:** Copy the downloaded CSV files into the compose directory:
    ```bash
    cp path/to/IP2LOCATION-LITE-DB11.CSV ./ 
    cp path/to/IP2LOCATION-LITE-DB11.IPV6.CSV ./
    ```
    - **Run the Amass Docker Compose:** While the Amass Docker Compose is up, execute the script to insert the geo information into the database:
    ```bash
    ./upload_ip2loc_data.sh
    ```


## :material-update: Update Process for the Compose Environment

**> Make the local repo your current working directory:**

```bash
cd amass
```

**> Shutdown the Amass framework within the Docker environment:**

```bash 
docker compose down
```

**> Backup the configuration files:**

```bash 
cp config/assetdb.env config/config.yaml config/datasources.yaml backups/
```

**> Backup the following directories: `assetdb` , `data` , `logs`.**

**> Update the local repo:**

```bash
git pull origin master
```

## :material-update: Update Process for the Docker Images

**> Make the local repo your current working directory:**
```bash
cd amass
```

**> Shutdown the Amass framework within the Docker environment:**

```bash
docker compose down
```

**> Update components from their GitHub repos:**

```bash
docker compose pull
docker compose build --pull --no-cache
```

---

License
--------
    Copyright 2017 Jeff Foley

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.  
