# :simple-owasp: Amass Docs 

**OWASP Amass** is an open-source, versatile **attack surface intelligence** framework designed to comprehensively map an organization’s footprint. Built for flexibility and depth, Amass combines advanced data collection, network mapping, and OSINT capabilities to deliver detailed insights into physical and digital assets. 

## Overview

[OWASP Amass](https://github.com/owasp-amass) extends **far beyond basic subdomain enumeration**, offering a comprehensive, automated approach to information gathering that reveals the full scope of an entity's **physical** and **digital** footprint.


??? info "Open Asset Model (OAM)"
    The [Open Asset Model](https://owasp-amass.github.io/docs/open-asset-model/) expands traditional specifications by modeling both the **physical** and **digital** structure of a target's asset landscape. Defining **asset types**, their unique **properties**, and the **relationships** that join them, the `OAM` compiles a comprehensive view of the attack surface from an adversarial perspective.

---

:fontawesome-brands-youtube:{ .youtube } 
__[Unlocking the Power of OWASP Amass]__ by [@jeff_foley](https://x.com/jeff_foley) - DEFCON 31 Recon Village :octicons-clock-24: 33m  

  [Unlocking the Power of OWASP Amass]: https://www.youtube.com/watch?v=IgxPsv8MXMw

- **Automated Deployment and Enumeration:** Easily deploy Amass with [Docker Compose](https://docs.docker.com/compose/) for quick, automated asset discovery across multiple domains with minimal configuration.

- **Centralized Asset Management with Asset Database:** Use the Asset Database for storing, managing, and retrieving discovered assets, with support for long-term tracking and consistent data collection via the Open Asset Model.

- **Scalable and Flexible Infrastructure:** Designed for enterprise environments, [Docker](https://www.docker.com/products/docker-desktop/) enables scalable deployments of Amass, ensuring consistent attack surface management for organizations of any size.

---

## :octicons-tools-16: Getting Started 

Users have several options when installing the Amass framework.

### Build from Source Code

Install the Amass swiss army knife executable in your preferred environment.

#### Prerequisites

- **Golang:** Install an up-to-date version of Go on your system. You can download it from the [Go Official Website](https://go.dev).

#### Perform the build and installation process

```bash
CGO_ENABLED=0 go install -v github.com/owasp-amass/amass/v5/cmd/amass@main
```

At this point, the binary should be in *$GOPATH/bin*.

#### Install with Libpostal for Street Address Parsing

**On Ubuntu/Debian**
```bash
sudo apt-get install curl autoconf make automake libtool pkg-config
```

**On CentOS/RHEL**
```bash
sudo yum install curl autoconf automake libtool pkgconfig
```

**On MacOS**
```bash
sudo brew install curl autoconf automake libtool pkg-config
```

**Installing libpostal**
```bash
git clone https://github.com/openvenues/libpostal.git
cd libpostal
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make
sudo make install
```

On Linux it's probably a good idea to run.
```bash
sudo ldconfig
```

Now, build OWASP Amass with libpostal compiled in for street address parsing.

```bash
CGO_ENABLED=1 go install -v github.com/owasp-amass/amass/v5/cmd/amass@main
```

At this point, the binary should be in *$GOPATH/bin*.

### Install using Homebrew

The OWASP Amass Project maintains a **Homebrew** package.

#### Prerequisites

- **Homebrew:** Intall an up-to-date version of the package manager on your system. You can download it from the [Homebrew Official Website](https://brew.sh/).

#### Perform the build and installation process

The following two commands will install Amass into your environment:

```bash
brew tap owasp-amass/homebrew-amass
brew install amass
```

### Containerized Execution within Docker Compose

Follow these steps to set up Amass using [Docker Compose](https://docs.docker.com/compose/):

#### Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Docker:** Up-to-date intallation running on your system. You can download it from the [Docker Official Website](https://www.docker.com/products/docker-desktop/).
  
- **Docker Compose:** Typically, Docker Compose is bundled with Docker Desktop, but you can verify the installation or install it seperately from
    [Docker Compose Installation](https://docs.docker.com/compose/).

- **Git:** To clone the Amass repository. Download it from the [Git Official Website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Step 1: Clone the Amass Docker Compose Directory

Start by cloning the OWASP Amass repository containing the Docker Compose setup files.

```bash
git clone https://github.com/owasp-amass/amass-docker-compose.git
mv amass-docker-compose amass   # Optional: Rename the directory to something shorter (e.g., amass)
cd amass   # Navigate to the local repository
```

#### Step 2: Configure the Compose Environment

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
nano config.yaml
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

#### Step 3: Building the Docker Images

Your **Amass** framework is now configured and ready to be built. [Docker Compose](https://docs.docker.com/compose/) will build the required images and start them correctly when you perform your first Amass command execution.

**> Type the following to get started:**

```bash
docker compose run --rm enum -active -d example.org # (1)!
```

1.   If the build process times out, simply execute the command again to resume.


#### :material-update: Update Process for the Compose Environment

**> Make the local repo your current working directory:**

```bash
cd amass
```

**> Shutdown the Amass containers within the Docker environment:**

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
git pull origin main
```

#### :material-update: Update Process for the Docker Images

**> Make the local repo your current working directory:**
```bash
cd amass
```

**> Shutdown the Amass containers within the Docker environment:**

```bash
docker compose down
```

**> Update components from their GitHub repos:**

```bash
docker compose build --pull --no-cache
```

### Amass Packages Maintained by a Third Party

[![Packaging status](https://repology.org/badge/vertical-allrepos/amass.svg)](https://repology.org/metapackage/amass/versions)

---

License
--------
    Copyright 2017-2025 Jeff Foley

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.  
