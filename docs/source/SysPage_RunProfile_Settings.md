<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> /
<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_RunProfile">Run profiles /</a> Run profile
settings

##### <span id="index"></span>Run profile settings

###### General settings

<table class="table table-bordered">
<thead class="table-secondary">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>The name of run profile</td>
</tr>
<tr class="even">
<td>Schedule (CRON)</td>
<td>The schedule</td>
</tr>
<tr class="odd">
<td>Temporarily turn off run profile</td>
<td>If set, the run profile will not be executed</td>
</tr>
</tbody>
</table>

###### Steps

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="table-secondary">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td><p>The type of operation. Choose from:</p>
<ul>
<li>ABAC: execute a background task in ABAC</li>
<li>Connector: execute a connector profile</li>
<li>BackgroundTask: execute a configured background task</li>
<li>PowerShellScript: execute a PowerShell script</li>
<li>Workflow: execute a configured workflow</li>
</ul></td>
</tr>
<tr class="even">
<td>ABAC</td>
<td><ul>
<li>Task: the task to execute</li>
<li>Timeout: the time in minutes IBIS will wait for ABAC to finish</li>
</ul></td>
</tr>
<tr class="odd">
<td>Connector</td>
<td><ul>
<li>Connector: the connector to execute</li>
<li>Operation: the operation to execute on the connector</li>
</ul></td>
</tr>
<tr class="even">
<td>BackgroundTask</td>
<td><ul>
<li>Background task: the task to execute. This task must be configured
on the <a href="BackgroundTask" target="_blank">background tasks</a>
page in order to be selectable</li>
</ul></td>
</tr>
<tr class="odd">
<td>Workflow</td>
<td><ul>
<li>Workflow: The workflow to execute</li>
</ul></td>
</tr>
<tr class="even">
<td>PowerShellScript</td>
<td><ul>
<li>Agent: optional, the agent the script must be executed on</li>
<li>Hostname: optional, the machine the script must be executed on</li>
<li>Username: the username of the account that must be used to execute
the script</li>
<li>Password: the password of above username</li>
<li>Script: the script to execute</li>
</ul></td>
</tr>
<tr class="odd">
<td>Disabled</td>
<td>If set, the run profile will not be executed</td>
</tr>
<tr class="even">
<td>Abort on error</td>
<td>If set, subsequent steps will not be executed in case an error
occurs</td>
</tr>
</tbody>
</table>
