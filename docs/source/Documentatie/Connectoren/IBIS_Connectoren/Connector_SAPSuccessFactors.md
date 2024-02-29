# SAP SuccessFactors

The SAP SuccessFactors module is capable of importing (full/delta) and
exporting employee data from and to SAP SuccessFactors through the OData
REST API.

## Parameters

|                Parameter               | Required |                                                                                         Description                                                                                         |
|:--------------------------------------|:--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OData URL                              | X        | The URL of the SuccessFactors endpoint                                                                                                                                                      |
| Username                               | X        | The HTTP basic authentication username                                                                                                                                                      |
| Password                               | X        | The HTTP basic authentication password                                                                                                                                                      |
| Left pad user ID                       |          | Can be used to fill up the userId property to a specified number of characters. This may come to use when the userId in IBIS is stored without the leading zero’s often seen in SAP systems |
| Padding total width                    |          | The total number of characters the userId property must become                                                                                                                              |
| Padding character                      |          | The character the userId property must be prepended with                                                                                                                                    |
| Enable photo support                   |          | When enabled, user photos will be fetched during import, and can be exported to SuccessFactors                                                                                              |
| Enable automatic photo resize          |          | Automatically resize the photo to 180x240 during export                                                                                                                                     |
| Photo name                             | X        | The name to use for photo objects handled by this connector                                                                                                                                 |
| Do not import users without department |          | When enabled, users without a department (value = N/A) will not be imported                                                                                                                 |
| SAP ID private phone                   |          | The SAP dropdown ID for the private phone number                                                                                                                                            |
| SAP ID private mobile phone            |          | The SAP dropdown ID for the private mobile phone number                                                                                                                                     |
| SAP ID business phone                  |          | The SAP dropdown ID for the business phone number                                                                                                                                           |
| SAP ID business mobile phone           |          | The SAP dropdown ID for the business mobile phone number                                                                                                                                    |
| Employee class mappings                |          | Contains a list of conversions for SAP employee class to IBIS employment type main group.<br> <br>Format: SAPID:IBISID;SAPID2:IBISID2                                                       |
| Employment type mappings               |          | Contains a list of conversions for SAP employement type to IBIS employment type subgroup.<br> <br>Format: SAPID:IBISID;SAPID2:IBISID2                                                       |

## Special properties

### \_photo

Photos are stored as separate objects in SuccessFactors. Since the
connector only supports 1 on 1 relations, the connector will query
SuccessFactors for the user photo with the name specified in the
connector settings and add it to the \_**photo** property of the user.

On export, the \_**photo** property will be downsized to 180\*240 and
added/updated in SuccessFactors. When the \_photo property is cleared
and a photo with *\[Photo name\]* exists in SuccessFactors it will be
deleted.

### \_ibisEmploymentTypeMainGroup

Contains the converted value of EmployeeClass using configuration
parameter **Employee class mappings**

### \_ibisEmploymentTypeSubGroup

Contains the converted value of EmploymentType using configuration
parameter **Employment type mappings**

### \_phone\_home

Contains the phone number where phoneType == **SAP ID private phone**

### \_phone\_home\_mobile

Contains the phone number where phoneType == **SAP ID private mobile
phone**

### \_phone\_primary

Contains the phone number where isPrimary == true

### \_phone\_work

Contains the phone number where phoneType == **SAP ID business phone**

### \_phone\_work\_mobile

Contains the phone number where phoneType == **SAP ID business mobile
phone**
