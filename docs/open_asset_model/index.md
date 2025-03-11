# :simple-owasp: Open Asset Model

The **Amass Project's** [Open Asset Model](https://github.com/owasp-amass/open-asset-model) redefines the understanding of an attack surface. Shifting the paradigm away from narrow, internet infrastructure-focused collection, the **OAM** broadens its scope to include both physical and digital assets. This approach delivers a realistic view of **assets and their lesser-known associations**, utilizing adversarial tactics to gain visibility into potential risks and attack vectors that might otherwise be overlooked.

---

## **//** Overview

- **Deep Attack Surface Intelligence:** Identifies both **physical and digital assets**, moving beyond IT infrastructure.
- **Standardized Asset Framework:** Ensures **consistency in asset classification**, facilitating efficient data exchange and streamlined analysis.
- **Cyclic Discovery:** Recursively approaches data exploration, leveraging each finding to dynamically **expand the target scope**.
- **Community-Driven:** Developed and continuously refined by security experts within the **OWASP Amass** ecosystem.
- **Risk Mapping:** Exposes hidden attack vectors by **mapping asset relationships** and tracking their changes over time.

---


## :material-graph: Graph Structure and Data Model
    
=== "[Assets]()"
    [:simple-github:](https://github.com/owasp-amass/open-asset-model/blob/master/asset.go)
     ``` json      
        - Account
        - Certificate
        - Contact
        - DNS
        - File
        - Financial
        - Identifier
        - Network
        - Organization
        - People
        - Platform
        - Registration
        - URL
     ```      


=== "[Relations]()" 
    [:simple-github:](https://github.com/owasp-amass/open-asset-model/blob/master/relation.go) 
    
    ``` json
        - Also referred to as edges.
        - Always have a direction to establish asset associations.
        - Able to store properties for enriched data analysis.
        - Explicit naming convention improves query performance.
        - Enable graph traversal to uncover asset associations.
        - Define structured links between discovered assets.
        - Facilitate discovery of infrastructure dependencies.
        - Support queries that reveal attack surface risks.
        - Allow efficient correlation of connected entities.
    ```
     
    
=== "[Properties]()"
    [:simple-github:](https://github.com/owasp-amass/open-asset-model/blob/master/property.go)

    ``` json
        - Store metadata for discovered assets and their relationships.  
        - Attach structured data to entities and relationships.  
        - Standardize attributes like timestamps and source IDs.  
        - Enable querying and filtering of asset metadata.  
        - Support enrichment with additional asset details.  
        - Provide a flexible structure across asset types.  
    ```

    
### Explore each asset type and their distinct relationships:

---


<div class="grid cards" markdown>


-   :material-file-account:{ .lg .middle } __Account__

    ---

    Collect usernames, account types, and related attributes to track exposed user accounts

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/account/)


-   :material-file-certificate-outline:{ .lg .middle } __Certificate__

    ---

    Gather SSL/TLS certificate details, issuers, and expiration dates for asset verification

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/certificate/)


-   :material-comment-outline:{ .lg .middle } __Contact__

    ---

    Link email addresses, phone numbers, and locations to discovered entities

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/contact/)


-   :material-dns:{ .lg .middle } __DNS__

    ---

    Record domain resolutions, DNS records, and associated metadata

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/dns/)


-   :material-file-find:{ .lg .middle } __File__

    ---

    Capture file names and hashes to analyze digital artifacts

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/file/)


-   :material-bank:{ .lg .middle } __Financial__

    ---

    Identify bank accounts, payment systems, and transaction details

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/financial/)


-   :material-id-card:{ .lg .middle } __Identifier__

    ---

	Track unique IDs, references, or numerical values 

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/identifier/)


-   :material-router:{ .lg .middle } __Network__

    ---

    Discover IPs, subnets, and routing structures to uncover key infrastructure

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/network/)


-   :material-office-building-marker:{ .lg .middle } __Organization__

    ---

    Uncover entity designations, locations, and operational details to expose connections

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/organization/)


-   :material-account-outline:{ .lg .middle } __People__

    ---

     Collect names, locations, and attributes to build individual profiles 

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/people/)


-   :material-apps:{ .lg .middle } __Platform__

    ---

     Identify online services, cloud providers, and software ecosystems 

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/platform/)


-   :material-registered-trademark:{ .lg .middle } __Registration__

    ---

    
    Gather domain insights, including Whois and registrar details

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/registration/)


-   :material-web-refresh:{ .lg .middle } __URL__

    ---

    Log web addresses and associated content to track online presence

    [:octicons-arrow-right-24: Learn more](https://51nk0r5w1m.github.io/docs/open-asset-model/url/)

</div>






   

    


    
