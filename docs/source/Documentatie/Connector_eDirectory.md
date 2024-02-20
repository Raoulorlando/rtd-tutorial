<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / NetIQ eDirectory

# NetIQ eDirectory

The eDirectory module is capable of importing and exporting data to
NetIQ eDirectory by using the LDAP protocol.

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
<th><p>Hostname</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The DNS name or IP address of the eDirectory server on which it
accepts LDAP requests</p></th>
</tr>
<tr class="header">
<th><p>Port</p></th>
<th><p><strong> </strong></p></th>
<th><p>The LDAP port to use. When no port is specified the following
port will be used:</p>
<p>Encryption = none                              : port 389</p>
<p>Encryption = SecureSocketLayer        : port 636</p></th>
</tr>
<tr class="odd">
<th><p>Secure Socket Layer</p></th>
<th><p><strong>X</strong></p></th>
<th><p>use SSL encryption (recommended)</p></th>
</tr>
<tr class="header">
<th><p>Allow invalid certificates</p></th>
<th><p><strong> </strong></p></th>
<th><p>allow the use of self-signed / expired certificates</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The fully distinguished name of the account to use to
authenticate to eDirectory.</p>
<p>For example: <em>cn=admin,o=org</em></p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of above username</p></th>
</tr>
<tr class="odd">
<th><p>Base container</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The base container to start searching for objects. This container
should be a parent of all managed containers</p></th>
</tr>
<tr class="header">
<th><p>Object class</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The object class that is managed by this connector.</p>
<p>Every eDirectory connector can only manage a single object class.</p>
<p>For example: <em>inetOrgPerson</em></p></th>
</tr>
<tr class="odd">
<th><p>Naming attribute</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The attribute used for naming objects of the specified object
class in the directory. In general this is ‘cn’, but some object types
require a different naming attribute</p></th>
</tr>
<tr class="header">
<th><p>Managed containers</p></th>
<th><p><strong>X</strong></p></th>
<th><p>A list of containers that are managed by this connector, one per
line. Objects outside of this containers will not be touched. It is also
not possible to create new objects in containers that are not in this
list.</p>
<p>The containers must be formatted using their full distinguished
name.</p>
<p>For example:</p>
<p><em>ou=staff,ou=users,ou=iam,o=org</em></p>
<p><em>ou=factory,ou=users,ou=iam,o=org</em></p></th>
</tr>
</thead>
&#10;</table>

## Destination container

The destination container should be set through an export flow to
attribute:

-   \_param\_container
