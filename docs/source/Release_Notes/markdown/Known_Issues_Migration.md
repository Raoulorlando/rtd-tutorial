## New installation / migration / Known issues

### IBIS 6.0 to IBIS 6.01

- Check the format of the Export expiration date and Import expiration date where you use the AD connector.
- With a new update of IBIS, you need to open and save all reports once. You could potentially solve this with a WF (e.g., updating a certain field of each report).
- Check your ResourceAssignment table for empty values in your DossierID and DossierType columns. This can cause your assignments not to appear in the UI.
- If the "Disallow manual assignment" attribute is not updated, it is best to create a TreeManager connector and flow the attribute to ensure everything is back in sync.