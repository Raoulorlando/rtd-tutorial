<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / SAP SuccessFactors

##### SAP SuccessFactors

The SAP SuccessFactors module is capable of importing (full/delta) and
exporting employee data from and to SAP SuccessFactors through the OData
REST API.

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
<td><p>OData URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The URL of the SuccessFactors endpoint</p></td>
</tr>
<tr class="even">
<td><p>Username</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The HTTP basic authentication username</p></td>
</tr>
<tr class="odd">
<td><p>Password</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The HTTP basic authentication password</p></td>
</tr>
<tr class="even">
<td><p>Left pad user ID</p></td>
<td><p><strong> </strong></p></td>
<td><p>Can be used to fill up the userId property to a specified number
of characters. This may come to use when the userId in IBIS is stored
without the leading zero’s often seen in SAP systems</p></td>
</tr>
<tr class="odd">
<td><p>Padding total width</p></td>
<td><p><strong> </strong></p></td>
<td><p>The total number of characters the userId property must
become</p></td>
</tr>
<tr class="even">
<td><p>Padding character</p></td>
<td><p><strong> </strong></p></td>
<td><p>The character the userId property must be prepended with</p></td>
</tr>
<tr class="odd">
<td><p>Enable photo support</p></td>
<td></td>
<td><p>When enabled, user photos will be fetched during import, and can
be exported to SuccessFactors</p></td>
</tr>
<tr class="even">
<td><p>Enable automatic photo resize</p></td>
<td></td>
<td><p>Automatically resize the photo to 180x240 during export</p></td>
</tr>
<tr class="odd">
<td><p>Photo name</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The name to use for photo objects handled by this
connector</p></td>
</tr>
<tr class="even">
<td><p>Do not import users without department</p></td>
<td></td>
<td><p>When enabled, users without a department (value = N/A) will not
be imported</p></td>
</tr>
<tr class="odd">
<td><p>SAP ID private phone</p></td>
<td></td>
<td><p>The SAP dropdown ID for the private phone number</p></td>
</tr>
<tr class="even">
<td><p>SAP ID private mobile phone</p></td>
<td></td>
<td><p>The SAP dropdown ID for the private mobile phone number</p></td>
</tr>
<tr class="odd">
<td><p>SAP ID business phone</p></td>
<td></td>
<td><p>The SAP dropdown ID for the business phone number</p></td>
</tr>
<tr class="even">
<td><p>SAP ID business mobile phone</p></td>
<td></td>
<td><p>The SAP dropdown ID for the business mobile phone number</p></td>
</tr>
<tr class="odd">
<td><p>Employee class mappings</p></td>
<td></td>
<td><p>Contains a list of conversions for SAP employee class to IBIS
employment type main group.</p>
<p>Format: SAPID:IBISID;SAPID2:IBISID2</p></td>
</tr>
<tr class="even">
<td><p>Employment type mappings</p></td>
<td></td>
<td><p>Contains a list of conversions for SAP employement type to IBIS
employment type subgroup.</p>
<p>Format: SAPID:IBISID;SAPID2:IBISID2</p></td>
</tr>
</tbody>
</table>

#### Special properties

##### \_photo

Photos are stored as separate objects in SuccessFactors. Since the
connector only supports 1 on 1 relations, the connector will query
SuccessFactors for the user photo with the name specified in the
connector settings and add it to the \_**photo** property of the user.

On export, the \_**photo** property will be downsized to 180\*240 and
added/updated in SuccessFactors. When the \_photo property is cleared
and a photo with *\[Photo name\]* exists in SuccessFactors it will be
deleted.

##### \_ibisEmploymentTypeMainGroup

Contains the converted value of EmployeeClass using configuration
parameter **Employee class mappings**

##### \_ibisEmploymentTypeSubGroup

Contains the converted value of EmploymentType using configuration
parameter **Employment type mappings**

##### \_phone\_home

Contains the phone number where phoneType == **SAP ID private phone**

##### \_phone\_home\_mobile

Contains the phone number where phoneType == **SAP ID private mobile
phone**

##### \_phone\_primary

Contains the phone number where isPrimary == true

##### \_phone\_work

Contains the phone number where phoneType == **SAP ID business phone**

##### \_phone\_work\_mobile

Contains the phone number where phoneType == **SAP ID business mobile
phone**
