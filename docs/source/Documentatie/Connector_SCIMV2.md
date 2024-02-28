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

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>URL</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The URL of the SCIM API</p></th>
</tr>
<tr class="header">
<th><p>Schema endpoint</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the schema endpoint</p></th>
</tr>
<tr class="odd">
<th><p>Singular schema</p></th>
<th> </th>
<th><p>If set, the schema endpoint is expected to return a single
schemaresult instead of a schema collection</p></th>
</tr>
<tr class="header">
<th><p>Resource endpoint</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the resource endpoint</p></th>
</tr>
<tr class="odd">
<th><p>Resource type</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The type of resource to manager. Available options are:</p>
<p>User</p>
<p>EnterpriseUser</p></th>
</tr>
<tr class="header">
<th><p>Authentication</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The authentication scheme to use when connecting to the SCIM
API.</p>
<p>Available options are:</p>
<p>None: No authentication</p>
<p>Windows : Windows authentication (NTLM)</p>
<p>Basic: HTTP Basic authentication</p>
<p>Oauth : Oauth authentication (only tested with Azure AD)</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th> </th>
<th><p>The username to use when <strong>Windows</strong> or
<strong>Basic</strong> authentication is selected</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th> </th>
<th><p>The password to use when <strong>Windows</strong> or
<strong>Basic</strong> authentication is selected</p></th>
</tr>
<tr class="odd">
<th><p>OAuth - Token endpoint</p></th>
<th> </th>
<th><p>The URL of the OAuth token endpoint</p></th>
</tr>
<tr class="header">
<th><p>OAuth - Client ID</p></th>
<th> </th>
<th><p>The client ID</p></th>
</tr>
<tr class="odd">
<th><p>OAuth - Client secret</p></th>
<th> </th>
<th><p>The client secret</p></th>
</tr>
<tr class="header">
<th><p>OAuth - Resource id</p></th>
<th> </th>
<th><p><strong>AZURE ONLY</strong> - The ID of the resource that hosts
the SCIM API</p></th>
</tr>
<tr class="odd">
<th><p>Token Type</p></th>
<th> </th>
<th><p>When added a token is also needed. The result of the token and
token type will be placed in a Http header with key “Authorization” and
value “{token type} {token}”</p></th>
</tr>
<tr class="header">
<th><p>Token</p></th>
<th> </th>
<th><p>When added a token type is also needed. The result of the token
and token type will be placed in a Http header with key “Authorization”
and value “{token type} {token}”</p></th>
</tr>
<tr class="odd">
<th><p>Maximum write requests (per minute)</p></th>
<th> </th>
<th><p>Time to wait after each object export.</p>
<p>100 =&gt; 600 milliseconds</p></th>
</tr>
<tr class="header">
<th><p>Request batch size</p></th>
<th> </th>
<th><p>Batch size to use for import</p></th>
</tr>
</thead>
&#10;</table>

** **
