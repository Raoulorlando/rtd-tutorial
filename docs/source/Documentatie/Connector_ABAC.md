<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / ABAC

# ABAC

The ABAC module supports import- and export of ABAC targets.

Only base properties are supported, criteria need to be managed through
target modules in ABAC.

ABAC will reload the criteria for a target after each successful export.
In order to trigger a successful export, you can for example flow a
ModifieDate value to one of the extension attributes of the target.

## Module parameters

|                       Parameter                       | Required |                                                                      Description                                                                     |
|:-----------------------------------------------------:|:--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|
| Use custom settings instead of the IBIS configuration | X        | Use this to override the IBIS connection settings for ABAC. If disabled, the ABAC connection settings will be determined from the IBIS configuration |
| Dossier type                                          |          | Specify the dossier type of the targets to manage. If left empty, all targets will be imported                                                       |
| API URL                                               |          | The base URL of the ABAC instance (without /API or /OData)                                                                                           |
| Authentication                                        |          | The type of authentication to use for connecting to ABAC                                                                                             |
| Username                                              |          | The username to use for connecting to ABAC                                                                                                           |
| Password                                              |          | The password of above username                                                                                                                       |
| OAuth - Tenant ID                                     |          | The unique identifier of the tenant in which ABAC is hosted                                                                                          |
| OAuth - Application ID                                |          | The unique identifier of the ABAC application                                                                                                        |
| OAuth - Client ID                                     |          | The client ID to use for connecting to ABAC                                                                                                          |

 
