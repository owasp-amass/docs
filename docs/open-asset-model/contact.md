``` mermaid
graph TD
Contact[("Contact Assets")]
Email("Full Email
Address")

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
