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

<br><br>

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

| Configuration | Required? |                                                                                 Description                                                                                 |
|:-------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Content type  | Required  | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed                                                     |
| Mode          | Required  | Defines the way to handle property changes:<br> <br> <br>- AND : All specified properties must be changed<br> <br>- OR : Any of the specified properties must be changed        |
| Property      | Optional  | Defines the properties to filter on in combination with the ***Mode*** setting. If specified, the workflow will only be executed when on or more of these properties have changed |

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

| Configuration | Required? |                                                       Description                                                       |
|:--------------|:----------|:------------------------------------------------------------------------------------------------------------------------|
| Content type  | Required  | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed |

|        Available workflow arguments        | Required? |                                                       Description                                                       |
|:-------------------------------------------|:----------|:------------------------------------------------------------------------------------------------------------------------|
| This event is not fired with any arguments | Required  | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed |

### DatasetIn

This event fires when an object is added to a dataset. The object itself
is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results |                                 Description                                |                                                       Description                                                       |
|:--------|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| Done    | The incoming object is added to the dataset specified in the configuration | The type of object to act on. If the incoming object does not correspond to this type the workflow will not be executed |

| Configuration | Required? |      Description      |
|:--------------|:----------|:----------------------|
|  Dateset name |  Required | The dataset to act on |

|        Available workflow arguments        | Required? |      Description      |
|:-------------------------------------------|:----------|:----------------------|
| This event is not fired with any arguments |  Required | The dataset to act on |

### DatasetOut

This event fires when an object is removed from a dataset. The object
itself is added as workflow content and available with the data lookup
expressions ( {propertyname} ).

| Results |                                   Description                                  |      Description      |
|:--------|:-------------------------------------------------------------------------------|:----------------------|
|   Done  | The incoming object is removed from the dataset specified in the configuration | The dataset to act on |

| Configuration | Required? |      Description      |
|:--------------|:----------|:----------------------|
|  Dateset name |  Required | The dataset to act on |

|        Available workflow arguments        | Required? |      Description      |
|:-------------------------------------------|:----------|:----------------------|
| This event is not fired with any arguments |  Required | The dataset to act on |

### OrganizationChange

This event fires when the organization of an iDossier or
applicationDossier has changed.

The object itself is added as workflow content and available with the
data lookup expressions ( {propertyname} ).

| Results |                                                                                                                                                                       Description                                                                                                                                                                       |      Description      |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
|   True  | - The organization of the incoming object has changed  <br> - The organization of the incoming object has changed to CONFIG/TargetOrganization <br>  - The organization of the incoming object was changed from CONFIG/SourceOrganization  <br> - The organization of the incoming object has changed to CONFIG/TargetOrganization   from CONFIG/SourceOrganization | The dataset to act on |
|  False  |                                                                                                                                               The organization of the incoming object has not been changed                                                                                                                                              |                       |

|    Configuration   | Required? |                   Description                   |
|:-------------------|:----------|:------------------------------------------------|
| SourceOrganization |  Optional | The value of the organization before the change |
| TargetOrganization |  Optional |  The value of the organization after the change |

| Available workflow arguments |                                              |                   Description                   |
|:-----------------------------|:---------------------------------------------|:------------------------------------------------|
|      SourceOrganization      | The id of the organization before the change | The value of the organization before the change |
|      TargetOrganization      |  The id of the organization after the change |  The value of the organization after the change |

### StateChange

This event fires when the state of an iDossier, applicationDossier or
applicationDossierProduct has changed. The object itself is added as
workflow content and available with the data lookup expressions (
{propertyname} ).

| Results |                                                                                                                                                     Description                                                                                                                                                     |                   Description                   |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
|   True  | - The state of the incoming object has changed  <br> - The state of the incoming object has changed to CONFIG/ExpectedNewState  <br> - The state of the incoming object was changed from CONFIG/ExpectedOldState   <br>- The state of the incoming object has changed to CONFIG/ExpectedNewState   from CONFIG/ExpectedOldState | The value of the organization before the change |
|  False  |                                                                                                                                The state of the incoming object has not been changed                                                                                                                                |  The value of the organization after the change |

|   Configuration  | Required? |              Description             |
|:-----------------|:----------|:-------------------------------------|
| ExpectedNewState |  Optional | The value of state before the change |
| ExpectedOldState |  Optional |  The value of state after the change |

| Available workflow arguments |                                      |
|:-----------------------------|:-------------------------------------|
|           OldState           | The value of state before the change |
|           NewState           |  The value of state after the change |

### Timer

This event fires at specific intervals.

|  Results |      Description      |
|:---------|:----------------------|
| Executed | The timer is executed |

| Configuration | Required? |                          Description                          |
|:--------------|:----------|:--------------------------------------------------------------|
|    Interval   |  Required | The interval (in minutes) at which the timer must be executed |

|        Available workflow arguments        |
|:-------------------------------------------|
| This event is not fired with any arguments |

### ManualEventTrigger

This event is used for workflows that need to be triggered manually
through the API. The endpoints for manually triggering a workflow are:

-   Synchronous : /odata/workflows(workflow id)/TriggerWorkflow
-   Asynchronous : /odata/workflows(workflow id)/TriggerWorkflowAsync

The asynchronous method will execute the workflow in the background and
immediately return a HTTP 200 result. The synchronous method will
execute the workflow in the current thread and return a HTTP 200 result
when the workflow is finished.

| Results |               Description               |
|:--------|:----------------------------------------|
|   Done  | The event is of type ManualEventTrigger |

|                    Configuration                   |
|:---------------------------------------------------|
| This event does not have any configurable settings |

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



|                    Configuration                   |
|:---------------------------------------------------|
| This event does not have any configurable settings |

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

| Configuration | Required? |                      Description                     |
|:-------------:|:---------:|:----------------------------------------------------:|
| Argument      | Required  | The name of the argument to perform the check on     |
| Ignore case   | Required  | Whether or not to ignore casing                      |
| Criteria      |           | Dynamic linq statement or constant value to match on |

### CreateArgument

This activity adds a new argument to the workflow.

| Results |                                     Description                                    |
|:-------:|:----------------------------------------------------------------------------------:|
| Success |                        The argument is added to the workflow                       |
| Failure | An error occurred while adding the argument. Check the Reason argument for details |

| Configuration | Required? |                Description               |
|:-------------:|:---------:|:----------------------------------------:|
| ArgumentName  | Required  | The name of the argument to add          |
| ProviderType  | Required  | The provider used to create the argument |


<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Providers</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Datalookup</td>
<td>Used to query the system for data.
<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
<tr class="odd">
<th>ContentType</th>
<th>Object type to query</th>
</tr>
<tr class="header">
<th>SelectProperty</th>
<th>The property to select from the result. If this setting is left
empty, the entire result object or collection will be placed in an
argument</th>
</tr>
<tr class="odd">
<th>SortProperty</th>
<th>The property to sort the result set on</th>
</tr>
<tr class="header">
<th>SortDirection</th>
<th>The direction in which to sort</th>
</tr>
<tr class="odd">
<th>Criteria</th>
<th>Dynamic linq statement If you want to set criteria on
DynamicProperties you should use the following syntax:
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>DataType</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>String</td>
<td>DynamicProperties["PropertyName"] == """stringvalue"""</td>
</tr>
<tr class="even">
<td>Boolean</td>
<td>DynamicProperties["PropertyName"] == “””true”””</td>
</tr>
<tr class="odd">
<td>Int</td>
<td>DynamicProperties["PropertyName"] == 123</td>
</tr>
<tr class="even">
<td>Date</td>
<td><p>DynamicProperties["PropertyName"] == """2021-12-31"""</p>
<p><em> </em></p>
<p><em>Check in the DynamicPropertyValues table in which format dates
are stored. In this example we're using the 'yyyy-MM-dd'
format.</em></p></td>
</tr>
</tbody>
</table></th>
</tr>
<tr class="header">
<th>Create a collection of the selected property</th>
<th><p>Works in combination with <strong>SelectProperty</strong>. When
set, an array will be created with the values of the
<strong>SelectProperty</strong> property from all objects returned by
<strong>Criteria</strong></p>
<p>For example, when</p>
<p>- <strong>ContentType:</strong> Idossier</p>
<p>- <strong>SelectProperty:</strong> _42_01_Persoon_IdmNummer</p>
<p>- <strong>Criteria:</strong> ID != null</p>
<p>an array of strings will be created with the values of
_42_01_Persoon_IdmNummer of all Idossiers where ID is not null.</p></th>
</tr>
</thead>
&#10;</table>
<p>In case SortProperty and SortDirection are unset, the entire
resultset will be selected</p>
<p>In case SortProperty and SortDirection are set, the first entry in
the resultset will be selected</p></td>
</tr>
<tr class="even">
<td>ConstantValue</td>
<td>Adds a constant value to the argument. The input can contain text,
data lookup and functions.</td>
</tr>
<tr class="odd">
<td>RegularExpression</td>
<td><table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th>Regular expression</th>
<th>Required</th>
<th>The regular expression to execut</th>
</tr>
<tr class="header">
<th>Expression type</th>
<th>Required</th>
<th><p>The action to perform:</p>
<p>- Match à Check if the source meets the regex</p>
<p>- Matches à Returns all matches of regex</p>
<p>- FirstMatch  à Returns the first match or regex</p>
<p>- Replace à Replaces matches in source with regex</p></th>
</tr>
<tr class="odd">
<th>Source argument</th>
<th>Required</th>
<th><p>The argument which contains the string to execute the regular
expression on.</p>
<p>Use {@ArgumentName}</p></th>
</tr>
<tr class="header">
<th>Result argument</th>
<th>Optional</th>
<th>The argument in which to store the result(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th></th>
<th></th>
<th></th>
</tr>
&#10;</tbody>
</table></td>
</tr>
<tr class="even">
<td>Sql</td>
<td>This will place the result of the SQL statement in a collection of
objects. Thw objects will have the properties according to the columns
from the sql statement result.
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th>ConnectionString</th>
<th>Required</th>
<th>The connectionstring to the database</th>
</tr>
<tr class="header">
<th>Use value from the first column of the first row</th>
<th>Optional</th>
<th>When this is checked, the value from the first column of the first
row will be placed in the argument. So the result will be single value
instead of an collection of objects.</th>
</tr>
<tr class="odd">
<th>Query</th>
<th>Required</th>
<th><p>The SQL query statement</p>
<p>Example: SELECT * FROM Table WHERE Column = ‘{@argument}’</p></th>
</tr>
</thead>
&#10;</table></td>
</tr>
</tbody>
<tbody>
<tr class="odd">
<td>TreeManagerAttributeValue</td>
<td>This will lookup an Attribute value from TreeManager.
<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Description</th>
</tr>
<tr class="odd">
<th>Base URI</th>
<th>Location of the TreeManager api “Treemanager/Api”</th>
</tr>
<tr class="header">
<th>ApiKey</th>
<th>ApiKey of the user accessing the Api</th>
</tr>
<tr class="odd">
<th>Password</th>
<th>Password for the ApiKey</th>
</tr>
<tr class="header">
<th>NodeId</th>
<th>ID of the node in treemanager to get attribute values from</th>
</tr>
<tr class="odd">
<th>AttributeID</th>
<th>ID of the attribute to get the values from</th>
</tr>
</thead>
&#10;</table></td>
</tr>
</tbody>
</table>

### CreateResource

This activity creates a new resource in the system.

| Results |                                                    Description                                                   |
|:-------:|:----------------------------------------------------------------------------------------------------------------:|
| Success | The new resource is succesfully created                                                                          |
| Failure | An error occurred while creating the new resource.<br> <br>The error description is added to the Reason argument |

| Configuration | Required? |                       Description                       |
|:-------------:|:---------:|:-------------------------------------------------------:|
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
|:-------:|:------------------------------------------------------------------------------------------:|
| Success | The password was successfully generated.                                                   |
| Failure | An error occurred during password generation. Details are available in the Error argument. |

|     Configuration    | Required? |                                                                                                                                                                 Description                                                                                                                                                                 |
|:--------------------:|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
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
|:-------:|:----------------------------------------------------------------------------------------------------------------------:|
| Success |                              A HTTP success status code was received from the Topdesk API                              |
| Failure | An error status code was received from the Topdesk API.<br> <br>The error description is added to the Reason argument. |

<br>

|  Configuration  | Required? |                                                                  Description                                                                  |
|:---------------:|:---------:|:---------------------------------------------------------------------------------------------------------------------------------------------:|
| TopDesk API URL | Required  | The URL of the Topdesk API                                                                                                                    |
| Resource        | Required  | Name of the resource to create (plural). For example:<br> <br>- incidents<br> <br>- operators<br> <br>- departments<br> <br>- operatorChanges |
| Login method    | Required  | Topdesk login method. Operator or Person                                                                                                      |
| Username        | Required  | The Topdesk username                                                                                                                          |
| Password        | Required  | The Topdesk password                                                                                                                          |
| Body            | Required  | The JSON body defining the resource to create. See the Topdesk documentation for instructions: https://developers.topdesk.com/documentation   |

### CreateUniqueValue

This activity creates a unique value

|     Results    |                                      Description                                     |
|:--------------:|:------------------------------------------------------------------------------------:|
|     Success    |        A unique value is created and available in the given target attribute.        |
|     Failure    | An error has occurred.<br> <br>The error description is added to the Reason argument |
| NoValueCreated |             When all expression result in a conflict no value is created.            |

|         Configuration        | Required? |                                                                                                              Description                                                                                                              |
|:----------------------------:|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| UniquenewKey                 | Optional  | Give a number which you can add to the expression to make it unique. This number will be increased when a conflict is found.<br> <br>This value is available in argument {@UniquenewKey}                                              |
| UniquenewKeyLength           | Optional  | Give the total result length of the required uniquenewkey result.<br> <br>In case the generated key is shorter than this value, it will be prepended with UniquenewKeyLeadingCharacter until this number is reached.                  |
| UniquenewKeyLeadingCharacter | Optional  | The character to prepend the uniqueNewKey with.                                                                                                                                                                                       |
| AllowDiacritics              | Required  | Tells if the expressionresult can have diacritics.                                                                                                                                                                                    |
| Target Argument              | Required  | The result of the expression is placed in the argument. This argument must be used in Conflict filter to query on it.<br> <br>Write name without ‘@’<br> <br>When all expressions result in a conflict Target argument will be empty. |

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Conflict Providers</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IBIS</p></td>
<td><p>Used to query IBIS for conflicts. Only available in IBIS</p>
<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>ObjectType</p></th>
<th><p>Object type to query</p></th>
</tr>
<tr class="header">
<th><p>Criteria</p></th>
<th><p>Dynamic linq statement</p></th>
</tr>
</thead>
&#10;</table></td>
</tr>
<tr class="even">
<td><p>SQL</p></td>
<td><p>Used to query an SQL source</p>
<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>ConnectionString</p></th>
<th><p>The connectionstring to the SQL Server database</p></th>
</tr>
<tr class="header">
<th><p>Criteria</p></th>
<th><p>SQL Statement to check for results.</p>
<p>Example: SELECT * FROM table WHERE Column =
‘{@createdvalue}’</p></th>
</tr>
</thead>
&#10;</table></td>
</tr>
<tr class="odd">
<td><p>PowerShell</p></td>
<td><p>Execute a PowerShell script to check for duplicates. A duplicate
is found if the script returns one or more result objects</p>
<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Agent</p></td>
<td><p>Optional, the PowerShell agent to use</p></td>
</tr>
<tr class="even">
<td><p>Hostname</p></td>
<td><p>Optional, the name of the host to connect to</p></td>
</tr>
<tr class="odd">
<td><p>Username</p></td>
<td><p>The username of the account to use for authentication. This
cannot be the same as the IBIS app pool account</p></td>
</tr>
<tr class="even">
<td><p>Password</p></td>
<td><p>The password of above user account</p></td>
</tr>
<tr class="odd">
<td><p>Script</p></td>
<td><p>The PowerShell command to execute. Dynamic expressions may be
used</p>
<p>For example: Get-LocalGroup -Name {@argumentNameWithValue}
-ErrorAction Ignore</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### Decision

Checks whether or not the workflow content satisfies the specified
filter criteria.

| Results |                    Description                   |
|:-------:|:------------------------------------------------:|
|   True  |     The content satisfies the filter criteria    |
|  False  | The content does not satisfy the filter criteria |

+---------------------+----------+
| Property            | Earth    |
+=============+=======+==========+
|             | min   | -89.2 °C |
| Temperature +-------+----------+
| 1961-1990   | mean  | 14 °C    |
|             +-------+----------+
|             | max   | 56.7 °C  |
+-------------+-------+----------+

<table class="table table-bordered">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Content type</p></td>
<td><p>Required</p></td>
<td><p>The type of object expected in workflow content</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Criteria</p></td>
<td><p>Required</p></td>
<td><p>Dynamic linq statement to which the content should satisfy</p>
<p>Example:</p>
<p>· _16_10_Dossier_Nummer == “{_16_98_Dossier_Master}”</p>
<p>If you want to set criteria on DynamicProperties you should use the
following syntax:</p>
<table>
<thead class="thead-light">
<tr class="header">
<th><p><strong>DataType</strong></p></th>
<th><p><strong>Example</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>String</p></td>
<td><p>DynamicProperties.ContainsKey("PropertyName") &amp;&amp;
Convert.ToString(DynamicProperties["PropertyName"]) ==
"stringvalue"</p></td>
</tr>
<tr class="even">
<td><p>Boolean</p></td>
<td><p>DynamicProperties.ContainsKey("PropertyName") &amp;&amp;
Convert.ToBoolean(DynamicProperties["PropertyName"]) == true</p></td>
</tr>
<tr class="odd">
<td><p>Int</p></td>
<td><p>DynamicProperties.ContainsKey("PropertyName") &amp;&amp;
Convert.ToInt32(DynamicProperties["PropertyName"]) == 123</p></td>
</tr>
</tbody>
</table></td>
<td></td>
</tr>
</tbody>
</table>

### Delete

Deletes a resource from the system.

| Results |                                                 Description                                                 |
|:-------:|:-----------------------------------------------------------------------------------------------------------:|
|  Succes |                                     The resource was succesfully deleted                                    |
| Failure | An error occurred while deleting the object.<br> <br>The error description is added to the Reason argument. |

| Configuration | Required? |                                                                                                                                             Description                                                                                                                                            |
|:-------------:|:---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|     Entry     |  Required | Type of resource to delete. Options are:<br> <br>- Current object à The resource present in workflow content<br> <br>- Object from argument à An resource present in a workflow argument<br> <br>Please note that deleting the current object also removes the resource from the workflow content! |
|    Argument   |  Required |                                                                                                                         The argument which contains the resource to delete                                                                                                                         |

### Email

Creates a notification.

|        Results       |                      Description                      |
|:--------------------:|:-----------------------------------------------------:|
|         Sent         |              The notification is created              |
|        Failed        | An error occurred during creation of the notification |
| RecipientNotResolved |       The specified recipient cannot be resolved      |

|  Configuration  | Required? |                             Description                            |
|:---------------:|:---------:|:------------------------------------------------------------------:|
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
|:-------:|:------------------------------------------------------------------------------------------------------------:|
| Success |                                      The script was succesfully executed                                     |
| Failure | An error occurred while executing the script.<br> <br>The error description is added to the Reason argument. |

| Configuration | Required? |                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                   |
|:-------------:|:---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
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
|:-------:|:-----------------------------------------------------------------------------------------------------------:|
|   Done  |                                      The task was succesfully executed                                      |
|  Error  | An error occurred while processing the task.<br> <br>The error description is added to the Reason argument. |

| Configuration | Required? |                            Description                            |
|:-------------:|:---------:|:-----------------------------------------------------------------:|
|    Argument   |  Required | The argument whichs contains the collection of objects to process |
|  Content type |  Required |            The type of object contained in the argument           |
|    Workflow   |  Required |       The workflow which should be executed for each object       |

### ForEachActivity

Executes an activity for each object in an argument.

| Results |                                                 Description                                                 |
|:-------:|:-----------------------------------------------------------------------------------------------------------:|
|   Done  |                                      The task was succesfully executed                                      |
|  Error  | An error occurred while processing the task.<br> <br>The error description is added to the Reason argument. |

|      Configuration     | Required? |                                                                             Description                                                                            |
|:----------------------:|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|        Argument        |  Required |                                                  The argument whichs contains the collection of objects to process                                                 |
|   Tijdelijk argument   |  Required |                        The temporary argument to place the object in. This argument can be used in the target activity using {@argumentname}                       |
|       Activiteit       |  Required |               The activity which should be executed for each object. Configuration for this activity will be available once the activity is selected               |
| Run in separate proces |           | If set, the activity will be wrapped in it’s own lifetimescope each time it’s called. This may be useful with large datasets to minimize the SQL transaction size. |

### HasResult

Provides the ability to query resources in the system using a specified
filter. Returns true if the query has results, and false in case the
query returned zero results.

| Results |               Description              |
|:-------:|:--------------------------------------:|
|   True  |      The query returned no results     |
|  False  | The query returned one or more results |

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Content type</p></th>
<th><p>Required</p></th>
<th><p>The type of object to query</p></th>
</tr>
<tr class="header">
<th><p>Criteria</p></th>
<th><p>Required</p></th>
<th><p>Dynamic linq statement with a criteria to filter on</p>
<p>If you want to set criteria on DynamicProperties you should use the
following syntax:</p>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th><p><strong>DataType</strong></p></th>
<th><p><strong>Example</strong></p></th>
</tr>
<tr class="odd">
<th><p>String</p></th>
<th><p>DynamicProperties["PropertyName"] == """stringvalue"""</p></th>
</tr>
<tr class="header">
<th><p>Boolean</p></th>
<th><p>DynamicProperties["PropertyName"] == “””true”””</p></th>
</tr>
<tr class="odd">
<th><p>Int</p></th>
<th><p>DynamicProperties["PropertyName"] == 123</p></th>
</tr>
<tr class="header">
<th><p>Date</p></th>
<th><p>DynamicProperties["PropertyName"] == """2021-12-31"""</p>
<p><em> </em></p>
<p><em>Check in the DynamicPropertyValues table in which format dates
are stored. In this example we're using the 'yyyy-MM-dd'
format.</em></p></th>
</tr>
</thead>
&#10;</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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
|:-------:|:--------------------------------------------------------------------------------------------------------------------------------:|
|   Done  |                                            The IdentityDossier was succesfully created                                           |
|  Error  | An error occurred while creating or updating the IdentityDossier.<br> <br>The error description is added to the Reason argument. |

|                Configuration                | Required? | Description |
|:-------------------------------------------:|:---------:|:-----------:|
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
|:-------:|:-------------------------------------------------------------------------------------------------------------------------------:|
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
|:--------------------:|:---------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|   IdmNumberLocation  |  Required |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The property which contains the IDM number to perform the activity on                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AliasDossierArgument |  Optional |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      The argument name to place the created / updated alias dossier in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     Configuration    |  Required | Activity configuration XML<br> <br><?xml version="1.0"?> <br> <br><AliasDossier><br> <br><CompleetDossierStatus>1</CompleetDossierStatus><br> <br><IDossierFilter>DienstverbandWerkduurMeesteUren</IDossierFilter><br> <br><MailDomain>domain.tld</MailDomain><br> <br><DomainNetbiosNaam>AD</DomainNetbiosNaam><br> <br><Upn>domain.tld</Upn><br> <br><UseAanmeldnaamEnAanmelddomeinUitiDossier>false</UseAanmeldnaamEnAanmelddomeinUitiDossier><br> <br><UseMailAdresUitiDossier>false</UseMailAdresUitiDossier><br> <br><MaximaleAanmeldnaamLengte>20</MaximaleAanmeldnaamLengte><br> <br><CreateMailAddressBasedOnDirectoryAccountSetting>false</CreateMailAddressBasedOnDirectoryAccountSetting><br> <br><AlleenMastersVerwerken>false</AlleenMastersVerwerken><br> <br><AantalDagenUitdienstVoorVerwijderenAccount>365</AantalDagenUitdienstVoorVerwijderenAccount><br> <br><ExchangeProvisioningViaPlugin>true</ExchangeProvisioningViaPlugin><br> <br><ExchangeKeepOffExistingMailboxes>false</ExchangeKeepOffExistingMailboxes><br> <br><ExchangeDatabaseDeterminationMethod>Automatic</ExchangeDatabaseDeterminationMethod><br> <br><ExchangePowerShellUri></ExchangePowerShellUri><br> <br><ExchangePoweShellUser></ExchangePoweShellUser><br> <br><ExchangePowerShellPassword></ExchangePowerShellPassword><br> <br><ExchangeControllers><br> <br><ExchangeControllerConfiguration><br> <br><Aanmeldsysteem>AD</Aanmeldsysteem><br> <br><ExchangePowerShellUri>http://server.domain.tld/PowerShell</ExchangePowerShellUri><br> <br><ExchangePoweShellUser></ExchangePoweShellUser><br> <br><ExchangePowerShellPassword></ExchangePowerShellPassword><br> <br><ExchangeDatabaseDeterminationMethod>Automatic</ExchangeDatabaseDeterminationMethod><br> <br></ExchangeControllerConfiguration><br> <br></ExchangeControllers><br> <br><ExchangNewMailboxActiveSyncEnabled>true</ExchangNewMailboxActiveSyncEnabled><br> <br><ExchangNewMailboxOwaEnabled>true</ExchangNewMailboxOwaEnabled><br> <br><ExchangNewMailboxOwaForDevicesEnabled>true</ExchangNewMailboxOwaForDevicesEnabled><br> <br><ExchangNewMailboxPopEnabled>false</ExchangNewMailboxPopEnabled><br> <br><ExchangNewMailboxImapEnabled>false</ExchangNewMailboxImapEnabled><br> <br><IgnoreOrganizationMandatoryValidation>false</IgnoreOrganizationMandatoryValidation><br> <br><HomeFoldersAanmaken>false</HomeFoldersAanmaken><br> <br><HomeFoldersAanmakenUsername></HomeFoldersAanmakenUsername><br> <br><HomeFoldersAanmakenPassword></HomeFoldersAanmakenPassword><br> <br></AliasDossier> |

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
|:-------------------------------------------------------:|:------------------------------------------:|
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

|        Alias dossier property        |          Source property or mapping logic          |
|:------------------------------------:|:--------------------------------------------------:|
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

Property resolver

Returns

**AliasAanmeldnaamResolver**

Returns:

-   \_09\_33\_Alias\_Aanmeldnaam if it is already set

<!-- -->

-   \_01\_52\_Dienstverband\_SSOAccountNaam if

*UseAanmeldnaamEnAanmelddomeinUitiDossier* is set to **true** in the
configuration and \_01\_52\_Dienstverband\_SSOAccountNaam is not NULL on
the source iDossier

-   NULL if source. \_02\_30\_Plaatsing\_DirectoryAccountAanmaken is not
    a variant of true (ja,yes,true,1,j,y,waar)

<!-- -->

-   The result of the default property creator (can be overriden in
    customer DLL):

1.  {all first letters of all first names}{all first letters of all
    prepositions}{lastname}

In case the above logic results in a duplicate name, a number will be
prepended to the username until it is unique.

**AliasAanmeldsysteemResolver**

Returns:

-   \_09\_33\_Alias\_Aanmeldnaam if it is already set

<!-- -->

-   \_01\_51\_Dienstverband\_SSODomein if

*UseAanmeldnaamEnAanmelddomeinUitiDossier*is set to **true** in the
configuration and \_01\_51\_Dienstverband\_SSODomein is not NULL on the
source iDossier

-   NULL if source. \_02\_30\_Plaatsing\_DirectoryAccountAanmaken is not
    a variant of true (ja,yes,true,1,j,y,waar)

<!-- -->

-   \_04\_79\_Organisatie\_Adaanmeldsysteem from the organization

<!-- -->

-   The result of the default property creator (can be overriden in
    customer DLL)

<!-- -->

-   The value of the *DomainNetbiosNaam* configuration setting

**AliasADcommonNameResolver**

Returns:

-   NULL (?)

**AliasADinitieelWachtwoordResolver**

Returns:

-   \_09\_78\_Alias\_AdinitieelWachtwoord if it is already set

<!-- -->

-   The result of the default property creator (can be overriden in
    customer DLL): NULL

**AliasADloginscriptResolver**

Returns:

-   \_04\_75\_Organisatie\_ADloginScript from the organization

**AliasADprofileFolderResolver**

Returns:

-   \_04\_77\_Organisatie\_ADprofileFolderPad from the organization

**AliasDeprovisioningBoolResolver**

Returns:

-   “0” in case \_09\_41\_Alias\_DatumEindeGeldigheid is today or in the
    future
-   “1” in case the current day is smaller than

(\_09\_41\_Alias\_DatumEindeGeldigheid  -
AantalDagenUitdienstVoorVerwijderenAccount)

**AliasDisplaynameResolver**

Returns:

-   The result of the default property creator (can be overriden in
    customer DLL):
    -   \[\_42\_11\_Persoon\_Geslachtsnaam\]
    -   ,
    -   \[\_42\_30\_Persoon\_Aanhef\]
    -   \[\_42\_31\_Persoon\_TitelsVoor \_42\_24\_Persoon\_Voorletters\]
    -   \[\_42\_32\_Persoon\_TitelsAchter\]
    -   \[\_42\_12\_Persoon\_VoorvoegselGeslachtsnaam\]
    -   (\[\_42\_23\_Persoon\_Roepnaam\])

**AliasHomeMdbResolver**

Returns:

-   The value of the *ExchangeVipMailboxDatabase* configuration setting
    in case \_42\_10\_Persoon\_IsVip is set to true and
    *ExchangeVipMailboxDatabase* is set

<!-- -->

-   \_09\_37\_Alias\_HomeMDB from the organization

**AliasUpnResolver**

Returns:

-   destination.\_09\_38\_Alias\_UPN if it is already set

<!-- -->

-   The result of the default property creator (can be overriden in
    customer DLL):

<!-- -->

-   \_09\_33\_Alias\_Aanmeldnaam @
    \[\_04\_70\_Organisatie\_AccountDomein from the organisation when
    available\]
-   \_09\_33\_Alias\_Aanmeldnaam @ \[the value of *Upn* from the
    configuration when set\]
-   NULL

**CommunicatieGegevensResolver**

Returns:

-   destination.\_09\_38\_Alias\_UPN if it is already set

<!-- -->

-   source.\_01\_59\_Dienstverband\_EmailAdres if
    UseMailAdresUitiDossier is set to true in the settings, and
    source.\_01\_59\_Dienstverband\_EmailAdres is not NULL

<!-- -->

-   CreateMailAddressBasedOnDirectoryAccountSetting is true in the
    settings and \_02\_30\_Plaatsing\_DirectoryAccountAanmaken is set to
    a variant of true?
    -   The result of the default property creator (can be overriden in
        customer DLL): *see below*

<!-- -->

-   \_02\_31\_Plaatsing\_EmailAdresAanmaken is a variant of true?
    -   The result of the default property creator (can be overriden in
        customer DLL):
        1.  \_09\_33\_Alias\_Aanmeldnaam @
            \_04\_78\_Organisatie\_Admaildomein from the organisation
            when available\]
        2.  \_09\_33\_Alias\_Aanmeldnaam @ \[the value of *MailDomain*
            from the configuration when set\]
        3.  NULL

**OrganisatieADcompanyResolver**

Returns:

-   The value of \_04\_80\_Organisatie\_ADcompany from the organization

**OrganisatieADcontainerBeheerdersResolver**

Returns:

-   The value of \_04\_81\_Organisatie\_ADcontainerBeheerders from the
    organization

**OrganisatieADcontainerResolver**

Returns:

-   The value of \_04\_74\_Organisatie\_Adcontainer from the
    organization

**OrganisatieADdepartmentResolver**

Returns:

-   The value of \_04\_71\_Organisatie\_Addepartment from the
    organization

**OrganisatieADdescriptionResolver**

Returns:

-   The value of \_04\_73\_Organisatie\_ADdescription from the
    organization

**OrganisatieCoderingOrganisatieResolver**

Returns:

-   The value of \_04\_22\_Organisatie\_CoderingOrganisatie from the
    organization

**OrganisatieManagerResolver**

Returns:

-   The result of the default property creator (can be overriden in
    customer DLL):
    -   The value of \_42\_01\_Persoon\_IdmNummer from the manager
        dossier. The manager dossier is determined by using the method
        specified in the ManagerLookupOption setting in IBIS general
        settings

**OrganisatieNiveau1SpecificeringResolver**

-   The value of \_04\_55\_Organisatie\_Niveau1Specificering from the
    organization

**OrganisatieNiveau2SpecificeringResolver**

Returns:

-   The value of \_04\_56\_Organisatie\_Niveau2Specificering from the
    organization

**OrganisatieNiveau3SpecificeringResolver**

Returns:

-   The value of \_04\_57\_Organisatie\_Niveau3Specificering from the
    organization

**OrganisatieNiveau4SpecificeringResolver**

Returns:

-   The value of \_04\_58\_Organisatie\_Niveau4Specificering from the
    organization

**OrganizatiePersoneelsGebiedResolver**

Returns:

-   The value of \_04\_38\_Organisatie\_Personeelsgebiednummer from the
    organization

### Log

Writes a message to the system log.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Done</p></th>
<th><p>The activity was finished</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>LogLevel</p></th>
<th><p>Required</p></th>
<th><p>The loglevel to write the message in</p></th>
</tr>
<tr class="header">
<th><p>LogMessage</p></th>
<th><p>Required</p></th>
<th><p>The message to write to the log. Data lookup and functions are
supported</p></th>
</tr>
<tr class="odd">
<th><p>LoggerName</p></th>
<th><p>Optional</p></th>
<th><p>A custom name to use for the logger</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### OrganisationFilter

Checks whether or not the object in workflow content is assigned to the
specified organization.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>True</p></th>
<th><p>The resource in the workflow content is a member of the specified
organization or a child of the specified organization.</p></th>
</tr>
<tr class="header">
<th><p>False</p></th>
<th><p>The resource in the workflow content is NOT a member of the
specified organization or a child of the specified
organization.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>OrganisationNumber</p></th>
<th><p>Required</p></th>
<th><p>The organization number to check on</p></th>
</tr>
<tr class="header">
<th><p>IncludeChilds</p></th>
<th><p>Required</p></th>
<th><p>Also return True if the content is a member of a child
organization</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### RegularExpression

Executes a regular expression, and optionally places the result in a
workflow argument.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The regular expression was executed succesfully or a match was
found</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>The regular expression failed or no match was found</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Regular expression</p></th>
<th><p>Required</p></th>
<th><p>The regular expression to execute</p></th>
</tr>
<tr class="header">
<th><p>Expression type</p></th>
<th><p>Required</p></th>
<th><p>The action to perform:</p>
<p>- Match à Check if the source meets the regex</p>
<p>- Matches à Returns all matches of regex</p>
<p>- FirstMatch  à Returns the first match or regex</p>
<p>- Replace à Replaces matches in source with regex</p></th>
</tr>
<tr class="odd">
<th><p>Source argument</p></th>
<th><p>Required</p></th>
<th><p>The argument which contains the string to execute the regular
expression on</p></th>
</tr>
<tr class="header">
<th><p>Result argument</p></th>
<th><p>Optional</p></th>
<th><p>The argument in which to store the result(s)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### RestMethod

Performs a HTTP method on an external API.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The result HTTP statuscode is between 199 and 300</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>The result HTTP statuscode is lower than 200 or higher than
299.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

*This activity is capable of communicating with Amazon Web Services
(AWS).  
To achieve this, set the required Amazon Signature parameters in the
activity configuration.*

*This activity is capable of communicating with the Google API.  
To achieve this, set the required Google API settings in the activity
configuration.*

<table class="table table-bordered">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
<th></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Request</strong></p></th>
</tr>
<tr class="header">
<th><p>Method</p></th>
<th><p>Required</p></th>
<th><p>The HTTP method to perform</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Base URI</p></th>
<th><p>Required</p></th>
<th><p>The URI of the remote API. Can be specified using data lookup and
functions</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Resource</p></th>
<th><p>Required</p></th>
<th><p>The resource. Can be specified using data lookup and
functions</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Content-Type</p></th>
<th><p>Required</p></th>
<th><p>JSON, XML or ContentTypeHeader. In case ContentTypeHeader is
selected, a custom header must be added named “content-type”</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Source Encoding</p></th>
<th><p>Optional</p></th>
<th><p>Encoding type of the body content. Leave empty for system
default</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Target Encoding</p></th>
<th><p>Optional</p></th>
<th><p>Target encoding for the body content. Leave empty for system
default</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Body</p></th>
<th><p>Optional</p></th>
<th><p>Message body. Datalookup and functions can be used</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Enable Cookie container</p></th>
<th><p>Optional</p></th>
<th><p>If set, cookies set or unset in responses will be used in
subsequent requests</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Follow redirects</p></th>
<th><p>Optional</p></th>
<th><p>Follow redirects like 302</p></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Authentication</strong></p></th>
</tr>
<tr class="header">
<th><p>PreAuthenticatie</p></th>
<th><p>Optional</p></th>
<th><p>Enable NTLM pre-authentication</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Use NTLM Authentication</p></th>
<th><p>Optional</p></th>
<th><p>Use Windows authentication</p>
<p><strong>Warning: when no username is specified, the credentials of
the application pool are used to make the request. Make sure you
understand what this means, and prevent abuse by enabling SMB signing in
your infrastructure</strong></p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p>Optional</p></th>
<th><p>Username. If NTLM authentication is enabled, this username will
be used for NTLM. If NTLM is not enabled, Basic authentication will be
used</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p>Optional</p></th>
<th><p>Password for above user</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Client certificate</p></th>
<th><p>Optional</p></th>
<th><p>Client certificate to use for the connection. The certificate can
be specified as the full path to a certificate file or the serial number
of a certificate stored in the User store (app-pool user). Format of
serial number is without spaces.</p></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Microsoft Graph</strong></p></th>
</tr>
<tr class="header">
<th><p>Token Endpoint</p></th>
<th><p>Optional</p></th>
<th><p>URL for the Oauth token endpoint</p>
<p>https://login.microsoftonline.com/<u>{tenantId}</u>/oauth3/token</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Resource</p></th>
<th><p>Optional</p></th>
<th><p>The resource for which to acquire a token</p>
<p>https://graph.microsoft.com</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>ClientId</p></th>
<th><p>Optional</p></th>
<th><p>The OAuth client (or application) id</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>ClientSecret</p></th>
<th><p>Optional</p></th>
<th><p>Secret key for the client/application specified in
ClientId</p></th>
<th></th>
</tr>
<tr class="header">
<th colspan="4"><p><strong>Amazon AWS</strong></p></th>
</tr>
<tr class="odd">
<th><p>Access Key</p></th>
<th><p>Optional</p></th>
<th><p>The Amazon Web Services (AWS) access key</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Access Key Secret</p></th>
<th><p>Optional</p></th>
<th><p>The secret of the AWS access key. Required if Access Key is
set</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Scope</p></th>
<th><p>Optional</p></th>
<th><p>The scope of the AWS request. Required if Access Key is
set</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Region</p></th>
<th><p>Optional</p></th>
<th><p>The region of the AWS request. Required if Access Key is
set</p></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="4"><p><strong>Google API</strong></p></th>
</tr>
<tr class="header">
<th><p>Service account</p></th>
<th><p>Optional</p></th>
<th><p>The name of the Google API service account</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Certificate</p></th>
<th><p>Optional</p></th>
<th><p>The full path to the certificate of the Google API service
account</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Scope</p></th>
<th><p>Optional</p></th>
<th><p>The Oauth permission scope(s) to use for the request. Multiple
scopes must be separated by a space. If not set, the following scopes
will be used:</p>
<p>- https://www.googleapis.com/auth/admin.directory.user</p>
<p>- https://www.googleapis.com/auth/admin.directory.group</p></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
<th></th>
</tr>
<tr class="odd">
<th><p>Store headers</p></th>
<th><p>Optional</p></th>
<th><p>When set, result and request headers will be stored in workflow
arguments.</p>
<p>Requires the setting <strong>Argument result prefix</strong>. Headers
will be stored as:</p>
<p>Response:</p>
<p>- Argument name : [Result Prefix][Header key]</p>
<p>- Argument value  : [Header value]</p>
<p>Request:</p>
<p>- Argument name : [Result Prefix]Request[Header key]</p>
<p>- Argument value  : [Header value]</p></th>
</tr>
<tr class="header">
<th><p>Store HTTP statuscode</p></th>
<th><p>Optional</p></th>
<th><p>When set, the result statuscode will be stored in a workflow
argument.</p>
<p>Requires the setting <strong>Argument result prefix.</strong>
Statuscode will be stored as:</p>
<p>Response:</p>
<p>- Argument name : [Result Prefix]StatusCode</p>
<p>- Argument value  : [statuscode]</p></th>
</tr>
<tr class="odd">
<th><p>Store body</p></th>
<th><p>Optional</p></th>
<th><p>When set, the result and request body will be stored in a
workflow argument.</p>
<p>Requires the setting <strong>Argument result prefix</strong>. Body
will be stored as:</p>
<p>Response:</p>
<p>- Argument name : [Result Prefix]Body</p>
<p>- Argument value  : [HTTP body]</p>
<p>Request:</p>
<p>- Argument name : [Result Prefix]RequestBody</p>
<p>- Argument value  : [HTTP body]</p></th>
</tr>
<tr class="header">
<th><p>Result prefix</p></th>
<th><p>Optional</p></th>
<th><p>The result prefix for above store settings</p></th>
</tr>
</thead>
&#10;</table>

### SendEmail

Sends a notification using an SMTP server. The notification should be
present in the workflow content.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The notification was succesfully sent</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during send.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Host</p></th>
<th><p>Required</p></th>
<th><p>Hostname of the SMTP server</p></th>
</tr>
<tr class="header">
<th><p>Port</p></th>
<th><p>Required</p></th>
<th><p>SMTP Port on the SMTP server</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th><p>Optional</p></th>
<th><p>A username to authenticate with on the SMTP server</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th><p>Optional</p></th>
<th><p>Password of above username</p></th>
</tr>
<tr class="odd">
<th><p>EnableSSL</p></th>
<th><p>Optional</p></th>
<th><p>Use SSL or not</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Toastr

Sends a toastr to the frontend. By default the toastr will be send to
the user initiating the workflow action button.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Done</td>
<td>When the activity is fisnished</td>
</tr>
</tbody>
</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td>Required</td>
<td>The type of toastr which will be send</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Optional</td>
<td>The title to show in the toastr</td>
</tr>
<tr class="odd">
<td>Message</td>
<td>Required</td>
<td>The message to show in the toastr. Data lookup and functions
supported.</td>
</tr>
<tr class="even">
<td>Show to admins</td>
<td></td>
<td>When selected the toastr will be send to all the admin users instead
of the initiating workflow action user</td>
</tr>
<tr class="odd">
<td>Add to history</td>
<td></td>
<td>When selected the toastr notification will be saved in the
notification panel</td>
</tr>
<tr class="even">
<td>Show permanent</td>
<td></td>
<td>When selected the toastr will not have a timeout and will be on the
screen until the user removed it</td>
</tr>
</tbody>
</table>

### TreeManagerAttributeValue

Retrieves the value of a TreeManager attribute for a specified node

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The value was succesfully retrieved, and stored in the following
argument(s):</p>
<p>- TmResolvedValue à Single value result</p>
<p>- TmResolvedValues à Multiple values</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred while retrieving the value.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Base URI</p></th>
<th><p>Required</p></th>
<th><p>URL of the TreeManager API</p></th>
</tr>
<tr class="header">
<th><p>API key</p></th>
<th><p>Required</p></th>
<th><p>API key</p></th>
</tr>
<tr class="odd">
<th><p>API password</p></th>
<th><p>Required</p></th>
<th><p>Password of above API key</p></th>
</tr>
<tr class="header">
<th><p>Node Id</p></th>
<th><p>Required</p></th>
<th><p>The node for which to retrieve the value. Data lookup and
functions supported. May contain:</p>
<p>- Id</p>
<p>- ExternalId</p>
<p>- ExternalKey</p></th>
</tr>
<tr class="odd">
<th><p>Attribute ID</p></th>
<th><p>Required</p></th>
<th><p>The attribute Id for which to retrieve the value. Data lookup and
functions supported</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Update

Updates on or more properties on the specified resource.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The property was succesfully updated</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during the update.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Argument</p></th>
<th><p>Optional</p></th>
<th><p>The argument which contains the object to update. When left
empty, the object present in workflow content will be used.</p></th>
</tr>
<tr class="header">
<th><p>Content type</p></th>
<th><p>Required</p></th>
<th><p>The object type of the object to update</p></th>
</tr>
<tr class="odd">
<th><p>Property</p></th>
<th><p>Required</p></th>
<th><p>The property to update</p></th>
</tr>
<tr class="header">
<th><p>Value</p></th>
<th><p>Required</p></th>
<th><p>The new value for the property. Data lookup and functions
supported</p></th>
</tr>
<tr class="odd">
<th><p>Allow validation errors on save</p></th>
<th><p>Optional</p></th>
<th><p>If set, object validations will not take place when saving the
entity. Use with caution because data inconsistencies may be
introduced</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### WithdrawAssets

Creates withdraw dossiers for all assets of the specified iDossier.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The activity was succesfully executed.</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during execution.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>IDossier argument</p></th>
<th><p>Optional</p></th>
<th><p>The argument whicht contains the iDossier. When left empty, the
iDossier in the workflow content will be used.</p></th>
</tr>
<tr class="header">
<th><p>IDossierIdmNumber</p></th>
<th><p>Optional</p></th>
<th><p>The idmnumber to use. If not given the Idmnumber of the IDossier
will be used.</p></th>
</tr>
<tr class="odd">
<th><p>IDossierId</p></th>
<th><p>Optional</p></th>
<th><p>The IDossier ID to use. If not given the ID of the IDossier will
be used.</p></th>
</tr>
<tr class="header">
<th><p>Verwerk automatische aangemaakte</p></th>
<th><p>Required</p></th>
<th><p>Should automatically assigned assets be withdrawn?</p></th>
</tr>
<tr class="odd">
<th><p>Verwerk handmatig aangemaakte</p></th>
<th><p>Required</p></th>
<th><p>Should manually assigned assets be withdrawn?</p></th>
</tr>
<tr class="header">
<th><p>AanvraagDossier status</p></th>
<th><p>Required</p></th>
<th><p>The status for the withdraw dossiers</p></th>
</tr>
<tr class="odd">
<th><p>AanvraagDossierProduct status</p></th>
<th><p>Required</p></th>
<th><p>The status for the withdraw dossier products</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p><strong>Result Parameters</strong></p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>WithdrawnApplicationDossierProducts</p></th>
<th><p>All the created ApplicationDossierProducts in withdrawn
dossiers</p></th>
</tr>
</thead>
&#10;</table>

### SMTPMessage

This activity sends an email message using the specified mailserver.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The activity was succesfully executed.</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during execution.</p>
<p>The error description is added to the
<strong><em>Reason</em></strong> argument.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Hostname</p></th>
<th><p>Required</p></th>
<th><p>The DNS name or IP address of the SMTP server</p></th>
</tr>
<tr class="header">
<th><p>Port</p></th>
<th><p>Required</p></th>
<th><p>The port to use on the SMTP server (usually 25 for non-encrypted
connections)</p></th>
</tr>
<tr class="odd">
<th><p>EnableSSL</p></th>
<th><p>Required</p></th>
<th><p>Wether or not to use SSL to secure the communcations with the
mailserver</p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p>Optional</p></th>
<th><p>A username to authenticatie to the SMTP server</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p>Optional</p></th>
<th><p>Password for above username</p></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><p>From</p></th>
<th><p>Required</p></th>
<th><p>E-mailaddress of the sender. This field may contain data
resolution and functions.</p></th>
</tr>
<tr class="header">
<th><p>TO</p></th>
<th><p>Required</p></th>
<th><p>E-mailaddress of the recipient. This field may contain data
resolution and functions.</p></th>
</tr>
<tr class="odd">
<th><p>CC</p></th>
<th><p>Optional</p></th>
<th><p>E-mailaddress of carbon-copy recipient. This field may contain
data resolution and functions.</p></th>
</tr>
<tr class="header">
<th><p>BCC</p></th>
<th><p>Optional</p></th>
<th><p>E-mailaddress of blind carbon-copy recipient. This field may
contain data resolution and functions.</p></th>
</tr>
<tr class="odd">
<th><p>Subject</p></th>
<th><p>Optional</p></th>
<th><p>The subject of the message. This field may contain data
resolution and functions.</p></th>
</tr>
<tr class="header">
<th><p>Message</p></th>
<th><p>Required</p></th>
<th><p>The body of the message (the mail message). This field may
contain data resolution and functions.</p></th>
</tr>
<tr class="odd">
<th><p>Message contains HTML</p></th>
<th><p>Optional</p></th>
<th><p>True to create a valid HTML formatted message</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### FileSystem

This activity can perform various filesystem operations. A custom
username and password is required when not running in Azure to prevent
abuse of the IBIS service account.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The activity was succesfully executed</p>
<p><strong><em>OR</em></strong></p>
<p>In case the action is <strong>FolderOrFileExists</strong>, the folder
or file exists</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during execution. The error description is
added to the <strong><em>Reason</em></strong> argument.</p>
<p><strong><em>OR</em></strong></p>
<p>In case the action is FolderOrFileExists, the folder or file does not
exist</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Action</p></th>
<th><p>Required</p></th>
<th><p>- <strong>FolderCreate</strong></p>
<p><em>Create a new folder</em></p>
<p>- <strong>FolderDelete</strong></p>
<p><em>Delete a folder</em></p>
<p>- <strong>FolderMove</strong></p>
<p><em>Move a folder to another location</em></p>
<p>- <strong>FileCreateOrOverwrite</strong></p>
<p><em>Create a new file, overwrite any existing file</em></p>
<p>- <strong>FileCreateOrAppend</strong></p>
<p><em>Create a new file, append if the file already exists</em></p>
<p>- <strong>FileMove</strong></p>
<p><em>Move a file to another location</em></p>
<p>- <strong>FileDelete</strong></p>
<p><em>Delete a file</em></p>
<p>- <strong>FileReadAll</strong></p>
<p><em>Read the contents of a file to an argument (string)</em></p>
<p>- <strong>FileReadAllLines</strong></p>
<p><em>Read the contents of a file to an argument (array)</em></p>
<p>- <strong>FolderOrFileExists</strong></p>
<p><em>Returns success if the specified file or folder exists</em></p>
<p>- <strong>GetTempfileName</strong></p>
<p><em>Returns the full path and filename of a temporary
file</em></p></th>
</tr>
<tr class="header">
<th><p>Argument</p></th>
<th><p>Conditional</p></th>
<th><p>Required for <strong>GetTempfileName</strong>,
<strong>FileReadAll</strong> and
<strong>FileReadAllLines</strong></p></th>
</tr>
<tr class="odd">
<th><p>SourcePath</p></th>
<th><p>Conditional</p></th>
<th><p>The full path of the source file or folder</p></th>
</tr>
<tr class="header">
<th><p>DestinationPath</p></th>
<th><p>Conditional</p></th>
<th><p>The full path of the destination file or folder</p></th>
</tr>
<tr class="odd">
<th><p>Content</p></th>
<th><p>Not required</p></th>
<th><p>The content to write to file when using
<strong>FileCreateOrOverwrite</strong> or
<strong>FileCreateOrAppend</strong>. The value of this setting may
contain placeholders</p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p>Required</p></th>
<th><p>The username of the account used to perform the filesystem
action</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p>Required</p></th>
<th><p>The password of above username</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ParseJson

This activity can parse a JSON string into an object, so it can be used
with the data resolution functions.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The activity was succesfully executed, and the object is stored
in the destination argument. Propertyvalues from this object can be
accessed like:</p>
<p>- {@<em>targetArgumentName</em>.property}</p>
<p>- {@<em>targetArgumentName</em>.property.property}</p>
<p>- {@<em>targetArgumentName</em>.property.property.property}</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>The activity failed, either because of a configuration error or
an invalid JSON file. The exact reason is added to the workflow argument
@Reason.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>SourceArgument</p></th>
<th><p>Required</p></th>
<th><p>The name of the workflow argument which contains the JSON
string</p></th>
</tr>
<tr class="header">
<th><p>DestinationArgument</p></th>
<th><p>Required</p></th>
<th><p>The name of the workflow argument in which to store the parsed
object</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### PowerShellDecision

Executes the specified PowerShell script and continues down the True of
False path based on the script output.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>True</p></th>
<th><p>The script returned a ReturnValue of 'True'</p></th>
</tr>
<tr class="header">
<th><p>False</p></th>
<th><p>The script returned a ReturnValue of 'False'</p></th>
</tr>
<tr class="odd">
<th><p>Error</p></th>
<th><p>An error occurred during script execution. The error message is
in the error log and in the workflow argument 'PowerShellError'</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Agent</td>
<td></td>
<td>If set, the script will be executed on this PowerShell agent</td>
</tr>
<tr class="even">
<td>Hostname</td>
<td></td>
<td>If set, the script will be executed on this server</td>
</tr>
<tr class="odd">
<td>Username</td>
<td><strong>X</strong></td>
<td>The username of the account to use for executing the script</td>
</tr>
<tr class="even">
<td>Password</td>
<td><strong>X</strong></td>
<td>The password of above username</td>
</tr>
<tr class="odd">
<td>Script</td>
<td><strong>X</strong></td>
<td><p>The script to execute</p>
<p>The script must return an object with a boolean 'ReturnValue'
property. Curly braces must be escaped using a '\'. For example:</p>
<p>if ([int]{_16_99_Dossier_Status} -eq 0) \{ return New-Object PSObject
-Property (@\{ReturnValue=$true\}) \} else \{ New-Object PSObject
-Property (@\{ReturnValue=$false\}) \}</p></td>
</tr>
</tbody>
</table>

### ExecuteIbisConnector

This activity can execute an IBIS Connector operation or runprofile.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Results</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Success</p></th>
<th><p>The operation or runprofile was successfully executed</p></th>
</tr>
<tr class="header">
<th><p>Failure</p></th>
<th><p>An error occurred during execution. The reason is added to the
workflow argument @Reason.</p></th>
</tr>
</thead>
&#10;</table>
<br><br>
<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Configuration</th>
<th>Required?</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>RunProfile</p></th>
<th><p>The runprofile to execute</p></th>
<th></th>
</tr>
<tr class="header">
<th><p>Connector</p></th>
<th><p>The connector to execute</p></th>
<th></th>
</tr>
<tr class="odd">
<th><p>Operation</p></th>
<th><p>The operation to execute on the connector</p></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
