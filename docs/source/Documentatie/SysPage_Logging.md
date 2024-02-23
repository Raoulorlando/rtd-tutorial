# <span id="index"></span>Logging

Logging is handled by Log4net and written to the IBIS database in the
table dbo.Logentry. The log level is set to INFO by default, which means
the log will contain INFO, WARN and ERROR messages.

To view the log, browse to: ~/Logging

#### Debug logging

In case the default logging does not show enough information to
troubleshoot a problem, it's possible to enable DEBUG logging. Do this
with caution because DEBUG logging will create a huge amount of data in
the IBIS database and may seriously slow down your system. Whenever you
are done troubleshooting set the log level back to INFO.

To enable DEBUG logging:

1.  Open Log4Net.config in a text editor. This file is in the App\_Data
    folder.

2.  Search for the line:

    &lt;threshold value="INFO" /&gt;

    **and change it to:**

    &lt;threshold value="DEBUG" /&gt;

3.  Save the file. Debug logging is now enabled.

4.  Change the threshold back to INFO to disable DEBUG logging

#### Data cleanup

To configure the data cleanup settings for the log:

1.  Click on the **cog** (settings) icon in the top right corner of the
    page
2.  Click the **Data cleanup** tab
3.  Change the settings (see below)
4.  Click on the **Save and close&lt;/&gt;** button

The following settings are available for Data cleanup:

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="321"><p>Remove DEBUG log older than (days)(0 means
off)</p></td>
<td width="302"><p>If set, DEBUG log entries older than the specified
number of days will automatically be removed from the system</p></td>
</tr>
<tr class="even">
<td width="321"><p>Remove INFO log older than (days)(0 means
off)</p></td>
<td width="302"><p>If set, INFO log entries older than the specified
number of days will automatically be removed from the system</p></td>
</tr>
<tr class="odd">
<td width="321"><p>Remove WARN log older than (days)(0 means
off)</p></td>
<td width="302"><p>If set, WARN log entries older than the specified
number of days will automatically be removed from the system</p></td>
</tr>
<tr class="even">
<td width="321"><p>Remove ERROR log older than (days)(0 means
off)</p></td>
<td width="302"><p>If set, ERROR log entries older than the specified
number of days will automatically be removed from the system</p></td>
</tr>
</tbody>
</table>

#### Log source

IBIS will use a standard log source by default. To change it to an
alternative (SQL server) log source:

1.  Click on the **cog** (settings) icon in the top right corner of the
    page
2.  Click the **Log source** tab
3.  Change the **Log source** dropdownn list to **Alternative**
4.  Configure the necessary fields (see below)
5.  (Optional) Click on **Test connection** to test the connection
6.  Click on the **Save and close&lt;/&gt;** button

The following settings are available for an alternative log source:

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="142"><p>Sql server</p></td>
<td width="482"><p>The SQL server which contains the logging
database</p></td>
</tr>
<tr class="even">
<td width="142"><p>Sql server database name</p></td>
<td width="482"><p>The name of the logging database</p></td>
</tr>
<tr class="odd">
<td width="142"><p>Username</p></td>
<td width="482"><p>The username to connect to above SQL server /
database</p></td>
</tr>
<tr class="even">
<td width="142"><p>Password</p></td>
<td width="482"><p>The password of above username</p></td>
</tr>
<tr class="odd">
<td width="142"><p>Log tablename</p></td>
<td width="482"><p>The name of table which contains logentries</p></td>
</tr>
</tbody>
</table>

[Top](#index)

  
