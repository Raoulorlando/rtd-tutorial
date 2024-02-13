<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Active Directory

##### Active Directory Connector

The Active Directory module communicates with Microsoft Active
Directory. The module supports import and export of ***User*** and
***Group*** objects.

#### Primary key

The primary key for objects delivered by this module is the
***objectGUID*** property. The value of this property is the string
representation of the Active Directory objectGUID attribute, which is a
Guid.

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
<tr class="odd">
<th><p>Hostname</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The DNS name or IP address of an Active Directory domain
controller. This value can be set to the domain name if DNS resolution
can resolve Active Directory objects. For example:</p>
<p> </p>
<p>§   192.168.10.1</p>
<p>§   dc01.testdomain.local</p>
<p>§   testdomain.local</p></th>
</tr>
<tr class="header">
<th><p>DomainName</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the Active Directory domain to connect to. For
example:</p>
<p> </p>
<p>§   testdomain.local</p></th>
</tr>
<tr class="odd">
<th><p>BaseContainer</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The distinguished name of the base container for Active Directory
operations. For example:</p>
<p> </p>
<p>§   DC=testdomain,DC=local</p></th>
</tr>
<tr class="header">
<th><p>Authentication</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The type of authentication to use.</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th><p><strong> </strong></p></th>
<th><p>The upn of the account to use for connecting to Active
Directory</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th><p><strong> </strong></p></th>
<th><p>The password of the above username</p></th>
</tr>
<tr class="odd">
<th><p>Schema</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The schema to use. Select <strong>Dynamic</strong> to fetch the
schema from the server. The other 2 options can be used as fallback in
case live schema fetch does not work.</p>
<p> </p>
<p>1.     Dynamic</p>
<p>2.     Windows Server 2012 R2</p>
<p>3.     Windows Server 2016</p></th>
</tr>
<tr class="header">
<th><p>ObjectClass</p></th>
<th><p><strong> </strong></p></th>
<th><p>The name of the object class to manage in Active
Directory</p></th>
</tr>
<tr class="odd">
<th><p>ManagedContainers</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The distinguished name of the container(s) for which to manage
user objects. Each container should be placed on a new line. For
example:</p>
<p> </p>
<p>OU=Users,DC=testdomain,DC=local</p>
<p>OU=Users,OU=IDM,DC=testdomain,DC=local</p></th>
</tr>
<tr class="header">
<th><p>Export expiration date format</p></th>
<th></th>
<th>The date format to use when exporting the accountExpires attribute:
<ul>
<li>Local: change to local time</li>
<li>Universal: change to universal time</li>
<li>Original: export as-is</li>
</ul></th>
</tr>
<tr class="odd">
<th><p>Import expiration date format</p></th>
<th></th>
<th>The date format to use when importing the accountExpires attribute:
<ul>
<li>Local: change to local time</li>
<li>Universal: change to universal time</li>
<li>Original: import as-is</li>
</ul></th>
</tr>
</thead>
&#10;</table>

#### Password management

The Active Directory module can set the password of the user object
<u>on creation</u> of the object.

**Authentication** must be set to Negotiate otherwise the password set
will fail with an Unauthotized message. To export the password, create
an export flow (provision only) with the password to property:

-   *\_param\_password*

#### Disable an account

To disable an account, set an export attribute flow to the attribute:

-   *\_param\_disabled*

If the value of this attribute is true, the user will be disabled (by
adding 2 to userAccountControl)

If the value of this attribute is false, the user will be enabled (by
removing 2 from userAccountControl)

An example export flow for disabling account, based on the end date of
an aliasDossier, is:

**{?{?{\_09\_41\_Alias\_DatumEindeGeldigheid},dateistodayorfuture},iif(false,True,False)}**

#### Destination container

The destination container should be set through an export flow to
attribute:

-   \_param\_container

The value of this attribute should be the distinguished name of an
Active Directory container.

#### Object rename (move)

The connector will move a user object when one of the following
conditions are satisfied:

-   The property **cn** is changed by an export flow
-   The property **\_param\_container** is changed by an export flow

#### Communications

In order to function correctly, the following TCP/IP ports should be
open between the IBIS server and the configured Active Director domain
controller:

-   TCP/UDP 389
-   TCP 636
-   TCP/UDP 88
-   TCP/UDP 464
-   UDP 137
-   TCP 139
