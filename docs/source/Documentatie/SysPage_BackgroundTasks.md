# <span id="index"></span>Background tasks

IBIS uses Hangfire to schedule and trigger background tasks. The
hangfire dashboard is available for members of an administrator role at
~/hangfire

-   [AanvraagDossierMailConsumer](#AanvraagDossierMailConsumer)
-   [DetermineDataSetInOut](#DetermineDataSetInOut)
-   [FetchTreeManagerOrganizations](#FetchTreeManagerOrganizations)
-   [ProcessApplicationDossierProducts](#ProcessApplicationDossierProducts)
-   [SyncAuthorisations](#SyncAuthorisations)
-   [UpdateIDossierLocations](#UpdateIDossierLocations)
-   [WorkflowTimer](#WorkflowTimer)

The following tasks run in the background by default and cannot be
altered:

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Task</th>
<th>Interval</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="207"><p>System_CleanupData</p></td>
<td width="77"><p>Every hour</p></td>
<td width="340"><p>Responsible for audit-trail en logentry
cleanup</p></td>
</tr>
<tr class="even">
<td width="207"><p>System_AuthorizationObjectsManager</p></td>
<td width="77"><p>Every hour</p></td>
<td width="340"><p>Responsible for synchronizing authorizable API
objects between the domain and the database</p></td>
</tr>
<tr class="odd">
<td width="207"><p>System_AclSyncManager</p></td>
<td width="77"><p>Every hour</p></td>
<td width="340"><p>Responsible for synchronizing authorizable objects
and ACLs between IBIS and TreeManager</p></td>
</tr>
</tbody>
</table>

### Create a new task

Perform the following steps to create a new task. After creation, the
new task will be scheduled using hangfire and run at the configured
interval.

1.  Go to ~/BackgroundTask
2.  Click the **Add scheduled task** button in the top left corner. An
    overlay/sidepanel will be shown
3.  Select the Name of the background task (the 'parameters' tab will
    appear relevant for this task)
4.  Enter a name
5.  Enter a description
6.  Enter a valid CRON schedule
7.  Click on the 'Parameters' tab
8.  Fill in the parameter fields belonging to the selected task
9.  Save and close settings

### Run a task on demand

Background tasks can run on demand. To do this:

1.  Go to ~/BackgroundTask
2.  Click the hamburger (options) menu behind a task, select one of the
    following options
    1.  Run (asynchronous): The task will be executed in the background
    2.  Run (synchronous) : The task will be executed in the user
        process

### Change task interval

In some environments the default interval for a task is not sufficient.
In that case it can be changed manually. To achieve this:

1.  Go to ~/BackgroundTask
2.  Edit the task by opening the hamburger menu behind the task and
    clicking on the **Modify scheduled task** button
3.  Change the value of the Schedule (cron) field to a valid CRON value.
    Take a look at
    [https://crontab-generator.org](https://crontab-generator.org/) for
    examples
4.  Save and close settings

### Delete a task

Perform the following steps to delete a background task:

1.  Go to ~/BackgroundTask
2.  Click the hamburger (options) menu behind a task
3.  Click the 'Delete scheduled task' option
4.  In the popup window, confirm your choice by clicking on 'Delete
    scheduled task'

## Available tasks

#### <span id="AanvraagDossierMailConsumer"></span>AanvraagDossierMailConsumer

This task is responsible for processing applicationdossier / asset
request mails in the mailbox

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="255"><p>MailConsumerArchiveFolder</p></td>
<td width="368"><p>Name of the folder in which to place processed e-mail
items.</p>
<p>If unset (empty), processed e-mails will be deleted</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerDefaultFolder</p></td>
<td width="368"><p>Name of the folder which contains e-mail items to
process</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerExchangeVersion</p></td>
<td width="368"><p>Specifies which server of Exchange is running. Choose
from the following options:</p>
<p>· Exchange2007_SP1</p>
<p>· Exchange2010</p>
<p>· Exchange2010_SP1</p>
<p>· Exchange2010_SP2</p>
<p>· Exchange2013</p>
<p>· Exchange2013_SP1</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerForwardDefaultMailAdres</p></td>
<td width="368"><p>An e-mail address to forward e-mails to that cannot
be processed</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerMailAdres</p></td>
<td width="368"><p>Specifies the mailbox to use for processing</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerMailBoxPassword</p></td>
<td width="368"><p>The password of above username</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerMailBoxUserId</p></td>
<td width="368"><p>The username used to sign in the mail server</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerMailNumberOfMails</p></td>
<td width="368"><p>The number of e-mail messages to process during each
run</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerMailServerDomain</p></td>
<td width="368"><p>The domain in which the Exchange server is
running</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerMailServerPort</p></td>
<td width="368"><p>Specifies the port to use when connecting to a
POP/IMAP server</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerMailServerUrl</p></td>
<td width="368"><p>Specifies the URL of the mail server, for
example:</p>
<p>§ pop.gmail.com</p>
<p>§ imap.gmail.com</p>
<p>§ https://domain.tld/EWS/exchange.asmx</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerServerType</p></td>
<td width="368"><p>Defines the type of mailserver which is used
(Exchange, IMAP, POP)</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerUseDefaultCredentials</p></td>
<td width="368"><p>If enabled, Exchange will be contacted using the
credentials of the service account, otherwise the username/password
above will be used</p></td>
</tr>
<tr class="even">
<td width="255"><p>MailConsumerUsePlainText</p></td>
<td width="368"><p>Force reading the plain-text version of an
e-mail</p></td>
</tr>
<tr class="odd">
<td width="255"><p>MailConsumerUseSsl</p></td>
<td width="368"><p>If enabled, SSL will be used when connecting to a
POP/IMAP server</p></td>
</tr>
</tbody>
</table>



#### <span id="DetermineDataSetInOut"></span>DetermineDataSetInOut

This task is responsible for evaluating datasets, and triggering
workflow events on dataset changes.

The scheduling of this task depends on the IBIS configuration and
business needs. If your IBIS configuration does not contain any datasets
this task is not needed.



#### <span id="FetchTreeManagerOrganizations"></span>FetchTreeManagerOrganizations

This task is responsible for synchronizing the TreeManager organization
tree to the IBIS organization table. The task has the ability to process
optional attribute/property mappings.

The following general settings need to be set in order for this task to
run succesfully:

-   TreeManager / Service URL
-   TreeManager / API Key
-   TreeManager / Password
-   Organization / TreeManager operational organization id

By default, the following properties are synchronized between a
TreeManager organization

and an IBIS organization:

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>TreeManager node</th>
<th>IBIS organization</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="198"><p>Id</p></td>
<td width="425"><p>ID</p></td>
</tr>
<tr class="even">
<td width="198"><p>ExternalKey</p></td>
<td
width="425"><p>_04_20_Organisatie_IdentificatieOperationeleOrganisatie</p></td>
</tr>
<tr class="odd">
<td width="198"><p>DateCreated</p></td>
<td width="425"><p>_04_40_Organisatie_DatumIngangGeldigheid</p></td>
</tr>
<tr class="even">
<td width="198"><p><em>9999-12-31</em></p></td>
<td width="425"><p>_04_41_Organisatie_DatumEindeGeldigheid</p></td>
</tr>
<tr class="odd">
<td width="198"><p>+</p></td>
<td width="425"><p>_04_30_Organisatie_Naam</p></td>
</tr>
<tr class="even">
<td width="198"><p>[parent organization].ExternalKey</p></td>
<td
width="425"><p>_04_16_Organisatie_IdentificatieOperationeleOrganisatieBovenliggend</p></td>
</tr>
</tbody>
</table>

Besides the default mappings, custom mappings can be configured. In
order to do this, alter the task configuration through
~/Tasks/TaskRunner.aspx according to the table below.

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="121"><p>DeltaDateTimeOffset</p></td>
<td width="60"><p>No</p></td>
<td width="443"><p>Give a negative number of hours to get the delta’s
from.</p></td>
</tr>
<tr class="even">
<td width="121"><p>MappingsJson</p></td>
<td width="60"><p>no</p></td>
<td width="443"><p>A JSON string which contains the TreeManager
attribute / organization property mappings. Below is an example of such
a string. Lookup attributes are described in the next table</p>
<p>--- START OF JSON STRING, DO NOT INCLUDE THIS LINE ---</p>
<p>[</p>
<p>{</p>
<p>"AttributeId":"02653f8a-8a2e-4825-8a3d-71af218f0d77",</p>
<p>"OrganizationProperty":"_14_05_Kostenplaats_Budgethouder"</p>
<p>},</p>
<p>{</p>
<p>"AttributeId":"21f14293-e4b1-4d6b-a707-a80b69b0ac71",</p>
<p>"OrganizationProperty":"_04_05_Organisatie_IdmNummerManager",</p>
<p>"Lookup": true,</p>
<p>"LookupTargetType": "IDossier",</p>
<p>"LookupSearchProperty":
"_42_08_Persoon_IdentificatieBronsysteem",</p>
<p>"LookupResultProperty": "_42_01_Persoon_IdmNummer"</p>
<p>},</p>
<p>{</p>
<p>"AttributeId":"45b1401a-72eb-46cc-b329-b3a0ea074919",</p>
<p>"OrganizationProperty":"_04_92_Organisatie_IsEenPersoneelsgebied"</p>
<p>}</p>
<p>]</p>
<p>--- END OF JSON STRING, DO NOT INCLUDE THIS LINE ---</p></td>
</tr>
<tr class="odd">
<td width="121"><p>IgnoreValidationErrors</p></td>
<td width="60"><p>no</p></td>
<td width="443"><p>If set, any validation errors that occur during save
will be ignored</p></td>
</tr>
<tr class="even">
<td width="121"><p>AlwaysForceFull</p></td>
<td width="60"><p>No</p></td>
<td width="443"><p>If set, the task will always perform a Full instead
of a Delta run.</p></td>
</tr>
</tbody>
</table>

As you can see in the table above, a mapping can perform a lookup. This
way the property of an IBIS object can be used instead of the
TreeManager property. To do this, configure the mapping with a lookup
according to the table below (see previous table for an example).

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
<td width="151"><p>Lookup</p></td>
<td width="472"><p>If set to true, a lookup will be performed</p></td>
</tr>
<tr class="even">
<td width="151"><p>LookupTargetType</p></td>
<td width="472"><p>The type of IBIS object to search for, for
example:</p>
<p>§ IDossier</p>
<p>§ AliasDossier</p>
<p>§ IdentityDossier</p></td>
</tr>
<tr class="odd">
<td width="151"><p>LookupSearchProperty</p></td>
<td width="472"><p>The name of the property whose value should be
compared to the incoming TreeManager value. In case the values match,
the first object with a match will be returned</p></td>
</tr>
<tr class="even">
<td width="151"><p>LookupResultProperty</p></td>
<td width="472"><p>The name of the property of which the value should be
returned</p></td>
</tr>
</tbody>
</table>



#### <span id="ProcessApplicationDossierProducts"></span>ProcessApplicationDossierProducts

This task is responsible for processing products of applicationdossier
/asset request and sends the requests to the suppliers


#### <span id="SyncAuthorisations"></span>SyncAuthorisations

Syncs ACL's from Treemanager to IBIS, push configurations from IBIS to
Treemanager


#### <span id="UpdateIDossierLocations"></span>UpdateIDossierLocations

Update all iDossier work adresses with adresses from locations



#### <span id="WorkflowTimer"></span>WorkflowTimer

This task is responsible for executing workflow timer events. If your
IBIS configuration does not contain workflows with Timer events, this
task is not needed.

The recommended schedule for this task is every 1 minute (Cron: \* \* \*
\* \*).


  
