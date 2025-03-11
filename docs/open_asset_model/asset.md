# :simple-owasp: `Asset`

The [`asset.go`](https://github.com/owasp-amass/open-asset-model/blob/master/asset.go) file  cdefines the **core asset interface** and all supported **asset types** within the **Open Asset Model**. It provides a structured way to represent, manage, and process various digital and physical asset types in a standardized manner.

## Table of Contents

- [Overview](#overview)
- [Asset Interface](#asset-interface)
- [AssetType Enumerations](#assettype-enumerations)
- [AssetList Variable](#assetlist-variable)
- [Usage](#usage)

---

## **//** Overview

The **Open Asset Model** provides a consistent framework for defining, categorizing, and processing different **asset types** used in **security intelligence**, **asset tracking**, and **reconnaissance workflows**. The `asset.go` file establishes a foundation for working with assets by:

- **Defining an Asset Interface**: A unified contract that all asset objects must implement.

- **Enumerating Asset Types**: Clearly defined asset categories as constants.

- **Supporting JSON Serialization**: Built-in methods for data interchange.

- **Ensuring Type Safety**: Restricting asset type values to predefined categories.

These features **enhance interoperability** and **enable structured data processing** across asset intelligence applications.

---

## **//** Asset Interface

The **`Asset interface`** defines a common structure for all asset types, ensuring consistency when interacting with different assets. Any asset in the model must implement the following methods:

```go
// Asset Interface

type Asset interface {
    Key() string                    // Returns a unique identifier for the asset
    AssetType() AssetType           // Returns the type of asset
    JSON() ([]byte, error)          // Serializes the asset to JSON
}
```

### Method Breakdown

| **Method**        | **Return Type**   | **Description**                                            |
|-------------------|-------------------|------------------------------------------------------------|
| **`Key()`**       | `string`          | Returns a **unique identifier** for the asset              |
| **`AssetType()`** | `AssetType`       | Identifies the **type of asset** (e.g., FQDN, IP Address)  |
| **`JSON()`**      | `([]byte, error)` | Serializes the **asset into JSON format**                  |

### Usage Considerations

- **`Key()`**: ensures each asset is uniquely identifiable.

- **`AssetType()`**: provides categorization for structured asset processing.

- **`JSON()`**: enables easy data interchange across APIs and databases.

---

## **//** AssetType Enumerations 

The **`AssetType`** is defined as a **string alias**, ensuring type safety and consistency across the model:

```go
type AssetType string
```

### Asset Type Constants

The file defines the constants representing different asset types:

| **Asset Constant**      | **String Value**        | **Description**                                            |
|-------------------------|-------------------------|------------------------------------------------------------|
| **`Account`**           | `"Account"`             | Represents a **user or service account**                   |
| **`AutnumRecord`**      | `"AutnumRecord"`        | Records related to **autonomous system numbers**           |
| **`AutonomousSystem`**  | `"AutonomousSystem"`    | Record for an **autonomous system (AS)**                 |
| **`ContactRecord`**     | `"ContactRecord"`       | **Contact details** and associated metadata                |
| **`DomainRecord`**      | `"DomainRecord"`        | Represents **domain registration information**             |
| **`File`**              | `"File"`                | Represents a **file asset**                                |
| **`FQDN`**              | `"FQDN"`                | **Fully Qualified Domain Name**                            |
| **`FundsTransfer`**     | `"FundsTransfer"`       | Represents a **financial transaction**                     |
| **`Identifier`**        | `"Identifier"`          | Generic **identifier for assets**                          |
| **`IPAddress`**         | `"IPAddress"`           | Represents an **IP address**                               |
| **`IPNetRecord`**       | `"IPNetRecord"`         | Records related to **IP networks/subnets**                 |
| **`Location`**          | `"Location"`            | **Geographical** or **logical location** data              |
| **`Netblock`**          | `"Netblock"`            | Represents a **block of network addresses**                |
| **`Organization`**      | `"Organization"`        | Organizational details for **companies and institutions**  |
| **`Person`**            | `"Person"`              | Represents an **individual entity**                        |
| **`Phone`**             | `"Phone"`               | **Phone** number/**contact** information                   |
| **`Product`**           | `"Product"`             | Details about **technologies**                             |
| **`ProductRelease`**    | `"ProductRelease"`      | Specific **versions or releases** of technology products   |
| **`Service`**           | `"Service"`             | Represents a **service offering**                          |
| **`TLSCertificate`**    | `"TLSCertificate"`      | Information about **TLS certificates**                     |
| **`URL`**               | `"URL"`                 | Represents a **URL (web address)**                         |

---

## **//** AssetList Variable 

To streamline validation and iteration over supported asset types, the file defines **`AssetList`**, which includes all asset type constants:

```go
var AssetList = []AssetType{
    Account, AutnumRecord, AutonomousSystem, ContactRecord, DomainRecord,
    File, FQDN, FundsTransfer, Identifier, IPAddress, IPNetRecord,
    Location, Netblock, Organization, Person, Phone, Product,
    ProductRelease, Service, TLSCertificate, URL,
}
```

**Purpose of `AssetList`:**  

- Provides a **centralized registry** of all asset types.

- Allows **iteration over supported asset types** in functions.

- Ensures **type safety** by validating asset types against the list.

---

## **//** Usage

The **Open Asset Model** provides a structured way to manage diverse asset types.

Below is an example demonstrating how to:

- **Create** a new asset implementing the **`Asset`** interface.

- **Retrieve** the asset type.

- **Serialize** the asset to JSON.

```go
package main

import (
    "encoding/json"
    "fmt"
    "github.com/owasp-amass/open-asset-model"
)

// Example implementation of an asset

type CustomAsset struct {
    key  string
    atype open_asset_model.AssetType
}

func (ca CustomAsset) Key() string {
    return ca.key
}

func (ca CustomAsset) AssetType() open_asset_model.AssetType {
    return ca.atype
}

func (ca CustomAsset) JSON() ([]byte, error) {
    return json.Marshal(ca)
}

func main() {
    asset := CustomAsset{
        key:  "example-key",
        atype: open_asset_model.FQDN,
    }

    jsonData, err := asset.JSON()
    if err != nil {
        fmt.Println("Error serializing asset to JSON:", err)
        return
    }

    fmt.Printf("Asset Type: %s\n", asset.AssetType())
    fmt.Printf("Serialized JSON: %s\n", string(jsonData))
}
```

---

## **//** Summary

The `asset.go` file is fundamental to the **Open Asset Model**, ensuring **standardized asset representation** across various security and reconnaissance applications.

Key takeaways:

- **Defines a structured Asset interface** for consistent asset management.

- **Enumerates asset types** to ensure type safety and consistency.

- **Provides JSON serialization support** for data interchange.

- **Includes `AssetList`** to facilitate asset type validation and iteration.

By implementing this structured approach, **contributors** can extend asset handling capabilities while **users** can integrate asset intelligence into their security workflows efficiently. 

---
