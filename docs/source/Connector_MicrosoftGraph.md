<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Microsoft Graph

# Microsoft Graph

The Microsoft Graph connector supports all CRUD operations on the
Microsoft Graph API.

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
<th><p>OAuth - Tenant ID</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The ID of the Azure tenant to connect to</p></th>
</tr>
<tr class="header">
<th><p>OAuth - Application ID</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The ID of the Azure AD application that should be used to
connector to the Graph API</p></th>
</tr>
<tr class="odd">
<th><p>OAuth - Application Secret</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The secret key of the above Azure AD application</p></th>
</tr>
<tr class="header">
<th><p>Type</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The type of resource this connector is targeting. Available
options are:</p>
<ul>
<li>AdministrativeUnit</li>
<li>Contract</li>
<li>Device</li>
<li>DirectoryRole</li>
<li>DirectoryRoleTemplate</li>
<li>Group</li>
<li>GroupSettingTemplate</li>
<li>Organization</li>
<li>User</li>
</ul></th>
</tr>
<tr class="odd">
<th><p>Resource URI override</p></th>
<th><p><strong> </strong></p></th>
<th><p>If set, the specified resource name will be used for all
operations instead of the default. The resource name is the last part in
the API request, for example:</p>
<p>https://graph.microsoft.com/v1.0/<strong>users</strong></p></th>
</tr>
<tr class="header">
<th><p>Additional properties to fetch</p></th>
<th><p><strong> </strong></p></th>
<th><p>By default, the Graph API returns only a subset of the properties
of a resource. In case more properties are needed in the sync, specify
them here, separated by a comma. For example:</p>
<p><strong>AccountEnabled,PasswordProfile</strong></p></th>
</tr>
</thead>
&#10;</table>
