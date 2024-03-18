# Topdesk

The Topdesk module communicates with Topdesk through the Topdesk REST
API. The module supports full import and export of person cards.

## Primary key

The primary key for objects delivered by this module is stored in the
***id*** property. The value of this property is the string
representation of the Topdesk id property, which is a Guid.

|      Parameter     | Required |                                               Description                                               |
|:-------------------|:--------:|:--------------------------------------------------------------------------------------------------------|
|         Url        |     X    |                                        The URL of the Topdesk API                                       |
|      Username      |     X    |                                     The username for the connection                                     |
|      Password      |     X    |                                      The password of above username                                     |
|   EnableArchiving  |          |     If set, archiving will be handled in the module. See the archiving chapter for more information     |
|   ArchiveReasonId  |          | If archiving is enabled, this property must be set, and contain the (Guid) value for the archive reason |
| Managed properties |          |          Branch only, comma separated list of properties that will be managed by this connector         |

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
