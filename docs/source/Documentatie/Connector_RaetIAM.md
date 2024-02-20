<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Raet IAM

##### Raet IAM

The RAET IAM connector is capable of managing user account data in RAET.

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
<tr class="odd">
<th width="172"><p>Consumer ID</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The consumer ID</p></th>
</tr>
<tr class="header">
<th width="172"><p>Consumer Secret</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The secret key that corresponds with the consumer
ID</p></th>
</tr>
<tr class="odd">
<th width="172"><p>Tenant ID</p></th>
<th width="68"><p><strong>X</strong></p></th>
<th width="378"><p>The ID of the tenant to retrieve data for.</p>
<p>If set to 0, the ID will be determined by the API based on Consumer
ID.</p></th>
</tr>
<tr class="header">
<th width="172"><p>Ignore HTTP 400 errors during export</p></th>
<th width="68"><p><strong> </strong></p></th>
<th width="378"><p>When turned on, error 400 (bad requests) will be
ignored during export so that holograms will be created from
records.</p>
<p>The IAM implementation returns an error 400 bad request when you try
to update a value that is the same as an existing loginid value. As a
result, no holograms are created for existing records (making it
impossible to connect systems with existing data). This checkbox makes
migration possible. After a migration/connection the toggle can be
disabled again and "real" errors are treated as errors again</p></th>
</tr>
</thead>
&#10;</table>
