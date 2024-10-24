``` mermaid
flowchart TD
Contact[("fa:fa-comment Contact Assets")]

Email("fa:fa-envelope Email")
Location("fa:fa-location-dot Location")
Phone("fa:fa-phone Phone")

Email ==> Contact
Location ==> Contact
Phone ==> Contact

Person(["fa:fa-user Person"])
Organization(["fa:fa-building Organization"])
TLSCertificate(["fa:fa-lock TLS Certificate"])
Registrar(["fa:fa-folder Registrar"])
Whois[("fa:fa-globe Whois")]


whoisEmail@{shape: subproc, label: "admin_email
tech_email
billing_email
registrant_email" }





whoisEmail --> Email
Whois --> whoisEmail
```
