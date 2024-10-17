# 🧩 Amass Docs 

**OWASP Amass** is an open-source, versatile Attack Surface Intelligence platform designed to comprehensively map an organization’s footprint. Built for flexibility and depth, Amass combines advanced data collection, network mapping, and OSINT capabilities to deliver detailed insights into physical and digital assets. 

## Overview

Amass extends far beyond basic subdomain enumeration, offering a comprehensive, automated approach to information gathering that reveals the full scope of an organization's infrastructure.

!!! info "Open Asset Model (OAM)"
    The Open Asset Model expands traditional asset specifications by covering both physical and digital assets, aiming to provide a comprehensive view of 
    organization'sattack surface. It defines assets and their relationships, capturing the real-world interconnectedness between them.
    (https://github.com/owasp-amass/open-asset-model/blob/master/docs/taxonomy.md)

- **Broader Data Collection Capabilities**: Gather a wide range of information to uncover assets and connections that traditional methods might miss.
- **Advanced Recon Features**: Use powerful tools for detailed network mapping and asset identification to fully understand potential attack surfaces.
- **Community-Driven Innovation**: Contributors actively share insights, demos, and practical applications, driving ongoing improvements.
- **Continuous Development**: Regular updates introduce new functionalities and enhanced performance, keeping Amass aligned with the latest reconnaissance needs.

---

## Getting Started 

🔧 Follow these steps to set up the OWASP Amass project using Docker Compose:

#### Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Docker:** Installed and running on your system. You can download it from [Docker's Official Website](https://www.docker.com/products/docker-desktop/).
  
- **Docker Compose:** Typically, Docker Compose is bundled with Docker Desktop, but you can verify the installation or install in seperately from
    [Docker Compose Installation](https://docs.docker.com/compose/)).

- **Git:** To clone the Amass repository. Download it from [Git's Official Website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Step 1: Clone the Amass GitHub Repository

Start by cloning the OWASP Amass repository, which contains the Docker Compose setup files.







1. **Installation**: Check out the [installation guide](installation.md) for setup instructions.

2. **Basic Usage**: Learn practical ways to use Amass in the [user manual](user-manual.md).

3. **Configuration**: Customize Amass with settings described in the [configuration guide](configuration.md).


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
