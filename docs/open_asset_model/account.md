# :simple-owasp: `Account`

The [`account.go`](https://github.com/owasp-amass/open-asset-model/blob/master/account/account.go) file defines the **Account asset** within the **Open Asset Model**. An **Account** represents a financial or entity-managed asset, such as a **bank account, online payment account, or corporate account**. The model allows accounts to establish structured relationships with **entities (individuals or organizations), funds transfers, and financial identifiers** such as **IBAN and SWIFT** codes.  

## Table of Contents

- [Overview](#overview)
- [Account Structure](#account-structure)
- [Attributes](#attributes)
- [Implemented Interfaces and Methods](#implemented-interfaces-and-methods)
- [Key()](#key)
- [AssetType()](#assettype)
- [JSON()](#json)
- [Relationship with the Open Asset Model](#relationship-with-the-open-asset-model)
- [Usage](#usage)

---

## **//** Overview

The **Account asset** is an integral part of the **Open Asset Model**, designed to support:

- **Financial & entity-managed accounts** (e.g., bank, corporate, or payment accounts).

- **Multiple relationships** such as **entity ownership (Person/Organization)** and **fund transfers**.

- **Standardized data structure** for integration with external financial and asset-tracking systems.

The **`Account`** struct is designed with **JSON tags for serialization**, ensuring seamless integration with **APIs and structured storage systems**.

---

## **//** Account Structure

The **`Account` struct** defines key attributes necessary for financial asset representation.

```go
// Account represents an account managed by an organization.
type Account struct {
    ID       string  `json:"unique_id"`         // Unique identifier
    Type     string  `json:"account_type"`      // Type of account (e.g., savings, checking)
    Username string  `json:"username,omitempty"` // Optional username
    Number   string  `json:"account_number,omitempty"` // Account number
    Balance  float64 `json:"balance,omitempty"`  // Account balance
    Active   bool    `json:"active,omitempty"`  // Status of the account
}
```

---

**Attribute Breakdown**

| **Field Name** | **Type**  | **JSON Tag**                 | **Description**                                                          |
|----------------|-----------|------------------------------|--------------------------------------------------------------------------|
| **`ID`**       | `string`  | `"unique_id"`                | **Unique identifier** for the account (used as the **asset key**)        |
| **`Type`**     | `string`  | `"account_type"`             | Represents the **type of account** (e.g., savings, checking)             |
| **`Username`** | `string`  | `"username,omitempty"`       | Optional **username** associated with the account                        |
| **`Number`**   | `string`  | `"account_number,omitempty"` | Optional **account number** used as a secondary identifier               |
| **`Balance`**  | `float64` | `"balance,omitempty"`        | Represents the **current balance** of the account                        |
| **`Active`**   | `bool`    | `"active,omitempty"`         | Indicates whether the **account is active**                              |

---

!!! info " omitempty "
    The `omitempty` option in the JSON tags ensures that if a field is empty or its default value, it will be omitted from JSON serialization. This helps keep the data streamlined.

---

## **//** Implemented Interfaces and Methods

The **Account** struct implements the **Asset interface**, ensuring consistency across the **Open Asset Model**.

### `Key()`

- **Purpose:**  
  Returns a unique key (identifier) for the asset. This key is fundamental for distinguishing between different assets.

- **Implementation:**

  ```go
  // Key implements the Asset interface.
  func (a Account) Key() string { 
      return a.ID 
  }
  ```
  **Usage:** 
  -  Used to **uniquely identify** the account.
  - Serves as the **primary key** for asset indexing and retrieval.

---

### `AssetType()`

- **Purpose:**  
  Returns the specific type of the asset within the **Open Asset Model**.

- **Implementation:**

  ```go
  // AssetType implements the Asset interface.
  func (a Account) AssetType() model.AssetType { 
      return model.Account 
  }
  ```
  **Usage:** 
  - Allows systems to **categorize the asset** as an **`Account`**.  
  - Ensures **type consistency** when processing different asset categories.

---

### JSON()

- **Purpose:**  
  Serializes the **`Account`** struct into **JSON format** for **data exchange and storage**. 

- **Implementation:**

  ```go
  // JSON implements the Asset interface.
  func (a Account) JSON() ([]byte, error) { 
      return json.Marshal(a) 
  }
  ```

  **Usage:** 
  - Converts the asset into **JSON format** for **APIs, databases, and logging**.
  - Enables **data transmission** across services.

---

## **//** Relationship with the Open Asset Model

The **Open Asset Model** provides a standardized approach to handling digital and physical assets. The **`Account`** asset is a critical component and supports:

- **User Entities**: Representing **Persons or Organizations** that own the account.

- **Funds Transfers**: Tracking **financial transactions** between accounts.

- **Banking Identifiers**: Supporting **IBAN and SWIFT codes** for financial integration.

By adhering to these relationships, the **`Account model`** ensures structured data exchange between **security, financial, and asset management systems**.

---

## **//** Usage

The **Open Asset Model** provides structured asset management for accounts. Below is an example demonstrating how to:

- **Retrieve account details**.

- **Serialize an account to JSON**.

```go
package main

import (
    "encoding/json"
    "fmt"
    "github.com/owasp-amass/open-asset-model/account"
)

func main() {
    // Define an example account asset
    acc := account.Account{
        ID:       "acc-12345",
        Type:     "Savings",
        Username: "johndoe",
        Number:   "987654321",
        Balance:  1500.75,
        Active:   true,
    }

    // Serialize the account to JSON
    jsonData, err := acc.JSON()
    if err != nil {
        fmt.Println("Error serializing account to JSON:", err)
        return
    }

    fmt.Printf("Account Type: %s\n", acc.Type)
    fmt.Printf("Serialized JSON: %s\n", string(jsonData))
}
```

---

## **//** Summary

The **`account.go`** file is a fundamental part of the **Open Asset Model**, ensuring structured and standardized management of **financial and user-managed accounts**. 

Key takeaways:

- **Defines an `Account` struct** that represents various financial accounts.

- **Implements the Asset interface** to ensure consistency.

- Supports relationships with **user entities, financial transactions, and banking identifiers**.

- Provides **JSON serialization** for easy data exchange.

By following this structured approach, **contributors** can extend account functionality, while **users** can efficiently manage financial assets in their security and asset intelligence workflows.

---