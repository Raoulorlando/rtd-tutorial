## Hotfix 1 - 8

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