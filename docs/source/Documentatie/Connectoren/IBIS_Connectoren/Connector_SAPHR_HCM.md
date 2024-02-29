# SAP HR / HCM

The SAP HR module is capable of importing employee data from SAP HRMD
IDoc files. The module supports the following IDoc versions:

-   HRMD A03
-   HRMD A05
-   HRMD A07

The IDoc files need to be placed on a network share that is accesible by
IBIS. IBIS will process all files that do not have the extension
*.processed*, and after successful processing it will rename the file to
\[filename\].processed

## Parameters

|   Parameter   | Required |                                                        Description                                                        |
|:-------------|:--------:|:-------------------------------------------------------------------------------------------------------------------------|
|  IDoc version |     X    |             The expected IDoc version. In case the IDoc contains a different version it will not be processed             |
| System number |          |                                                        [future use]                                                       |
| Client number |     X    | The client number the connector must handle. In case the IDoc contains a different client number it will not be processed |
| IDoc location |     X    |                                         The location of the IDoc files to process                                         |

## Primary key

The primary key for SAP objects is stored in the ***Identifier***
property of the hologram.  
This property contains a concatenated string that is made up of:

| P0001:PLANS<br> <br> <br> <br>Position | -<br><br> <br><br><br>| P0001:ORGEH<br> <br> <br> <br>Organization | - <br><br> <br><br><br>| P0001:BEGDA<br> <br> <br> <br>Start date |
|----------------------------------------|---|--------------------------------------------|---|------------------------------------------|
<br>

These combined properties will render a unique identifier for each
position/organization/startdate combination.  
  
In case an IDoc contains multiple position/organization relations an
object will be created for each combination. All other information
contained in the IDoc (personal info, communication, address, etc.) will
be stored on every object.
