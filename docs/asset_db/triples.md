# Triples Query Language

The **Triples Query Language** allows users of the OWASP Amass framework to request data from the Asset Database using the **OWASP Open Asset Model**. This query language enables traversals across the graph, where each triple describes a directed edge between two nodes.

A **triple** is a traversal path that describes a step in a graph walk, or a "hop" in your graph between two nodes. Each triple consists of a **subject**, a **predicate**, and an **object**. The subject is the node being queried, the predicate describes the relationship, and the object is the target node. Results from the previous triple can serve as subjects for subsequent triples, enabling complex queries across the graph.

## Syntax Overview

A single **triple** follows the format for outgoing relations from the subject:

```
<subject> - <predicate> -> <object>
```

Or, the arrow pointing in the other direction for incoming relations to the subject:

```
<subject> <- <predicate> - <object>
```

- **Subject**: The starting node of the traversal.
- **Predicate**: Describes the relationship.
- **Object**: The ending node of the traversal.

### Components of a Triple

Each node and predicate in the triple has the following format:

```
<type:label,since:DATE,prop:[type:label,atrribute:value]>

<ipaddress:#/72.*/#,prop:[sourceproperty:DNS-IP,since:2025-07-01,confidence:80]>
```

Here is an example of 

- **type**: The type of the node (e.g., `fqdn` or `ipaddress`).
- **label**: The specific value associated with the node (e.g. `dns_record`).
- **since**: An optional filter specifying a date to limit results after a certain point.
- **prop**: Optional properties for the node, such as additional attributes or metadata.
- **attributes**: Optional fields from the data type used for filtering (e.g. `header.rr_type:#/1|28/#`).

### Supported Query Elements

- **Constant Values**: Specific, static values for filtering (e.g., `fqdn:owasp.org`).
- **Wildcard ('*')**: A wildcard character that can match any value (e.g., `ipaddress:*`).
- **Regular Expressions ('#//#')**: A regular expression for more specific filtering (e.g. `#/.*google.*/#`).

## Example Queries

### 1. From Root Domain Name to IP Addresses

This query retrieves all IP addresses associated with the root domain name `owasp.org`, starting from the domain and considering DNS records since July 1st, 2025.

```
<fqdn:owasp.org> - <*:dns_record,since:2025-07-01> -> <ipaddress:*>
```

- **Subject**: `<fqdn:owasp.org>`
- **Predicate**: `<*:dns_record,since:2025-07-01>`
- **Object**: `<ipaddress:*>`

### 2. Root Domain Name to Subdomains

This query retrieves all subdomains of the root domain `owasp.org`, starting from the domain and considering the relationship to nodes since July 1st, 2025.

```
<fqdn:owasp.org> - <*:node,since:2025-07-01> -> <*>
```

- **Subject**: `<fqdn:owasp.org>`
- **Predicate**: `<*:node,since:2025-07-01>`
- **Object**: `<*>`

The object can simply specify the wildcard character, since the 'node' relation outcoming from an FQDN must connect with another FQDN.

### 3. Subdomain to IP Address

This query retrieves IP addresses for all subdomain names (e.g. `subdomain.owasp.org`), acquired from a previous triple, and their DNS records since July 1st, 2025.

```
<fqdn:#/.*owasp.org/#> - <*:dns_record,since:2025-07-01> -> <ipaddress:*>
```

- **Subject**: `<fqdn:#/.*owasp.org/#>`
- **Predicate**: `<*:dns_record,since:2025-07-01>`
- **Object**: `<ipaddress:*>`

## Filtering with Regular Expressions

You can use regular expressions to filter the query results. For example, if you want to query IP addresses associated with domain names that match a specific pattern, you can use:

```
<fqdn:google.com> - <*:dns_record> -> <ipaddress:#/192.168.*/#>
```

- **Subject**: `<fqdn:google.com>`
- **Predicate**: `<*:dns_record>`
- **Object**: `<ipaddress:#/192.168.*/#>`

This query retrieves IP addresses for `google.com` where the IP address matches the `192.168.*` range.

## Traversing Multiple Steps

Triples allow for multiple traversals in a query. You can chain multiple triples to traverse from one node to another through various relationships. For example:

```
amass assoc -t1 '<fqdn:owasp.org> - <*:node> -> <*>' -t2 '<fqdn:*> - <*:dns_record> -> <ipaddress:*>'
```

Here, the first triple retrieves all nodes related to the root domain `owasp.org`, and the second triple retrieves IP addresses associated with those nodes. The entire walk that traverses all triples, and all related properties, is provided in the JSON output.

## Conclusion

The **Triples Query Language** is a powerful way to interact with the OWASP Asset Database and extract relevant data from the Open Asset Model. By using this language, users can perform flexible, precise queries to navigate the complex relationships between assets, making it a valuable tool for asset discovery and attack surface management.

## See Also

* [Asset Database](./index.md)
* [Setting Up PostgreSQL](./postgres.md)
