# :simple-owasp: GeoLocation

The **GeoLocation** asset type in the [OWASP](https://owasp.org)
[Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM)
represents a geographic position: a point on the Earth given by its latitude
and longitude in decimal degrees (WGS 84), as observed, with or without a
street address.

- **Definition:** A `GeoLocation` holds a latitude and longitude, with an
  optional altitude and an optional uncertainty radius. A photo's GPS, an IP
  geolocation record, a map feature and a registry's coordinates are each a
  `GeoLocation`; a street address geocoded to a point links to one.

- **Purpose:** Positions tie digital assets to the physical world: where a
  photo in a published document was taken, where an IP address is placed,
  where an office stands. Modeling them as assets lets the same point, seen by
  different sources, become one node that can be pivoted on.

- **Design Choice:** Its identity is the position rounded to six decimal
  places (about 11 cm), so observations of the same point converge on one
  asset. Nearby points are not merged: clustering them is a judgment made when
  the data is read. `altitude` and `uncertainty` describe the observation and
  are not part of the identity. `uncertainty` matters as much as the position
  itself, since a photo's GPS is good to meters and an IP geolocation often
  only to a city. A `GeoLocation` is kept separate from
  [`StreetAddress`](./street_address.md), which holds a street address.

## :material-crosshairs-gps: GeoLocation Attributes

| Attributes       | Type      | Required   | Description  |
| :--------------: | :-------: | :--------: | :----------- |
| `latitude` | number | :material-check-decagram: | Latitude in decimal degrees (WGS 84), from -90 to 90 |
| `longitude` | number | :material-check-decagram: | Longitude in decimal degrees (WGS 84), from -180 to 180 |
| `altitude` | number | :material-checkbox-blank-circle-outline: | Meters above the WGS 84 ellipsoid, when known |
| `uncertainty` | number | :material-checkbox-blank-circle-outline: | The radius in meters within which the position lies, when known (RFC 5870's `u` parameter) |

The asset's key is `"<latitude>,<longitude>"`, each rounded to six decimal
places (e.g., `42.468644,-75.064000`).

## :material-crosshairs-gps: GeoLocation Properties

| Property Type       | Property Name       | Description   |
| :-----------------: | :-----------------: | :------------ |
| [`SimpleProperty`](../properties/simple_property.md) | `last_monitored` | Tracks when a data source was last queried regarding this GeoLocation |
| [`SourceProperty`](../properties/source_property.md) | Source Plugin Name | Indicates that the specified data source discovered this GeoLocation |

## :material-crosshairs-gps: GeoLocation Outgoing Relations

A `GeoLocation` is a position that other assets point to; it has no outgoing
relations. It is reached through:

| Source Asset     | Relation Label     | Description   |
| :--------------: | :----------------: | :------------ |
| [`IPAddress`](./ip_address.md) | `geolocation` | Where a geolocation source places the address |
| [`StreetAddress`](./street_address.md) | `geolocation` | The position of a street address |
| [`File`](./file.md) | `contains` | A position the file records, such as the GPS position in an embedded photo's EXIF |

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
