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

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>IDoc version</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The expected IDoc version. In case the IDoc contains a different
version it will not be processed</p></th>
</tr>
<tr class="header">
<th><p>System number</p></th>
<th><p><strong> </strong></p></th>
<th><p><em>[future use]</em></p></th>
</tr>
<tr class="odd">
<th><p>Client number</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The client number the connector must handle. In case the IDoc
contains a different client number it will not be processed</p></th>
</tr>
<tr class="header">
<th><p>IDoc location</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The location of the IDoc files to process</p></th>
</tr>
</thead>
&#10;</table>

## Primary key

The primary key for SAP objects is stored in the ***Identifier***
property of the hologram.  
This property contains a concatenated string that is made up of:

<table class="table table-bordered">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>P0001:PLANS</p>
<p> </p>
<p><em>Position</em></p></td>
<td width="16"><p>-</p></td>
<td><p>P0001:ORGEH</p>
<p> </p>
<p><em>Organization</em></p></td>
<td><p>-</p></td>
<td><p>P0001:BEGDA</p>
<p> </p>
<p><em>Start date</em></p></td>
</tr>
</tbody>
</table>

These combined properties will render a unique identifier for each
position/organization/startdate combination.  
  
In case an IDoc contains multiple position/organization relations an
object will be created for each combination. All other information
contained in the IDoc (personal info, communication, address, etc.) will
be stored on every object.
