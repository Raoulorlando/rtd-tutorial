## Hotfix 1 - 8

### Hotfix 1

- **Added functionalities:**
    - IBIS Connector
        > *Easily add mandatory fields to attribute relationships.*
    - IBIS Active Directory Connector
        > *Passing account expiration as a \_param value instead of a standard flow.*
    - IBIS Documentation:
        > *Workflow documentation included as a help file in IBIS. Documentation can be found at <https://ibisurl/help>*

- **Resolved bugs:**
    - 11931: SysPages does not display authorization and delete icons completely to the right.
    - 11933: Logging: database login and password do not work for alternative settings.
    - 11937: Manager is not saved and displayed correctly.
    - 11945: No confirmation prompt when deleting Unique Value Register.
    - 11947: Connector agent disconnect.
    - 11948: SMTP alias buttons can authorize (RLv2 user account).
    - 11950: Staging area sometimes shows black mask without overlay.
    - 11951: Linq statements do not support '.com'.
    - 11967: Pages: toggle button sometimes does not work from grid.

### Hotfix 2

- **Added functionalities:**
    - Include IBIS Connector module documentation as a help file in IBIS.

- **Resolved bugs:**
    - 11980: Extending dossier fills in incorrect dates.
    - 11984: IBIS AD Connector: End Date interpretation sometimes goes wrong with AD Connector (agent).
    > *Note: Before installing the hotfix, turn off the Run Profiles. After installing the hotfix, perform a Sync on all connectors first so that the Dates in the Staging Area are re-evaluated. Only then can an Export be done to the connected target systems. So, never perform an Export immediately after installing the hotfix.*

### Hotfix 3

- **Added functionalities:**
    - Performance improvements.

### Hotfix 5

- **Added functionalities:**
    - IBIS Connector:
        > *Enable join functionality between external system and staging area object.*

### Hotfix 7

- **Added functionalities:**
    - IBIS-IBIS Connector:
        > *A new IBIS Connector that allows connection to another IBIS instance for importing and exporting data.*
        >
        > *The data*

### Hotfix 8

- **Resolved bugs:**
    - 12228: Workflow does not retrieve organization data for iDossiers where field 02_60 is filled.
