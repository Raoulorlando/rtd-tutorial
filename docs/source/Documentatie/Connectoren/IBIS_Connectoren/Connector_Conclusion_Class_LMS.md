# Conclusion Class LMS

The Class connector is capable of writing to the Class ImportService
endpoint.

## Parameters

|             Parameter            | Required |                                                                                Description                                                                                |
|:--------------------------------|:--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| API URL                          | X        | The URL of the Class system endpoint<br> <br> For example: http://server.tld/crmimport/CrmImportService.svc                                                               |
| Token                            | X        | The authorization token to use when making requests to Class                                                                                                              |
| Catalog ID                       | X        | The ID of the target catalog in Class                                                                                                                                     |
| Delay between requests (seconds) |          | In case the Class endpoint gets overflooded with requests, this setting can be used to wait a certain amount of seconds before sending the next request                   |
| Block employee on disconnect     |          | If set the employee object in Class will get the isBlocked property set to true when the object gets disconnected                                                         |
| Fill employment from iDossier    |          | If set the employments collection of the employee will be mapped from the available iDossiers in IBIS. See the mapping paragraph below for information on field mappings. |

## Employment mappings

|                                               iDossier property                                               | Employment property |                                                                                Description                                                                                |
|:-------------------------------------------------------------------------------------------------------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _01_20_Dienstverband_DienstverbandNummer<br> <br>**OR**<br> <br>_01_75_Dienstverband_SectoraalDienstverbandNummer |         code        | The URL of the Class system endpoint<br> <br> For example: http://server.tld/crmimport/CrmImportService.svc                                                               |
|                                   _04_38_Organisatie_Personeelsgebiednummer                                   |      companyId      | The authorization token to use when making requests to Class                                                                                                              |
|                                      _14_20_Kostenplaats_KostenplaatsCode                                     |      costCentre     | The ID of the target catalog in Class                                                                                                                                     |
|                                     _02_41_Plaatsing_DatumEindeGeldigheid                                     |    departureDate    | In case the Class endpoint gets overflooded with requests, this setting can be used to wait a certain amount of seconds before sending the next request                   |
|                                    _01_25_Dienstverband_FunctieOmschrijving                                   |       jobTitle      | If set the employee object in Class will get the isBlocked property set to true when the object gets disconnected                                                         |
|                                                  CreatedDate                                                  |     creationDate    | If set the employments collection of the employee will be mapped from the available iDossiers in IBIS. See the mapping paragraph below for information on field mappings. |
|                                               OrganisationNumber                                              |      department     |                                                                                                                                                                           |

 
