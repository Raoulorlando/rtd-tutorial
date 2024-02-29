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

| Parameter | Required |                                                Description                                               |
|:---------|:--------:|:--------------------------------------------------------------------------------------------------------|
|    URL    |     X    | The URL of the ZO API endpoint, without any resource part.<br> <br>For example: https://zoapi.domain.tld |
|  Username |     X    |                                 The username for API Basic authentication                                |
|  Password |     X    |                                    The password of above user account                                    |

## Primary key

The primary key of accounts is stored in the ‘objectGuid’ property. The
value of this property should contain the ObjectGuid of the associated
Active Directory account.
