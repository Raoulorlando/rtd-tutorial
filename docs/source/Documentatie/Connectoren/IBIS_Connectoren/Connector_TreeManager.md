# TreeManager

The TreeManager module is capable of importing nodes from- and exporting
nodes to a TreeManager tree.

During import, a distinction is made between direct- and inherited
attribute values. This is done to make sure inherited attributes don’t
get mixed up with direct attributes during import and export.

All attributes (direct and inherited) are added as effective to the node
on import. The name of the attribute is preceded by “effective.”. Direct
attributes are also added, preceded with “attribute.”.

For example, when a node has 1 direct attribute called Name, and 2
inherited attributes called Owner and Location, the following will be
available:

-   attribute.Name
-   effective.Name
-   effective.Owner
-   -effective.Location

To export an attribute value, always use the “attribute.” variant.
“effective.” attributes will never be exported to TreeManager. When
importing to IBIS, use the “effective.” variant. This way, you don’t
have so create 2 import flows, and always flow the correct value to
IBIS.

## Parameters

|       Parameter       | Required |                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                  |
|:---------------------|:--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        API URL        |     X    |                                                                                                                                                                                                                The URL of the TreeManager API, including the /API part.<br> <br>For example: https://domain.tld/TreeManager/API                                                                                                                                                                                                                |
|        API key        |     X    |                                                                                                                                                                                                                                              The API key to use for communication with TreeManager                                                                                                                                                                                                                                             |
|      API password     |     X    |                                                                                                                                                                                                                                                          The password of above API key                                                                                                                                                                                                                                                         |
|        Tree ID        |     X    |                                                                                                                                                                                                                                                          The ID of the Tree to manage                                                                                                                                                                                                                                                          |
|    Static Parent ID   |          |                                                                                                                                                                                              If set, only childs of this parent will be imported during a delta and/or full import. On export the ParentNodeId of nodes will be set to this value                                                                                                                                                                                              |
|     OAuth - App ID    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|   OAuth - Client ID   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OAuth - Client secret |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|   OAuth - Tenant ID   |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|   Primary key method  |     X    | The method to use for identifying nodes in the Tree and how to relate to the parent object. In case a node identifier is not set during export it will be generated by TreeManager.<br> <br> <br>**Id**<br> <br>Type                         : Guid<br> <br>Parent id property   : ParentId<br>  <br> <br> <br>**ExternalId**<br> <br>Type                         : Integer<br> <br>Parent id property   : ParentExternalId <br> <br> <br>**ExternalKey**<br> <br>Type                         : String<br> <br>Parent id property   : ParentExternalKey  |
