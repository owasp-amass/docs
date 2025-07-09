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

## :material-graph: Explore OAM Asset Types

---

<div class="grid cards" markdown>

-   :material-file-account:{ .lg .middle } __Account__

    ---

    Collect usernames, account types, and related attributes to track exposed user accounts

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/account/)

-   :material-registered-trademark:{ .lg .middle } __Domain Record__

    ---
    
    Gather domain insights, including Whois and registrar details

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/domain_record/)

-   :material-comment-outline:{ .lg .middle } __Contact Record__

    ---

    Link email addresses, phone numbers, and locations to discovered entities

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/contact_record/)

-   :material-dns:{ .lg .middle } __FQDN__

    ---

    Record domain resolutions, DNS records, and associated metadata

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/fqdn/)

-   :material-file-find:{ .lg .middle } __File__

    ---

    Capture file names and hashes to analyze digital artifacts

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/file/)

-   :material-bank:{ .lg .middle } __Funds Transfer__

    ---

    Identify bank accounts, payment systems, and transaction details

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/funds_transfer/)

-   :material-id-card:{ .lg .middle } __Identifier__

    ---

	Track unique IDs, references, or numerical values 

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/identifier/)

-   :material-router:{ .lg .middle } __IP Address__

    ---

    Discover IPs, subnets, and routing structures to uncover key infrastructure

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/ip_address/)

-   :material-office-building-marker:{ .lg .middle } __Organization__

    ---

    Uncover entity designations, locations, and operational details to expose connections

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/organization/)

-   :material-account-outline:{ .lg .middle } __Person__

    ---

     Collect names, locations, and attributes to build individual profiles 

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/person/)

-   :material-apps:{ .lg .middle } __Product__

    ---

     Identify online services, cloud providers, and software ecosystems 

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/product/)

-   :material-file-certificate-outline:{ .lg .middle } __TLS Certificate__

    ---

    Gather SSL/TLS certificate details, issuers, and expiration dates for asset verification

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/tls_certificate/)

-   :material-web-refresh:{ .lg .middle } __URL__

    ---

    Log web addresses and associated content to track online presence

    [:octicons-arrow-right-24: Learn more](https://owasp-amass.github.io/docs/open-asset-model/assets/url/)

</div>
