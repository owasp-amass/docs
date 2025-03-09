# :simple-owasp: `Relation`

The [`relation.go`](https://github.com/owasp-amass/open-asset-model/blob/master/relation.go) file manages and validates relationships between different asset types in the **Open Asset Model**. This document explains its purpose, core components, and role in defining the structure of asset properties.



## Table of Contents 

- [Overview](#overview)
- [Relation Interface and Types](#relation-interface-and-types)
- [Asset Relationship Mappings](#asset-relationship-mappings)
- [Utility Functions](#utility-functions)
  - [GetAssetOutgoingRelations](#getassetoutgoingrelations)
  - [GetTransformAssetTypes](#gettransformassettypes)
  - [assetTypeRelations](#assettyperelations)
  - [ValidRelationship](#validrelationship)
- [Usage Example](#usage-example)
- [Summary](#summary)

---

## **//** Overview

The **Open Asset Model** is designed to manage complex relationships between various types of assets (such as accounts, domain records, IP addresses, organizations, etc.) in a flexible and extensible way. The `relation.go` file focuses on defining:

- **Relation Types** – A set of constants representing different types of relationships.
- **Relationship Mappings** – Predefined mappings which specify which asset types can be related to one another.
- **Validation & Transformation Functions** – Helper functions to query, transform, and validate relationships according to the defined taxonomy.

This model is useful in contexts where assets need to be interconnected in a structured taxonomy, ensuring data integrity and consistency throughout asset intelligence gathering.

---

## **//** Relation Interface and Types

### Relation Interface

The file defines a central **Relation** interface that any relation entity must implement. This interface requires the following methods:

- **`Label() string`**  
  Returns a label that identifies the relation.
  
- **`RelationType() RelationType`**  
  Returns the type of the relationship.
  
- **`JSON() ([]byte, error)`**  
  Provides a JSON representation of the relation.

This abstraction allows different relation types to share a consistent interface, facilitating serialization and integration with other components.

### RelationType

The `RelationType` is defined as a string alias and is used to distinguish among various types of asset relations. The code defines several constants for different relation types:

| **Constant**           | **Description**                                               |
|------------------------|---------------------------------------------------------------|
| `BasicDNSRelation`     | Basic DNS record relation                                     | 
| `PortRelation`         | Relation concerning service ports                             | 
| `PrefDNSRelation`      | Preferred DNS relation                                        |
| `SimpleRelation`       | Standard/simple relation                                      | 
| `SRVDNSRelation`       | Server DNS relation                                           |

Additionally, `RelationList` aggregates these types into a slice for easy iteration and reference.

---

## **//** Asset Relationship Mappings

The file declares several mapping variables that define **which asset types can be related to others**. Each mapping is a nested Go map structure organized as follows:

- **Key**: A string label representing the nature or role of the relationship (e.g., `"id"`, `"user"`, `"registrant_contact"`).
- **Value**: A nested map where:
    + **Key**: A `RelationType` constant (e.g., `SimpleRelation`, `PortRelation`).
    + **Value**: A slice of asset types (e.g., `Identifier`, `Person`, `FQDN`) that are allowed as the target of that relationship.

### Example: Account Relationships

For an [**Account**]() asset type (defined via the `accountRels` variable), the relationships are:

| **Label**        | **Relation Type** | **Allowed Target Asset Types**        |
|------------------|-------------------|---------------------------------------|
| id               | SimpleRelation    | Identifier                            |
| user             | SimpleRelation    | Person, Organization                  |
| funds_transfer   | SimpleRelation    | FundsTransfer                         |

Similar mappings exist across asset types. These relations ensure that only appropriate asset types are connected, maintaining data consistency across the asset taxonomy.

---

## **//** Utility Functions

The file implements several helper functions that provide key functionality in managing asset relations.

### GetAssetOutgoingRelations

**Purpose:**  
Retrieves the list of **relation labels** (as strings) allowed to be used when the subject is of a specified asset type.

**Signature:**  
```go
func GetAssetOutgoingRelations(subject AssetType) []string
```

**How It Works:**

- Retrieves the mapping for the given asset type using `assetTypeRelations(subject)`.
- Iterates over the mapping keys (labels) and returns them as a slice of strings.
- Returns `nil` if an invalid asset type is provided.

---

### GetTransformAssetTypes

**Purpose:**  
Returns the allowable destination asset types for a given subject asset type, based on a specified relation label and relation type.

**Signature:**  
```go
func GetTransformAssetTypes(subject AssetType, label string, rtype RelationType) []AssetType
```

**How It Works:**

- Retrieves the relations for the provided asset type.
- Converts the provided label to lowercase to ensure consistent mapping.
- Iterates through the mapping for the label, comparing the relation type (`rtype`).
- Collects and returns unique allowed asset types.
- Returns `nil` if the asset type is invalid or if no matching relationship is found.

---

### assetTypeRelations

**Purpose:**  
A helper function that returns the relationship mappings for a specific asset type.

**Signature:**  
```go
func assetTypeRelations(atype AssetType) map[string]map[RelationType][]AssetType
```

**How It Works:**

- Uses a switch-case statement to match the provided asset type.
- Returns the corresponding relationship mapping variable (e.g., `accountRels`, `fqdnRels`).
- Returns `nil` if the asset type is not recognized.

---

### ValidRelationship

**Purpose:**  
Determines if a relationship from a source asset type to a destination asset type is valid within the defined taxonomy.

**Signature:**  
```go
func ValidRelationship(src AssetType, label string, rtype RelationType, destination AssetType) bool
```

**How It Works:**

- Retrieves the list of allowed transformation asset types for the given source asset by invoking `GetTransformAssetTypes`.
- Iterates over the allowed asset types to check if the specified destination asset type exists.
- Returns `true` if a valid match is found; otherwise, returns `false`.

**Example Code Block:**
```go
if ValidRelationship(Account, "id", SimpleRelation, Identifier) {
    fmt.Println("Valid relationship!")
} else {
    fmt.Println("Invalid relationship!")
}
```

---

## **//**  Usage Example

Below is an example demonstrating the application of these functions:

```go
package main

import (
    "fmt"
    "open_asset_model" // Ensure the package path is correct
)

func main() {
    // Determine allowed outgoing relation labels for an Account asset
    outgoingRelations := open_asset_model.GetAssetOutgoingRelations(open_asset_model.Account)
    fmt.Printf("Allowed relation labels for Account: %v\n", outgoingRelations)

    // Determine allowed target asset types when linking an Account's "user" relationship
    allowedTypes := open_asset_model.GetTransformAssetTypes(open_asset_model.Account, "user", open_asset_model.SimpleRelation)
    fmt.Printf("Allowed asset types for Account 'user' relation: %v\n", allowedTypes)

    // Validate if a relationship is allowed from Account (with label "id") to Identifier
    isValid := open_asset_model.ValidRelationship(open_asset_model.Account, "id", open_asset_model.SimpleRelation, open_asset_model.Identifier)
    if isValid {
        fmt.Println("The relationship is valid! ✅")
    } else {
        fmt.Println("The relationship is invalid! ❌")
    }
}
```

This example shows:

1. **Retrieving relation labels** allowed for a given asset type.
2. **Transforming** the relation to get allowed target asset types.
3. **Validating** the relationship between two asset types.

---

## **//** Summary

The `relation.go` file is a key component of the **Open Asset Model**. It establishes a rigorous framework for defining, querying, and validating relationships between assets by leveraging:

- A well-structured **Relation interface**,
- A comprehensive set of **RelationType constants**
- Detailed **relationship mappings** for each asset type, and
- Robust **utility functions** for transformation and validation,

This model facilitates consistent asset interconnections which are critical to comprehensive visibility, network mapping, and data governance.
