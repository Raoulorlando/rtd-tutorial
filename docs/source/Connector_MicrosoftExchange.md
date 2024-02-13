<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Microsoft Exchange

##### Exchange Connector

This module communicates with Microsoft Exchange Server and Office 365  
The following infrastructure types are supported:

-   On premises - Local Exchange server (2013 and higher)
-   Hybrid - Local users with Office 365 mailboxes
-   Office 365 - All users and mailboxes are contained in Office 365

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
<td><p>Infrastructure type</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The type of infrastructure that is used:</p>
<ul>
<li>Cloud - Office 365</li>
<li>Hybrid - Combined on-premises and Office 365</li>
<li>OnPremises - On premises (Exchange Server 2013 and higher)</li>
</ul></td>
</tr>
<tr class="even">
<td><p>Hostname</p></td>
<td><p><strong></strong></p></td>
<td><p>Required when using the hybrid or on-premises
configuration.<br />
Contains the DNS name or IP address of the Exchange server to
use.</p></td>
</tr>
<tr class="odd">
<td><p>Authentication method</p></td>
<td><p><strong></strong></p></td>
<td><p>Required when using the hybrid or on-premises
configuration.<br />
Specifies the authentication method to use.</p></td>
</tr>
<tr class="even">
<td><p>Username</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The username of the service account to use for connecting to
Exchange Server / Office 365</p></td>
</tr>
<tr class="odd">
<td><p>Password</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The password of the above user</p></td>
</tr>
<tr class="even">
<td><p>Certificate thumbprint</p></td>
<td></td>
<td><p>Cloud only: The certificate to use for connecting to Exchange
server</p></td>
</tr>
<tr class="odd">
<td><p>Application ID</p></td>
<td></td>
<td><p>Cloud only: The AppId to use for connecting to Exchange
server</p></td>
</tr>
<tr class="even">
<td><p>Organization</p></td>
<td></td>
<td><p>Cloud only: The organization to use for connecting to Exchange
server</p></td>
</tr>
<tr class="odd">
<td><p>Create method</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The command to use when creating new objects:</p>
<ul>
<li>New-[Remote]Mailbox - Creates a new mailbox and corresponding
user</li>
<li>Enable-[Remote]Mailbox - Mail-enables an existing AD or Office 365
user</li>
</ul></td>
</tr>
<tr class="even">
<td><p>Excluded SMTP domains</p></td>
<td></td>
<td><p>A list of SMTP domains that should be ignored in the
<strong>EmailAddresses</strong> collection.<br />
E-mail addresses that end with any of these domain names will not be
imported, and will be left alone on export.</p></td>
</tr>
</tbody>
</table>

#### Password management

The Exchange module can set the password of the user object <u>on
creation</u> of the object.

When using an on-premises or hybrid configuration, authentication must
be set to Negotiate or CredSSP otherwise the password set will fail with
an unauthorized message. To export the password, create an export flow
(provision only) with the password to property:

-   *\_param\_password*

#### SMTP address handling

The module is capable of managing SMTP addresses through the
***EmailAddresses*** property.  
On export, the property will be overwritten with the actual status
according to IBIS.

-   The export flow to this attribute should contain a collection of
    SMTP addresses
-   The primary e-mail address should be the last one in the list
-   Best is to use the IBIS property
    ***EmailAddresses\_IncludingPrimary***, which already contains
    e-mail addresses in the correct format

**Export process**

-   Fetch current value of EmailAddresses
-   Create a new empty collection
-   Add all current non-smtp addresses (X500, etc.) to the collection
-   Add all current non-managed (Excluded SMTP domains) smtp addresses
    to the collection
-   Add all addresses available in the export flow to the collection,
    where the primary address type identifier will be in uppercase
    (SMTP), and all other in lowercase (smtp)

#### Communications

In order to function correctly, the following TCP/IP ports should be
open between the IBIS server and the Exchange host

-   TCP 80
-   TCP 443
-   TCP 5985
-   TCP 5986
