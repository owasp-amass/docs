# :simple-owasp: Contact Assets 

**Contact Assets**—encompassing **email**, **location**, and **phone** properties—are essential components for comprehensive Attack Surface Intelligence. These assets represent both physical and digital points of contact associated with entities such as WHOIS records, organizations, certificates, and registrars. By organizing contact details with specific properties and relationships, the model enables visibility into connections across various resources, supporting a holistic understanding of an organization's asset landscape.

This structure aids in mapping relationships, tracing asset discovery paths, and providing context for each contact point, enhancing the ability to identify potential exposures and improve security measures.

---

!!! Info annotate "OAM Taxonomy"
    The diagrams and data tables below outline the properties and incoming relationships for each `Contact Asset` type: `Email`, `Location`, and `Phone`. # (1)!

1. :material-check-decagram: Required fields are denoted in the tables below.

---

## :material-email: Email Address


``` mermaid
graph TD
Contact[("Contact Assets")]
Email("Email
Properties")

Email ==> Contact

Person[("Person")]
Organization[("Organization")]
TLSCertificate[("Fingerprint")]
Registration[("Registration")]

registrationEmail@{ shape: braces, label: "admin_email
tech_email
billing_email
registrant_email
abuse_email"}

personEmail@{ shape: braces, label: "email"}
tlsEmail@{ shape: braces, label: "subject_email_address"}

registrationEmail --> Email
Registration --o registrationEmail

personEmail --> Email
Person --o personEmail
Organization --o personEmail 

tlsEmail --> Email
TLSCertificate --o tlsEmail
```

---

??? Warning "Email Requirement"
    A full email `address`, formatted as a `string`, is required to map the related relationships.

---

### :material-email: Email Properties

| Property | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `address` | string | :material-check-decagram: | The full email address |
| `local` | string | - | The local part of the email address |
| `domain` | string | - | The part of the address after the @ symbol |


#### Incoming Relationships

| Relationship | Type |
| ------------ | ---- |
| `admin_email` | [`Whois`](#whois) |
| `tech_email` | [`Whois`](#whois) |
| `billing_email` | [`Whois`](#whois) |
| `registrant_email` | [`Whois`](#whois) |
| `email` | [`Person`](#person) |
| `email` | [`Organization`](#organization) |
| `abuse_email` | [`Registrar`](#registrar) |
| `subject_email_address` | [`TLSCertificate`](#tls-certificate) |

---

## :material-map-marker: Location

| Property | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `formatted_address` | string | - | The formatted address |
| `building_number` | string | - | the number of the building at the location |
| `street_name` | string | - | the name of the street at the location |
| `unit` | string | - | the unit number at the location |
| `building` | string | - | the name of the building at the location |
| `town` | string | - | the name town or city at the location |
| `locality` | string | - | the locality at the location |
| `region` | string | - | the name of the region or state at the location |
| `country_code` | string | - | the ISO 3166-1 alpha-2 country code |
| `postal_code` | string | - | the postal code at the location |


#### Incoming Relationships

| Relationship | Type |
| ------------ | ---- |
| `admin_location` | [`Whois`](#whois) |
| `tech_location` | [`Whois`](#whois) |
| `billing_location` | [`Whois`](#whois) |
| `registrant_location` | [`Whois`](#whois) |
| `location` | [`Person`](#person) |
| `location` | [`Organization`](#organization) |
| `subject_state_or_province` | [`TLSCertificate`](#tls-certificate) |
| `subject_locality` | [`TLSCertificate`](#tls-certificate) |

---

## :material-phone: Phone

| Property | Type | Required | Description |
| -------- | ---- | :--------: | ----------- |
| `type` | string | - | The type of phone number |
| `raw` | string | :material-check-decagram: | The raw phone number |
| `e164` | string | - | The E.164 formatted phone number |
| `country_abbrev` | string | - | The ISO 3166-1 alpha-2 country code |
| `country_code` | string | - | The ISO 3166-1 numeric country code |
| `subscriber_number` | string | - | The subscriber number |
| `ext` | string | - | The extension of the phone number |


#### Incoming Relationships

| Relationship | Type |
| ------------ | ---- |
| `admin_phone` | [`Whois`](#whois) |
| `tech_phone` | [`Whois`](#whois) |
| `billing_phone` | [`Whois`](#whois) |
| `registrant_phone` | [`Whois`](#whois) |
| `phone_number` | [`Person`](#person) |
| `phone_number` | [`Organization`](#organization) |
| `abuse_phone` | [`Registrar`](#registrar) |
