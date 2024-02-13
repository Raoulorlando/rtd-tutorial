<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Booq

##### Booq

The Booq connector module enables user maintenance
(create/update/delete) in Booq.

#### Parameters

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
</thead>
<tbody>
<tr class="odd">
<td><p>API URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The full URL of the Booq instance to connect to. For example:</p>
<p>https://customer.sandbox.booqcloud.com</p></td>
</tr>
<tr class="even">
<td><p>OAuth - Token URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The full URL of the Booq token endpoint. For example:</p>
<p>https://partners.sandbox.booqcloud.com/oauth2/token</p></td>
</tr>
<tr class="odd">
<td><p>OAuth - Client ID</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The OAuth client ID to use for connecting to Booq</p></td>
</tr>
<tr class="even">
<td><p>OAuth - Client Secret</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The OAuth client secret that belongs to above client ID</p></td>
</tr>
<tr class="odd">
<td><p>User location</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The resource URI for users. For example:</p>
<p>partner/integration/v1/users</p></td>
</tr>
<tr class="even">
<td><p>Store location</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The resource URI for stores. For example:</p>
<p>partner/onboarding/v1/stores</p></td>
</tr>
</tbody>
</table>
