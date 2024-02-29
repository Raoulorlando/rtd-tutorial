# Microsoft SQL Connector

The SQL-module communicates with a Microsoft SQL Server table or view.

-   In order to update a view, it must not span multiple tables.
-   Export is only supported when a primary key column is used, not when
    using a primary key expression.

## Primary key

The primary key for objects delivered by this module is defined in the
***Key column*** or the ***Primary key expression*** parameter in the
module settings.

|        Parameter       | Required |                                                                                                                                              Description                                                                                                                                              |
|:----------------------|:--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    Connectionstring    |     X    |                                                                            The connection string used for communication with the database.<br> <br>See https://www.connectionstrings.com/sql-server/ for more information.                                                                            |
|  Authentication method |          |                                                                                                                     The type of authentication to use for connecting to SQL server                                                                                                                    |
|        Username        |          |                                                                                                                                    The username for the connection                                                                                                                                    |
|        Password        |          |                                                                                                                                      The password for above user                                                                                                                                      |
|      Table or view     |     X    |                                                                                                                    The name of the table or view to load data from / write data to                                                                                                                    |
|       Key column       |     X    |                                                                                                                    The name of the column to use as primary key for this connector                                                                                                                    |
| Primary key expression |     X    | An expression used to format the primary key. This expression will be translated by the dynamic lookup module. For example:<br> <br>§   {Employee}{Contract}-{OuCode}<br> <br>When this method is used, a _PrimaryKey property will be added to each imported object containing the calculated value. |
|      WHERE filter      |          |                                                                                         A where statement used to filter data from the result set. This should be the complete statement and start with WHERE                                                                                         |
|     ORDER BY clause    |          |                                                                                                 An order by clause to order the result set. This should be the complete clause and start with ORDER BY                                                                                                |
|  Enable delta support  |          |                                                                                                                   If checked, the module will support delta import (once configured)                                                                                                                  |
|         Method         |          |                                       DateTime column - The table or view contains a DateTime column which is updated during add/modify of the record<br> <br>Delta table/view - The primary keys of records with changes are stored in a separate table or view                                      |
|   Table or view name   |          |                                                                                               (Delta table/view) The name of the table (or view) which contains the primary keys of records with changes                                                                                              |
|   Primary key column   |          |                                                                             (Delta table/view) The name of the column in the delta table (or view) which contains the primary key of the record changed in the main table                                                                             |
|         Column         |          |                                                                                                           (DateTime column) The name of the column which contains the last updated timestamp                                                                                                          |
