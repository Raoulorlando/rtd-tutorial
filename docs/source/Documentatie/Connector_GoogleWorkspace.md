# Google Workspace (Google Api)

The Google Workspace connector supports the following actions:

-   Provision users
-   Update users
-   Make users admin
-   Deprovision users
-   Provision groups
-   Deprovision groups

## Parameters

|                 Parameter                | Required |                                                                                                                                                                                    Description                                                                                                                                                                                   |
|:----------------------------------------:|:--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                Object Type               |     X    |                                                                                                                                                                             Type of object to process                                                                                                                                                                            |
| Json with private key of service account |     X    |                                                                                                                                                                 Service account json string from google dashboard                                                                                                                                                                |
|    Super admin user for impersonating    |     X    |                                                                                                                                                                     Super admin user to use for impersonation                                                                                                                                                                    |
|                  Domain                  |     X    |                                                                                                                                      Domain is only used for validation purposes. That the users e-mail address is the same as this domain.                                                                                                                                      |
|             Column separator             |     X    |                                                                                                                                                                 The character(s) that is used to separate columns                                                                                                                                                                |
|              Text qualifier              |          |                                                                                                                                                                   The character(s) that is used to specify text                                                                                                                                                                  |
|                 Encoding                 |     X    |                                                                                                                                                                             The encoding of the file                                                                                                                                                                             |
|            Primary key column            |     X    |                                                                                                                              The name of the primary key column in the file. This is used to set the ExternalID property on the staging area entity                                                                                                                              |
|             Naming attribute             |     X    |                                                                                                     The attribute used for naming objects of the specified object class in the directory. In general this is ‘cn’, but some object types require a different naming attribute                                                                                                    |
|            Managed containers            |     X    | A list of containers that are managed by this connector, one per line. Objects outside of this containers will not be touched. It is also not possible to create new objects in containers that are not in this list.   The containers must be formatted using their full distinguished name.   For example:   ou=staff,ou=users,ou=iam,o=org   ou=factory,ou=users,ou=iam,o=org |

## AppSettings

Parameter

Description

IBIS.Connector.Modules.GSuite.ReturnEmptyAliasesArray

When set to 'False' the Aliases array will be returned as 'NULL' when
empty. When set to 'True' the Aliases array wil be returned as '\[\]'
when empty

Documentation:
<https://developers.google.com/admin-sdk/directory/v1/reference/users>
