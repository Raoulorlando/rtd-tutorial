<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Google Workspace

# Google Workspace (Google Api)

The Google Workspace connector supports the following actions:

-   Provision users
-   Update users
-   Make users admin
-   Deprovision users
-   Provision groups
-   Deprovision groups

## Parameters

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Object Type</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Type of object to process</p></th>
</tr>
<tr class="header">
<th><p>Json with private key of service account</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Service account json string from google dashboard</p></th>
</tr>
<tr class="odd">
<th><p>Super admin user for impersonating</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Super admin user to use for impersonation</p></th>
</tr>
<tr class="header">
<th><p>Domain</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Domain is only used for validation purposes. That the users
e-mail address is the same as this domain.</p></th>
</tr>
</thead>
&#10;</table>

## AppSettings

Parameter

Description

IBIS.Connector.Modules.GSuite.ReturnEmptyAliasesArray

When set to 'False' the Aliases array will be returned as 'NULL' when
empty. When set to 'True' the Aliases array wil be returned as '\[\]'
when empty

Documentation:
<https://developers.google.com/admin-sdk/directory/v1/reference/users>
