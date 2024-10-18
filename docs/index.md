# :simple-owasp: Amass Docs 

**OWASP Amass** is an open-source, versatile Attack Surface Intelligence platform designed to comprehensively map an organization’s footprint. Built for flexibility and depth, Amass combines advanced data collection, network mapping, and OSINT capabilities to deliver detailed insights into physical and digital assets. 

## Overview

Amass extends far beyond basic subdomain enumeration, offering a comprehensive, automated approach to information gathering that reveals the full scope of an organization's infrastructure.


!!! info "Open Asset Model (OAM)"
    The Open Asset Model expands traditional asset specifications by covering both physical and digital assets, aiming to provide a comprehensive view of organization's attack surface.
    It defines assets and their relationships, capturing the real-world interconnectedness between them, allowing for concurrent data collection and querying, making it easier to analyze and visualize reconnaissance results.

---

:fontawesome-brands-youtube:{ .youtube } 
__[Unlocking the Power of OWASP Amass]__ by [@jeff_foley](https://x.com/jeff_foley) - DEFCON 31 Recon Village :octicons-clock-24: 33m  

  [Unlocking the Power of OWASP Amass]: https://www.youtube.com/watch?v=IgxPsv8MXMw

- **Automated Deployment and Enumeration**: Easily deploy Amass with [Docker Compose](https://docs.docker.com/compose/) for quick, automated asset discovery across multiple domains with minimal configuration.

- **Centralized Asset Management with Asset DB**: Use the Asset DB for storing, managing, and retrieving discovered assets, with support for long-term tracking and consistent data collection through the Open Asset Model.

- **Scalable and Flexible Infrastructure**: Designed for enterprise environments, [Docker Compose](https://docs.docker.com/compose/) enables scalable deployments of Amass, ensuring consistent attack surface management for organizations of any size.

- **Advanced Collection and Monitoring**: The Collections Engine refines the data collection process, while open-source tools like [Loki](https://grafana.com/oss/loki/) provide centralized logging, enabling real-time monitoring and diagnostics.

- **Visualization and Data-Driven Insights**: The latest release features a fully integrated [Grafana](https://grafana.com/oss/grafana/) dashboard, providing dynamic visualization and analysis for deeper attack surface intelligence.

---

## :octicons-tools-16: Getting Started 

Follow these steps to set up the OWASP Amass project using Docker Compose:

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Docker:** Installed and running on your system. You can download it from [Docker's Official Website](https://www.docker.com/products/docker-desktop/).
  
- **Docker Compose:** Typically, Docker Compose is bundled with Docker Desktop, but you can verify the installation or install in seperately from
    [Docker Compose Installation](https://docs.docker.com/compose/)).

- **Git:** To clone the Amass repository. Download it from [Git's Official Website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Step 1: Clone the Amass GitHub Repository

Start by cloning the OWASP Amass repository, which contains the Docker Compose setup files.

```bash
git clone https://github.com/OWASP/Amass.git
cd Amass/docker
```

### Step 2: Review the Docker Compose File

Navigate to the `docker/` folder within the cloned repository. In this folder, you will find the `docker-compose.yml` file, which is pre-configured for the Amass setup.

The Docker Compose file defines the services (such as Amass and supporting services) that will be run. You don’t need to make any changes, but it's good to understand how it works. It sets up Amass with the necessary configurations and pulls external data sources like GoIP for better mapping results.

### Step 3: Pull Docker Images

Run the following command to pull the necessary Docker images specified in the `docker-compose.yml` file:

```bash
docker-compose pull
```

This command ensures that you have all the latest dependencies needed to run Amass.

### Step 4: Configure Amass Enumeration

The Amass tool allows you to perform enumeration of external assets. You can set parameters or adjust settings in the configuration file, but if you’re using the default Docker Compose setup, it's ready to go.

Here’s a basic command to enumerate domains using Amass with Docker:

```bash
docker-compose run amass enum -d <target_domain>
```

For example:

```bash
docker-compose run amass enum -d example.com
```

This command runs Amass’s enumeration mode, which collects data from various public sources and scans the target domain for subdomains, IP addresses, and other details.

### Step 5: Run the Docker Compose Setup

Once you are satisfied with the configuration, start the Amass service with Docker Compose:

```bash
docker-compose up
```

This command will bring up all the containers defined in the `docker-compose.yml` file. You will see the containers starting up, and Amass will begin its operations, including data collection.

### Step 6: Monitor and Analyze Data

Once the containers are running, Amass will start collecting information on the domain you specified. The data is logged and can be visualized using the newly introduced [dashboards](advanced-usage.md).

You can also inspect logs from the running containers by using:

```bash
docker-compose logs
```

This helps you understand the progress of the enumeration process.

### Step 7: Stopping and Cleaning Up

To stop the Docker containers and services, use the following command:

```bash
docker-compose down
```

### Step 8: Viewing Results

Amass stores its results in various formats, including text and JSON. To view the results of the enumeration:

```bash
cat output/amass.txt
```

You can further process this data using your preferred tools for visualization or analysis.

---
## :material-tune-variant: Additional Configurations

!!! tip "Custom Configuration and Advanced Usage" 
    [Configurations](configuration.md): If you wish to customize Amass beyond the default setup, you can edit the `config.ini` file to modify settings like source lists, APIs, etc. 

    [GoIP Data](advanced-usage.md): You can integrate GoIP databases into Amass for more geographical insight into discovered assets. Configure this and other advanced features within the `docker-compose.yml` file. 

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
