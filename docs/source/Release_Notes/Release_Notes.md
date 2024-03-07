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

Test

</details>