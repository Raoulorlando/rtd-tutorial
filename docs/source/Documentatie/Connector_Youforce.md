<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Youforce

# Youforce

The Youforce connector is capable of importing employee data from the
Youforce API.

## Primary key

The primary key for Youforce objects is stored in the ***Identifier***
property of the hologram.  
This property contains a concatenated string that is made up of:

<table class="table table-bordered" style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td width="110"><p>Person_PersonCode</p></td>
<td width="16"><p>-</p></td>
<td width="104"><p>Employment_Code</p></td>
<td width="21"><p>-</p></td>
<td width="215"><p>Assignment_OrganizationUnit_ShortName</p>
<p><strong>OR</strong></p>
<p>Employment_OrganizationUnit_ShortName</p></td>
<td width="16"><p>-</p></td>
<td width="141"><p>Assignment_StartDate</p>
<p><strong>OR</strong></p>
<p>Employment_HireDate</p>
<p><em>in the format: yyyyMMdd</em></p></td>
</tr>
</tbody>
</table>

## Parameters

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
<tr class="odd">
<th width="172"><p>Tenant ID</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The ID of the tenant to retrieve data for.</p>
<p>If set to 0, the ID will be determined by the API based on Consumer
ID.</p></th>
</tr>
<tr class="header">
<th width="172"><p>Consumer ID</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The consumer ID</p></th>
</tr>
<tr class="odd">
<th width="172"><p>Consumer Secret</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The secret key that corresponds with the consumer
ID</p></th>
</tr>
<tr class="header">
<th width="172"><p>Use assignments</p></th>
<th width="68"><p><strong> </strong></p></th>
<th width="378"><p>If set to true the assignment data will be used when
creating iDossiers.</p>
<p>If set to false iDossiers will be created based only on employment
data</p></th>
</tr>
<tr class="odd">
<th width="172"><p>Fetch loginnames during import</p></th>
<th width="68"><p><strong> </strong></p></th>
<th width="378"></th>
</tr>
<tr class="header">
<th width="172"><p>Ignore HTTP 400 errors during export</p></th>
<th width="68"><p><strong> </strong></p></th>
<th width="378"><p>When turned on, error 400 (bad requests) will be
ignored during export so that holograms will be created from
records.</p>
<p>The youforce iam implementation returns an error 400 bad request when
you try to update a value that is the same as an existing loginid value.
As a result, no holograms are created for existing records (making it
impossible to connect systems with existing data). This checkbox makes
migration possible. After a migration/connection the toggle can be
disabled again and "real" errors are treated as errors again</p></th>
</tr>
</thead>
&#10;</table>
