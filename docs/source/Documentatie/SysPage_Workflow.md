# Workflow

The workflow engine enables an organization to perform actions based on
events in the system. A workflow is triggered for an event (create,
update, delete, etc.) and contains the resource for which the event was
triggered (workflow content).

This section describes the events and activities available in the
workflow engine.

## Events

An event is the starting point of a workflow

### ContentCreated

This event fires when a new object is created in the system. The object
itself is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results|                                    Description                                     |
|:-------|:-----------------------------------------------------------------------------------|
|   Done | The incoming object corresponds to the type specified in the activity configuration|

<br>

| Configuration| Required?|                                                       Description                                                      |
|:-------------|:---------|:-----------------------------------------------------------------------------------------------------------------------|
| Content type | Required | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed|

<br>

|        Available workflow arguments       |
|:------------------------------------------|
| This event is not fired with any arguments|

### ContentUpdated

This event fires when an object is updated in the system. The object
itself is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results|                                     Description                                    |
|:-------|:-----------------------------------------------------------------------------------|
| Done   | The incoming object corresponds to the type specified in the activity configuration|

<br>

| Configuration | Required? |                                                                                 Description                                                                                 |
|:-------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Content type  | Required  | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed                                                     |
| Mode          | Required  | Defines the way to handle property changes:<br> <br> <br>- AND : All specified properties must be changed<br> <br>- OR : Any of the specified properties must be changed        |
| Property      | Optional  | Defines the properties to filter on in combination with the ***Mode*** setting. If specified, the workflow will only be executed when on or more of these properties have changed |

<br>

| Available workflow arguments |                                                                                                                                                                                                                                   |
|:-----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OldStateObject               | The object as it was before the update. Only properties that have actualy been changed are present on this argument. All other values are present on the current state of the object, which is available in the workflow content. |

### ContentDeleted

This event fires when an object is deleted in the system. The object
itself is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results |                                     Description                                     |
|:--------|:------------------------------------------------------------------------------------|
| Done    | The incoming object corresponds to the type specified in the activity configuration |

<br>

| Configuration | Required? |                                                       Description                                                       |
|:--------------|:----------|:------------------------------------------------------------------------------------------------------------------------|
| Content type  | Required  | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### DatasetIn

This event fires when an object is added to a dataset. The object itself
is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results |                                 Description                                |
|:--------|:---------------------------------------------------------------------------|
| Done    | The incoming object is added to the dataset specified in the configuration | 
<br>

| Configuration | Required? |      Description      |
|:--------------|:----------|:----------------------|
|  Dateset name |  Required | The dataset to act on |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### DatasetOut

This event fires when an object is removed from a dataset. The object
itself is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results |                                   Description                                  |
|:--------|:-------------------------------------------------------------------------------|
|   Done  | The incoming object is removed from the dataset specified in the configuration |

<br>

| Configuration | Required? |      Description      |
|:--------------|:----------|:----------------------|
|  Dateset name |  Required | The dataset to act on |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### OrganizationChange

This event fires when the organization of an iDossier or
applicationDossier has changed.

The object itself is added as workflow content and available with the
data lookup expressions ( {propertyname} ).

| Results |                                                                                                                                                                       Description                                                                                                                                                                       |  
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   True  | - The organization of the incoming object has changed  <br> - The organization of the incoming object has changed to CONFIG/TargetOrganization <br>  - The organization of the incoming object was changed from CONFIG/SourceOrganization  <br> - The organization of the incoming object has changed to CONFIG/TargetOrganization   from CONFIG/SourceOrganization|
|  False  |                                                                                                                                               The organization of the incoming object has not been changed                                                                                                                                              

<br>

|    Configuration   | Required? |                   Description                   |
|:-------------------|:----------|:------------------------------------------------|
| SourceOrganization |  Optional | The value of the organization before the change |
| TargetOrganization |  Optional |  The value of the organization after the change |

<br>

| Available workflow arguments |                                              |
|:-----------------------------|:---------------------------------------------|
|      SourceOrganization      | The id of the organization before the change |
|      TargetOrganization      |  The id of the organization after the change |

### StateChange

This event fires when the state of an iDossier, applicationDossier or
applicationDossierProduct has changed. The object itself is added as
workflow content and available with the data lookup expressions (
{propertyname} ).

| Results |                                                                                                                                                     Description                                                                                                                                                     |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|   True  | - The state of the incoming object has changed  <br> - The state of the incoming object has changed to CONFIG/ExpectedNewState  <br> - The state of the incoming object was changed from CONFIG/ExpectedOldState   <br>- The state of the incoming object has changed to CONFIG/ExpectedNewState   from CONFIG/ExpectedOldState
|  False  |                                                                                                                                The state of the incoming object has not been changed                                                                                                                                |

<br>

|   Configuration  | Required? |              Description             |
|:-----------------|:----------|:-------------------------------------|
| ExpectedNewState |  Optional | The value of state before the change |
| ExpectedOldState |  Optional |  The value of state after the change |

<br>

| Available workflow arguments |                                      |
|:-----------------------------|:-------------------------------------|
|           OldState           | The value of state before the change |
|           NewState           |  The value of state after the change |

### Timer

This event fires at specific intervals.

|  Results |      Description      |
|:---------|:----------------------|
| Executed | The timer is executed |

<br>

| Configuration | Required? |                          Description                          |
|:--------------|:----------|:--------------------------------------------------------------|
|    Interval   |  Required | The interval (in minutes) at which the timer must be executed |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### ManualEventTrigger

This event is used for workflows that need to be triggered manually
through the API. The endpoints for manually triggering a workflow are:

-   Synchronous : `/odata/workflows(workflow id)/TriggerWorkflow`
-   Asynchronous : `/odata/workflows(workflow id)/TriggerWorkflowAsync`

The asynchronous method will execute the workflow in the background and
immediately return a HTTP 200 result. The synchronous method will
execute the workflow in the current thread and return a HTTP 200 result
when the workflow is finished.

| Results |               Description               |
|:--------|:----------------------------------------|
|   Done  | The event is of type ManualEventTrigger |

<br>

|                    Configuration                   |
|:---------------------------------------------------|
| This event does not have any configurable settings |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### CustomEvent

This event fires for custom events in the system.

| Results |                                          Description                                         |                                                     |
|:--------|:---------------------------------------------------------------------------------------------|:----------------------------------------------------|
|   Done  | The incoming object is connected to the custom event specified in the event list down here   |                                                     |
|         |                                           **Event**                                          |                    **Description**                  |
|         |                                ImportTresholdValueExceeded                                   |   Fires when a configured threshold value exceeds   |

<br>

|                    Configuration                   |
|:---------------------------------------------------|
| This event does not have any configurable settings |

<br>

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

## Activities

Activities are the workflow steps after an Event has occurred.

### AddProductsByProductGroup

This activity adds all products from a product group to an
applicationDossier. Product groups are resolved using function and
organization.

|       Results       |                       Description                       |
|:--------------------|:--------------------------------------------------------|
|       Success       | The products have been added to the application dossier |
|       Failure       |       Something went wrong in the workflow (error)      |
| NoProductsAvailable |          There are no products available to add         |

<br>

|        Configuration        | Required? |                                                                                                                                   Description                                                                                                                                  |
|:---------------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ApplicationDossier Argument | Required  | The argument which contains the applicationDossier to add the products to                                                                                                                                                                                                      |
| Product state               | Optional  | The product state to assign to the newly added products.                                                                                                                                                                                                                       |
| Fallback Product State      | Optional  | The product state to assign to the newly added products. However when a product or productgroupproduct state is available that would prefer. The order in which states are used are as following: <br> <br>1. ProductGroupProduct<br> <br>2. Product<br> <br>3. Fallback product state  |
| Group by supplier           | Optional  | When this is checked a separate applicationdossier for every supplier will be created. The products for the supplier will be placed in the created applicationdossier.                                                                                                         |

### ArgumentDecision

This activity determines whether the specified argument matches the
specified criteria. The criteria is entered using dynamic linq or a
constant value.

|      Results     |                      Description                      |
|:-----------------|:------------------------------------------------------|
|       True       |      The argument matched the specified criteria      |
|       False      |   The argument does not match the specified criteria  |
| ArgumentNotFound | The specified argument is not present in the workflow |

<br>

| Configuration | Required? |                      Description                     |
|:--------------|:----------|:-----------------------------------------------------|
| Argument      | Required  | The name of the argument to perform the check on     |
| Ignore case   | Required  | Whether or not to ignore casing                      |
| Criteria      |           | Dynamic linq statement or constant value to match on |

### CreateArgument

This activity adds a new argument to the workflow.

| Results |                                     Description                                    |
|:--------|:-----------------------------------------------------------------------------------|
| Success |                        The argument is added to the workflow                       |
| Failure | An error occurred while adding the argument. Check the Reason argument for details |

<br>

| Configuration | Required? |                Description               |
|:--------------|:----------|:-----------------------------------------|
| ArgumentName  | Required  | The name of the argument to add          |
| ProviderType  | Required  | The provider used to create the argument |


#### ProviderTypes

##### Datalookup
Used to query the system for data.
In case SortProperty and SortDirection are unset, the entire resultset will be selected<br> In case SortProperty and SortDirection are set, the first entry in the resultset will be selected                                                                                                                                        


|                    Setting                   |                                                                                                                                                                                                                  Description                                                                                                                                                                                                                 |
|:---------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  ContentType                 |                                                                                                                                                                                                             Object type to query                                                                                                                                                                                                            
|                SelectProperty                |                                                                                                                                                  The property to select from the result. If this setting is left empty, the entire result object or collection will be placed in an argument                                                                                                                                                
|                 SortProperty                 |                                                                                                                                                                                                    The property to sort the result set on                                                                                                                                                                                                    
|                 SortDirection                |                                                                                                                                                                                                        The direction in which to sort                                                                                                                                                                                                        
|                   Criteria                   |                                                                                                                                         Dynamic linq statement <br> If you want to set criteria on DynamicProperties you should use the syntax as described in ['Dynamic properties'](#dynamic-properties) 
| Create a collection of the selected property | Works in combination with SelectProperty. When set, an array will be created with the values of the SelectProperty property from all objects returned by Criteria<br> <br>For example, when<br> <br>- ContentType: Idossier<br> <br>- SelectProperty: _42_01_Persoon_IdmNummer<br> <br>- Criteria: ID != null<br> <br>an array of strings will be created with the values of _42_01_Persoon_IdmNummer of all Idossiers where ID is not null. 

###### Dynamic properties

| DataType |                                                                                                 Example                                                                                                 |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String   | `DynamicProperties["PropertyName"] == """stringvalue"""`                                                                                                                                                  |
| Boolean  | `DynamicProperties["PropertyName"] == “””true”””`                                                                                                                                                         |
| Int      | `DynamicProperties["PropertyName"] == 123`                                                                                                                                                                |
| Date     | `DynamicProperties["PropertyName"] == """2021-12-31"""`<br> <br> <br> <br>Check in the DynamicPropertyValues table in which format dates are stored. In this example we're using the 'yyyy-MM-dd' format. |





##### ConstantValue

Adds a constant value to the argument. The input can contain text,
data lookup and functions.

##### RegularExpression

|    Configuration   | Required? |                                                                                                                 Description                                                                                                                 |
|:-------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Regular expression |  Required |                                                                                                       The regular expression to execut                                                                                                      |
|   Expression type  |  Required | The action to perform:<br> <br>- Match: Check if the source meets the regex<br> <br>- Matches: Returns all matches of regex<br> <br>- FirstMatch: Returns the first match or regex<br> <br>- Replace: Replaces matches in source with regex |
|   Source argument  |  Required |                                                                   The argument which contains the string to execute the regular expression on.<br> <br>Use {@ArgumentName}                                                                  |
|   Result argument  |  Optional |                                                                                                 The argument in which to store the result(s)                                                                                                |

##### Sql

This will place the result of the SQL statement in a collection of
objects. The objects will have the properties according to the columns
from the sql statement result.

|                   Configuration                  | Required? |                                                                                   Description                                                                                  |
|:-------------------------------------------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 ConnectionString                 |  Required |                                                                      The connectionstring to the database                                                                      |
| Use value from the first column of the first row |  Optional | When this is checked, the value from the first column of the first row will be placed in the argument. So the result will be single value instead of an collection of objects. |
|                       Query                      |  Required |                                            The SQL query statement<br> <br>Example: SELECT * FROM Table WHERE Column = ‘{@argument}’                                           |

##### TreeManagerAttributeValue
This will lookup an Attribute value from TreeManager.

| Configuration |                         Description                        |
|:--------------|:-----------------------------------------------------------|
|    Base URI   |      Location of the TreeManager api “Treemanager/Api”     |
|     ApiKey    |            ApiKey of the user accessing the Api            |
|    Password   |                   Password for the ApiKey                  |
|     NodeId    | ID of the node in treemanager to get attribute values from |
|  AttributeID  |         ID of the attribute to get the values from         |




### CreateResource

This activity creates a new resource in the system.

| Results |                                                    Description                                                   |
|:--------|:-----------------------------------------------------------------------------------------------------------------|
| Success | The new resource is succesfully created                                                                          |
| Failure | An error occurred while creating the new resource.<br> <br>The error description is added to the Reason argument |

<br>

| Configuration | Required? |                       Description                       |
|:--------------|:----------|:--------------------------------------------------------|
| Content type  | Required  | The type of resource to create                          |
| Argument name | Optional  | An argument in which to place to newly created resource |
| Property      | Optional  | Properties to add to the new object                     |

### CreateSecurePassword

This activity creates a password and stores it in a workflow argument.
When encryption is configured, the result will be saved in the following
format:

-   salt|iterations|encryptedvalue

To decrypt the password, split the value (delimiter = |), and use the
salt and number of iterations in combination with the passphrase to
decrypt the encrypted value.

| Results |                                         Description                                        |
|:--------|:-------------------------------------------------------------------------------------------|
| Success | The password was successfully generated.                                                   |
| Failure | An error occurred during password generation. Details are available in the Error argument. |

<br>

|     Configuration    | Required? |                                                                                                                                                                 Description                                                                                                                                                                 |
|:---------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetArgument       |           | The name of the argument to add the generated password to.                                                                                                                                                                                                                                                                                  |
| AddPlaintextArgument |           | If enabled, a readable (plaintext) version of the password is added as a workflow argument. The name of this argument is the value of TargetArgument with _Plain behind it.<br> <br>For example, when the value of TargetArgument is Password, the plain text version will be stored in Password_Plain                                      |
| PassPhrase           |           | If set the password will be encrypted using AES encryption. There are no length restrictions for the passphrase, but the longer the phrase the harder it will be to crack the password. A minimum length of 32 is recommended. Try combining uppercase, lowercase, numerals and special characters for improved security                    |
| Iterations           |           | The number of iterations to use when encrypting the password                                                                                                                                                                                                                                                                                |
| SaltLength           |           | The length of the random salt to generate when encrypting the password                                                                                                                                                                                                                                                                      |
| MinLength            |           | The minimum length of the password to generate                                                                                                                                                                                                                                                                                              |
| Template             |           | A template to use when generating the password. The template is processed by the dynamic lookup module to resolve properties and function values.<br> <br>In case the result of the template is shorter than the required minimum password length, random characters are added to the end of the result until the minimum length is reached |
| Blacklist            |           | A list of phrases to disallow in the generated password<br> <br> <br>one phrase per line<br> <br>phrases are translated by the dynamic lookup module before evaluation, thus the use of object properties and functions is allowed                                                                                                          |
| UseLowerCase         |           | Enable the use of lowercase characters when generating a password                                                                                                                                                                                                                                                                           |
| UseUpperCase         |           | Enable the use of uppercase characters when generating a password                                                                                                                                                                                                                                                                           |
| UseNumeric           |           | Enable the use of numeric characters when generating a password                                                                                                                                                                                                                                                                             |
| UseSpecial           |           | Enable the use of special characters when generating a password                                                                                                                                                                                                                                                                             |

### CreateTopdeskObject

This activity creates a new object in the Topdesk API.

| Results |                                                       Description                                                      |
|:--------|:-----------------------------------------------------------------------------------------------------------------------|
| Success |                              A HTTP success status code was received from the Topdesk API                              |
| Failure | An error status code was received from the Topdesk API.<br> <br>The error description is added to the Reason argument. |

<br>

|  Configuration  | Required? |                                                                  Description                                                                  |
|:----------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| TopDesk API URL | Required  | The URL of the Topdesk API                                                                                                                    |
| Resource        | Required  | Name of the resource to create (plural). For example:<br> <br>- incidents<br> <br>- operators<br> <br>- departments<br> <br>- operatorChanges |
| Login method    | Required  | Topdesk login method. Operator or Person                                                                                                      |
| Username        | Required  | The Topdesk username                                                                                                                          |
| Password        | Required  | The Topdesk password                                                                                                                          |
| Body            | Required  | The JSON body defining the resource to create. See the Topdesk documentation for instructions: https://developers.topdesk.com/documentation   |

### CreateUniqueValue

This activity creates a unique value

|     Results    |                                      Description                                     |
|:---------------|:-------------------------------------------------------------------------------------|
|     Success    |        A unique value is created and available in the given target attribute.        |
|     Failure    | An error has occurred.<br> <br>The error description is added to the Reason argument |
| NoValueCreated |             When all expression result in a conflict no value is created.            |

<br>

|         Configuration        | Required? |                                                                                                              Description                                                                                                              |
|:-----------------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UniquenewKey                 | Optional  | Give a number which you can add to the expression to make it unique. This number will be increased when a conflict is found.<br> <br>This value is available in argument {@UniquenewKey}                                              |
| UniquenewKeyLength           | Optional  | Give the total result length of the required uniquenewkey result.<br> <br>In case the generated key is shorter than this value, it will be prepended with UniquenewKeyLeadingCharacter until this number is reached.                  |
| UniquenewKeyLeadingCharacter | Optional  | The character to prepend the uniqueNewKey with.                                                                                                                                                                                       |
| AllowDiacritics              | Required  | Tells if the expressionresult can have diacritics.                                                                                                                                                                                    |
| Target Argument              | Required  | The result of the expression is placed in the argument. This argument must be used in Conflict filter to query on it.<br> <br>Write name without ‘@’<br> <br>When all expressions result in a conflict Target argument will be empty. |


#### Conflict Providers

##### IBIS

Used to query IBIS for conflicts. Only available in IBIS.

|   Setting  |       Description      |
|:----------:|:----------------------:|
| ObjectType |  Object type to query  |
|  Criteria  | Dynamic linq statement |

##### SQL

Used to query an SQL source.

|      Setting     |                                             Description                                             |
|:----------------:|:---------------------------------------------------------------------------------------------------:|
| ConnectionString |                           The connectionstring to the SQL Server database                           |
|     Criteria     | SQL Statement to check for results.   Example: ```SELECT * FROM table WHERE Column = ‘{@createdvalue}’``` |


##### PowerShell

Execute a PowerShell script to check for duplicates. A duplicate is found if the script returns one or more result objects.

|  Setting |                                                                        Description                                                                        |
|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Agent    | Optional, the PowerShell agent to use                                                                                                                     |
| Hostname | Optional, the name of the host to connect to                                                                                                              |
| Username | The username of the account to use for authentication. This cannot be the same as the IBIS app pool account                                               |
| Password | The password of above user account                                                                                                                        |
| Script   | The PowerShell command to execute. Dynamic expressions may be used<br> <br>For example: ```Get-LocalGroup -Name {@argumentNameWithValue} -ErrorAction Ignore``` |



### Decision

Checks whether or not the workflow content satisfies the specified
filter criteria.

| Results |                    Description                   |
|:--------|:-------------------------------------------------|
|   True  |     The content satisfies the filter criteria    |
|  False  | The content does not satisfy the filter criteria |


| Configuration | Required? |                                                                                                               Description                                                                                                               |
|:-------------:|:---------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Content type  | Required  | The type of object expected in workflow content                                                                                                                                                                                         |
| Criteria      | Required  | Dynamic linq statement to which the content should satisfy<br> <br>Example:<br> <br>```· _16_10_Dossier_Nummer == “{_16_98_Dossier_Master}”```<br> <br>If you want to set criteria on DynamicProperties you should use the syntax as listed in the table below. |


| DataType |                                                        Example                                                                |
|:---------|:------------------------------------------------------------------------------------------------------------------------------|
| String   |  ```DynamicProperties.ContainsKey("PropertyName") && Convert.ToString(DynamicProperties["PropertyName"]) == "stringvalue" ``` |
| Boolean  |      ```DynamicProperties.ContainsKey("PropertyName") && Convert.ToBoolean(DynamicProperties["PropertyName"]) == true```      |
| Int      |        ```DynamicProperties.ContainsKey("PropertyName") && Convert.ToInt32(DynamicProperties["PropertyName"]) == 123```       |

### Delete

Deletes a resource from the system.

| Results |                                                 Description                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------|
|  Succes |                                     The resource was succesfully deleted                                    |
| Failure | An error occurred while deleting the object.<br> <br>The error description is added to the Reason argument. |

<br>

| Configuration | Required? |                                                                                                                                             Description                                                                                                                                            |
|:--------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     Entry     |  Required | Type of resource to delete. Options are:<br> <br>- Current object à The resource present in workflow content<br> <br>- Object from argument à An resource present in a workflow argument<br> <br>Please note that deleting the current object also removes the resource from the workflow content! |
|    Argument   |  Required |                                                                                                                         The argument which contains the resource to delete                                                                                                                         |

### Email

Creates a notification.

|        Results       |                      Description                      |
|:---------------------|:------------------------------------------------------|
|         Sent         |              The notification is created              |
|        Failed        | An error occurred during creation of the notification |
| RecipientNotResolved |       The specified recipient cannot be resolved      |

<br>

|  Configuration  | Required? |                             Description                            |
|:----------------|:----------|:-------------------------------------------------------------------|
|    Recipient    |  Required |                     The recipient of the e-mail                    |
| Locale argument |  Optional | The argument containing the locale value to select the template by |
|       From      |  Required |               The e-mail address to use as the sender              |
|        CC       |  Optional |                       A carbon copy recipient                      |
|       BCC       |  Optional |                    A blind carbon copy recipient                   |
|     Template    |  Required |                  The notification template to use                  |

### ExecutePowershell

Executes a Powershell script on the local- or a remote machine. A custom
username and password is required when not running in Azure to prevent
abuse of the IBIS service account.

| Results |                                                  Description                                                 |
|:--------|:-------------------------------------------------------------------------------------------------------------|
| Success |                                      The script was succesfully executed                                     |
| Failure | An error occurred while executing the script.<br> <br>The error description is added to the Reason argument. |

<br>

| Configuration | Required? |                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                   |
|:--------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Script path  |  Optional |                                                                        The full path to a Powershell scipt file. Parameters can be added using the \| symbol<br> <br>For example: C:\Script files\Run.ps1\|{Id}\|{Name} will call the script contained in file C:\Scripts files\Run.ps1 with 2 parameters. The parameters in the example will be replaced with the values from the Id and Name properties.                                                                       |
|     Script    |  Optional |                                                                                                                                                                                                                         The Powershell script to execute                                                                                                                                                                                                                         |
|      Host     |  Optional | The hostname of the server on which to execute te Powershell script. The value should be a valid URI, for example:<br> <br>-  https://server.domain.com/PowerShell<br> <br>-  http://computername:5985<br> <br>-  https://computername:5986<br> <br>5985 (http) en 5986 (https) are the default Powershell ports for WinRM.<br> Exchange uses port 80 (http) and 443 (https) by default.<br> <br> This value is not required when the script must be executed on the IBIS server |
|    Username   |  Required |                                                                                                                                                                                 The username of the account used to execute the script.<br> <br>Cannot be identical to the application pool user                                                                                                                                                                                 |
|    Password   |  Required |                                                                                                                                                                                                                          The password of above username                                                                                                                                                                                                                          |

### ForEach

Executes a workflow for each object in an argument. All start activities
of the specified workflow will be called with the specified object as
workflow content.

| Results |                                                 Description                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------|
|   Done  |                                      The task was succesfully executed                                      |
|  Error  | An error occurred while processing the task.<br> <br>The error description is added to the Reason argument. |

<br>

| Configuration | Required? |                            Description                            |
|:--------------|:----------|:------------------------------------------------------------------|
|    Argument   |  Required | The argument whichs contains the collection of objects to process |
|  Content type |  Required |            The type of object contained in the argument           |
|    Workflow   |  Required |       The workflow which should be executed for each object       |

### ForEachActivity

Executes an activity for each object in an argument.

| Results |                                                 Description                                                 |
|:--------|:------------------------------------------------------------------------------------------------------------|
|   Done  |                                      The task was succesfully executed                                      |
|  Error  | An error occurred while processing the task.<br> <br>The error description is added to the Reason argument. |

<br>

|      Configuration     | Required? |                                                                             Description                                                                            |
|:-----------------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        Argument        |  Required |                                                  The argument whichs contains the collection of objects to process                                                 |
|   Tijdelijk argument   |  Required |                        The temporary argument to place the object in. This argument can be used in the target activity using {@argumentname}                       |
|       Activiteit       |  Required |               The activity which should be executed for each object. Configuration for this activity will be available once the activity is selected               |
| Run in separate proces |           | If set, the activity will be wrapped in it’s own lifetimescope each time it’s called. This may be useful with large datasets to minimize the SQL transaction size. |

### HasResult

Provides the ability to query resources in the system using a specified
filter. Returns true if the query has results, and false in case the
query returned zero results.

| Results |               Description              |
|:--------|:---------------------------------------|
|   True  |      The query returned no results     |
|  False  | The query returned one or more results |

| Configuration | Required? |                                                             Description                                                            |
|:-------------:|:---------:|:----------------------------------------------------------------------------------------------------------------------------------:|
|  Content type |  Required |                                                     The type of object to query                                                    |
|    Criteria   |  Required | Dynamic linq statement with a criteria to filter on.   If you want to set criteria on DynamicProperties you should use the following syntax: <br> String: ```DynamicProperties["PropertyName"] == """stringvalue"""``` <br> Boolean: ```DynamicProperties["PropertyName"] == “””true”””```  <br> Int: ```DynamicProperties["PropertyName"] == 123``` <br> Date: ```DynamicProperties["PropertyName"] == """2021-12-31"""``` |

```{eval-rst}
.. note:: Check in the DynamicPropertyValues table in which format dates are stored. In this example we're using the 'yyyy-MM-dd' format.
```


### IdentityDossier

Creates an IdentityDossier if the workflow content is an iDossier.

The source iDossier must contain the follow properties to succesfully
create the IdentityDossier:

-   \_42\_11\_Persoon\_Geslachtsnaam
-   \_42\_05\_Persoon\_GeboorteDatum
-   \_42\_25\_Persoon\_Voorletters1
-   \_42\_09\_Persoon\_Geslacht

An existing IdentityDossier will be updated if found using a match on
the following properties:

-   \_42\_11\_Persoon\_Geslachtsnaam
-   \_42\_05\_Persoon\_GeboorteDatum
-   \_42\_25\_Persoon\_Voorletters1
-   \_42\_09\_Persoon\_Geslacht

| Results |                                                            Description                                                           |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------|
|   Done  |                                            The IdentityDossier was succesfully created                                           |
|  Error  | An error occurred while creating or updating the IdentityDossier.<br> <br>The error description is added to the Reason argument. |

<br>

|                Configuration                | Required? | Description |
|:--------------------------------------------|:----------|:------------|
| This activity does not have a configuration |           |             |

### AliasDossier

Creates or updates an alias dossier for the specified IDM number.

The source iDossier must contain the follow properties to succesfully
create the alias dossier:

\- \_01\_20\_Dienstverband\_DienstverbandNummer OR
\_01\_75\_Dienstverband\_SectoraalDienstverbandNummer

\- \_01\_40\_Dienstverband\_DatumIngangGeldigheid

\- \_01\_41\_Dienstverband\_DatumEindeGeldigheid

\- \_02\_60\_Plaatsing\_Organisatieeenheid OR

\- \_42\_01\_Persoon\_IdmNummer

\- \_16\_10\_Dossier\_Nummer

| Results |                                                           Description                                                           |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------|
| Success |                                       The aliasDossier was succesfully created or updated                                       |
| Failure | An error occurred during creation or update of the aliasDossier.<br> <br>The error description is added to the Reason argument. |

The following logic is applied when choosing which iDossier should act
as the source for an

alias dossier when multiple iDossiers are available for a single alias
dossier:

-   There is at least one valid iDossier: the valid iDossier with the
    furthest placement enddate

<!-- -->

-   There is is at least one expired iDossier, no valid iDossier(s), and
    no future valid iDossier(s): the expired iDossier with the furthest
    placement enddate

<!-- -->

-   There are no valid iDossier(s), and there is at least one future
    valid iDossier: the iDossier with the furthest placement startdate

|     Configuration    | Required? |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:---------------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   IdmNumberLocation  |  Required |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The property which contains the IDM number to perform the activity on                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AliasDossierArgument |  Optional |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      The argument name to place the created / updated alias dossier in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     Configuration    |  Required | Activity configuration XML<br> <br>```<?xml version="1.0"?>``` <br> <br>```<AliasDossier>```<br> <br>```<CompleetDossierStatus>1</CompleetDossierStatus>```<br> <br>```<IDossierFilter>DienstverbandWerkduurMeesteUren</IDossierFilter>```<br> <br>```<MailDomain>domain.tld</MailDomain>```<br> <br>```<DomainNetbiosNaam>AD</DomainNetbiosNaam>```<br> <br>```<Upn>domain.tld</Upn>```<br> <br>```<UseAanmeldnaamEnAanmelddomeinUitiDossier>false</UseAanmeldnaamEnAanmelddomeinUitiDossier>```<br> <br>```<UseMailAdresUitiDossier>false</UseMailAdresUitiDossier>```<br> <br>```<MaximaleAanmeldnaamLengte>20</MaximaleAanmeldnaamLengte>```<br> <br>```<CreateMailAddressBasedOnDirectoryAccountSetting>false</CreateMailAddressBasedOnDirectoryAccountSetting>```<br> <br>```<AlleenMastersVerwerken>false</AlleenMastersVerwerken>```<br> <br>```<AantalDagenUitdienstVoorVerwijderenAccount>365</AantalDagenUitdienstVoorVerwijderenAccount>```<br> <br>```<ExchangeProvisioningViaPlugin>true</ExchangeProvisioningViaPlugin>```<br> <br>```<ExchangeKeepOffExistingMailboxes>false</ExchangeKeepOffExistingMailboxes>```<br> <br>```<ExchangeDatabaseDeterminationMethod>Automatic</ExchangeDatabaseDeterminationMethod>```<br> <br>```<ExchangePowerShellUri></ExchangePowerShellUri>```<br> <br>```<ExchangePoweShellUser></ExchangePoweShellUser>```<br> <br>```<ExchangePowerShellPassword></ExchangePowerShellPassword>```<br> <br>```<ExchangeControllers><br> <br><ExchangeControllerConfiguration>```<br> <br>```<Aanmeldsysteem>AD</Aanmeldsysteem>```<br> <br>```<ExchangePowerShellUri>http://server.domain.tld/PowerShell</ExchangePowerShellUri>```<br> <br>```<ExchangePoweShellUser></ExchangePoweShellUser>```<br> <br>```<ExchangePowerShellPassword></ExchangePowerShellPassword>```<br> <br>```<ExchangeDatabaseDeterminationMethod>Automatic</ExchangeDatabaseDeterminationMethod>```<br> <br>```</ExchangeControllerConfiguration>```<br> <br>```</ExchangeControllers>```<br> <br>```<ExchangNewMailboxActiveSyncEnabled>true</ExchangNewMailboxActiveSyncEnabled>``` <br> <br>```<ExchangNewMailboxOwaEnabled>true</ExchangNewMailboxOwaEnabled>```<br> <br>```<ExchangNewMailboxOwaForDevicesEnabled>true</ExchangNewMailboxOwaForDevicesEnabled>```<br> <br>```<ExchangNewMailboxPopEnabled>false</ExchangNewMailboxPopEnabled>```<br> <br>```<ExchangNewMailboxImapEnabled>false</ExchangNewMailboxImapEnabled>```<br> <br>```<IgnoreOrganizationMandatoryValidation>false</IgnoreOrganizationMandatoryValidation>``` <br> <br>```<HomeFoldersAanmaken>false</HomeFoldersAanmaken>```<br> <br>```<HomeFoldersAanmakenUsername></HomeFoldersAanmakenUsername>```<br> <br>```<HomeFoldersAanmakenPassword></HomeFoldersAanmakenPassword>```<br> <br>```</AliasDossier> ```|

##### Homefolder creation

The activity is capable of creating homefolders for alias dossiers on
the filesystem.  
To enable this feature:

-   Set HomeFoldersAanmaken to true in the configuration
-   Optional: set HomeFoldersAanmakenUsername and
    HomeFoldersAanmakenPassword to use a custom account when creating
    the folder
-   \_09\_10\_Alias\_Identificatie should have a value
-   \_09\_74\_Alias\_Relatietype should be set to 'Provisioning'
-   \_09\_76\_Alias\_ADhomeFolderPad must be empty
-   The organization of the alias dossier must contain the parent folder
    path in \_04\_76\_Organisatie\_ADhomeFolderPad

The foldername will be set to the value of \_09\_33\_Alias\_Aanmeldnaam

In case the folder already exists it will be left unchanged and the path
will be stored in \_09\_76\_Alias\_ADhomeFolderPad

After creation, the user will be authorized on the folder with the
folling flags:

-   FileSystemRights.Modify
-   InheritanceFlags.ContainerInherit | InheritanceFlags.ObjectInherit
-   PropagationFlags.None
-   AccessControlType.Allow

##### Mappings

The following table describes the mappings for the various alias dossier
properties.

Property resolvers (written in bold) are pieces of logic which return
the final value for a property. IBIS contains a default set of property
resolvers, which can be overridden in a customer DLL. The logic for the
default property resolvers is described in the section ‘property
resolvers’.

|                  Alias dossier property                 |      Source property or mapping logic      |
|:--------------------------------------------------------|:-------------------------------------------|
|              _01_60_Dienstverband_Faxnummer             |       _01_60_Dienstverband_FaxNummer       |
|           _04_05_Organisatie_IdmNummerManager           |         OrganisatieManagerResolver         |
| _04_20_Organisatie_IdentificatieOperationeleOrganisatie |             OrganisationNumber             |
|          _04_22_Organisatie_CoderingOrganisatie         |   OrganisatieCoderingOrganisatieResolver   |
|        _04_38_Organisatie_Personeelsgebiednummer        |     OrganizatiePersoneelsGebiedResolver    |
|         _04_55_Organisatie_Niveau1Specificering         |   OrganisatieNiveau1SpecificeringResolver  |
|         _04_56_Organisatie_Niveau2Specificering         |   OrganisatieNiveau2SpecificeringResolver  |
|         _04_57_Organisatie_Niveau3Specificering         |   OrganisatieNiveau3SpecificeringResolver  |
|         _04_58_Organisatie_Niveau4Specificering         |   OrganisatieNiveau4SpecificeringResolver  |
|             _04_71_Organisatie_ADdepartment             |       OrganisatieADdepartmentResolver      |
|             _04_73_Organisatie_ADdescription            |      OrganisatieADdescriptionResolver      |
|              _04_74_Organisatie_ADcontainer             |       OrganisatieADcontainerResolver       |
|               _04_80_Organisatie_ADcompany              |        OrganisatieADcompanyResolver        |
|         _04_81_Organisatie_ADcontainerBeheerders        |  OrganisatieADcontainerBeheerdersResolver  |
|                 _07_20_Communicatie_Type                |                  "e-mail"                  |
|               _07_30_Communicatie_Gegevens              |        CommunicatieGegevensResolver        |
|                 _09_33_Alias_Aanmeldnaam                |          AliasAanmeldnaamResolver          |
|               _09_36_Alias_Aanmeldsysteem               |         AliasAanmeldsysteemResolver        |
|                   _09_37_Alias_HomeMDB                  |            AliasHomeMdbResolver            |
|                     _09_38_Alias_UPN                    |              AliasUpnResolver              |
|                 _09_39_Alias_Displayname                |          AliasDisplaynameResolver          |
|            _09_40_Alias_DatumIngangGeldigheid           | _01_40_Dienstverband_DatumIngangGeldigheid |
|            _09_41_Alias_DatumEindeGeldigheid            |  _01_41_Dienstverband_DatumEindeGeldigheid |
|             _09_70_Alias_DeprovisioningBool             |       AliasDeprovisioningBoolResolver      |
|                _09_75_Alias_ADloginScript               |         AliasADloginscriptResolver         |
|             _09_77_Alias_ADprofileFolderPad             |        AliasADprofileFolderResolver        |
|            _09_78_Alias_ADinitieelWachtwoord            |      AliasADinitieelWachtwoordResolver     |
|                _09_79_Alias_ADcommonName                |          AliasADcommonNameResolver         |

<br>

|        Alias dossier property        |          Source property or mapping logic          |
|:-------------------------------------|:---------------------------------------------------|
|      _16_11_Dossier_BronDossier      |                _16_10_Dossier_Nummer               |
|      _16_20_Dossier_PlaatsingID      |          _02_05_Plaatsing_PlaatsingNummer          |
| _16_40_Dossier_DatumIngangGeldigheid |     _01_40_Dienstverband_DatumIngangGeldigheid     |
|  _16_41_Dossier_DatumEindeGeldigheid |      _01_41_Dienstverband_DatumEindeGeldigheid     |
|      _16_82_Dossier_Opmerkingen      |             _16_82_Dossier_Opmerkingen             |
|         _16_98_Dossier_Master        |   _16_98_Dossier_Master ?? _16_10_Dossier_Nummer   |
|            _09_38_Alias_UPN          | _09_38_Alias_UPN_Definitief_AD ?? _09_38_Alias_UPN |

  
The following properties are <u>not</u> mapped from the source dossier
to the alias dossier:

-   ID
-   CreatedDate
-   ModifiedDate
-   \_16\_10\_Dossier\_Nummer
-   \_16\_12\_Dossier\_ExterneIdentifier
-   \_16\_61\_Dossier\_Info
-   \_16\_81\_Dossier\_AandachtVereist
-   \_16\_82\_Dossier\_Opmerkingen
-   \_16\_95\_Dossier\_MigratieDossier
-   \_16\_99\_Dossier\_Status
-   \_07\_30\_Communicatie\_Gegevens\_Definitief\_AD
-   \_09\_05\_Alias\_DN\_Definitief\_AD
-   \_09\_10\_Alias\_Identificatie
-   \_09\_12\_Alias\_IdentificatieBeheerAccount
-   \_09\_13\_Alias\_ImmutableID
-   \_09\_14\_Alias\_Applicatienaam
-   \_09\_20\_Alias\_Type
-   \_09\_30\_Alias\_Gegevens
-   \_09\_33\_Alias\_Aanmeldnaam\_Definitief\_AD
-   \_09\_35\_Alias\_UserAccountControl\_Definitief\_AD
-   \_09\_38\_Alias\_UPN\_Definitief\_AD
-   \_09\_73\_Alias\_AdlastLogon
-   \_09\_74\_Alias\_Relatietype
-   \_09\_76\_Alias\_AdhomeFolderPad
-   \_09\_98\_Alias\_AliasMaster

##### Property resolvers

|                                          Property resolver                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Returns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              <br>AliasAanmeldnaamResolver                                          |                              <br>Returns:<br>                             <br>                                 <br>- _09_33_Alias_Aanmeldnaam if it is already set                             <br>                              <br>                                 <br>- _01_52_Dienstverband_SSOAccountNaam if UseAanmeldnaamEnAanmelddomeinUitiDossier is set to **true** in the configuration and _01_52_Dienstverband_SSOAccountNaam is not NULL on the source iDossier                             <br>                              <br>                                 <br>- NULL if source. _02_30_Plaatsing_DirectoryAccountAanmaken is not a variant of true (ja,yes,true,1,j,y,waar)                                                              <br>                              <br>                                 <br>- The result of the default property creator (can be overriden in customer DLL):                             <br>                              <br>          &emsp; - {all first letters of all first names}{all first letters of all prepositions}{lastname}                                                              <br>                              <br> In case the above logic results in a duplicate name, a number will be prepended to the username until it is unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                              <br>AliasAanmeldsysteemResolver                                       | <br>Returns:<br>                             <br>                                 <br>- _09_33_Alias_Aanmeldnaam if it is already set                             <br>                              <br>                                 <br>- _01_51_Dienstverband_SSODomein if UseAanmeldnaamEnAanmelddomeinUitiDossieris set to **true** in the configuration and _01_51_Dienstverband_SSODomein is not NULL on the source iDossier                             <br>                              <br>                                 <br>- NULL if source. _02_30_Plaatsing_DirectoryAccountAanmaken is not a variant of true (ja,yes,true,1,j,y,waar)                                                              <br>                              <br>                                 <br>- _04_79_Organisatie_Adaanmeldsysteem from the organization                             <br>                              <br>                                 <br>- The result of the default property creator (can be overriden in customer DLL)                             <br>                              <br>                                 <br>- The value of the *DomainNetbiosNaam* configuration setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                              <br>AliasADcommonNameResolver                                         |                              <br>Returns:<br>                             <br>                                 <br>- NULL (?)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                              <br>AliasADinitieelWachtwoordResolver                                 |                              <br>Returns:<br>                             <br>                                 <br>- _09_78_Alias_AdinitieelWachtwoord if it is already set                             <br>                              <br>                                 <br>- The result of the default property creator (can be overriden in customer DLL): NULL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                              <br>AliasADloginscriptResolver                                        |                              <br>Returns:<br>                             <br>                                 <br>- _04_75_Organisatie_ADloginScript from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                              <br>AliasADprofileFolderResolver                                      |                              <br>Returns:<br>                             <br>                                 <br>- _04_77_Organisatie_ADprofileFolderPad from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                              <br>AliasDeprovisioningBoolResolver                                   |                              <br>Returns:<br>                             <br>                                 <br>- “0” in case _09_41_Alias_DatumEindeGeldigheid is today or in the future                                 <br>                                 <br>- “1” in case the current day is smaller than (_09_41_Alias_DatumEindeGeldigheid  - AantalDagenUitdienstVoorVerwijderenAccount)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                              <br>AliasDisplaynameResolver                                          |                              <br>Returns:<br>                             <br>                                 <br>- The result of the default property creator (can be overriden in customer DLL):                                     <br>                                         <br>&emsp;- [_42_11_Persoon_Geslachtsnaam]<br>                                                                                <br>&emsp;- [_42_30_Persoon_Aanhef]<br>                                         <br>&emsp;- [_42_31_Persoon_TitelsVoor _42_24_Persoon_Voorletters]<br>                                         <br>&emsp;- [_42_32_Persoon_TitelsAchter]<br>                                         <br>&emsp;- [_42_12_Persoon_VoorvoegselGeslachtsnaam]<br>                                         <br>&emsp;- ([_42_23_Persoon_Roepnaam])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                              <br>AliasHomeMdbResolver                                              |                              <br>Returns:<br>                             <br>- The value of the *ExchangeVipMailboxDatabase* configuration setting if  _42_10_Persoon_IsVip is set to **true** and *ExchangeVipMailboxDatabase* is set                                                              <br>                              <br>                                 <br>- _09_37_Alias_HomeMDB from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                              <br>AliasUpnResolver                                                  |                              <br>Returns:<br>                             <br>                                 <br>- destination._09_38_Alias_UPN if it is already set                             <br>                              <br>                                 <br>- The result of the default property creator (can be overriden in customer DLL):                             <br>                              <br>                                 <br>                                     &emsp;- _09_33_Alias_Aanmeldnaam @ [_04_70_Organisatie_AccountDomein from the organisation when available]                                 <br>                                 <br>                                    &emsp;- _09_33_Alias_Aanmeldnaam @ [the value of Upn from the configuration when set]                                 <br>                                 <br>&emsp;- NULL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                              <br>CommunicatieGegevensResolver                                      |                              <br>Returns:<br>                             <br>                                 <br>- destination._09_38_Alias_UPN if it is already set                             <br>                              <br>                                 <br>- source._01_59_Dienstverband_EmailAdres if UseMailAdresUitiDossier is set to **true** in the settings, and source._01_59_Dienstverband_EmailAdres is not NULL                                                              <br>                              <br>                                 <br>- CreateMailAddressBasedOnDirectoryAccountSetting is **true** in the settings and _02_30_Plaatsing_DirectoryAccountAanmaken is set to a variant of true?                                     <br>                                         <br>       &emsp;- The result of the default property creator (can be overriden in customer DLL): *see below*                                                                                                                                                                                         <br>                              <br>                                 <br>- _02_31_Plaatsing_EmailAdresAanmaken is a variant of true?                                     <br>                                         <br>       &emsp;- The result of the default property creator (can be overriden in customer DLL):                                             <br>                                                 <br>            &emsp;&emsp;- _09_33_Alias_Aanmeldnaam @ _04_78_Organisatie_Admaildomein from the organisation when available]                                                 <br>                                                 <br>            &emsp;&emsp;- _09_33_Alias_Aanmeldnaam @ [the value of MailDomain from the configuration when set]                                                 <br>                                                 <br>            &emsp;&emsp;- NULL                                                                                                                                                                                                                   |
|                              <br>OrganisatieADcompanyResolver                                      |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_80_Organisatie_ADcompany from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                              <br>OrganisatieADcontainerBeheerdersResolver                          |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_81_Organisatie_ADcontainerBeheerders from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                              <br>OrganisatieADcontainerResolver                                    |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_74_Organisatie_Adcontainer from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                              <br>OrganisatieADdepartmentResolver                                   |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_71_Organisatie_Addepartment from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                              <br>OrganisatieADdescriptionResolver                                  |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_73_Organisatie_ADdescription from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                              <br>OrganisatieCoderingOrganisatieResolver                            |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_22_Organisatie_CoderingOrganisatie from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                              <br>OrganisatieManagerResolver                                        |                              <br>Returns:<br>                             <br>- The result of the default property creator (can be overriden in customer DLL):                                     <br>                                         <br>&emsp;- The value of _42_01_Persoon_IdmNummer from the manager dossier. The manager dossier is determined by using the method specified in the ManagerLookupOption setting in IBIS general settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                              <br>OrganisatieNiveau1SpecificeringResolver                           |                              <br>                                 <br>- The value of _04_55_Organisatie_Niveau1Specificering from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                              <br>OrganisatieNiveau2SpecificeringResolver                           |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_56_Organisatie_Niveau2Specificering from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                              <br>OrganisatieNiveau3SpecificeringResolver                           |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_57_Organisatie_Niveau3Specificering from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                              <br>OrganisatieNiveau4SpecificeringResolver                           |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_58_Organisatie_Niveau4Specificering from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                              <br>OrganizatiePersoneelsGebiedResolver                               |                              <br>Returns:<br>                             <br>                                 <br>- The value of _04_38_Organisatie_Personeelsgebiednummer from the organization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Log

Writes a message to the system log.
| Results |        Description        |
|:--------|:--------------------------|
|   Done  | The activity was finished |

<br>

| Configuration | Required? |                                Description                               |
|:--------------|:----------|:-------------------------------------------------------------------------|
|    LogLevel   |  Required |                   The loglevel to write the message in                   |
|   LogMessage  |  Required | The message to write to the log. Data lookup and functions are supported |
|   LoggerName  |  Optional |                    A custom name to use for the logger                   |

### OrganisationFilter

Checks whether or not the object in workflow content is assigned to the
specified organization.

| Results |                                                          Description                                                         |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------|
|   True  |   The resource in the workflow content is a member of the specified organization or a child of the specified organization.   |
|  False  | The resource in the workflow content is NOT a member of the specified organization or a child of the specified organization. |

<br>

|    Configuration   | Required? |                             Description                             |
|:-------------------|:----------|:--------------------------------------------------------------------|
| OrganisationNumber |  Required |                 The organization number to check on                 |
|    IncludeChilds   |  Required | Also return True if the content is a member of a child organization |

### RegularExpression

Executes a regular expression, and optionally places the result in a
workflow argument.

| Results |                              Description                             |
|:--------|:---------------------------------------------------------------------|
| Success | The regular expression was executed succesfully or a match was found |
| Failure |          The regular expression failed or no match was found         |

<br>

|    Configuration   | Required? |                                                                                                                 Description                                                                                                                 |
|:-------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Regular expression |  Required |                                                                                                      The regular expression to execute                                                                                                      |
|   Expression type  |  Required | The action to perform:<br> <br>- Match: Check if the source meets the regex<br> <br>- Matches: Returns all matches of regex<br> <br>- FirstMatch: Returns the first match or regex<br> <br>- Replace: Replaces matches in source with regex |
|   Source argument  |  Required |                                                                                 The argument which contains the string to execute the regular expression on                                                                                 |
|   Result argument  |  Optional |                                                                                                 The argument in which to store the result(s)                                                                                                |

### RestMethod

Performs a HTTP method on an external API.

| Results |                                                           Description                                                           |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------|
| Success |                                        The result HTTP statuscode is between 199 and 300                                        |
| Failure | The result HTTP statuscode is lower than 200 or higher than 299.<br> <br>The error description is added to the Reason argument. |

*This activity is capable of communicating with Amazon Web Services
(AWS).  
To achieve this, set the required Amazon Signature parameters in the
activity configuration.*

*This activity is capable of communicating with the Google API.  
To achieve this, set the required Google API settings in the activity
configuration.*

|      Configuration      | Required? |                                                                                                                                    Description                                                                                                                                    |
|:------------------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         **Request**         |           |                                                                                                                                                                                                                                                                                   |
|          Method         |  Required |                                                                                                                             The HTTP method to perform                                                                                                                            |
|         Base URI        |  Required |                                                                                                    The URI of the remote API. Can be specified using data lookup and functions                                                                                                    |
|         Resource        |  Required |                                                                                                           The resource. Can be specified using data lookup and functions                                                                                                          |
|       Content-Type      |  Required |                                                                             JSON, XML or ContentTypeHeader. In case ContentTypeHeader is selected, a custom header must be added named “content-type”                                                                             |
|     Source Encoding     |  Optional |                                                                                                         Encoding type of the body content. Leave empty for system default                                                                                                         |
|     Target Encoding     |  Optional |                                                                                                        Target encoding for the body content. Leave empty for system default                                                                                                       |
|           Body          |  Optional |                                                                                                                 Message body. Datalookup and functions can be used                                                                                                                |
| Enable Cookie container |  Optional |                                                                                                   If set, cookies set or unset in responses will be used in subsequent requests                                                                                                   |
|     Follow redirects    |  Optional |                                                                                                                             Follow redirects like 302                                                                                                                             |
|      **Authentication**     |           |                                                                                                                                                                                                                                                                                   |
|     PreAuthenticatie    |  Optional |                                                                                                                           Enable NTLM pre-authentication                                                                                                                          |
| Use NTLM Authentication |  Optional |            Use Windows authentication<br> <br>Warning: when no username is specified, the credentials of the application pool are used to make the request. Make sure you understand what this means, and prevent abuse by enabling SMB signing in your infrastructure            |
|         Username        |  Optional |                                                                    Username. If NTLM authentication is enabled, this username will be used for NTLM. If NTLM is not enabled, Basic authentication will be used                                                                    |
|         Password        |  Optional |                                                                                                                              Password for above user                                                                                                                              |
|    Client certificate   |  Optional |                  Client certificate to use for the connection. The certificate can be specified as the full path to a certificate file or the serial number of a certificate stored in the User store (app-pool user). Format of serial number is without spaces.                 |
|     **Microsoft Graph**     |           |                                                                                                                                                                                                                                                                                   |
|      Token Endpoint     |  Optional |                                                                                         URL for the Oauth token endpoint<br> <br>https://login.microsoftonline.com/{tenantId}/oauth3/token                                                                                        |
|         Resource        |  Optional |                                                                                                   The resource for which to acquire a token<br> <br>https://graph.microsoft.com                                                                                                   |
|         ClientId        |  Optional |                                                                                                                        The OAuth client (or application) id                                                                                                                       |
|       ClientSecret      |  Optional |                                                                                                            Secret key for the client/application specified in ClientId                                                                                                            |
|        **Amazon AWS**       |           |                                                                                                                                                                                                                                                                                   |
|        Access Key       |  Optional |                                                                                                                      The Amazon Web Services (AWS) access key                                                                                                                     |
|    Access Key Secret    |  Optional |                                                                                                          The secret of the AWS access key. Required if Access Key is set                                                                                                          |
|          Scope          |  Optional |                                                                                                            The scope of the AWS request. Required if Access Key is set                                                                                                            |
|          Region         |  Optional |                                                                                                            The region of the AWS request. Required if Access Key is set                                                                                                           |
|        **Google API**       |           |                                                                                                                                                                                                                                                                                   |
|     Service account     |  Optional |                                                                                                                     The name of the Google API service account                                                                                                                    |
|       Certificate       |  Optional |                                                                                                         The full path to the certificate of the Google API service account                                                                                                        |
|          Scope          |  Optional | The Oauth permission scope(s) to use for the request. Multiple scopes must be separated by a space. If not set, the following scopes will be used:<br> <br>- https://www.googleapis.com/auth/admin.directory.user<br> <br>- https://www.googleapis.com/auth/admin.directory.group |

|        Results        | Description |                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     Store headers     |   Optional  | When set, result and request headers will be stored in workflow arguments.<br> <br>Requires the setting Argument result prefix. Headers will be stored as:<br> <br>Response:<br> <br>- Argument name : [Result Prefix][Header key]<br> <br>- Argument value  : [Header value]<br> <br>Request:<br> <br>- Argument name : [Result Prefix]Request[Header key]<br> <br>- Argument value  : [Header value] |
| Store HTTP statuscode |   Optional  |                                                                When set, the result statuscode will be stored in a workflow argument.<br> <br>Requires the setting Argument result prefix. Statuscode will be stored as:<br> <br>Response:<br> <br>- Argument name : [Result Prefix]StatusCode<br> <br>- Argument value  : [statuscode]                                                                |
|       Store body      |   Optional  |             When set, the result and request body will be stored in a workflow argument.<br> <br>Requires the setting Argument result prefix. Body will be stored as:<br> <br>Response:<br> <br>- Argument name : [Result Prefix]Body<br> <br>- Argument value  : [HTTP body]<br> <br>Request:<br> <br>- Argument name : [Result Prefix]RequestBody<br> <br>- Argument value  : [HTTP body]            |
|     Result prefix     |   Optional  |                                                                                                                                                                               The result prefix for above store settings                                                                                                                                                                               |

### SendEmail

Sends a notification using an SMTP server. The notification should be
present in the workflow content.

| Results |                                          Description                                          |
|:--------|:----------------------------------------------------------------------------------------------|
| Success |                             The notification was succesfully sent                             |
| Failure | An error occurred during send.<br> <br>The error description is added to the Reason argument. |

<br>

| Configuration | Required? |                     Description                    |
|:--------------|:----------|:---------------------------------------------------|
|      Host     |  Required |             Hostname of the SMTP server            |
|      Port     |  Required |            SMTP Port on the SMTP server            |
|    Username   |  Optional | A username to authenticate with on the SMTP server |
|    Password   |  Optional |             Password of above username             |
|   EnableSSL   |  Optional |                   Use SSL or not                   |

### Toastr

Sends a toastr to the frontend. By default the toastr will be send to
the user initiating the workflow action button.

| Results |           Description          |
|:--------|:-------------------------------|
| Done    | When the activity is fisnished |

<br>

|  Configuration | Required? |                                                 Description                                                 |
|:---------------|:----------|:------------------------------------------------------------------------------------------------------------|
| Type           | Required  | The type of toastr which will be send                                                                       |
| Title          | Optional  | The title to show in the toastr                                                                             |
| Message        | Required  | The message to show in the toastr. Data lookup and functions supported.                                     |
| Show to admins |           | When selected the toastr will be send to all the admin users instead of the initiating workflow action user |
| Add to history |           | When selected the toastr notification will be saved in the notification panel                               |
| Show permanent |           | When selected the toastr will not have a timeout and will be on the screen until the user removed it        |

### TreeManagerAttributeValue

Retrieves the value of a TreeManager attribute for a specified node

| Results |                                                                                 Description                                                                                |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Success | The value was succesfully retrieved, and stored in the following argument(s):<br> <br>- TmResolvedValue à Single value result<br> <br>- TmResolvedValues à Multiple values |
| Failure |                                An error occurred while retrieving the value.<br> <br>The error description is added to the Reason argument.                                |

<br>

| Configuration | Required? |                                                                     Description                                                                     |
|:--------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
|    Base URI   |  Required |                                                              URL of the TreeManager API                                                             |
|    API key    |  Required |                                                                       API key                                                                       |
|  API password |  Required |                                                              Password of above API key                                                              |
|    Node Id    |  Required | The node for which to retrieve the value. Data lookup and functions supported. May contain:<br> <br>- Id<br> <br>- ExternalId<br> <br>- ExternalKey |
|  Attribute ID |  Required |                                The attribute Id for which to retrieve the value. Data lookup and functions supported                                |

### Update

Updates on or more properties on the specified resource.

| Results |                                             Description                                             |
|:--------|:----------------------------------------------------------------------------------------------------|
| Success |                                 The property was succesfully updated                                |
| Failure | An error occurred during the update.<br> <br>The error description is added to the Reason argument. |

<br>

|          Configuration          | Required? |                                                               Description                                                              |
|:--------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------|
|             Argument            |  Optional |         The argument which contains the object to update. When left empty, the object present in workflow content will be used.        |
|           Content type          |  Required |                                                 The object type of the object to update                                                |
|             Property            |  Required |                                                         The property to update                                                         |
|              Value              |  Required |                                   The new value for the property. Data lookup and functions supported                                  |
| Allow validation errors on save |  Optional | If set, object validations will not take place when saving the entity. Use with caution because data inconsistencies may be introduced |

### WithdrawAssets

Creates withdraw dossiers for all assets of the specified iDossier.

| Results |                                             Description                                            |
|:--------|:---------------------------------------------------------------------------------------------------|
| Success |                               The activity was succesfully executed.                               |
| Failure | An error occurred during execution.<br> <br>The error description is added to the Reason argument. |

<br>

|           Configuration          | Required? |                                                   Description                                                  |
|:---------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|
|         IDossier argument        |  Optional | The argument whicht contains the iDossier. When left empty, the iDossier in the workflow content will be used. |
|         IDossierIdmNumber        |  Optional |                 The idmnumber to use. If not given the Idmnumber of the IDossier will be used.                 |
|            IDossierId            |  Optional |                    The IDossier ID to use. If not given the ID of the IDossier will be used.                   |
| Verwerk automatische aangemaakte |  Required |                               Should automatically assigned assets be withdrawn?                               |
|   Verwerk handmatig aangemaakte  |  Required |                                  Should manually assigned assets be withdrawn?                                 |
|      AanvraagDossier status      |  Required |                                      The status for the withdraw dossiers                                      |
|   AanvraagDossierProduct status  |  Required |                                  The status for the withdraw dossier products                                  |

<br>

|          Result Parameters          |                                                                  |
|:------------------------------------|:-----------------------------------------------------------------|
| WithdrawnApplicationDossierProducts | All the created ApplicationDossierProducts in withdrawn dossiers |

### SMTPMessage

This activity sends an email message using the specified mailserver.

| Results |                                             Description                                            |
|:--------|:---------------------------------------------------------------------------------------------------|
| Success |                               The activity was succesfully executed.                               |
| Failure | An error occurred during execution.<br> <br>The error description is added to the Reason argument. |

<br>

|     Configuration     | Required? |                                             Description                                             |
|:----------------------|:----------|:----------------------------------------------------------------------------------------------------|
|        Hostname       |  Required |                            The DNS name or IP address of the SMTP server                            |
|          Port         |  Required |            The port to use on the SMTP server (usually 25 for non-encrypted connections)            |
|       EnableSSL       |  Required |               Wether or not to use SSL to secure the communcations with the mailserver              |
|        Username       |  Optional |                            A username to authenticatie to the SMTP server                           |
|        Password       |  Optional |                                     Password for above username                                     |
|                       |           |                                                                                                     |
|          From         |  Required |          E-mailaddress of the sender. This field may contain data resolution and functions.         |
|           TO          |  Required |        E-mailaddress of the recipient. This field may contain data resolution and functions.        |
|           CC          |  Optional |    E-mailaddress of carbon-copy recipient. This field may contain data resolution and functions.    |
|          BCC          |  Optional | E-mailaddress of blind carbon-copy recipient. This field may contain data resolution and functions. |
|        Subject        |  Optional |          The subject of the message. This field may contain data resolution and functions.          |
|        Message        |  Required |  The body of the message (the mail message). This field may contain data resolution and functions.  |
| Message contains HTML |  Optional |                            True to create a valid HTML formatted message                            |

### FileSystem

This activity can perform various filesystem operations. A custom
username and password is required when not running in Azure to prevent
abuse of the IBIS service account.

| Results |                                                                                        Description                                                                                        |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Success |                                The activity was succesfully executed<br> <br>***OR***<br> <br>In case the action is FolderOrFileExists, the folder or file exists                               |
| Failure | An error occurred during execution. The error description is added to the Reason argument.<br> <br>***OR***<br> <br>In case the action is FolderOrFileExists, the folder or file does not exist |

<br>

|  Configuration  |   Required?  |                                                                                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      Action     |   Required   | - **FolderCreate**<br> <br>*Create a new folder*<br> <br>- **FolderDelete**<br> <br>*Delete a folder*<br> <br>- **FolderMove**<br> <br>*Move a folder to another location*<br> <br>- **FileCreateOrOverwrite**<br> <br>*Create a new file, overwrite any existing file*<br> <br>- **FileCreateOrAppend**<br> <br>*Create a new file, append if the file already exists*<br> <br>- **FileMove**<br> <br>*Move a file to another location*<br> <br>- **FileDelete**<br> <br>*Delete a file*<br> <br>- **FileReadAll**<br> <br>*Read the contents of a file to an argument (string)*<br> <br>- **FileReadAllLines**<br> <br>*Read the contents of a file to an argument (array)*<br> <br>- **FolderOrFileExists**<br> <br>*Returns success if the specified file or folder exists*<br> <br>- **GetTempfileName**<br> <br>*Returns the full path and filename of a temporary file* |
|     Argument    |  Conditional |                                                                                                                                                                                                                                                                                                                                                                        Required for **GetTempfileName**, **FileReadAll** and **FileReadAllLines**                                                                                                                                                                                                                                                                                                                                                                        |
|    SourcePath   |  Conditional |                                                                                                                                                                                                                                                                                                                                                                                  The full path of the source file or folder                                                                                                                                                                                                                                                                                                                                                                                  |
| DestinationPath |  Conditional |                                                                                                                                                                                                                                                                                                                                                                                The full path of the destination file or folder                                                                                                                                                                                                                                                                                                                                                                               |
|     Content     | Not required |                                                                                                                                                                                                                                                                                                                                    The content to write to file when using **FileCreateOrOverwrite** or **FileCreateOrAppend**. The value of this setting may contain placeholders                                                                                                                                                                                                                                                                                                                                   |
|     Username    |   Required   |                                                                                                                                                                                                                                                                                                                                                                       The username of the account used to perform the filesystem action                                                                                                                                                                                                                                                                                                                                                                      |
|     Password    |   Required   |                                                                                                                                                                                                                                                                                                                                                                                        The password of above username                                                                                                                                                                                                                                                                                                                                                                                        |

### ParseJson

This activity can parse a JSON string into an object, so it can be used
with the data resolution functions.

| Results |                                                                                                                                                Description                                                                                                                                               |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Success | The activity was succesfully executed, and the object is stored in the destination argument. Propertyvalues from this object can be accessed like:<br> <br>- `{@targetArgumentName.property}`<br> <br>- `{@targetArgumentName.property.property}`<br> <br>- `{@targetArgumentName.property.property.property}` |
| Failure |                                                                             The activity failed, either because of a configuration error or an invalid JSON file. The exact reason is added to the workflow argument @Reason.                                                                            |

<br>

|    Configuration    | Required? |                              Description                              |
|:--------------------|:----------|:----------------------------------------------------------------------|
|    SourceArgument   |  Required |    The name of the workflow argument which contains the JSON string   |
| DestinationArgument |  Required | The name of the workflow argument in which to store the parsed object |

### PowerShellDecision

Executes the specified PowerShell script and continues down the True of
False path based on the script output.

| Results |                                                           Description                                                           |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------|
|   True  |                                           The script returned a ReturnValue of 'True'                                           |
|  False  |                                           The script returned a ReturnValue of 'False'                                          |
|  Error  | An error occurred during script execution. The error message is in the error log and in the workflow argument 'PowerShellError' |

<br>

| Configuration | Required? |                                                                                                                                                                     Description                                                                                                                                                                     |
|:--------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Agent         |           | If set, the script will be executed on this PowerShell agent                                                                                                                                                                                                                                                                                        |
| Hostname      |           | If set, the script will be executed on this server                                                                                                                                                                                                                                                                                                  |
| Username      | X         | The username of the account to use for executing the script                                                                                                                                                                                                                                                                                         |
| Password      | X         | The password of above username                                                                                                                                                                                                                                                                                                                      |
| Script        | X         | The script to execute<br> <br>The script must return an object with a boolean 'ReturnValue' property. Curly braces must be escaped using a '\\'. For example:<br> <br>```if ([int]{_16_99_Dossier_Status} -eq 0) \{ return New-Object PSObject -Property (@\{ReturnValue=$true\}) \} else \{ New-Object PSObject -Property (@\{ReturnValue=$false\}) \}``` |

### ExecuteIbisConnector

This activity can execute an IBIS Connector operation or runprofile.

| Results |                                        Description                                        |
|:--------|:------------------------------------------------------------------------------------------|
| Success |                   The operation or runprofile was successfully executed                   |
| Failure | An error occurred during execution. The reason is added to the workflow argument @Reason. |

<br>

| Configuration | Required? |                Description                |
|:--------------|:----------|:------------------------------------------|
|   RunProfile  |  Required |         The runprofile to execute         |
|   Connector   |  Required |          The connector to execute         |
|   Operation   |  Required | The operation to execute on the connector |
