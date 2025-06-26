# :simple-owasp: `Property`

The [`property.go`](https://github.com/owasp-amass/open-asset-model/blob/master/property.go) file defines the **core functionality** for managing and representing asset properties within the **Open Asset Model**. It provides a standardized way to **store, categorize, and serialize metadata** associated with various asset types.

## Table of Contents

- [Overview](#overview)
- [Property Interface](#property-interface)
- [PropertyType Enumeration](#propertytype-enumeration)
- [PropertyList Variable](#propertylist-variable)
- [Usage](#usage)

---

## **//** Overview

The **Open Asset Model** provides a structured approach to handling **metadata** for different asset types. The **`property.go`** file establishes key components that ensure **consistency and extensibility** in property management:

- **Property Interface** – Defines a common structure that all asset properties must implement.

- **PropertyType Enumeration** – Predefined constants that categorize different asset properties.

- **PropertyList** – A list of all supported property types for **validation and iteration**.

These components allow **standardized metadata representation**, ensuring structured **asset intelligence, security analysis, and interoperability** across various applications.

---

## **//** Property Interface

The **Property interface** defines the required methods that any asset property must implement. This ensures that all properties are represented in a consistent format.

```go
// Property Interface
type Property interface {
    Name() string          // Returns the property name (identifier)
    Value() string         // Returns the value of the property
    PropertyType() PropertyType // Categorizes the property type
    JSON() ([]byte, error) // Serializes the property to JSON
}
```

| **Method**           | **Return Type**        | **Description**                                       |
| --------------- -----| ---------------------- | ------------------------------------------------------|
| **`Name()`**         | `string`               | Returns the **identifier name** of the property       |
| **`Value()`**        | `string`               | Retrieves the value associated with the property      |
| **`PropertyType()`** | `PropertyType`         | Provides the **category** of the property             |
| **`JSON()`**         | `([]byte, error)`      | Serializes the **property into JSON format**          |

### Usage Considerations

- **Encapsulation**: Ensures that property data remains structured.

- **Serialization**: Allows for seamless integration with JSON-based systems.

- **Extensibility**: Developers can introduce new property types while maintaining compatibility.

---

## **//** PropertyType Enumeration

The `PropertyType` is a **string alias** that categorizes asset properties, ensuring clarity and **structured property handling**.

```go
type PropertyType string
```


**Predefined Property Types:**

| **Constant Name**         | **Actual Value**       | **Description**                                         |
| ------------------------- | -----------------------| --------------------------------------------------------|
| **`DNSRecordProperty`**   | `"DNSRecordProperty"`  | Represents properties related to **DNS records**        |
| **`SimpleProperty`**      | `"SimpleProperty"`     | **General-purpose** property for miscellaneous metadata |
| **`SourceProperty`**      | `"SourceProperty"`     | Indicates the **origin or source** of asset data        |
| **`VulnProperty`**        | `"VulnProperty"`       | Represents **vulnerability-related** properties         |


**Property Type Declaration**

```go
const (
    DNSRecordProperty PropertyType = "DNSRecordProperty"
    SimpleProperty    PropertyType = "SimpleProperty"
    SourceProperty    PropertyType = "SourceProperty"
    VulnProperty      PropertyType = "VulnProperty"
)
```

---

## **//** PropertyList Variable

To facilitate **validation and iteration**, the model defines **`PropertyList`**, which contains all property types.

```go
var PropertyList = []PropertyType{
    DNSRecordProperty, SimpleProperty, SourceProperty, VulnProperty,
}
```

**Why `PropertyList` is Useful:**

- **Validation**: Ensures that only **supported property types** are used.

- **Iteration**: Allows for **dynamic property processing** across multiple systems.

- **Maintainability**: New property types can be **added easily** while keeping the model consistent.

---

## **//** Usage

The **Open Asset Model** uses **`property.go`** for structured metadata handling. 

Below is an example demonstrating how to:

- **Retrieve property type information**.

- **Serialize properties to JSON**.

- **Validate whether a property type exists in `PropertyList`**.

```go
package main

import (
    "encoding/json"
    "fmt"
    "github.com/owasp-amass/open-asset-model"
)

func main() {
    // Define an example property type (predefined in the model)
    propertyType := open_asset_model.DNSRecordProperty

    // Serialize the property type into JSON format
    jsonData, err := json.Marshal(propertyType)
    if err != nil {
        fmt.Println("Error serializing property type to JSON:", err)
        return
    }

    fmt.Printf("Property Type: %s\n", propertyType)
    fmt.Printf("Serialized JSON: %s\n", string(jsonData))

    // Validate if the property type exists in PropertyList
    isValid := false
    for _, p := range open_asset_model.PropertyList {
        if p == propertyType {
            isValid = true
            break
        }
    }

    if isValid {
        fmt.Println("The property type is valid! ✅")
    } else {
        fmt.Println("The property type is invalid! ❌")
    }
}
```

---

## **//** Summary

The **`property.go`** file is a fundamental part of the **Open Asset Model**, ensuring **structured metadata representation** for asset intelligence workflows. 

Key takeaways:

- **Defines a structured Property interface** to standardize asset metadata.

- **Enumerates property types** to ensure data consistency.

- **Provides JSON serialization support** for data interchange.

- **Includes `PropertyList`** to facilitate property type validation and iteration.

By following this structured approach, **contributors** can extend the property model, while **users** can leverage predefined properties for efficient asset intelligence and metadata management.