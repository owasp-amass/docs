# :simple-owasp: `Asset`

The [`asset.go`](https://github.com/owasp-amass/open-asset-model/blob/master/asset.go) file defines the **`Asset` interface** and the **`AssetType`** within the **Open Asset Model**. The `Asset` interface acts as a blueprint or a unified contract that every type of asset within the Open Asset Model must adhere. It provides a standardized way to represent, interact, manage, and process various digital and physical assets. This file is fundamental to the model as it **establishes the core structure** for all supported asset types.

- **Filepath:** `open-asset-model/asset.go`
- **Language**: This file is written in **Go** 

## Core Interface

The `Asset` interface defines the common methods that all asset types within the **Open Asset Model** must implement. It is defined as follows:

``` go

type Asset interface {
    Key() string
	  AssetType() AssetType
	  JSON() ([]byte, error)
}

```

This interface specifies three essential methods that every asset must implement:

- `Key() string`: This method is responsible for returning a **unique identifier** for a specific asset instance, allowing for consistent identification and tracking of individual assets.

- `AssetType() AssetType`: This method returns the **type of the asset** as a as a string of the `AssetType`. This allows for categorization and specific handling of different asset types within the mod

- `JSON() ([]byte, error)`: This method is responsible for **serializing the asset's data into a JSON format**. It returns a byte slice representing the JSON encoding of the asset and an error if the serialization fails. 

---

## Defining Asset Categories

The `AssetType` is defined as a straightforward string type. Its purpose is to act as a textual identifier for the various categories of assets we might encounter within an organization's external attack surface. By directly representing each asset type with a string value, we achieve clarity and make comparisons between different categories simple.

To ensure a well-defined and consistent set of asset types, the `asset.go` file includes a comprehensive list of constants of the `AssetType`. Here are the currently supported asset types:

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

As you can see, each constant, such as `FQDN`, `IPAddress`, and `Account`, is assigned a unique string value representing a distinct type of asset. This approach not only makes the model easier to understand but also simplifies the process of extending it with new asset categories. The system can then easily validate and process these diverse asset categories without ambiguity.

## Registry of Supported Asset Types

Complementing the `AssetType` constants, the `asset.go` file also declares a variable `AssetList` as a slice ([]AssetType), a dynamically sized array that holds elements of the `AssetType`. Crucially, `AssetList` is initialized with all of the defined `AssetType` constants that we just saw, providing a comprehensive list of all asset types handled by the model.

Here's the code defining `AssetList`:

``` go
var AssetList = []AssetType{
	Account, AutnumRecord, AutonomousSystem, ContactRecord, DomainRecord, File, FQDN, FundsTransfer,
	Identifier, IPAddress, IPNetRecord, Location, Netblock, Organization, Person, Phone, Product,
	ProductRelease, Service, TLSCertificate, URL,
}
```

The `AssetList` serves several important purposes:

- It acts as a **centralized registry** of all the asset types that the Open Asset Model currently supports.

- It provides a convenient way to **iterate over all the supported asset types** in functions that need to process or display them.

- It plays a key role in **ensuring type safety** by allowing us to easily validate whether a given string corresponds to a valid AssetType within the model.

## `AssetType` vs `AssetList`

- `AssetType` is the fundamental definition, like saying "color". It's the string type used to categorize assets and the basis for creating the specific asset type constants.

- `AssetList` is a concrete collection, similar to a list containing "red," "blue," and "green". It's a specific instance that holds all the currently defined `AssetType` constant values, making them readily accessible.


## Summary 

The `asset.go` file is truly the cornerstone of the **Open Asset Model**. By defining a structured `Asset` interface, enumerating asset categories through `AssetType` constants, and providing a central `AssetList` for validation and iteration, this file ensures standardized asset representation across various security and reconnaissance applications. This well-defined structure allows for the consistent management and processing of a wide range of assets, ultimately enhancing our attack surface intelligence.

## Summary

This `asset.go` file is crucial for defining the fundamental structure of assets within the **OWASP Amass Open Asset Model**, ensuring that all asset implementations adhere to a common interface and are properly categorized by their type. The defined `AssetType` constants provide a clear and extensible enumeration of the asset categories the model currently supports.

---
