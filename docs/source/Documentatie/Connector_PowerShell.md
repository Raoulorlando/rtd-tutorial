# PowerShell

The PowerShell module is capable of importing the results of a
PowerShell command

## Parameters

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Hostname</p></th>
<th></th>
<th><p>Optional, the name of the Windows or Exchange host to connect
to</p></th>
</tr>
<tr class="header">
<th><p>PowerShell Agent</p></th>
<th></th>
<th><p>Optional, the PowerShell agent to use. Cannot be used in
conjunction with a connector agent</p></th>
</tr>
<tr class="odd">
<th><p>Mode</p></th>
<th><p><strong>X</strong></p></th>
<th><p>Used to determine the shell URI if a host is set</p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The username of the account to use for authentication. This
cannot be the same as the IBIS app pool account</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of above user account</p></th>
</tr>
<tr class="header">
<th><p>Command</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The PowerShell command (one-liner) to execute. Dynamic
expressions may be used. Either command or script are required</p></th>
</tr>
<tr class="odd">
<th><p>Script</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The PowerShell script to execute. Dynamic expressions may be
used. Either command or script are required</p></th>
</tr>
<tr class="header">
<th><p>Identifier</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The name of the property to use as primary key</p></th>
</tr>
</thead>
&#10;</table>
