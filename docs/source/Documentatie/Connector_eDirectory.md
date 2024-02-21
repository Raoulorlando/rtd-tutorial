<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / NetIQ eDirectory

# NetIQ eDirectory

The eDirectory module is capable of importing and exporting data to
NetIQ eDirectory by using the LDAP protocol.

## Parameters

|          Parameter         | Required |                                                                                                                                                                                    Description                                                                                                                                                                                   |
|:--------------------------:|:--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|          Hostname          |     X    |                                                                                                                                               The DNS name or IP address of the eDirectory server on which it accepts LDAP requests                                                                                                                                              |
|            Port            |          |                                                                                          The LDAP port to use. When no port is specified the following port will be used:   Encryption = none                              : port 389   Encryption = SecureSocketLayer        : port 636                                                                                         |
|     Secure Socket Layer    |     X    |                                                                                                                                                                         use SSL encryption (recommended)                                                                                                                                                                         |
| Allow invalid certificates |          |                                                                                                                                                                allow the use of self-signed / expired certificates                                                                                                                                                               |
|          Username          |     X    |                                                                                                                                  The fully distinguished name of the account to use to authenticate to eDirectory.   For example: cn=admin,o=org                                                                                                                                 |
|          Password          |     X    |                                                                                                                                                                          The password of above username                                                                                                                                                                          |
|       Base container       |     X    |                                                                                                                                  The base container to start searching for objects. This container should be a parent of all managed containers                                                                                                                                  |
|        Object class        |     X    |                                                                                                               The object class that is managed by this connector.   Every eDirectory connector can only manage a single object class.   For example: inetOrgPerson                                                                                                               |
|      Naming attribute      |     X    |                                                                                                     The attribute used for naming objects of the specified object class in the directory. In general this is ‘cn’, but some object types require a different naming attribute                                                                                                    |
|     Managed containers     |     X    | A list of containers that are managed by this connector, one per line. Objects outside of this containers will not be touched. It is also not possible to create new objects in containers that are not in this list.   The containers must be formatted using their full distinguished name.   For example:   ou=staff,ou=users,ou=iam,o=org   ou=factory,ou=users,ou=iam,o=org |

## Destination container

The destination container should be set through an export flow to
attribute:

-   \_param\_container
