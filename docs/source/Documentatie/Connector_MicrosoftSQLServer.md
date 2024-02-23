<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Microsoft SQL server

# Microsoft SQL Connector

The SQL-module communicates with a Microsoft SQL Server table or view.

-   In order to update a view, it must not span multiple tables.
-   Export is only supported when a primary key column is used, not when
    using a primary key expression.

## Primary key

The primary key for objects delivered by this module is defined in the
***Key column*** or the ***Primary key expression*** parameter in the
module settings.

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
<th><p>Connectionstring</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The connection string used for communication with the
database.</p>
<p>See https://www.connectionstrings.com/sql-server/ for more
information.</p></th>
</tr>
<tr class="header">
<th><p>Authentication method</p></th>
<th></th>
<th><p>The type of authentication to use for connecting to SQL
server</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th></th>
<th><p>The username for the connection</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th></th>
<th><p>The password for above user</p></th>
</tr>
<tr class="odd">
<th><p>Table or view</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the table or view to load data from / write data
to</p></th>
</tr>
<tr class="header">
<th><p>Key column</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the column to use as primary key for this
connector</p></th>
</tr>
<tr class="odd">
<th><p>Primary key expression</p></th>
<th><p><strong>X</strong></p></th>
<th><p>An expression used to format the primary key. This expression
will be translated by the dynamic lookup module. For example:</p>
<p>§   <em>{Employee}{Contract}-{OuCode}</em></p>
<p>When this method is used, a _PrimaryKey property will be added to
each imported object containing the calculated value.</p></th>
</tr>
<tr class="header">
<th><p>WHERE filter</p></th>
<th></th>
<th><p>A where statement used to filter data from the result set. This
should be the complete statement and start with WHERE</p></th>
</tr>
<tr class="odd">
<th><p>ORDER BY clause</p></th>
<th></th>
<th><p>An order by clause to order the result set. This should be the
complete clause and start with ORDER BY</p></th>
</tr>
<tr class="header">
<th><p>Enable delta support</p></th>
<th></th>
<th><p>If checked, the module will support delta import (once
configured)</p></th>
</tr>
<tr class="odd">
<th><p>Method</p></th>
<th></th>
<th><p><strong>DateTime column</strong> - The table or view contains a
DateTime column which is updated during add/modify of the record</p>
<p><strong>Delta table/view</strong> - The primary keys of records with
changes are stored in a separate table or view</p></th>
</tr>
<tr class="header">
<th><p>Table or view name</p></th>
<th></th>
<th><p>(Delta table/view) The name of the table (or view) which contains
the primary keys of records with changes</p></th>
</tr>
<tr class="odd">
<th><p>Primary key column</p></th>
<th></th>
<th><p>(Delta table/view) The name of the column in the delta table (or
view) which contains the primary key of the record changed in the main
table</p></th>
</tr>
<tr class="header">
<th><p>Column</p></th>
<th></th>
<th><p>(DateTime column) The name of the column which contains the last
updated timestamp</p></th>
</tr>
</thead>
&#10;</table>
