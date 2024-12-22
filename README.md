# UUID Generator Action

This GitHub Action generates a [Universally Unique Identifier](https://datatracker.ietf.org/doc/html/rfc9562) (UUID).

## Usage

```yaml
- name: Generate UUID
  uses: celsiusnarhwal/uuid-action@v1
```

### Inputs

Both inputs are optional. Providing only one or neither will always result in a random UUID.

| **Name**    | **Description**                                                                                                                                                                                                                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `namespace` | A namespace identifier. This can be an arbitrary UUID or one of `dns`, `oid`, `url`, or `x500` to use the corresponding [RFC 9652](https://datatracker.ietf.org/doc/html/rfc9562#section-6.6) namespace identifier. Any given combination of this and `name` will always produce the same UUID. Defaults to a random UUID. |
| `name`      | An arbitrary string to be used in conjunction with `namespace`. Any given combination of this and `namespace` will always produce the same UUID. Defaults to a random UUID.                                                                                                                                                |

### Outputs

| **Name**    | **Description**                                                              |
|-------------|------------------------------------------------------------------------------|
| `uuid`      | The generated UUID.                                                          | |
| `hex`       | The UUID as a 32-character lowercase hexadecimal string.                     |
| `int`       | The UUID as a 128-bit integer.                                               |
| `urn`       | The UUID as an [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122) URN. |
| `namespace` | The namespace identifier used to generated the UUID.                         |
| `name`      | The name used to generate the UUID.                                          |
| `json`      | All other outputs as a single JSON object.                                   |

