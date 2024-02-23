<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / ASPOS

# ASPOS

The ASPOS connector module enables group-user maintenance
(create/update/delete) in ASPOS.

## Parameters

|            Parameter            | Required |                                                    Description                                                    |
|:-------------------------------:|:--------:|:-----------------------------------------------------------------------------------------------------------------:|
| API URL                         | X        | The full URL of the ASPOS instance to connect to. For example:                                                    |
| OAuth - Token URL               | X        | The full URL of the ASPOS token endpoint. For example:                                                            |
| OAuth - Client ID               | X        | The OAuth client ID to use for connecting to ASPOS                                                                |
| OAuth - Client Secret           | X        | The OAuth client secret that belongs to above client ID                                                           |
| Append all stores during create | X        | If enabled, all stores available in ASPOS will be added to the UserStores property of the user when it is created |
|          OrderBy fields         |          |                                                                                                                   |
|         RowFilter fields        |          |                                                                                                                   |
|         RowFilter types         |          |                                                                                                                   |
|         RowFilter values        |          |                                                                                                                   |
