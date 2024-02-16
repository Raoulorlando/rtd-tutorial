<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Afas

# Afas

The Afas module communicates with Afas Online through an *Afas Get
Connector*. The module supports Full Import only because Afas does not
provide a delta mechanism. Exporting data to Afas should be done by
using the IBIS workflow engine.

## Primary key

The primary key for objects delivered by this module is stored in the
\_***PrimaryKey*** property. The value of this property is calculated
during import using the ***Primary key expression*** parameter.

## Module parameters

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
<th><p>API URL</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The URL to the Afas REST connector API. For example:</p>
<p> </p>
<p>§   <em>https://[customer
id].rest.afas.online/profitrestservices/connectors</em></p></th>
</tr>
<tr class="header">
<th><p>Token ID</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The security token used to authenticate to Afas</p></th>
</tr>
<tr class="odd">
<th><p>Connector name</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the Get Connector</p></th>
</tr>
<tr class="header">
<th><p>Primary key expression</p></th>
<th><p><strong>X</strong></p></th>
<th><p>An expression used to format the primary key. This expression
will be translated by the dynamic lookup module. For example:</p>
<p> </p>
<p>§   <em>{Employee}{Contract}-{OuCode}</em></p></th>
</tr>
<tr class="odd">
<th><p>Batch size</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The maximum number of objects to retrieve in each call to Afas.
The default is 20.</p></th>
</tr>
<tr class="header">
<th><p>OrderBy fields</p></th>
<th><p> </p></th>
<th><p> </p></th>
</tr>
<tr class="odd">
<th><p>RowFilter fields</p></th>
<th><p> </p></th>
<th><p> </p></th>
</tr>
<tr class="header">
<th><p>RowFilter types</p></th>
<th><p> </p></th>
<th><p> </p></th>
</tr>
<tr class="odd">
<th><p>RowFilter values</p></th>
<th><p> </p></th>
<th><p> </p></th>
</tr>
</thead>
&#10;</table>

 
