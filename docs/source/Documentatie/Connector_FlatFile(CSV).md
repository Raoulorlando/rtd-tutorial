<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Flat File (CSV)

# Flat File (CSV)

The CSV connector is capable of reading from- and writing to character
separated text files. the module supports import and export operations.

The file should contain columns separated by the ***Column separator***
parameter. A ***Text qualifier*** can be set in order for IBIS to
recognize the text portion of a column.

If the data in a colum contains the text qualifier itself (for example,
the text qualifier is **‘**, en the data is **Dhr. A in 't Veld**), the
qualifier should be escaped by duplicating it (**Dhr. A in 't Veld**).

## Parameters

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>File path</p></th>
<th><p><strong> </strong></p></th>
<th><p>The full path name of the file which contains the objects to
import</p></th>
</tr>
<tr class="header">
<th><p>Export file path</p></th>
<th><p><strong> </strong></p></th>
<th><p>The full path name of the file in which exported objects will be
written</p></th>
</tr>
<tr class="odd">
<th><p>File contains a header</p></th>
<th><p><strong>X</strong></p></th>
<th><p>If set, the first row in the file contains the column
names</p></th>
</tr>
<tr class="header">
<th><p>File header</p></th>
<th><p><strong> </strong></p></th>
<th><p>In case the file does not contain a header, specify the header
here. Use the same format as the file contents (including the column
separator and optional text-qualifier)</p></th>
</tr>
<tr class="odd">
<th><p>Column separator</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The character(s) that is used to separate columns</p></th>
</tr>
<tr class="header">
<th><p>Text qualifier</p></th>
<th><p><strong> </strong></p></th>
<th><p>The character(s) that is used to specify text</p></th>
</tr>
<tr class="odd">
<th><p>Encoding</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The encoding of the file</p></th>
</tr>
<tr class="header">
<th><p>Primary key column</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the primary key column in the file. This is used to
set the ExternalID property on the staging area entity</p></th>
</tr>
</thead>
&#10;</table>
