## IBIS-suite 6.01 Updates until 21st of September 2023

#### Compared to IBIS-suite version 6.0

Important for new installation / migration / Known issues:

- Check the format of the Export expiration date and Import expiration date where you use the AD connector.
- With a new update of IBIS, you need to open and save all reports once. You could potentially solve this with a WF (e.g., updating a certain field of each report).
- Check your ResourceAssignment table for empty values in your DossierID and DossierType columns. This can cause your assignments not to appear in the UI.
- If the "Disallow manual assignment" attribute is not updated, it is best to create a TreeManager connector and flow the attribute to ensure everything is back in sync.


21-09-2023 Build 6.0.1 +54


-   Opgelost: Mailserver instellingen correct opslaan


21-09-2023 Build 6.0.1 +53


-   Diverse verbeteringen in de workflow designer


20-09-2023 Build 6.0.1 +52


-   Opgelost: geboortedatum mag niet meer kleiner zijn dan 01-01-1900


20-09-2023 Build 6.0.1 +51


-   Diverse performance verbeteringen.


18-09-2023 Build 6.0.1 +50


-   Connector sync performance verbetering.
-   Log4Net.config aanpassingen tbv performance verbeteringen:\
    Voeg deze toe aan de adoNetAppender:\
    OnlyFixPartialEventData value=\"true\"\
    Wijzig de BufferSize\
    bufferSize value=\"200\"\
    voeg de RollingFileAppenderBuffer toe uit log4net.example


15-09-2023 Build 6.0.1 +49


-   De knop \"Resources aanvragen\" altijd zichtbaar in de profiel
    pagina bij het overzicht Toegewezen resources.


15-09-2023 Build 6.0.1 +48


-   De SSPR wachtwoordherstel configuratie is uitgebreid met een optie
    om het zakelijke e-mailadres (07.30) te gebruiken als ontvanger van
    de OTP links..


15-09-2023 Build 6.0.1 +47


-   Resource aanvraag is uitgebreid met de toegepaste regels voor
    automatische/handmatige toewijzing. Daarnaast worden de goedkeuring
    eigenschappen ook direct opgeslagen. Deze informatie wordt getoond
    bij de aanvraag en toegewezen resources.


15-09-2023 Build 6.0.1 +46


-   De configuratie voor het opzoeken van een bestaand IDM-nummer of het
    genereren van een nieuw IDM-nummer is vereenvoudigd. Dit is te
    configureren op de IBIS instellingen pagina -- Identiteit -\>
    Identificatie -\> IDM-nummer.

    Een bestaand IDM-nummer wordt opgezocht altijd als eerst in de
    identiteit registratie, indien niet gevonden dan in bestaand
    registratie type. Indien niet gevonden dan wordt er een nieuw
    IDM-nummer gegenereerd.

    Het opzoeken wordt bepaald op basis van de standaard opties:

    -   Personeelsnummer, en-/of
    -   Naamgegevens + voornamen , en-/of
    -   Naamgegevens + voorletters

-   De configuratie voor het opzoeken van een bestaande identiteit
    registratie of het genereren van een nieuwe identiteit registratie
    is vereenvoudigd. Dit is te configureren op de IBIS instellingen
    pagina -- Identiteit -\> Identificatie -\> Identiteit registratie.

    Een bestaande identiteit wordt opgezocht op basis van de standaard
    opties:

    -   Personeelsnummer, en-/of
    -   Naamgegevens + voornamen , en-/of
    -   Naamgegevens + voorletters

-   De aanschrijfwijze van het eigenschap IDM-nummer overal gewijzigd


14-09-2023 Build 6.0.1 +45


-   ABAC Targets kunnen nu vanuit IBIS geprovisioned worden door een
    Connector. Targets kunnen hiermee worden aangemaakt, bijgewerkt en
    verwijderd. Zie Connector documentatie in /Help
-   ABAC Targets object is uitgebreid met extensionAttribute01 t/m 10.
    Hiermee kan bij de inrichting van connectoren gebruik gemaakt worden
    van eigenschappen die real-time worden geprovisioned. Dit resulteert
    in het triggeren van ABAC om de bijbehorende criteria bij te werken.


14-09-2023 Build 6.0.1 +44


-   In de overzichten \"Resources aanvragen\" en \"Resources\" de link
    toon meer is vervangen door paginering.


14-09-2023 Build 6.0.1 +43


-   Opgelost: Taak historie overzicht uitkomst kolom toont bij het
    optreden van bepaalde foutmelding de gehele foutmelding ipv status
    icon.


13-09-2023 Build 6.0.1 +42


-   Laatste run datumtijd van ABAC achtergrond taken kunnen nu vanuit
    IBIS worden gewist. Te vinden in IBIS instellingen -\> ABAC --
    Algemeen


12-09-2023 Build 6.0.1 +41


-   Opgelost: Staging area: Koppelen overlay houd zich niet aan
    ingestelde \'resultaten weergeven\' in de paginering


12-09-2023 Build 6.0.1 +40


-   Tags die momenteel actief/opgeslagen in de resources kunnen bij
    andere resources opnieuw worden gebruikt


12-09-2023 Build 6.0.1 +39


-   Opgelost: kopiëren van een connector weer werkt.


11-09-2023 Build 6.0.1 +38


-   In de proces queue wordt nu rekening gehouden met dat Workflow taken
    rechtstreeks naar hangfire terugsturen afhankelijk van configuratie.


11-09-2023 Build 6.0.1 +37


-   In de resource aanvragen scherm: wanneer een medewerker of resource
    met het plustje is toegevoegd, dan is het nu duidelijk zichtbaar wat
    die toegevoegd heeft. Een tooltip verschijnt in het tab het
    aanvraagoverzicht.


11-09-2023 Build 6.0.1 +36


-   Het beheer van IBIS gebruikers in TreeManager is verbeterd.
    Wijziging op een gebruiker in IBIS wordt doorgevoerd in TreeManager.
    Bijvoorbeeld, inactiveren en blokkeren.


08-09-2023 Build 6.0.1 +35


-   De iconen die je ziet bij de \"Alle pagina\'s\" overlay en in de
    registratie pagina's zijn gelijkgetrokken.


07-09-2023 Build 6.0.1 +34


-   De functionaliteit van de workflow activiteit IdentityDossier is
    gekopieerd naar IBIS core. Deze functionaliteit kan vanuit IBIS
    instellingen - Identiteit kaart aan/uitzetten. Indien aangezet dan
    worden de identiteit registraties vanuit IBIS instellingen beheerd
    en niet meer vanuit een workflow. Het opzoeken, aanmaken en
    bijwerken van identiteit registraties volgt de bestaande
    instellingen voor het opzoeken en genereren van IDM-nummer.
-   IBIS instellingen -\> Identiteit kaart is gereorganiseerd. Twee tabs
    zijn toegevoegd waarin de verschillende IDM-nummer opzoek en
    persoonsgegevens instellingen zijn toegevoegd

LET OP: indien je er gebruik gaat maken van deze functionaliteit dan
moet je de workflows/connectoren die de identiteit registraties beheert
uitzetten.


05-09-2023 Build 6.0.1 +33


-   Nadat de aanvrager resources aanvraag heeft gedaan kan de medewerker
    direct naar de \'Door mij aangevraagd\' gaan. De link verschijnt de
    bevestiging overlay


04-09-2023 Build 6.0.1 +31


-   Bij nieuwe installatie staat vanaf deze versie \"Mijn afdeling
    tonen\" in de profiel pagina uit.


#### New features

- There is a new page called 'Data model' (/DomainModel) where you can see an overview of the domain object properties and dynamic properties all at once.

- IBIS now has a \'Process queue\' page (\~/ProcessQueue) that can process (Hangfire) tasks in batches. Tasks of the same type (making SQL connections) can then be submitted as one Hangfire job, making the task processing more efficient. The Process queue can be configured via: IBIS settings \> Process queue.


#### The following enhancements have been implemented:

- Ability to manually cancel resource requests from the "Assigned resources" overview. The request will then no longer be visible to the approvers.

- The requester can view the canceled requests in the "Archived" overview.


-   Improved visibility of task history log names in the overview.

-   In IBIS settings -> Entitlement Management card, two properties that were no longer in use were listed. These have been removed.

-   The \'Request resource\' button is now available not only for employee registration but also for identity registration, user account registration, PBS registration, facility management registration, and EPIC registration.

- Properties with the value \"process\" can now be used in the IBIS Connectors without any issues.

- The settings for retrieving organizations (IBIS settings \> Organization management) have been clarified.

- Creating/editing/deleting a resource in IBIS is now processed more efficiently, allowing the results to be visible in the UI after a few seconds.

- The profile page no longer displays the same assigned resource on multiple lines but as a single line.

- In the Task History page (\~/ProcessHistory), an orange warning icon indicates if a task has been stopped/deleted prematurely.

- In the assigned resource overview of an employee:

    - You can click on a resource card to display an overlay. This overlay shows a dropdown list of registrations that are currently in progress, assigned, or archived for that resource.
    - Rejected resource requests have been moved from \'In progress\' to \'Archived\'.

- The assigned resource details overlay now retrieves its information from an IBIS source instead of ABAC. If ABAC is not available, the data from this overlay is still available to the user.

- Several performance enhancements in the connector sync process.



#### The following issues have been resolved:

- IBIS configuration crashes when exporting a configuration file.
- All pages overlay that was not displayed on the 'Requests and Approvals' page.
- Registration designer displaying a too dark gray color.
- Adding resource to resource set does not retain selection after new filtering.
- Background task WorkflowTimerTask was incorrectly created in bare IBIS installation.
- Task history page filter / data refresh does not work properly when an accordion is expanded.
- Retrieving organizations (IBIS settings) is not properly saved in specific situations.
- In the Resources request page, you cannot sort date fields on the 'For employee(s)' tab.

