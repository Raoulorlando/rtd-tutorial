<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / ASPOS

# ASPOS

The ASPOS connector module enables group-user maintenance
(create/update/delete) in ASPOS.

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
</thead>
<tbody>
<tr class="odd">
<td><p>API URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The full URL of the ASPOS instance to connect to. For
example:</p>
<p><a href="https://customername.aspos.nl/api"></a></p></td>
</tr>
<tr class="even">
<td><p>OAuth - Token URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The full URL of the ASPOS token endpoint. For example:</p>
<p><a href="https://customername.aspos.nl/connect/token"></a></p></td>
</tr>
<tr class="odd">
<td><p>OAuth - Client ID</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The OAuth client ID to use for connecting to ASPOS</p></td>
</tr>
<tr class="even">
<td><p>OAuth - Client Secret</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The OAuth client secret that belongs to above client ID</p></td>
</tr>
<tr class="odd">
<td><p>Append all stores during create</p></td>
<td><p><strong>X</strong></p></td>
<td><p>If enabled, all stores available in ASPOS will be added to the
<em>UserStores</em> property of the user when it is created</p></td>
</tr>
</tbody>
</table>
