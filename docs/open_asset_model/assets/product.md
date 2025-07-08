# :simple-owasp: Product

The **Product** asset type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) represents a commercial or open-source technology product—hardware, software, or service—that plays a role in an organization's external attack surface. Products may include server software, security appliances, cloud services, content management systems, networking gear, and more.

- **Definition:** A `Product` asset includes a name, type, optional category and description, and optionally a country of origin. It represents a distinct technology offering as discovered in intelligence collection, vulnerability data, or infrastructure enumeration.

- **Purpose:** Modeling products as first-class assets allows the OAM to associate technologies with organizations, services, or infrastructure. This helps analysts answer questions like “What products are deployed by this organization?”, “Where are certain technologies concentrated?”, or “Is this vulnerable product version publicly exposed?”

- **Design Choice:** The `Product` structure is intentionally minimal to support broad applicability. While the `ProductRelease` handles additional information such as version, vendor, and licensing via `Identifier` assets and properties, the core type emphasizes identification and categorization. The inclusion of `country_of_origin` supports use cases related to supply chain risk and regulatory compliance.

## :material-package-variant: Product Attributes

| Attributes         | Type   | Required | Description |
|:------------------:|:------:|:--------:|:------------|
| `unique_id`        | string | :material-check-decagram: | Unique identifier for the product asset |
| `product_name`     | string | :material-check-decagram: | Name of the product (e.g., `nginx`, `Apache Tomcat`, `Zoom`) |
| `product_type`     | string | :material-check-decagram: | General type (`software`, `hardware`, `service`, etc.) |
| `category`         | string | :material-checkbox-blank-circle-outline: | Optional category (e.g., `web_server`, `load_balancer`, `crm`) |
| `description`      | string | :material-checkbox-blank-circle-outline: | Optional short description of the product |
| `country_of_origin`| string | :material-checkbox-blank-circle-outline: | Optional ISO country code or name (e.g., `US`, `Germany`) |

## :material-package-variant: Product Properties

| Property Type | Property Name | Description |
|:-------------:|:-------------:|:------------|
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this Product |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this Product |

## :material-package-variant: Product Outgoing Relations

```mermaid
graph TD
product["Product (nginx)"]
ident["Identifier"]
idRel@{ shape: braces; label: "id" }
product --o idRel
idRel --> ident

org["Organization"]
vendorRel@{ shape: braces; label: "manufacturer" }
product --o vendorRel
vendorRel --> org

url["URL"]
website@{ shape: braces; label: "website" }
product --o website
website --> url

prodrel["ProductRelease"]
release@{ shape: braces; label: "release" }
product --o release
release --> prodrel
```

---

| Relation Type       | Relation Label     | Target Assets    | Description   |
| :-----------------: | :----------------: | :--------------: | :------------ |
| [`SimpleRelation`](../relations/simple_relation.md) | `id` | [`Identifier`](./identifier.md) | Links the Product to `Identifier` assets, such as product identifiers |
| [`SimpleRelation`](../relations/simple_relation.md) | `manufacturer` | [`Organization`](./organization.md) | The organization that produces and supports the product |
| [`SimpleRelation`](../relations/simple_relation.md) | `website` | [`URL`](./url.md) | The website where information can be found about the product |
| [`SimpleRelation`](../relations/simple_relation.md) | `release` | [`ProductRelease`](./product_release.md) | Links the Product to known product releases and versions |

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*