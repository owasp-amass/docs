# :simple-owasp: `Relation`

The [`relation.go`](https://github.com/owasp-amass/open-asset-model/blob/master/relation.go) file manages and validates relationships between different asset types in the **Open Asset Model**.



## Table of Contents 

- [Overview](#overview)
- [Relation Interface and Types](#relation-interface-and-types)
- [Asset Relationship Mappings](#asset-relationship-mappings)
- [Utility Functions](#utility-functions)
  - [GetAssetOutgoingRelations](#getassetoutgoingrelations)
  - [GetTransformAssetTypes](#gettransformassettypes)
  - [assetTypeRelations](#assettyperelations)
  - [ValidRelationship](#validrelationship)
- [Usage](#usage)

---

## **//** Overview

The **Open Asset Model** is designed to manage complex relationships between various types of assets (such as accounts, domain records, IP addresses, organizations, etc.) in a flexible and extensible way. The `relation.go` file focuses on defining:

- **Relation Types** – A set of constants representing different types of relationships.
- **Relationship Mappings** – Predefined mappings specifying which asset types can be related to one another.
- **Validation & Transformation Functions** – Helper functions to query, transform, and validate relationships according to the defined taxonomy.

This model is particularly useful in contexts where assets need to be interconnected in a structured taxonomy, ensuring data integrity and consistency throughout asset intelligence gathering.

---

## **//** Relation Interface and Types

### Relation Interface

The file defines a central **Relation** interface that any relation entity must implement. This interface requires the following methods:

```go
Label() string  // Returns a label identifying the relation
RelationType() RelationType  // Returns the type of the relationship
JSON() ([]byte, error)  // Provides a JSON representation of the relation
```

This abstraction ensures consistency across different relation types, facilitating serialization and integration with other components.

### RelationType

The **`RelationType`** is defined as a string alias and is used to distinguish different types of asset relations. The file defines several constants:

| **Constant**             | **Description**                    |
|--------------------------|------------------------------------|
| `BasicDNSRelation`       | Basic DNS record relation          | 
| `PortRelation`           | Relation concerning service ports  | 
| `PrefDNSRelation`        | Preferred DNS relation             |
| `SimpleRelation`         | Standard/simple relation           | 
| `SRVDNSRelation`         | Server DNS relation                |

Additionally, `RelationList` aggregates these types into a slice for easy iteration and reference.

---

## **//** Asset Relationship Mappings

The file declares several mapping variables that define **which asset types can be related to others**. Each entry is a nested Go map structured as follows:

- **Key** – String label representing the nature of the relationship (e.g., `"id"`, `"user"`, `"registrant_contact"`).
- **Value** – Nested map where:
    + **Key**: `RelationType` constant (e.g., `SimpleRelation`, `PortRelation`).
    + **Value**: Slice of asset types (e.g., `Identifier`, `Person`, `FQDN`) allowed as the target of that relationship.

### Example: Account Relationships

| **Label**        | **Relation Type** | **Allowed Target Asset Types**        |
|------------------|-------------------|---------------------------------------|
| id               | SimpleRelation    | Identifier                            |
| user             | SimpleRelation    | Person, Organization                  |
| funds_transfer   | SimpleRelation    | FundsTransfer                         |

Similar mappings exist across asset types. These relations ensure that only appropriate asset types are connected, maintaining data consistency across the asset taxonomy.

---

## **//** Utility Functions

### `GetAssetOutgoingRelations`

**Purpose:**  
Retrieves the list of **relation labels** allowed when the subject is of a specified asset type.

**Signature:**  
```go
func GetAssetOutgoingRelations(subject AssetType) []string
```
---

### `GetTransformAssetTypes`

**Purpose:**  
Returns the allowable destination asset types for a given subject asset type, based on a specified relation label and relation type.

**Signature:**  
```go
func GetTransformAssetTypes(subject AssetType, label string, rtype RelationType) []AssetType
```

---

### `ValidRelationship`

**Purpose:**  
Determines if a relationship from a source asset type to a destination asset type is valid within the defined taxonomy.

**Signature:**  
```go
func ValidRelationship(src AssetType, label string, rtype RelationType, destination AssetType) bool
```

---

## **//** Usage

The following example demonstrates how to:

- Retrieve outgoing relation labels for a specific asset type.

- Determine valid target asset types for a relation.

- Validate whether a given relationship is allowed.

```go
package main

import (
    "fmt"
    "open_asset_model" 
)

func main() {
    // Retrieve allowed relation labels for an FQDN asset
    outgoingRelations := open_asset_model.GetAssetOutgoingRelations(open_asset_model.FQDN)
    fmt.Printf("Allowed relation labels for FQDN: %v\n", outgoingRelations)

    // Determine valid target asset types for an FQDN's "dns_record" relation
    allowedTypes := open_asset_model.GetTransformAssetTypes(
        open_asset_model.FQDN, "dns_record", open_asset_model.BasicDNSRelation,
    )
    fmt.Printf("Allowed asset types for FQDN 'dns_record' relation: %v\n", allowedTypes)

    // Validate whether a relationship from an FQDN to an IP Address is allowed
    isValid := open_asset_model.ValidRelationship(
        open_asset_model.FQDN, "dns_record", open_asset_model.BasicDNSRelation, open_asset_model.IPAddress,
    )
    if isValid {
        fmt.Println("The relationship is valid! ✅")
    } else {
        fmt.Println("The relationship is invalid! ❌")
    }
}
```

## **//** Summary

The `relation.go` file plays a critical role in the **Open Asset Model**, ensuring a structured approach to defining and validating relationships between different assets. 

Key takeaways include:

- **Well-structured Relation interface** for consistency across asset relations.
- A comprehensive set of **RelationType constants** to define asset relationships.
- Detailed **relationship mappings** fthat maintain data integrity.
- **Robust utility functions** for  querying, validating, and transforming relationships.

This model facilitates **consistent asset interconnections** and is essential for **comprehensive asset intelligence**, **network mapping**, and **security investigations**.

---
