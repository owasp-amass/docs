# :simple-owasp: `Asset`

The [`asset.go`](https://github.com/owasp-amass/open-asset-model/blob/master/asset.go) file  contains the definitions for the core asset interface and all supported asset types. It provides a unified structure and ensures consistency across the **Open Asset Model**.

## Table of Contents

- [Overview](#overview)
- [Asset Interface](#asset-interface)
- [AssetType Enumerations](#assettype-enumerations)
- [AssetList Variable](#assetlist-variable)
- [Usage](#usage)

---

## **//** Overview

The **Open Asset Model** offers a standardized framework for managing and processing a variety of digital asset types. It does so by defining a common **Asset** interface that all asset objects should implement. This allows for a consistent way to retrieve key asset information, understand its type, and convert the asset into JSON for further processing or transportation.

Key features include:

- **Interface abstraction:** A unified way to represent different asset types.
- **Type safety:** Clearly defined asset types as string constants.
- **JSON serialization:** Built-in support for converting assets into JSON format.

---

## **//** Asset Interface

The **Asset** interface is at the heart of the **Open Asset Model** and defines the methods that any asset must implement:

```go
type Asset interface {
    Key() string                    // Returns a unique identifier for the asset.
    AssetType() AssetType           // Returns the type of asset.
    JSON() ([]byte, error)          // Returns the asset as a JSON byte slice.
}
```

### Method Details

- **Key() string**  
  **Purpose:** Returns a unique key (identifier) for the asset.  
  **Use Case:** Useful for indexing and retrieving specific assets.

- **AssetType() AssetType**  
  **Purpose:** Identifies the category or specific type of the asset.  
  **Use Case:** Allows the application to differentiate between asset types such as Domains, Contacts, and Organizations.

- **JSON() ([]byte, error)**  
  **Purpose:** Serializes the asset into JSON.  
  **Use Case:** Enables easy data transmission and storage, as JSON is a widely adopted format for data interchange.

---

## **//** AssetType Enumerations 

The code defines a custom type **AssetType**, which is simply an alias of a string, and uses it to create a list of constants for the supported asset types. This ensures consistency when referring to asset types across the application.

### Definition

```go
type AssetType string
```

### Constants

The file defines many constants representing different asset types:

| **Asset Constant**      | **String Value**        | **Description**                                                |
|-------------------------|-------------------------|----------------------------------------------------------------|
| **Account**             | "Account"               | Represents a user or service account.                          |
| **AutnumRecord**        | "AutnumRecord"          | Denotes records related to autonomous system numbers.          |
| **AutonomousSystem**    | "AutonomousSystem"      | A record for an autonomous system entry.                       |
| **ContactRecord**       | "ContactRecord"         | Contact details and related information.                       |
| **DomainRecord**        | "DomainRecord"          | Information related to domain registration.                    |
| **File**                | "File"                  | Represents a file asset.                                         |
| **FQDN**                | "FQDN"                  | Fully Qualified Domain Name.                                   |
| **FundsTransfer**       | "FundsTransfer"         | Represents a funds transfer transaction.                       |
| **Identifier**          | "Identifier"            | Generic identifier for assets.                                 |
| **IPAddress**           | "IPAddress"             | An asset that represents an IP address.                        |
| **IPNetRecord**         | "IPNetRecord"           | Records related to IP networks or subnets.                     |
| **Location**            | "Location"              | Information about a geographical or logical location.          |
| **Netblock**            | "Netblock"              | Represents a block of network addresses.                       |
| **Organization**        | "Organization"          | Organizational details, such as companies or institutions.     |
| **Person**              | "Person"                | Represents an individual in the system.                        |
| **Phone**               | "Phone"                 | Contact phone information.                                     |
| **Product**             | "Product"               | Details about a product asset.                                 |
| **ProductRelease**      | "ProductRelease"        | Specific versions/releases of a product.                       |
| **Service**             | "Service"               | Represents a service offering.                                 |
| **TLSCertificate**      | "TLSCertificate"        | Information about a TLS certificate.                           |
| **URL**                 | "URL"                   | Represents a URL.                                              |

---

## **//** AssetList Variable 

At the end of the file, an **AssetList** variable is declared. This is a slice containing all of the asset type constants defined in the model. It can be used for iteration or validation, ensuring that all supported types are captured.

### Declaration Code

```go
var AssetList = []AssetType{
    Account, AutnumRecord, AutonomousSystem, ContactRecord, DomainRecord,
    File, FQDN, FundsTransfer, Identifier, IPAddress, IPNetRecord,
    Location, Netblock, Organization, Person, Phone, Product,
    ProductRelease, Service, TLSCertificate, URL,
}
```

**Purpose:**  

- To serve as a central registry of all possible asset types.
- Ensures consistency and ease-of-use when handling assets in various parts of the application.

---

## **//** Usage

The **Open Asset Model** is intended to:

- **Manage Assets:** Provide a consistent way to represent diverse assets, whether for tracking, inventory, compliance, or intelligence purposes.
- **Data Interchange:** Services that need to serialize asset data to JSON for storage, logging, or transmission between microservices.
- **Asset Validation:** Tools that validate the type of asset being processed by comparing against the enumerated list (`AssetList`).
- **Extended Functionality:** Developers can extend the model by implementing the **Asset** interface for new types of assets while maintaining a consistent API.

**Example Scenario:**  
Consider a scenario that requires the tracking annd monitoring of  various asset categories, such as domain names, IP ranges, TLS certificates, and organizational entities. By implementing the `Asset` interface:

- Each asset is uniquely identifiable through `Key()`.
- Asset classification remains standardized via `AssetType()`.
- Assets can be serialized into JSON for seamless integration into reports and API responses.

This ensures a structured and scalable approach to asset representation within reconnaissance workflows. 

---

## **//** Summary

The **Open Asset Model** defined in `asset.go` offers a powerful and flexible way to standardize asset representation through a clear interface and enumerated types, which aids in maintaining consistency across different services and applications. 

---
