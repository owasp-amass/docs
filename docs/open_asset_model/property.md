# :simple-owasp: `Property`

The [`property.go`](https://github.com/owasp-amass/open-asset-model/blob/master/property.go) file defines core functionality for managing and representing asset properties within the **Open Asset Model**. It provides a standardized way to store, categorize, and serialize metadata associated with various asset types.

## Table of Contents

- [Overview](#overview)
- [Property Interface](#property-interface)
- [PropertyType Enumeration](#propertytype-enumeration)
- [PropertyList Variable](#propertylist-variable)
- [Example](#example)

---

## **//** Overview

The **Open Asset Model** is designed to offer a consistent way to manage and interact with various kinds of asset information. The `property.go` file outlines core components related to asset properties. The primary components defined in this file are:

- **Property Interface:** An interface that any asset property should implement.
- **PropertyType:** A string-based type that categorizes the different property types.
- **PropertyList:** A list of all defined property types for ease of access and iteration.

These components enable the creation of different asset property implementations that can be serialized (e.g., into JSON) while following a common interface.

---

## **//** Property Interface

The **Property** interface establishes the contract that all asset property types must satisfy. Implementing this interface ensures consistency across different property representations. Below are the key methods declared within the interface:

| **Method**      | **Return Type**        | **Description**                                                                                      |
| --------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **Name()**      | `string`               | Returns the name of the property. This serves as the identifier for the particular asset attribute. |
| **Value()**     | `string`               | Retrieves the value associated with the property in string format.                                  |
| **PropertyType()** | `PropertyType`      | Provides the type of the property, ensuring it aligns with one of the predefined categories.          |
| **JSON()**      | `([]byte, error)`      | Generates a JSON representation of the property, facilitating easy serialization and transmission.   |

**Key Points:**

- **Encapsulation:** Each property must encapsulate both its identifier and value.
- **Serialization:** The `JSON()` method allows for seamless integration with systems that rely on JSON data.
- **Extensibility:** By implementing this interface, new property types can be added without altering the core system.

**Example interface declaration:**

```go
type Property interface {
    Name() string
    Value() string
    PropertyType() PropertyType
    JSON() ([]byte, error)
}
```

---

## **//** PropertyType Enumeration

The `PropertyType` type is defined as a string alias. It is used to categorize different asset properties, enabling the nature of the properties to be quickly identified.

**Defined PropertyType Values:**

| **Constant Name**         | **Actual Value**            | **Description**                                                       |
| ------------------------- | --------------------------- | --------------------------------------------------------------------- |
| **DNSRecordProperty**     | "DNSRecordProperty"         | Represents properties related to DNS record data.                     |
| **SimpleProperty**        | "SimpleProperty"            | Used for properties that are generic or do not fit in another category. |
| **SourceProperty**        | "SourceProperty"            | Indicates the source or origin of the asset data.                     |
| **VulnProperty**          | "VulnProperty"              | Denotes properties concerning vulnerability details.                  |


Example constant declarations:

```go
type PropertyType string

const (
    DNSRecordProperty PropertyType = "DNSRecordProperty"
    SimpleProperty    PropertyType = "SimpleProperty"
    SourceProperty    PropertyType = "SourceProperty"
    VulnProperty      PropertyType = "VulnProperty"
)
```

---

## **//** PropertyList Variable

The `PropertyList` variable is a slice of all supported **PropertyType** values. This list is helpful for:

- Iterating over all available property types.
- Validating whether a given property type is supported.
- Populating selection options in user interfaces or configuration files.

*Code snippet from the file:*

```go
var PropertyList = []PropertyType{
    DNSRecordProperty, SimpleProperty, SourceProperty, VulnProperty,
}
```

**Why It's Useful:**

- **Convenience:** Instead of hardcoding property types elsewhere, you have a single source of truth.
- **Maintainability:** Adding a new property type in the enumeration automatically includes it in the list.

---

## **//** Example

Below is an example implementation the **Property** interface for a simple property type within a Go application. This example demonstrates creating a struct that represents a simple asset property and implements the required methods:

```go
package main

import (
    "encoding/json"
    "fmt"
    "open_asset_model" // Assuming the package is imported as such
)

// SimpleAssetProperty is an example implementation of the Property interface.
type SimpleAssetProperty struct {
    name  string
    value string
}

// Name returns the name of the property.
func (sap SimpleAssetProperty) Name() string {
    return sap.name
}

// Value returns the value of the property.
func (sap SimpleAssetProperty) Value() string {
    return sap.value
}

// PropertyType returns the property type of SimpleAssetProperty.
func (sap SimpleAssetProperty) PropertyType() open_asset_model.PropertyType {
    return open_asset_model.SimpleProperty
}

// JSON formats the property data into JSON.
func (sap SimpleAssetProperty) JSON() ([]byte, error) {
    return json.Marshal(sap)
}

func main() {
    // Create an instance of a simple asset property
    prop := SimpleAssetProperty{
        name:  "ExampleProperty",
        value: "Value123",
    }
    
    // Serialize the property to JSON
    jsonData, err := prop.JSON()
    if err != nil {
        fmt.Println("Error serializing property to JSON:", err)
        return
    }
    
    fmt.Println("Serialized JSON:", string(jsonData))
}
```

This example highlights:

- Implementation of the **Property** interface.
- How to assign a specific **PropertyType** (in this case, `SimpleProperty`).
- Utilizing JSON serialization for output or storage.

---

## **//** Summary

The `property.go` file is a fundamental part of the **Open Asset Model**. It provides a standardized interface and a set of defined property types to represent diverse asset metadata. Whether you're dealing with DNS records, vulnerability information, source data, or simple key-value pairs, this module offers a robust and extensible way to manage asset properties.

**Key takeaways:**

- **Modularity:** The **Property** interface ensures consistency across multiple property implementations.
- **Extensibility:** New property types can be added easily by extending the enumeration and providing corresponding implementations.
- **Serialization:** Built-in JSON support facilitates seamless integration with external systems and APIs.

--- 
