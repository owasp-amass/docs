``` mermaid
graph TD
Contact[("Contact Assets")]

Email("Full Email
Address")


Email ==> Contact


Person[("Person")]
Organization[("Organization")]
TLSCertificate[("TLS Certificate")]
Registrar[("Registrar")]
Whois[("Whois")]


whoisEmail@{ shape: braces, label: "admin_email
tech_email
billing_email
registrant_email" }


personEmail@{ shape: braces, label: "email"}
registrarEmail@{ shape: braces, label: "abuse_email"}
tlsEmail@{ shape: braces, label: "subject_email_address"}




whoisEmail --> Email
Whois --o whoisEmail

personEmail --> Email
Person --o personEmail
Organization --o personEmail 

registrarEmail --> Email
Registrar --o registrarEmail

tlsEmail --> Email
TLSCertificate --o tlsEmail






```
