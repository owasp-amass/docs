# :simple-owasp: VulnProperty

The `VulnProperty` is a specialized property type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) used to represent basic vulnerability information associated with an asset or relation. It is designed to capture structured yet concise details about known or observed security issues, such as CVEs, misconfigurations, or weak service configurations.

Each `VulnProperty` instance describes a single vulnerability and is linked to the asset or relationship it affects. This allows for clear attribution of risk within the asset graph and enables reasoning about exposure across a discovered attack surface.

The `VulnProperty` structure includes:

- **ID** – A unique identifier for the vulnerability entry, often matching a standard enumeration such as a CVE ID (e.g., `CVE-2024-12345`).
- **Description** – A brief summary of the vulnerability's nature or impact.
- **Source** – The origin of the vulnerability data, such as the scanner or source system that identified it (e.g., `nuclei`, `cvefeed`, `custom-rule-engine`).
- **Category** – A high-level classification of the vulnerability, such as `exposed-service`, `software-vuln`, or `configuration`.
- **Enumeration** – A standardized vulnerability taxonomy used to identify the issue, such as `CVE`, `CWE`, or a custom identifier.
- **Reference** – A URL or external reference to more detailed information (e.g., an NVD page or vendor advisory).

By standardizing how vulnerability metadata is attached to assets and relations, `VulnProperty` supports efficient integration of findings from vulnerability scanners, intelligence feeds, and custom assessment tooling. It also facilitates filtering, correlation, and prioritization of risks during triage or remediation workflows.

## :fontawesome-solid-tags: VulnProperty Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `id`           | string | :material-check-decagram: | A unique identifier for the vulnerability (e.g., `CVE-2024-12345`) |
| `desc`         | string | :material-check-decagram: | A brief human-readable summary of the vulnerability |
| `source`       | string | :material-checkbox-blank-circle-outline: | The name of the tool, feed, or method that reported the vulnerability |
| `category`     | string | :material-checkbox-blank-circle-outline: | A general classification of the vulnerability (e.g., `software-vuln`) |
| `enum`         | string | :material-checkbox-blank-circle-outline: | The taxonomy or enumeration system used (e.g., `CVE`, `CWE`) |
| `ref`          | string | :material-checkbox-blank-circle-outline: | An optional reference URL for more information about the vulnerability |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
