<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Conclusion Class LMS

##### Conclusion Class LMS

The Class connector is capable of writing to the Class ImportService
endpoint.

#### Parameters

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>API URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The URL of the Class system endpoint<br />
<br />
For example: http://server.tld/crmimport/CrmImportService.svc</p></td>
</tr>
<tr class="even">
<td><p>Token</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The authorization token to use when making requests to
Class</p></td>
</tr>
<tr class="odd">
<td><p>Catalog ID</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The ID of the target catalog in Class</p></td>
</tr>
<tr class="even">
<td><p>Delay between requests (seconds)</p></td>
<td><p><strong> </strong></p></td>
<td><p>In case the Class endpoint gets overflooded with requests, this
setting can be used to wait a certain amount of seconds before sending
the next request</p></td>
</tr>
<tr class="odd">
<td><p>Block employee on disconnect</p></td>
<td><p><strong> </strong></p></td>
<td><p>If set the employee object in Class will get the
<em>isBlocked</em> property set to true when the object gets
disconnected</p></td>
</tr>
<tr class="even">
<td><p>Fill employment from iDossier</p></td>
<td><p><strong> </strong></p></td>
<td><p>If set the employments collection of the employee will be mapped
from the available iDossiers in IBIS. See the mapping paragraph below
for information on field mappings.</p></td>
</tr>
</tbody>
</table>

#### Employment mappings

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>iDossier property</th>
<th>Employment property</th>
</tr>
<tr class="odd">
<th><p>_01_20_Dienstverband_DienstverbandNummer</p>
<p><strong>OR</strong></p>
<p>_01_75_Dienstverband_SectoraalDienstverbandNummer</p></th>
<th><p>code</p></th>
</tr>
<tr class="header">
<th><p>_04_38_Organisatie_Personeelsgebiednummer</p></th>
<th><p>companyId</p></th>
</tr>
<tr class="odd">
<th><p>_14_20_Kostenplaats_KostenplaatsCode</p></th>
<th><p>costCentre</p></th>
</tr>
<tr class="header">
<th><p>_02_41_Plaatsing_DatumEindeGeldigheid</p></th>
<th><p>departureDate</p></th>
</tr>
<tr class="odd">
<th><p>_01_25_Dienstverband_FunctieOmschrijving</p></th>
<th><p>jobTitle</p></th>
</tr>
<tr class="header">
<th><p>CreatedDate</p></th>
<th><p>creationDate</p></th>
</tr>
<tr class="odd">
<th><p>OrganisationNumber</p></th>
<th><p>department</p></th>
</tr>
</thead>
&#10;</table>

 
