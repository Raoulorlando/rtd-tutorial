# Simons Voss LSM

The Simons Voss LSM connector can manage persons in the Simons Voss
locking system application. The connector supports import and export
operations, and has the ability to create a transponder for new persons.

## Parameters

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Authentication service URL</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The full URL to the authentication service API</p></th>
</tr>
<tr class="header">
<th><p>Management service URL</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The full URL to the management service API</p></th>
</tr>
<tr class="odd">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The username of the account to use to connect to LSM</p></th>
</tr>
<tr class="header">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of the above user account</p></th>
</tr>
<tr class="odd">
<th><p>Create transponder for new persons</p></th>
<th><p><strong> </strong></p></th>
<th><p>If enabled, a new transponder will be created for new person
objects in Simons Voss</p></th>
</tr>
<tr class="header">
<th><p>Transponder type for new transponders</p></th>
<th><p><strong> </strong></p></th>
<th><p>The type of transponder to create when <strong><em>Create
transponder for new persons</em></strong> is enabled</p></th>
</tr>
</thead>
&#10;</table>

## Special parameters

The following table describe the additional parameters and options
supported by this connector through an export flow.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>_param_InactiveTransponderGroupId</p>
<p> </p></th>
<th><p>The ID of the transponder group to assign when a person becomes
inactive. If set, the transponder will be moved to this group on update.
A value of 0 will not trigger the group assignment.</p></th>
</tr>
<tr class="header">
<th><p>_param_NewTransponderGroupId</p>
<p> </p></th>
<th><p>The ID of the transponder group to assign when a new person with
transponder is created. If set, the transponder will be moved to this
group after create. A value of 0 will not trigger the group
assignment.</p></th>
</tr>
<tr class="odd">
<th><p>Address</p></th>
<th><p>A transformation is applied to the Address field during export
and import. This transformation formats the field for use in Simons
Voss.</p>
<p>On export, the | character is replaced by a line-break. This way a
complete address exported as {street} {number}|{postalcode}|{city} will
be shown in Simons Voss as</p>
<p>{street} {number}</p>
<p>{postalcode}</p>
<p>{city}</p>
<p>On import, the line-breaks are replaced by a |, so IBIS will not
export the property again.</p></th>
</tr>
</thead>
&#10;</table>
