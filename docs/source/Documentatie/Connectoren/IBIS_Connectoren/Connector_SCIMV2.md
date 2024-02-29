# SCIM 2.0 Connector

The SCIM connector performs user operations against a SCIM version 2
compatible API. At the moment the following schemas are implemented by
this connector:

-   **User**: urn:ietf:params:scim:schemas:core:2.0:User
-   **Enterprise User** :
    urn:ietf:params:scim:schemas:extension:enterprise:2.0:User

## Primary key

The primary key for this module is the **id** property of the resource.
You should not set this attribute in an export flow, but instead let the
connected system handle the generation. On succesfull creation
(provision export) of a resource, IBIS will automatically set the
primary key in the staging area.

The **externalId** property of the resource *can* be used to store an
IBIS identifier.

## Multivalue attributes

Multivalue attributes (addresses, phones, emails, etc.) in the connected
system are supported by this connector.

In order to export to a multivalued attribute, specify a JSON array
notation in the export flow, where the curly braces for specifying a
JSON object ({}) should be escaped with a backslash (\\. The export will
overwrite the complete array in the connected system. Do not replace the
curly braces for values that should be resolved. For example:

\[\\"value":"{\_42\_60\_Persoon\_TelefoonNummerPrive}",type":"mobile","primary":true\\\]

In order to import a value from a multivalued attribute array, use the
*ParseJsonArrayValue* funtion. The line below will select the **value**
property of the first element in the **emails** property array where
**type** matches **work**

{?{emails},parsejsonarrayvalue(type,work,value)}

## Attribute mappings

It yout want te select a property from a specific schema you can prefix
the property, for example: "User:externalId" or "Group:externalId"

## Parameters

|              Parameter              | Required |                                                                                                                                         Description                                                                                                                                        |
|:-----------------------------------|:--------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 URL                 |     X    |                                                                                                                                   The URL of the SCIM API                                                                                                                                  |
|           Schema endpoint           |     X    |                                                                                                                               The name of the schema endpoint                                                                                                                              |
|           Singular schema           |          |                                                                                           If set, the schema endpoint is expected to return a single schemaresult instead of a schema collection                                                                                           |
|          Resource endpoint          |     X    |                                                                                                                              The name of the resource endpoint                                                                                                                             |
|            Resource type            |     X    |                                                                                                 The type of resource to manager. Available options are:<br> <br>User<br> <br>EnterpriseUser                                                                                                |
|            Authentication           |     X    | The authentication scheme to use when connecting to the SCIM API.<br> <br>Available options are:<br> <br>None: No authentication<br> <br>Windows : Windows authentication (NTLM)<br> <br>Basic: HTTP Basic authentication<br> <br>Oauth : Oauth authentication (only tested with Azure AD) |
|               Username              |          |                                                                                                            The username to use when Windows or Basic authentication is selected                                                                                                            |
|               Password              |          |                                                                                                            The password to use when Windows or Basic authentication is selected                                                                                                            |
|        OAuth - Token endpoint       |          |                                                                                                                             The URL of the OAuth token endpoint                                                                                                                            |
|          OAuth - Client ID          |          |                                                                                                                                        The client ID                                                                                                                                       |
|        OAuth - Client secret        |          |                                                                                                                                      The client secret                                                                                                                                     |
|         OAuth - Resource id         |          |                                                                                                                 AZURE ONLY - The ID of the resource that hosts the SCIM API                                                                                                                |
|              Token Type             |          |                                                             When added a token is also needed. The result of the token and token type will be placed in a Http header with key “Authorization” and value “{token type} {token}”                                                            |
|                Token                |          |                                                          When added a token type is also needed. The result of the token and token type will be placed in a Http header with key “Authorization” and value “{token type} {token}”                                                          |
| Maximum write requests (per minute) |          |                                                                                                           Time to wait after each object export.<br> <br>100 => 600 milliseconds                                                                                                           |
|          Request batch size         |          |                                                                                                                                Batch size to use for import                                                                                                                                |

** **
