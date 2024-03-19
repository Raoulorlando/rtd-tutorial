## August 2023

- In IBIS settings -> Entitlement Management card, two properties that are no longer in use were listed. These have been removed.

- The 'Request Resources' button is now available not only for employee registration but also for: identity registration, user account registration, PBS registration, Facility management registration, and EPIC registration.

- There is a new page 'Data model' (/DomainModel) where you can see domain object properties and dynamic properties in one overview.

- IBIS now has a 'Process queue' page \(\~\/ProcessQueue\) that can process \(Hangfire\) tasks in batches. Tasks of the same type \(making SQL connections\) can be offered as one Hangfire job, making task processing more efficient. The Process queue can be configured via: IBIS settings \-\> Process queue.

- Various performance improvements in the connector sync process.

- In the IBIS Connectors, properties with the value "process" can now be used without issues.
  
- The settings for retrieving organizations (IBIS settings \> Organization management) have been clarified.

- Creating\/editing\/deleting a resource in IBIS is now processed more efficiently, allowing the result to be visible in the UI after a few seconds.

- The profile page no longer shows the same assigned resource multiple times but as a single line.

- In the Task History page \(\~/ProcessHistory\), an orange warning icon indicates if a task has been stopped\/deleted prematurely.

- In the assigned resource overview of an employee:
  - You can click on a resource card to display an overlay. This overlay shows a dropdown list of registrations that are currently in progress, assigned, or archived for that resource.
  - Rejected resource requests have been moved from 'In progress' to 'Archived'.

- The assigned resource details overlay now retrieves its information from an IBIS source instead of ABAC. If ABAC is not available, the data from this overlay is still accessible to the user.

- Fixed:
    - All pages overlay that was not displayed on the 'Requests and approvals' page.
    - Registration designer displaying a too dark gray color.
    - Adding a resource to a resource set does not retain selection after new filtering.
    - Background task WorkflowTimerTask was incorrectly created in a bare IBIS installation.
    - Task history page filter/data refresh does not work properly when an accordion is expanded.
    - Retrieving organizations (IBIS settings) is not properly saved in specific situations.
    - In the Resource requests page, you cannot sort date fields in the 'For employee(s)' tab.
