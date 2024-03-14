# December 2023

- Various API performance improvements implemented.
- Various security improvements implemented.
- Various usability improvements implemented.
- Entitlement management:
  - Number of required approvals is now displayed in the Approvals screen.
  - Resource icon is now displayed instead of just the style name.
- Connector:
  - Graph connector has been extended with extension property.
  - KPN Portal connector built for managing subscriptions.
- IBIS-suite service account creation during TreeManager installation so it can be used for communication between IBIS and ABAC with TreeManager.
- In the Universal search, you can now search within a single registration instead of searching across all registrations.

**Resolved issues**
  - Notification to CC and BCC not sent if filled out.
  - Connector DeltaSync evaluates only if the property is present in the hologram.
  - Organization selector displays department number if department is selected.
  - WidDossier search page lacks the WID registration button.
  - Withdrawn assigned resource remains available for re-withdrawing.
  - An invalid date can be entered in the resource request. There's no check if the end date falls within the target end date.
