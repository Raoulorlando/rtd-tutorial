# IBIS Suite Release Notes
<details>
<summary>IBIS V5.4 Hotfix 11</summary>

**Opgeloste bugs**

  **Reference**  |**Bug fix**
  |:--------------|:---------------------------------------------------------------|
  |12618           |Opzoek functie naar een bestaande register waarde is hoofdlettergevoelig bij het opslaan van een nieuwe waarde.|
  |12655           |Opzoek functie naar smtp alias is hoofdlettergevoelig bij het toevoegen of wijzigen van een smtp alias|
  |12511           |Wissen van de DataSet laatste verwerkte records is niet mogelijk.
  |12499           |DataSet wordt meerdere keren opgeslagen indien niet gekozen voor de knop "Opslaan" bij het opslaan van een nieuwe dataset.| 
  |12621           |IBIS manager opzoeken geeft een willekeurig manager indien de hoogste manager is bereikt|
  |12558           |IBIS instellingen toont de verkeerde keuze bij standaard AVD aanvraag/intrek status. Zie IBIS instellingen -\> Bedrijfsmiddelen -\> Bedrijfsmiddelen in bezit -\> Standaard AVD status voor product aanvraag **EN** Standaard AVD status voor product intrek                     |
  |12556           |Universal Search Index rebuilder werkt de geïndexeerde gegevens niet goed bij                                                  |
  |12582           |IBIS functie werkt niet indien de input voor de functie de tekst 'code' bevat.                                                 | 
</details>

<details>
<summary>IBIS V5.4 Hotfix 1</summary>

-   **Toegevoegde functionaliteiten:**

    -   IBIS Connector

        > *Makkelijk verplichte velden toevoegen aan attribuut relaties*

-   IBIS Active Directory Connector

    > *account expires als \_param waarde meegeven in plaats van een
    > standaard flow*

-   IBIS Documentatie:

    > *Workflow documentatie opgenomen als helpfile in IBIS. Documentatie is
    > te vinden op <https://ibisurl/help>*

-   **Opgeloste bugs**

    -   11931: SysPages toont autorisatie en delete icoontjes niet
        helemaal rechts

    -   11933: ogging: database login en wachtwoord werken niet voor
        alternatieve settings

    -   11937: Manager wordt niet opgeslagen en niet correct weergegeven

    -   11945: Bij verwijderen van Register unieke waarde wordt er geen
        bevestigingsvraag gesteld

    -   11947: Connector agent disconnect

    -   11948: SMTP alias knoppen kunnen autoriseren (RLv2
        gebruikersaccount)

    -   11950: Staging area geeft soms zwarte masker zonder overlay

    -   11951: Linq statements ondersteungen \'.com\' niet

    -   11967: Pages: toggle knop werkt soms niet vanuit grid

Hotfix 2

-   **Toegevoegde functionaliteiten:**

    -   IBIS Connector modules documentatie opnemen als helpfile in IBIS

-   **Opgeloste bugs**

    -   11980: Dossier verlengen vult verkeerde datums in

    -   11984: IBIS AD Connector: EindDatum interpretatie gaat soms fout
        bij AD Connector (agent).

    > *Let op. Zet voor de installatie van de hotfix de Run Profiles UIT. Na
    > installatie van de hotfix moet op alle connectoren eerst een Sync
    > gedaan worden zodat de Datums in de Staging Area opnieuw geëvalueerd
    > worden. Pas daarna kan een Export gedaan worden naar de aangesloten
    > doelsystemen. Dus nooit gelijk een Export doen na installatie van de
    > hotfix.*

Hotfix 3

-   **Toegevoegde functionaliteiten:**

    -   Performance verbeteringen

Hotfix 5

-   **Toegevoegde functionaliteiten:**

    -   IBIS Connector:

    > *Join functionaliteit mogelijk maken tussen extern systeem en staging
    > area object*

Hotfix 7

-   **Toegevoegde functionaliteiten:**

    -   IBIS-IBIS Connector:

    > *Een nieuwe IBIS Connector waarmee een connectie kan worden gelegd
    > naar een andere IBIS instantie om gegevens te kunnen importeren en
    > exporteren.*
    >
    > *De gegevens*

Hotfix 8

-   **Opgeloste bugs**

    -   12228: De workflow haalt de organisatiegegevens niet op voor
        iDossiers waarbij het veld 02_60 is gevuld.
</details>
<details> 
<summary>IBIS V5.4 Update 1</summary>

## New features


### Documentation                       

 The following documentation are added or updated and can be found in  
 IBIS                                                                  
                                                                       
 -   IBIS Settings                                                     
                                                                       
 -   IBIS Workflow engine                                              
                                                                       
 -   IBIS Connectors                                                   
                                                                       
 -   IBIS functions and data resolutions                               
                                                                       
 -   IBIS API connector                                                
                                                                       
 -   Localization                                                      
                                                                       
 -   Audit configuration                                               
                                                                       
 -   Import / Export IBIS configuration                                
                                                                       
 -   Background tasks                                                  
                                                                       
 -   Cryptography                                                      
                                                                       
 -   Logging                                                           
                                                                       
 Location: Navigation menu \> All pages \> Help Documentation          



### New configuration pages    

 New configuration pages have been added to replace the old ones, with 
 improvements in usability and look-and-feel. The new pages can now be 
 accessed by clicking the 'All pages' button in the navigation menu.   
 The following pages have replaced the old ones:                       
                                                                       
 -   IBIS settings page (formerly know as the 'General settings' page) 
                                                                       
      Navigation menu \> All pages \> IBIS settings                         
                                                                       
 -   DataSets page                                                     
                                                                       
      Navigation menu \> All pages \> Datasets                              
                                                                       
 -   Querylizer have been added to the Reporting page.                 
                                                                       
  	  Navigation menu \> All pages \> Reporting                             

 ![](..\markdown\images\media\image1.png)                                                                      
                                   


## Features update 1


### Registration page enhancements
-   **Option shortcuts** can now be set in the registration page      
    header. To set a shortcut, click on the 'Options' dropdownmenu to 
    show a list of options. Next, hover over an item and click on the 
    star to turn it into a shortcut                                                                 
    ![](..\markdown\images\media\image2.png)       
                                                                      
-   **Field width and offsets** can now be configured individually to 
    create different kinds of registration layouts. To change a field 
    size, go to a registration configuration page (i.e. Configure     
    employee registration). Hover over a field and click on the cog   
    icon. In the sidepanel that opens, make changes to the field      
    width and/or whitespace offsets.                              
                                                                     
    ![](..\markdown\images\media\image3.png)                                  
                                                                   
    Depending on the configuration, layouts for registration pages    
    can be changed dramatically.\                                     
                                                                    
    ![](..\markdown\images\media\image4.png)                   

 ### Workflow enhancements        
 -   Several new functions have been added. These can now be used in   
     the workflow engine and connectors:                               
 -   GetDay: returns the day from a day                                
                                                                       
 -   GetMonth: returns the month from a date                           
                                                                       
 -   GetYear: returns the year from a date                             
                                                                       
 -   IsIndefiniteDate: returns true if the year contains 9999          
                                                                       
 -   GetDate: returns a formatted date.                                
                                                                       
 -   You can now create sorted datasets for the workflow engine. To do 
     this, use the 'Order By' field in a dataset configuration         
                                                                       
 -   The user account linked objects has been expanded. It's now       
     easier to get lists of email aliases from a user account. There   
     are two versions:                                                 
                                                                       
     -   EmailAddresses_IncludingPrimary                               
                                                                       
     -   EmailAddresses                                                
                                                                       
 These are available in the workflow but also in the connectors        



 ### UI/UX Enhancements {#uiux-enhancements .unnumbered}               

 -   The setting 'Remove audit entries older dan (days)" has been      
     removed from the IBIS settings page. It can now be found in the   
     Audit page.                                                       
                                                                       
 Location: Navigation menu \> All pages \> Audit                       
                                                                       
 ![](..\markdown\images\media\image5.png)               
                                                                       
 -   Background tasks have been updated with quality of life changes   
     like: Dropdownlist for DetermineDatasetInOut, radiobuttons for    
     SyncAuthorisations, etc.                                          
                                                                       
 -   The E-mail aliases button in the user account registration is now 
     also available when it is set to readonly                         
                                                                       
 -   Fixed an issue where a long IBIS application name would push the  
     page title to the content page. The IBIS application name now     
     gets truncated if horizontal space runs out                       
                                                                       
 -   An (unhandled) error page will now show its message in Dutch by   
     default                                                           
                                                                       
 -   The organization selector field now always shows the selected     
     department by truncating the path before it. To see the whole     
     path, click the plus icon inside the field or by hovering over    
     the truncated text                                                
                                                                       
 -   The staging area can now be sorted by clicking on the column      
     headers, except for the 'Connector type'                          
                                                                       
 -   ABAC: fixed an issue where double clicking a role assignment in   
     the future would not show a popup                                 
                                                                       
 -   The Profile page left column has been changed to display Identity 
     registration instead of self service employee registration.       
                                                                       
 -   The Profile page can now show contracts, user accounts and assets 
     in other blocks. Click on the header to change what kind of data  
     each block should display.                                        


 ### Process and performance enhancements 
 -   The save order for AliasDossier (user accounts) and the          
     associated smtp aliases has been optimized                       
                                                                      
 -   IBIS register will now work out of the box with the              
     UI/API/WF/Connector, without having to resort to custom workflows
                                                                      
 -   Adding, modifying and deleting smtp aliases has been optimized   
     and will now work out of the box without having to resort to     
     custom workflows                                                 
                                                                      
 -   It's possible to set the batch size for committing a collection  
     (of records). This setting                                       
     "NHibernate.MaximumBatchSizeForCollections " can be found in the 
     'App_Data/AppSettings.config' file                               
                                                                      
 -   The IBIS register has been extended with field DomainName        

 ### Security {#security .unnumbered}                                 

 -   The 'Change password' button is now available in the User account
     registration, under the 'Options' menu                           
                                                                      
 -   The administrator checkbox is no longer available in the         
     application roles setting                                        
                                                                      
 -   The 'No access' error page has been removed. From now on, a user 
     with 'No access' will be redirected to the message center and    
     shown a message there                                            
                                                                      
 -   The username / password fields are required when using Windows   
     Authentication in the RESTMethod activity                        
                                                                      
 -   An ACL sync will be prevented from starting if another one is    
     already running                                                  



 ### Connectors {#connectors .unnumbered}                              
 -   A connector will now prevent an export if a previous export was   
     incomplete                                                        
                                                                       
 -   The IBIS-API connector now has a field 'OData filter (query)' to  
     filter the object data with                                       
                                                                       
 -   The Google Workspace connector                                    
                                                                       
     -   has been updated to work better with groups attribute         
         settings                                                      
                                                                       
     -   now allows the use for custom attributes                      
                                                                       
 -   The ServiceSites (vrijwilligersdossier) connector has been        
     updated to prevent double schema attributes                       


## Bugfixes

 
  |**Reference**  |**Bug fix**                                                   | 
  |---------------|--------------------------------------------------------------|
  |11987          |Fixed an issue where authorizations could not be configured for the 'Extend/Shorten' menu item (Assets in possession page) |
  |11997          |Fixed an issue where a duplicating a 'Direct Execute Workflow' would result in a 'Standard workflow'
  |12093           |Fixed an issue where the employee working stock page would give an error when trying to open a registration page in the new (RLv2) UI
  |12221           |Fixed an issue where a connector process would be slow
  |12236           |Fixed an issue where the SQL connector WHERE filter cannot use single quotes
  |12264           |Fixed an issue where the staging area would not be deleted when a connector has been deleted
  |12284           |Fixed an issue where the 'CreatedBy' tables would be filled with 'onbekend/unknown'. It will show 'IBIS' instead
  |12285           |Fixed an issue where the Universal search would not open the correct the identity registrations
  |12286           |Fixed an issue where a default value for \_16_99_dossier_status would not be used in a registration
  |12294           |Fixed an issue where the search filter in the employee registrations would not work correctly
  |12295           |Fixed an issue where field \_04_25_Organisatie_IdentificatieFormeleOrganisatie would show as a tree picker/dropdownlist instead of a regular field


## Migration notes

  
  **Description**
  
  Smtp alias buttons require at least readonly rights before they can be
  used. Note that if these rights have never been set before, you might
  not be able to use these buttons after the upgrade. To add these
  authorizations please configure them in the designated TreeManager ACL
  tree like any other field

  Previously, the DetermineDatasetInOut task would use all datasets if
  the dataset was not specified (dataset field was left empty). Now that
  the field has turned into a dropdownlist; to use **all datasets** you
  need to **specifically select** 'All datasets' in the dropdownlist.
  This means that after migration the previously set
  DetermineDatasetInOut background tasks will not work anymore if they
  were set to an empty field.

  It won't be possible to remove administrator rights from application
  roles through the UI. We recommend unchecking the administrator
  checkbox for these application roles before upgrading. After the
  upgrade, you can only remove administrator rights by changing it in the
  database.

</details>
<details>
<summary>IBIS V5.3</summary>

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

![](data:image/png;base64,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)


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

### Workflow enhancements

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

| Referentie | Bug fix                                                                                                                                                       |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
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

</details>
