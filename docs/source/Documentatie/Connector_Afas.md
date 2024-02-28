# Afas

The Afas module communicates with Afas Online through an *Afas Get
Connector*. The module supports Full Import only because Afas does not
provide a delta mechanism. Exporting data to Afas should be done by
using the IBIS workflow engine.

## Primary key

The primary key for objects delivered by this module is stored in the
\_***PrimaryKey*** property. The value of this property is calculated
during import using the ***Primary key expression*** parameter.

## Module parameters

|        Parameter       | Required |                                                                             Description                                                                             |
|:----------------------:|:--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|         API URL        |     X    |                 The URL to the Afas REST connector API. For example:<br>   _https://[customer id].rest.afas.online/profitrestservices/connectors_                 |
|        Token ID        |     X    |                                                           The security token used to authenticate to Afas                                                           |
|     Connector name     |     X    |                                                                    The name of the Get Connector                                                                    |
| Primary key expression |     X    | An expression used to format the primary key. This expression will be translated by the dynamic lookup module. For example:   <br><br>     §   {Employee}{Contract}-{OuCode} |
|       Batch size       |     X    |                                          The maximum number of objects to retrieve in each call to Afas. The default is 20.                                         |
|     OrderBy fields     |          |                                                                                                                                                                     |
|    RowFilter fields    |          |                                                                                                                                                                     |
|     RowFilter types    |          |                                                                                                                                                                     |
|    RowFilter values    |          |                                                                                                                                                                     |

 
