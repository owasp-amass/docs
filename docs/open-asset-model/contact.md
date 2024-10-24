``` mermaid
flowchart TD
Contact[("Contact Assets")]

Email(Email)
Location(Location)
Phone(Phone)

Email ==> Contact
Location ==> Contact
Phone ==> Contact

Person([Person])
Organization([Organization])
TLSCertificate(["TLS Certificate"])
Registrar([Registrar])
Whois[(Whois)]


 subgraph whoisEmail["fa:fa-globe"]
        direction RL
        adminLocation([admin_email])
        techEmail([tech_email])
        billingEmail([billing_email])
        registrantEmail([registrant_email])
    end

whoisEmail --> Email
Whois --> whoisEmail
```
