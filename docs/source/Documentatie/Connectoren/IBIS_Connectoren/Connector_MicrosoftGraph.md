# Microsoft Graph

The Microsoft Graph connector supports all CRUD operations on the
Microsoft Graph API.

## Parameters

|            Parameter           | Required |                                                                                                                                 Description                                                                                                                                                  |
|:-------------------------------|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        OAuth - Tenant ID       |     X    |                                                                                                                           The ID of the Azure tenant to connect to                                                                                                                           |
|     OAuth - Application ID     |     X    |                                                                                                     The ID of the Azure AD application that should be used to connector to the Graph API                                                                                                     |
|   OAuth - Application Secret   |     X    |                                                                                                                       The secret key of the above Azure AD application                                                                                                                       |
|              Type              |     X    | The type of resource this connector is targeting. Available options are:<br> <br> <br>- AdministrativeUnit<br> <br>- Contract<br> <br>- Device<br> <br>- DirectoryRole<br> <br>- DirectoryRoleTemplate<br> <br>- Group<br> <br>- GroupSettingTemplate<br> <br>- Organization<br> <br>- User  |
|      Resource URI override     |          |                                        If set, the specified resource name will be used for all operations instead of the default. The resource name is the last part in the API request, for example:<br> <br>https://graph.microsoft.com/v1.0/users                                        |
| Additional properties to fetch |          |                                 By default, the Graph API returns only a subset of the properties of a resource. In case more properties are needed in the sync, specify them here, separated by a comma. For example:<br> <br>AccountEnabled,PasswordProfile                                |
