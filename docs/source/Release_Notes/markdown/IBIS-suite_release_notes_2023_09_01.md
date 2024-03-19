## September 2023 (until 21st)

-   Various improvements in the workflow designer.
-   Various performance improvements.
-   Connector sync performance improvement.
-   Log4Net.config adjustments for performance improvements:  
    Add these to the adoNetAppender:  
    OnlyFixPartialEventData value="true"  
    Change the BufferSize  
    bufferSize value="200"  
    add the RollingFileAppenderBuffer from log4net.example
-   The "Request Resources" button is always visible on the profile page
    in the Assigned resources overview.

-   The SSPR password recovery configuration has been expanded with an option to use the business email address (07.30) as the recipient of the OTP links.

-   Resource request has been expanded with the applied rules for automatic/manual assignment. Additionally, approval properties are also saved directly. This information is displayed with the request and assigned resources.

-   The configuration for searching for an existing IDM number or generating a new IDM number has been simplified. This can be configured on the IBIS settings page – Identity \-\> Identification \-\> IDM number.

    An existing IDM number is always searched for first in the identity registration, if not found then in existing registration type. If not found then a new IDM number is generated.

    The search is determined based on the standard options:

    -   Employee number, and\/or
    -   Name details \+ first names, and\/or
    -   Name details \+ initials

-   The configuration for searching for an existing identity
    registration or generating a new identity registration
    has been simplified. This can be configured on the IBIS settings
    page – Identity \-\> Identification \-\> Identity registration.

    An existing identity is searched based on the standard
    options:

    -   Employee number, and/or
    -   Name details + first names, and/or
    -   Name details + initials

-   The wording of the IDM number property has been changed everywhere.

-   ABAC Targets can now be provisioned from IBIS by a Connector. Targets can be created, updated, and deleted. See Connector documentation in \/Help.
-   ABAC Targets object has been expanded with extensionAttribute01 to 10.
    This allows properties that are provisioned in real-time to be used during connector setup. This results in triggering ABAC to update the associated criteria.

-   In the "Request Resources" and "Resources" overviews, the "show more" link has been replaced by pagination.

-   Last run datetime of ABAC background tasks can now be cleared from IBIS. Found in IBIS settings \-\> ABAC – General.

-   Tags that are currently active/saved in the resources can be reused with
    other resources.

-   In the process queue, Workflow tasks are now taken
    into account to be sent directly back to hangfire depending on configuration.

-   In the resource request screen: when an employee or resource
    is added with the plus sign, it is now clearly visible what
    has been added. A tooltip appears in the tab the
    request overview.

-   Management of IBIS users in TreeManager has been improved.
    Changes to a user in IBIS are reflected in TreeManager.
    For example, deactivating and blocking.

-   The icons you see in the "All pages" overlay and in the
    registration pages have been aligned.

-   The functionality of the workflow activity IdentityDossier has been
    copied to IBIS core. This functionality can be turned on\/off from IBIS
    settings \- Identity card. If turned on, then
    identity registrations are managed from IBIS settings
    and no longer from a workflow. Searching, creating, and
    updating identity registrations follows the existing
    settings for searching and generating IDM number.
    
    ```{eval-rst}
    .. note:: If you start using this functionality, you must disable the workflows/connectors that manage the identity registrations.
    ```

-   IBIS settings \-\> Identity card has been reorganized. Two
    tabs have been added for the different IDM number lookup and
    personal data settings.



-   After the requester has requested resources, the employee can now go directly to 'Requested by me'. The link appears in the confirmation overlay.

-   "Show my department" is disabled by default on the profile page for new installations.

-   Can manually cancel resource requests from "Assigned resources" overview. The request will then no longer be visible
    to the approvers.
-   Requesters can view canceled requests in the "Archived" overview.

-   Task history log name made clearly visible in the overview.

- Fixed:
    - Correctly saving mail server settings.
    - Birth date cannot be earlier than 01-01-1900.
    - Task history overview outcome column displays the entire error message instead of status icon when certain error occurs.
    - Staging area: Linking overlay does not adhere to set 'show results' in pagination.
    - Copying a connector works again.
    - IBIS configuration freezes when exporting a configuration file.