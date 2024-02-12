# IBIS-suite Release Notes 5.3 (fixed)
## New features

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="universal-search" class="unnumbered">Universal
search</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Universal Search has been implemented. With Universal Search it's
possible to find items in IBIS faster. Results from the Universal Search
will be respecting the authorization settings.</p>
<p>The Universal Search relies on indexes which will be implemented per
type.</p>
<p>The function is implemented for the following object types:</p>
<ul>
<li><p>Employee registrations (IDossiers)</p></li>
<li><p>Identity registrations (IdentityDossiers)</p></li>
<li><p>User account registrations (AliasDossiers)</p></li>
<li><p>Access card registrations (PbsDossiers)</p></li>
<li><p>Legal ID-document scan registrations (WidDossiers)</p></li>
<li><p>facility registrations (FmhDossiers)</p></li>
<li><p>Telephone guide registrations (TgDossiers)</p></li>
<li><p>Product requests (AanvraagDossiers)</p></li>
<li><p>Group registrations (Group)</p></li>
<li><p>EPIC registrations (EpicDossier)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="new-configuration-pages" class="unnumbered">New
configuration pages</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New configuration pages have been added to replace the old ones
with an improvement in usability and look-and-feel. All these pages can
now be accessed by clicking on the ‘All pages’ button in the navigation
menu:</p>
<ul>
<li><p>Password Module settings*</p></li>
<li><p>Background tasks settings</p></li>
<li><p>Pages settings*</p></li>
<li><p>Audit entry settings*</p></li>
<li><p>CSS, Javascript module settings*</p></li>
<li><p>Export/import IBIS configuration*</p></li>
<li><p>Localisation settings</p></li>
<li><p>Cryptography settings*</p></li>
</ul>
<p>*These are no longer available in the /admin. As a result,
permissions can be added using ACL so that they’re no longer only
limited to only administrators.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="registration-pages" class="unnumbered">Registration pages
</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The following new registration pages has been added:</p>
<ul>
<li><p>Telephone guide registration (TgDossier)</p></li>
<li><p>Group registration (Group)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="changelog" class="unnumbered">Changelog</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IBIS changes can now be viewed in the new Changelog page. The proper
authorizations need to be set to access the page</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="edirectory-connector" class="unnumbered">eDirectory
Connector</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IBIS can now connect to NetIQ eDirectory.</p>
<p>The eDirectory module is capable of importing and exporting data to
NetIQ eDirectory by using the LDAP protocol. Simply go to "Connectors",
add a new connector and select "NetIQ eDirectory". For more information
about using this connector, please obtain the latest version of the IBIS
Connector documentation.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="add-dynamic-attributes-to-existing-objects-and-dossiers" 
class="unnumbered">Add Dynamic attributes to existing objects and
dossiers</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The IBIS-datamodel can now be extended using "dynamic fields" for a
better support of your Joiner, Mover and Leaver process. When added,
these "dynamic fields" can be used in registration forms, workflows
(Argument, Decision, HasResult), DataSets and IBIS connectors.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="group-management" class="unnumbered">Group
management</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>In previous versions of the IBIS suite, IBIS could only manage
the lifecycle of user accounts and manage user access based on
ABAC-rules. In a Microsoft environment, access is often given when the
user account of an employee is member of a certain AD-group. For access
management, IBIS managed only the “members” attribute of the
AD-group.</p>
<p>Creation and maintaining AD-groups were always done manually using
ADUC or the IDM Admin tool (Trusted-ID's web-based version of ADUC).</p>
<p>Groups can now be created and managed from IBIS. Groups are fully
integrated into the IBIS suite. Please note that Groups are generic and
not Microsoft AD-specific.</p>
<p>Added to the IBIS AD Connector: Group objects are now supported. IBIS
can create and manage AD Groups based on the new Group registration
option in IBIS. Only non-multivalued attributes are supported. The
multivalued "members" attribute will be managed by ABAC.</p>
<p>The managed groups are automatically added to the IBIS register and
are indexed by the Universal Search.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="new-widscan-form-post-catcher" class="unnumbered">New
Widscan / form post catcher</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>External systems (like BPI’s passport scanner) could “post” data
to an employee registration using a HTTP POST message to the
(deprecated) page InvoerFormulier.aspx.</p>
<p>To support this feature in the near future a more generic solution
has been created. A new entrypoint has been created to accommodate the
HTTP POST message and redirecting the “posted” data to the new
registration page. This new entrypoint supports all available
fields/attributes of the registration page, and for backward
compatibility, also the fixed attributes from BPI’s passport
scanner.</p>
<p>In cases where BPI’s ID document scanner is used with IBIS, the BPI
software has to be reconfigured to the new entrypoint URL</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="ic-connector-module-voor-treemanager" class="unnumbered">IC:
Connector module voor TreeManager</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IBIS can now connect to TreeManager using IBIS Connector. The
TreeManager connector is capable of importing nodes from- and exporting
nodes to a TreeManager tree. For more information about using this
connector, please obtain the latest version of the IBIS Connector
documentation.</p>
<p><img src="image1_2.png" /></p></td>
</tr>
</tbody>
</table>

## Features update

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="registration-pages-1" class="unnumbered">Registration
pages</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The following new registration pages has been updated:</p>
<ul>
<li><p>Employee registration (iDossier)</p></li>
<li><p>Identity registration (IdentityDossier)</p></li>
<li><p>User account registration (AliasDossier)</p></li>
<li><p>Access card registration (PbsDossier)</p></li>
<li><p>Facility management registration (FmhDossier)</p></li>
<li><p>Legal ID-document scan registration (WidDossier)</p></li>
<li><p>Product request (AanvraagDossier)</p></li>
<li><p>Epic registration (EpicDossier)</p></li>
</ul>
<p>Enhancements:</p>
<ul>
<li><p>In the new registration page you can open the Workflow Execution
History. You can find this under the "Option" menu.</p></li>
<li><p>Metadata fields in the new registration page are read-only from
now on: * CreatedDate * ModifiedDate * CreatedBy * ModifiedBy</p></li>
<li><p>In the new employee registration form, the "location" selector
has been added. When configured, selecting a location will fill the
corresponding address fields.</p></li>
<li><p>In the new employee registration form, when address fields are
configured, the postal code field will trigger a lookup for the
corresponding address and fill the address fields when found. Please
note that the postal code table in the database must be populated with
postal code data. Ask your implementation consultant for more
information.</p></li>
<li><p>The new registration page has an additional option to delete the
registration. This option can be found under the "Options" button.
Please note the following: * In order to enable this option you need to
have the "delete" access right. This can be set in the authorization
tree. * Actual deletion of the registration will be recorded in the
Auditlog. * The deletion of the registration will not trigger a cascade
of deletions of depending objects. If this is needed, create a custom
Workflow to handle this. * After deletion, IBIS will go back to the page
prior to the registration.</p></li>
<li><p>We will stop using the term "dossier". For example:
"Dossierhistory" will be renamed to "History". This will be changed
throughout the entire UI of the suite. The schema in the database will
not be affected for now.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="workflow-enhancements" class="unnumbered">Workflow
enhancements</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Function contains has been added to the workflow engine</p></li>
</ul>
<p><em>The Workflow "contains" Function has been added. Use this
function to check whether a text exists. Example:
{?{IncomingValue},contains(SearchText)}</em></p>
<ul>
<li><p>The iDossier organization attribute is no more required for the
Workflow AliasDossierActivity</p></li>
</ul>
<p><em>The AliasDossier Workflow Activity for generating user account
registrations has been changed to cope with implementations that do not
have organizational data. An extra
"IgnoreOrganizationMandatoryValidation" option has been added (default
set to false). Set this option to true to skip the organization
validation.</em></p>
<ul>
<li><p>The background color of the workflow Log activity has been
changed</p></li>
</ul>
<p><em>Changed color for Log activities in workflow designer.</em></p>
<ul>
<li><p>UTC function has been added to the workflow engine.</p></li>
</ul>
<p>Example: {?{IncomingValue},ToUniversalTime} </p>
<p>UTC FileTime function has been added to the workflow engine.<br />
Example: {?{IncomingValue},ToFileTimeUtc} </p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="uiux-enhancements" class="unnumbered">UI/UX
Enhancements</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>User TimeZone added</p></li>
</ul>
<p>The user can set the preferred timezone. Go to the user settings (top
right of the screen) and click on the "Timezone" dropdown to list
available timezones. Select one and save the user settings.</p>
<ul>
<li><p>Realtime Synchronization triggers in IBIS Connectors. By default,
the connector only synchronizes and exports data when either manually
triggered or called from a runprofile. Enable this option to trigger
realtime synchronization and export of a single object when the value of
this attribute is changed in IBIS. On synchronization/export, the
complete object is evaluated and exported, thus not only this
attribute.</p></li>
<li><p>Contents of HTML reports created by the Reporting functionality
can be filtered in the HTML report itself. When opening an HTML report
the filter can be found at the header of the report.</p></li>
<li><p>IBIS Connectors: Multiple export flows using the same source
expression were blocked by a validation. This has been fixed.</p></li>
<li><p>IBIS queue: the grid can now be sorted by clicking on the column
headers</p></li>
</ul>
<p>All standard UI grids (for the new UI pages) now show the total of
records next to the paging buttons.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="process-and-performance-enhancements" 
class="unnumbered">Process and performance enhancements</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>For all Connectors: IDM number lookup retry. In previous
versions, when the IDM number lookup has been defined when importing
data to IBIS, the connector tries to lookup the IDM number <u>once</u>
based on the given lookup criteria. If there is no match the lookup will
not be triggered again, even when the source data has been changed and a
match <u>could</u> occur based on the given lookup criteria. In this
release the IDM number will be triggered again when the IDM number
wasn’t found earlier.</p></li>
<li><p>Formatted name fields are implemented on FMH, EPIC and PBS
registrations. These fields are not filled automatically. *
_42_37_Persoon_EffectieveAchternaam *
_42_38_Persoon_EffectieveVoorvoegsels *
_42_39_Persoon_EffectieveAchternaamInclusiefVoorvoegsels</p></li>
<li><p>Stability improvements of the OData MA.</p></li>
<li><p>IBIS Connectors provisioning mode will be more specific, inbound
or outbound. If both inbound and outbound provisioning is needed for the
same connected systemen, two separate (one for inbound provisioning, one
for outbound provisioning) IBIS Connectors must be deployed.</p></li>
<li><p>All dossier object types now have a “IsValid” property based on
the start and end date of the record.</p></li>
<li><p>Stability improvements of the Connector Agents</p></li>
<li><p>Changes on Access Card registrations (used for card management)
are now eligible for audit logging. To turn this feature on go to the
Audit configuration page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h3 id="security" class="unnumbered">Security</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Live logger is now only available for IBIS
Administrators.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Bugfixes

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Referentie</strong></th>
<th><strong>Bug fix</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11125</td>
<td>When deploying a new IBIS suite where schema names are used, the
reference to the IBIS log table (found in General Settings) should also
use the schema name.</td>
</tr>
<tr class="even">
<td>11505</td>
<td>Fixed an issue in the SysInputFieldCleaner cleanup task</td>
</tr>
<tr class="odd">
<td>11535</td>
<td>Fixed an issue where sending the loginid back to Youforce did not
work properly in the Youforce connector</td>
</tr>
<tr class="even">
<td>11568</td>
<td>After ACL Sync do a refresh of the settings and the cache</td>
</tr>
<tr class="odd">
<td>11607</td>
<td>Removed the name “Dossier” from "All Pages"</td>
</tr>
<tr class="even">
<td>11642</td>
<td>Fixed an issue where Addtime function would not work properly with
max datetime 31-12-9999</td>
</tr>
<tr class="odd">
<td>11643</td>
<td>Fixed an issue where ‘Startdate’ and ‘Needed until’ from dependent
products had different values in applicationdossiers</td>
</tr>
<tr class="even">
<td>11645</td>
<td>Fixed an issue in the DecisionActivity for a nullable DateTime
error</td>
</tr>
<tr class="odd">
<td>11646</td>
<td>Fixed an issue where the Run Profiles order were not saved
correctly</td>
</tr>
<tr class="even">
<td>11667</td>
<td>Fixed an issue where FillLocationFromTreeManager would not properly
delete locations</td>
</tr>
<tr class="odd">
<td>11714</td>
<td>Fixed an issue where a casting error would occur when running a
connector sequence DI+S+E+S</td>
</tr>
</tbody>
</table>
