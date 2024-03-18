# Microsoft Active Directory Connector

The Active Directory module communicates with Microsoft Active
Directory. The module supports import and export of ***User*** and
***Group*** objects.

## Primary key

The primary key for objects delivered by this module is the
***objectGUID*** property. The value of this property is the string
representation of the Active Directory objectGUID attribute, which is a
Guid.

## Parameters

|           Parameter           | Required |                                                                                                                                      Description                                                                                                                                     |
|:------------------------------|:--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Hostname           |     X    | The DNS name or IP address of an Active Directory domain controller. This value can be set to the domain name if DNS resolution can resolve Active Directory objects. For example:<br> <br> <br> <br>§   192.168.10.1<br> <br>§   dc01.testdomain.local<br> <br>§   testdomain.local |
|           DomainName          |     X    |                                                                                      The name of the Active Directory domain to connect to. For example:<br> <br> <br> <br>§   testdomain.local                                                                                      |
|         BaseContainer         |     X    |                                                                        The distinguished name of the base container for Active Directory operations. For example:<br> <br> <br> <br>§   DC=testdomain,DC=local                                                                       |
|         Authentication        |     X    |                                                                                                                          The type of authentication to use.                                                                                                                          |
|            Username           |          |                                                                                                           The upn of the account to use for connecting to Active Directory                                                                                                           |
|            Password           |          |                                                                                                                          The password of the above username                                                                                                                          |
|             Schema            |     X    |         The schema to use. Select Dynamic to fetch the schema from the server. The other 2 options can be used as fallback in case live schema fetch does not work.<br> <br> <br> <br>1.     Dynamic<br> <br>2.     Windows Server 2012 R2<br> <br>3.     Windows Server 2016        |
|          ObjectClass          |          |                                                                                                              The name of the object class to manage in Active Directory                                                                                                              |
|       ManagedContainers       |     X    |                       The distinguished name of the container(s) for which to manage user objects. Each container should be placed on a new line. For example:<br> <br> <br> <br>OU=Users,DC=testdomain,DC=local<br> <br>OU=Users,OU=IDM,DC=testdomain,DC=local                      |
| Export expiration date format |          |                                                 The date format to use when exporting the accountExpires attribute: <br> <br>Local: change to local time<br> <br>Universal: change to universal time<br> <br>Original: export as-is                                                  |
| Import expiration date format |          |                                                 The date format to use when importing the accountExpires attribute: <br> <br>Local: change to local time<br> <br>Universal: change to universal time<br> <br>Original: import as-is                                                  |

## Password management

The Active Directory module can set the password of the user object
<u>on creation</u> of the object.

**Authentication** must be set to Negotiate otherwise the password set
will fail with an Unauthotized message. To export the password, create
an export flow (provision only) with the password to property:

-   *\_param\_password*

## Disable an account

To disable an account, set an export attribute flow to the attribute:

-   *\_param\_disabled*

If the value of this attribute is true, the user will be disabled (by
adding 2 to userAccountControl)

If the value of this attribute is false, the user will be enabled (by
removing 2 from userAccountControl)

An example export flow for disabling account, based on the end date of
an aliasDossier, is:

**{?{?{\_09\_41\_Alias\_DatumEindeGeldigheid},dateistodayorfuture},iif(false,True,False)}**

## Destination container

The destination container should be set through an export flow to
attribute:

-   \_param\_container

The value of this attribute should be the distinguished name of an
Active Directory container.

## Object rename (move)

The connector will move a user object when one of the following
conditions are satisfied:

-   The property **cn** is changed by an export flow
-   The property **\_param\_container** is changed by an export flow

## Communications

In order to function correctly, the following TCP/IP ports should be
open between the IBIS server and the configured Active Director domain
controller:

-   TCP/UDP 389
-   TCP 636
-   TCP/UDP 88
-   TCP/UDP 464
-   UDP 137
-   TCP 139
