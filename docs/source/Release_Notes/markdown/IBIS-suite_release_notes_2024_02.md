## February 2024

- Delegation:
  - Added new delegation functionality to IBIS. With this, an employee can delegate the execution of tasks in IBIS to a colleague.
  - If the delegate chooses to work in IBIS as the delegator, actions in IBIS will be audited from that moment onward as executed on behalf of the delegator.
- Connector:
  - TOPdesk connector has been expanded to manage Suppliers.
  - TOPdesk connector has been expanded to manage personGroups.
  - Connector Agent information has been expanded with the Last Contact Moment of the Agent.
- Monitoring:
  - Run profile information can now be sent to **cronitor** for central monitoring of various tasks and environments.
- Fixed:
  - Newly added records in the Audit configuration page are now not synchronous with values in the database.
  - Property WidDossier VISscan is not displayed as a photo but as a base64 string.
  - Adding a new property to a resource when ABAC is not available results in a background error message and does not show a notification to the user.
  - Mutation of certain resource properties is not applied immediately.
  - Readonly fields do not appear disabled.
  - Property 07_30_Communication_Data in user account remains empty after a change.
