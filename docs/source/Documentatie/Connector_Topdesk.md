# Topdesk

The Topdesk module communicates with Topdesk through the Topdesk REST
API. The module supports full import and export of person cards.

## Primary key

The primary key for objects delivered by this module is stored in the
***id*** property. The value of this property is the string
representation of the Topdesk id property, which is a Guid.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>Url</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The URL of the Topdesk API</p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The username for the connection</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of above username</p></th>
</tr>
<tr class="header">
<th><p>EnableArchiving</p></th>
<th><p><strong> </strong></p></th>
<th><p>If set, archiving will be handled in the module. See the
archiving chapter for more information</p></th>
</tr>
<tr class="odd">
<th><p>ArchiveReasonId</p></th>
<th><p><strong> </strong></p></th>
<th><p>If archiving is enabled, this property must be set, and contain
the (Guid) value for the archive reason</p></th>
</tr>
<tr class="header">
<th><p>Managed properties</p></th>
<th></th>
<th><p>Branch only, comma separated list of properties that will be
managed by this connector</p></th>
</tr>
</thead>
&#10;</table>

## Archiving

The Topdesk module is capable of archiving and unarchiving Topdesk
person cards. In order to achieve this, ***EnableArchiving*** must me
enabled in the module configuration, and a valid ***ArchiveReasonId***
must be specified.

If both prerequisites are met, archiving can be triggered using an
export flow to attribute:

-   ***\_param\_archive***

If the value of this attribute is true, the person card will be
archived.

If the value of this attribute is false, the person card will be
unarchived.

An example export flow for archiving, based on the end date of an
aliasDossier, is:

**{?{?{\_09\_41\_Alias\_DatumEindeGeldigheid},dateistodayorfuture},iif(false,True,False)}**

## Branch hierarchy

When exporting branches, it's possible to keep the IBIS organizational
hierarchy in Topdesk.

To achieve this, import the Branch Id back to a (dynamic) property of
the organization. Then export Parent.\[propertyname\] to headBranch.id.
