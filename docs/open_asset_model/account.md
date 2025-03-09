# Open Asset Model Documentation - Account Package

The [`account.go`](https://github.com/owasp-amass/open-asset-model/blob/master/account/account.go) file defines structures and interfaces for representing account-related assets and their identity associations in the **Open Asset Model**. This document explains its purpose, core components, and role in structuring account-based asset representation within the framework.  

## Table of Contents

- [Overview](#overview)
-  [Account Structure](#account-structure)
- [Attributes](#attributes)
- [Implemented Interfaces and Methods](#implemented-interfaces-and-methods)
- [Key()](#key)
- [AssetType()](#assettype)
- [JSON()](#json)
- [Usage & Integration](#usage--integration)
- [Relationship with the Open Asset Model](#relationship-with-the-open-asset-model)

---

## **//** Overview

The **Account Package** defines an **Account** asset that is managed by an organization. This asset can represent a bank account, an online payment account, or any similar financial or user-managed account. The account is designed to support multiple relationships, including associations with **users** (individuals or organizations) and **financial transactions** (like funds transfers). Additionally, it holds fields for identifiers such as **IBAN** and **SWIFT codes** for integrations with international banking systems. 

---

## **//** Account Structure

The `Account` struct represents an account with essential fields for identification and status. It is designed with JSON tags for easy serialization and integration with JSON-based APIs or data storage.

### Attributes

Below is a table detailing each field in the `Account` struct:

| **Field Name** | **Type**  | **JSON Tag**           | **Description**                                                                                                                                                          |
|----------------|-----------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ID**         | string    | "unique_id"            | The unique identifier for the account. This field is used as the asset key.                                                                                             |
| **Type**       | string    | "account_type"         | Represents the type of account (e.g., savings, checking, corporate account).                                                                                           |
| **Username**   | string    | "username,omitempty"   | Optional field for the username associated with the account.                                                                                                           |
| **Number**     | string    | "account_number,omitempty" | Optional field for the account number. This could serve as a secondary identifier in some systems.                                                                  |
| **Balance**    | float64   | "balance,omitempty"    | Represents the current balance of the account.                                                                                                                         |
| **Active**     | bool      | "active,omitempty"     | Indicates whether the account is currently active.                                                                                                                     |

!!! info " omitempty "
    The `omitempty` option in the JSON tags ensures that if a field is empty or its default value, it will be omitted from JSON serialization. This helps keep the data streamlined.

---

## **//** Implemented Interfaces and Methods

The **Account** struct implements the **Asset** interface defined in the **Open Asset Model**. This interface requires a few key methods for every asset:

### Key()

- **Purpose:**  
  Returns a unique key (identifier) for the asset. This key is fundamental for distinguishing between different assets.

- **Implementation:**

  ```go
  // Key implements the Asset interface.
  func (a Account) Key() string { 
      return a.ID 
  }
  ```
  - **Input:** None  
  - **Output:** A string representing the unique account ID  
  - **Usage:** The return value is used to uniquely identify the account within the system.

---

### AssetType()

- **Purpose:**  
  Returns the specific type of the asset in the context of the **Open Asset Model**. This helps in categorizing assets.

- **Implementation:**

  ```go
  // AssetType implements the Asset interface.
  func (a Account) AssetType() model.AssetType { 
      return model.Account 
  }
  ```
  - **Input:** None  
  - **Output:** `model.AssetType` (in this case returning the constant value `model.Account`)  
  - **Usage:** This method is used to identify the asset's type when processing or categorizing assets within the Open Asset Model framework.

---

### JSON()

- **Purpose:**  
  Serializes the `Account` struct into JSON format. This is essential for data exchange and persistence.

- **Implementation:**

  ```go
  // JSON implements the Asset interface.
  func (a Account) JSON() ([]byte, error) { 
      return json.Marshal(a) 
  }
  ```
  - **Input:** None  
  - **Output:** A byte slice containing the JSON representation of the account, or an error if the marshalling fails.  
  - **Usage:** Used for converting the asset into a JSON format for network transmission or storage.

---

## Usage & Integration

Here’s how you might use the **Account Package** in your Go projects:

1. **Import the Package:**

   ```go
   import "path/to/account"
   import "github.com/owasp-amass/open-asset-model"
   ```

2. **Creating an Account:**

   ```go
   myAccount := account.Account{
       ID:       "acc-12345",
       Type:     "savings",
       Username: "jdoe",
       Number:   "00123456789",
       Balance:  1000.50,
       Active:   true,
   }
   ```

3. **Accessing the Asset Interface Methods:**
   
   - **Retrieve the Account Key:**

     ```go
     key := myAccount.Key()
     // key should be "acc-12345"
     ```

   - **Get the Asset Type:**

     ```go
     assetType := myAccount.AssetType()
     // returns model.Account
     ```

   - **Serialize the Account to JSON:**

     ```go
     jsonData, err := myAccount.JSON()
     if err != nil {
         // handle error
     }
     fmt.Println(string(jsonData))
     ```

These simple steps show how the **Account** asset can be instantiated, manipulated, and serialized, making it a flexible component for financial and user account-related applications.

---

## Relationship with the Open Asset Model

The Open Asset Model aims to provide a standardized and extensible approach to handling diverse digital assets. The **Account Package** plays a key role in this by:

- Defining a clear and concise **Account** structure that encapsulates common attributes.
- Ensuring **consistency** across different types of assets through the **Asset interface**, which standardizes methods like `Key()`, `AssetType()`, and `JSON()`.
- Facilitating integration with various systems (e.g., banking, financial, and user management systems) by providing robust serialization to JSON. ☁️🔗

By adhering to these standards, the Account model supports relationships with other assets, such as:
- **User Entities:** Representing persons or organizations linked to an account.
- **Fund Transfers:** Tracking movement of funds between accounts.
- **Banking Identifiers:** For support in systems utilizing **IBAN** and **SWIFT codes**.

This structured approach simplifies integration and ensures a modular design, making it easier to extend and maintain in larger systems.

---

## License & Credits

The source code in this package is covered by the **Apache 2.0 License**. See the accompanying `LICENSE` file for detailed licensing information.

- **Copyright:**  
  © Jeff Foley 2017-2025. All rights reserved.

- **License Summary:**  
  The code is open source and can be used under the terms specified in the Apache 2.0 License.

---

## Conclusion

The **Account Package** is a crucial component of the Open Asset Model, providing a well-defined and extensible structure for managing accounts. Its implementation of the **Asset interface** ensures interoperability and ease of integration, while its design facilitates real-world applications such as financial transactions and user account management. With comprehensive JSON support and robust structure, it stands as an exemplary model for asset management in modern software systems. Happy coding! 😎🎉

--- 

For further details or contributions, please refer to the project's repository and documentation.