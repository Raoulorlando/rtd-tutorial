<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / ZO

# ZO

The ZO module is capable of importing and exporting accounts to and from
the ZO case management system.

Accounts are never deleted in the ZO system, instead they are made
inactive by setting the value of the ‘Actief’ property to ‘0’. The
downside of this is that inactive accounts will always be included in
the sync process because ZO keeps returning them in the import. To avoid
this, you can made an import filter which excludes accounts where the
‘Actief’ property equals ‘0’.

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
<th><p>The URL of the ZO API endpoint, without any resource part.</p>
<p>For example: <a
href="https://zoapi.domain.tld">https://zoapi.domain.tld</a></p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The username for API Basic authentication</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of above user account</p></th>
</tr>
</thead>
&#10;</table>

## Primary key

The primary key of accounts is stored in the ‘objectGuid’ property. The
value of this property should contain the ObjectGuid of the associated
Active Directory account.
