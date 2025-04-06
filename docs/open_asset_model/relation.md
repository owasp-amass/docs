# :simple-owasp: `Relation`

The [`relation.go`](https://github.com/owasp-amass/open-asset-model/blob/master/relation.go) implementation is designed to manage complex relationships between various assets in a flexible and extensible way. By specifying the types of relationships that can exist between assets and the **allowed target asset types** for a given source asset type and relationship within the **Open Asset Model**, this file serves as a crucial component for structuring interconnected assets, ensuring data integrity, and implementing consistency in asset intelligence gathering.

---

## Interface

Similar to the `Asset` interface, `relation.go` defines a `Relation` **interface** that represents the contract all relationship types within the Open Asset Model must implement and ensures a consistent structure for representing connections between assets.

```go
type Relation interface {
    Label() string
	RelationType() RelationType
	JSON() ([]byte, error)
}
```

The `Relation` interface consists of the following methods:

- `Label() string`: This method is responsible for returning a **string that describes the specific nature of the relationship** between two assets. For example, a relationship between an `FQDN` and an `IPAddress` with a `"dns_record"` label.

- `RelationType() RelationType`: This method returns the general type or category of the relationship as a `RelationType`. The `RelationType` itself is defined as a string type.

- `JSON() ([]byte, error)`: Similar to the Asset interface in `asset.go`, this method handles the serialization of the relation's data into JSON format. It returns a byte slice representing the JSON encoding and an error if the serialization fails

The `relation.go` file defines `RelationType` as a string type. It also declares several constants of `RelationType`, which represent the predefined categories of relationships supported by the model:

```go

const (
    BasicDNSRelation RelationType = "BasicDNSRelation"
	PortRelation     RelationType = "PortRelation"
	PrefDNSRelation  RelationType = "PrefDNSRelation"
	SimpleRelation   RelationType = "SimpleRelation"
	SRVDNSRelation   RelationType = "SRVDNSRelation"
)
```

These constants provide a standardized enumeration for classifying relationships between assets.

---

## Variable

Complementing the `RelationType` constants is the `RelationList` variable:

```go

var RelationList = []RelationType{
	BasicDNSRelation,
	PortRelation,
	PrefDNSRelation,
	SimpleRelation,
	SRVDNSRelation,
}
```

This variable is a slice containing all the defined `RelationType` constants. It serves as a centralized registry of all supported relationship types within the Open Asset Model.

---

## Asset Type Relationship Maps

A significant aspect of `relation.go` is the definition of **maps that specify the permitted outgoing relationships for each** `AssetType` defined in `asset.go`. These maps, such as `accountRels`, `fqdnRels`, and others, are structured to define:

- The label of the relationship (e.g., `"id"`, `"user"`, `"dns_record"`).

- The `RelationType` of the relationship (e.g., `SimpleRelation`, `BasicDNSRelation`, `PortRelation`).

- A slice of `AssetType`(s) that can be the target of this relationship.

For instance, the `fqdnRels` map defines the allowed outgoing relationships for the `FQDN` asset type and includes relationships like `"port"` of type `PortRelation` targeting `Service` assets, and `"dns_record"` of type `BasicDNSRelation`, `PrefDNSRelation`, and `SRVDNSRelation` targeting `FQDN` or `IPAddress` assets.

These maps are crucial for defining the **taxonomy of relationships** within the Open Asset Model, outlining which asset types can be connected and the nature of those connections.

---

## Helper Functions 

`relation.go` also includes several helper functions that facilitate the management and validation of relationships:

- `GetAssetOutgoingRelations(subject AssetType) []string`: This function takes an `AssetType` as input and returns a slice of strings representing the labels of the relations that can originate from this asset type. It retrieves this information from the asset type relationship maps.

- `GetTransformAssetTypes(subject AssetType, label string, rtype RelationType) []AssetType`: This function, given a subject `AssetType`, a relationship label, and a `RelationType`, returns a slice of `AssetTypes` **that can be the target of such a relationship**. It consults the relevant asset type relationship map to determine the valid target asset types.

- `assetTypeRelations(atype AssetType) map[string]map[RelationType][]AssetType`: This internal function takes an `AssetType` and returns the **corresponding relationship map** defined in the file (e.g., returns `fqdnRels` if the input is `FQDN`).

- `ValidRelationship(src AssetType, label string, rtype RelationType, destination AssetType) bool`: This function checks if a **proposed relationship** from a source `AssetType` to a destination `AssetType` with a given label and `RelationType` is valid according to the defined relationship maps. It utilizes `GetTransformAssetTypes` to determine if the destination `AssetType` is permitted for the given source, label, and relation type.

---

## Summary

The `relation.go` file is fundamental to the Open Asset Model. It defines the `Relation` **interface**, the `RelationType`, and the permissible relationships between different `AssetTypes` through a series of maps and helper functions. By establishing these rules, the Open Asset Model can effectively represent the interconnectedness of assets within an organization's attack surface. This structured approach allows for a more comprehensive and accurate understanding of potential attack vectors.

---
