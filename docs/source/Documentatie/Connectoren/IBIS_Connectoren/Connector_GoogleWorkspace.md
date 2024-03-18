# Google Workspace (Google Api)

The Google Workspace connector supports the following actions:

-   Provision users
-   Update users
-   Make users admin
-   Deprovision users
-   Provision groups
-   Deprovision groups

## Parameters

|                 Parameter                | Required | Description                                                                                            |
|:-----------------------------------------|:--------:|:-------------------------------------------------------------------------------------------------------|
|                Object Type               |     X    | Type of object to process                                                                              |
| Json with private key of service account |     X    | Service account json string from google dashboard                                                      |
|    Super admin user for impersonating    |     X    | Super admin user to use for impersonation                                                              |
|                  Domain                  |     X    | Domain is only used for validation purposes. That the users e-mail address is the same as this domain. |


## AppSettings

Parameter

Description

IBIS.Connector.Modules.GSuite.ReturnEmptyAliasesArray

When set to 'False' the Aliases array will be returned as 'NULL' when
empty. When set to 'True' the Aliases array wil be returned as '\[\]'
when empty

Documentation:
<https://developers.google.com/admin-sdk/directory/v1/reference/users>
