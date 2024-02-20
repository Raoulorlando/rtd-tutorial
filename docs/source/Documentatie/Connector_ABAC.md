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

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Use custom settings instead of the IBIS configuration</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Use this to override the IBIS connection settings for ABAC. If
disabled, the ABAC connection settings will be determined from the IBIS
configuration</p></th>
</tr>
<tr class="header">
<th><p>Dossier type</p></th>
<th></th>
<th><p>Specify the dossier type of the targets to manage. If left empty,
all targets will be imported</p></th>
</tr>
<tr class="odd">
<th><p>API URL</p></th>
<th></th>
<th><p>The base URL of the ABAC instance (without /API or
/OData)</p></th>
</tr>
<tr class="header">
<th><p>Authentication</p></th>
<th></th>
<th><p>The type of authentication to use for connecting to ABAC</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th></th>
<th><p>The username to use for connecting to ABAC</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th></th>
<th><p>The password of above username</p></th>
</tr>
<tr class="odd">
<th><p>OAuth - Tenant ID</p></th>
<th></th>
<th><p>The unique identifier of the tenant in which ABAC is
hosted</p></th>
</tr>
<tr class="header">
<th><p>OAuth - Application ID</p></th>
<th></th>
<th><p>The unique identifier of the ABAC application</p></th>
</tr>
<tr class="odd">
<th><p>OAuth - Client ID</p></th>
<th></th>
<th><p>The client ID to use for connecting to ABAC</p></th>
</tr>
</thead>
&#10;</table>

 
