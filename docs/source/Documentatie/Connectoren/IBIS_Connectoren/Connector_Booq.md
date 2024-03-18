# Booq

The Booq connector module enables user maintenance
(create/update/delete) in Booq.

## Parameters

|       Parameter       | Required |                                                 Description                                                 |
|:----------------------|:--------:|:------------------------------------------------------------------------------------------------------------|
| API URL               |    X     | The full URL of the Booq instance to connect to. For example:   https://customer.sandbox.booqcloud.com      |
| OAuth - Token URL     |    X     | The full URL of the Booq token endpoint. For example:   https://partners.sandbox.booqcloud.com/oauth2/token |
| OAuth - Client ID     |    X     | The OAuth client ID to use for connecting to Booq                                                           |
| OAuth - Client Secret |    X     | The OAuth client secret that belongs to above client ID                                                     |
| User location         |    X     | The resource URI for users. For example:   partner/integration/v1/users                                     |
| Store location        |    X     | The resource URI for stores. For example:   partner/onboarding/v1/stores                                    |
| RowFilter fields      |          |                                                                                                             |
| RowFilter types       |          |                                                                                                             |
| RowFilter values      |          |                                                                                                             |
