# :simple-owasp: `Asset`

The [`asset.go`](https://github.com/owasp-amass/open-asset-model/blob/master/asset.go) implementation defines the **`Asset` interface** and the **`AssetType`** within the **Open Asset Model**. The `Asset` interface acts as a blueprint or a unified contract that every type of asset within the Open Asset Model must adhere. It provides a standardized way to represent, interact, manage, and process various digital and physical assets. This file is fundamental to the model as it **establishes the core structure** for all supported asset types.

---

## Interface

The `asset.go` file defines the `Asset` **interface**, which serves as a unified contract that all asset types within the Open Asset Model must implement. This ensures consistency when interacting with different assets

``` go

type Asset interface {
    Key() string
	  AssetType() AssetType
	  JSON() ([]byte, error)
}

```

The `Asset` interface comprises the following methods:

- `Key() string`: This method is responsible for returning a **unique identifier** for a specific asset instance. This allows for consistent identification and tracking of individual assets.

- `AssetType() AssetType`: This method returns the type of the asset as a value of the `AssetType`. This enables categorization and specific handling of different asset types within the model. `AssetType` is defined as a simple string type.

- `JSON() ([]byte, error)`: This method handles the **serialization of the asset's data into a JSON** format. It returns a byte slice representing the JSON encoding of the asset and an error if the serialization fails. This facilitates easy **data interchange** across APIs and databases.

---

## Enumerations

The `AssetType` is defined as a string alias, ensuring type safety and consistency within the model. The `asset.go` file enumerates a comprehensive list of currently supported asset types as constants of the `AssetType`:

```go
const (
	Account        AssetType = "Account"
	AutnumRecord   AssetType = "AutnumRecord"
	AutonomousSystem AssetType = "AutonomousSystem"
	ContactRecord  AssetType = "ContactRecord"
	DomainRecord   AssetType = "DomainRecord"
	File           AssetType = "File"
	FQDN           AssetType = "FQDN"
	FundsTransfer  AssetType = "FundsTransfer"
	Identifier     AssetType = "Identifier"
	IPAddress      AssetType = "IPAddress"
	IPNetRecord    AssetType = "IPNetRecord"
	Location       AssetType = "Location"
	Netblock       AssetType = "Netblock"
	Organization   AssetType = "Organization"
	Person         AssetType = "Person"
	Phone          AssetType = "Phone"
	Product        AssetType = "Product"
	ProductRelease AssetType = "ProductRelease"
	Service        AssetType = "Service"
	TLSCertificate AssetType = "TLSCertificate"
	URL            AssetType = "URL"
)
```

These constants represent different categories of assets within an organization's attack surface inventory. The string value of each constant directly represents the specific asset type.

---

## Variable

Complementing the `AssetType` constants, the `asset.go` file declares a variable `AssetList`:

``` go
var AssetList = []AssetType{
	Account, AutnumRecord, AutonomousSystem, ContactRecord, DomainRecord, File, FQDN, FundsTransfer,
	Identifier, IPAddress, IPNetRecord, Location, Netblock, Organization, Person, Phone, Product,
	ProductRelease, Service, TLSCertificate, URL,
}
```

This variable is a slice containing all the defined `AssetType` constants. It serves as a centralized registry of all supported asset types. The `AssetList` provides a convenient way to access and iterate over all the predefined asset types handled by the model and can be used for validating if a given string represents a valid `AssetType`.
T

## `AssetType` vs `AssetList`

- `AssetType` is the definition of the type itself, a string used to categorize assets. It also serves as the type for the defined constants.

- `AssetList` is a concrete collection (a slice) containing all the values of the predefined `AssetType` constants. It's an instance that holds all the currently supported asset category identifiers.

The relationship can be analogized to "color" (`AssetType`) and a list containing "red," "blue," and "green" (`AssetList`).

---

## Summary 

The `asset.go` file is fundamental to the Open Asset Model, ensuring standardized asset representation across various security and reconnaissance applications. Key takeaways include:

- It defines a structured `Asset` **interface** for consistent asset management.

- It enumerates **asset types** as constants of `AssetType` to ensure type safety and consistency.

- It **provides JSON serialization support** through the JSON() method in the `Asset` interface for data interchange.

- It includes `AssetList` to facilitate asset type validation and iteration.

By implementing this structured approach, contributors can extend asset handling capabilities, while users can integrate asset intelligence into their security workflows efficiently.
