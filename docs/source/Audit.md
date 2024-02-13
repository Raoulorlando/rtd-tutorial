##### <span id="index"></span>Audit configuration

All user actions on IBIS objects can be audited. IBIS supports the
following audit actions.

-   Create
-   Read
-   Update
-   Delete

*NOTE: The auditing of READ events may seriously degrade system
performance*

An audit entry consists of:

-   The date and time the event took place
-   The account that performed the modification
-   The type of the object in question
-   The ID of the object in question
-   The old state of the object
-   The new state of the object

By default, auditing is turned off for all objects. To modify audit
settings:

-   Browse to the Audit configuration page at ~/Audit
-   Enable or disable the appropriate audit options using the checkboxes
    behind the objects
-   Click 'Save' to save changes
