# IBIS-suite Release Notes 5.3
## New features

### Universal search

Universal Search has been implemented. With Universal Search it's
possible to find items in IBIS faster. Results from the Universal Search
will be respecting the authorization settings.
The Universal Search relies on indexes which will be implemented per
type.
The function is implemented for the following object types:

- Employee registrations (IDossiers)
- Identity registrations (IdentityDossiers)
- User account registrations (AliasDossiers)
- Access card registrations (PbsDossiers)
- Legal ID-document scan registrations (WidDossiers)
- facility registrations (FmhDossiers)
- Telephone guide registrations (TgDossiers)
- Product requests (AanvraagDossiers)
- Group registrations (Group)
- EPIC registrations (EpicDossier)



### New configuration pages

New configuration pages have been added to replace the old ones
with an improvement in usability and look-and-feel. All these pages can
now be accessed by clicking on the ‘All pages’ button in the navigation
menu:

- Password Module settings*
- Background tasks settings
- Pages settings*
- Audit entry settings*
- CSS, Javascript module settings*
- Export/import IBIS configuration*
- Localisation settings
- Cryptography settings*

*These are no longer available in the /admin. As a result,
permissions can be added using ACL so that they’re no longer only
limited to only administrators.

### Registration pages
The following new registration pages has been added:

- Telephone guide registration (TgDossier)
- Group registration (Group)


### Changelog
IBIS changes can now be viewed in the new Changelog page. The proper
authorizations need to be set to access the page.

### NetIQ eDirectory Connector
IBIS can now connect to NetIQ eDirectory.
The eDirectory module is capable of importing and exporting data to
NetIQ eDirectory by using the LDAP protocol. Simply go to "Connectors",
add a new connector and select "NetIQ eDirectory". For more information
about using this connector, please obtain the latest version of the IBIS
Connector documentation.


### Add Dynamic attributes to existing objects and dossiers
The IBIS-datamodel can now be extended using "dynamic fields" for a
better support of your Joiner, Mover and Leaver process. When added,
these "dynamic fields" can be used in registration forms, workflows
(Argument, Decision, HasResult), DataSets and IBIS connectors.

### Group management
In previous versions of the IBIS suite, IBIS could only manage
the lifecycle of user accounts and manage user access based on
ABAC-rules. In a Microsoft environment, access is often given when the
user account of an employee is member of a certain AD-group. For access
management, IBIS managed only the “members” attribute of the
AD-group.
<br><br>Creation and maintaining AD-groups were always done manually using
ADUC or the IDM Admin tool (Trusted-ID's web-based version of ADUC).<br><br>
Groups can now be created and managed from IBIS. Groups are fully
integrated into the IBIS suite. Please note that Groups are generic and
not Microsoft AD-specific.<br><br>
Added to the IBIS AD Connector: Group objects are now supported. IBIS
can create and manage AD Groups based on the new Group registration
option in IBIS. Only non-multivalued attributes are supported. The
multivalued "members" attribute will be managed by ABAC.<br><br>
The managed groups are automatically added to the IBIS register and
are indexed by the Universal Search.

### New Widscan / form post catcher
External systems (like BPI’s passport scanner) could “post” data
to an employee registration using a HTTP POST message to the
(deprecated) page InvoerFormulier.aspx.<br><br>
To support this feature in the near future a more generic solution
has been created. A new entrypoint has been created to accommodate the
HTTP POST message and redirecting the “posted” data to the new
registration page. This new entrypoint supports all available
fields/attributes of the registration page, and for backward
compatibility, also the fixed attributes from BPI’s passport
scanner.<br><br>
In cases where BPI’s ID document scanner is used with IBIS, the BPI
software has to be reconfigured to the new entrypoint URL


### IC: Connector module voor TreeManager
IBIS can now connect to TreeManager using IBIS Connector. The
TreeManager connector is capable of importing nodes from- and exporting
nodes to a TreeManager tree. For more information about using this
connector, please obtain the latest version of the IBIS Connector
documentation.
<p><img src="image1_2.png" /></p></td>


## Features update

### Registration pages
The following new registration pages has been updated:

- Employee registration (iDossier)
- Identity registration (IdentityDossier)
- User account registration (AliasDossier)
- Access card registration (PbsDossier)
- Facility management registration (FmhDossier)
- Legal ID-document scan registration (WidDossier)
- Product request (AanvraagDossier)
- Epic registration (EpicDossier)

Enhancements:

- In the new registration page you can open the Workflow Execution History. You can find this under the "Option" menu.
- Metadata fields in the new registration page are read-only from
now on: 
    - CreatedDate 
    - ModifiedDate 
    - CreatedBy 
    - ModifiedBy
- In the new employee registration form, the "location" selector
has been added. When configured, selecting a location will fill the
corresponding address fields.
- In the new employee registration form, when address fields are
configured, the postal code field will trigger a lookup for the
corresponding address and fill the address fields when found. Please
note that the postal code table in the database must be populated with
postal code data. Ask your implementation consultant for more
information.
- The new registration page has an additional option to delete the
registration. This option can be found under the "Options" button.
Please note the following: 
    - In order to enable this option you need to have the "delete" access right. This can be set in the authorization tree. 
    - Actual deletion of the registration will be recorded in the Auditlog. 
    - The deletion of the registration will not trigger a cascade of deletions of depending objects. If this is needed, create a custom Workflow to handle this. 
    - After deletion, IBIS will go back to the page prior to the registration.
- We will stop using the term "dossier". For example:
"Dossierhistory" will be renamed to "History". This will be changed
throughout the entire UI of the suite. The schema in the database will
not be affected for now.

### Workflow enhancements</h3></th>
- Function contains has been added to the workflow engine
    
    *The Workflow "contains" Function has been added. Use this
    function to check whether a text exists. Example:*

    *{?{IncomingValue},contains(SearchText)}*
- The iDossier organization attribute is no more required for the
Workflow AliasDossierActivity\

    *The AliasDossier Workflow Activity for generating user account
    registrations has been changed to cope with implementations that do not
    have organizational data. An extra
    "IgnoreOrganizationMandatoryValidation" option has been added (default
    set to false). Set this option to true to skip the organization
    validation.*
- The background color of the workflow Log activity has been
changed

    *Changed color for Log activities in workflow designer.*
- UTC function has been added to the workflow engine.

    Example: {?{IncomingValue},ToUniversalTime} 
- UTC FileTime function has been added to the workflow engine.<br />
    Example: {?{IncomingValue},ToFileTimeUtc} 

### UI/UX Enhancements
- User TimeZone added

    The user can set the preferred timezone. Go to the user settings (top
    right of the screen) and click on the "Timezone" dropdown to list
    available timezones. Select one and save the user settings.
- Realtime Synchronization triggers in IBIS Connectors. By default,
the connector only synchronizes and exports data when either manually
triggered or called from a runprofile. Enable this option to trigger
realtime synchronization and export of a single object when the value of
this attribute is changed in IBIS. On synchronization/export, the
complete object is evaluated and exported, thus not only this
attribute.
- Contents of HTML reports created by the Reporting functionality
can be filtered in the HTML report itself. When opening an HTML report
the filter can be found at the header of the report.
- IBIS Connectors: Multiple export flows using the same source
expression were blocked by a validation. This has been fixed.
- IBIS queue: the grid can now be sorted by clicking on the column
headers
- All standard UI grids (for the new UI pages) now show the total of
records next to the paging buttons.


### Process and performance enhancements

- For all Connectors: IDM number lookup retry. In previous
versions, when the IDM number lookup has been defined when importing
data to IBIS, the connector tries to lookup the IDM number once
based on the given lookup criteria. If there is no match the lookup will
not be triggered again, even when the source data has been changed and a
match <u>could</u> occur based on the given lookup criteria. In this
release the IDM number will be triggered again when the IDM number
wasn’t found earlier.
- Formatted name fields are implemented on FMH, EPIC and PBS
registrations. These fields are not filled automatically. 
    - _42_37_Persoon_EffectieveAchternaam 
    - _42_38_Persoon_EffectieveVoorvoegsels 
    - _42_39_Persoon_EffectieveAchternaamInclusiefVoorvoegsels
- Stability improvements of the OData MA.
- IBIS Connectors provisioning mode will be more specific, inbound
or outbound. If both inbound and outbound provisioning is needed for the
same connected systemen, two separate (one for inbound provisioning, one
for outbound provisioning) IBIS Connectors must be deployed.
- All dossier object types now have a “IsValid” property based on
the start and end date of the record.
- Stability improvements of the Connector Agents
- Changes on Access Card registrations (used for card management)
are now eligible for audit logging. To turn this feature on go to the
Audit configuration page.


### Security

- Live logger is now only available for IBIS
Administrators.

## Bugfixes

| Referentie | Bug fix |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11125      | When deploying a new IBIS suite where schema names are used, the reference to the IBIS log table (found in General Settings) should also use the schema name. |
| 11505      | Fixed an issue in the SysInputFieldCleaner cleanup task                                                                                                       |
| 11535      | Fixed an issue where sending the loginid back to Youforce did not work properly in the Youforce connector                                                     |
| 11568      | After ACL Sync do a refresh of the settings and the cache                                                                                                     |
| 11607      | Removed the name “Dossier” from "All Pages"                                                                                                                   |
| 11642      | Fixed an issue where Addtime function would not work properly with max datetime 31-12-9999                                                                    |
| 11643      | Fixed an issue where ‘Startdate’ and ‘Needed until’ from dependent products had different values in applicationdossiers                                       |
| 11645      | Fixed an issue in the DecisionActivity for a nullable DateTime error                                                                                          |
| 11646      | Fixed an issue where the Run Profiles order were not saved correctly                                                                                          |
| 11667      | Fixed an issue where FillLocationFromTreeManager would not properly delete locations                                                                          |
| 11714      | Fixed an issue where a casting error would occur when running a connector sequence DI+S+E+S                                                                   |
