<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Facility<sup>2</sup>
Wish

# Facility<sup>2</sup> Wish

The Wish connector is capable of reading from- and writing to the Wish
API.

## Parameters

|              Parameter              | Required |                                                                Description                                                                |
|:-----------------------------------:|:--------:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
|               API URL               |     X    |                       The URL of the Wish system, without /API.    For example: https://wish3-api-test.facility2.nl                       |
|               Username              |     X    |                                         The username of the account to use when accessing the API                                         |
|               Password              |     X    |                                                       The password of above username                                                      |
| Translation file for function codes |          | Optional, the full path of a semicolon separated textfile (CSV) which contains function code translations. See chapter 9.8.1 for details. |
|  Target property for function code  |          |                                  Optional, the target property to apply the function code translation to                                  |
| Store location                      | X        | The resource URI for stores. For example:   partner/onboarding/v1/stores                                                                  |
|           RowFilter fields          |          |                                                                                                                                           |
|           RowFilter types           |          |                                                                                                                                           |
|           RowFilter values          |          |                                                                                                                                           |

## Function code translation

The Wish connector is capable of translating function codes to a desired
Wish format. In order to achieve this, you need to create a CSV file
with translations and alter the configuration settings to enable this
feature.

The CSV file must contain 2 columns. Column 1 will contain the IBIS
(lookup) value for the translation, column 2 will contain the Wish
value. The columns must be separated by a semicolon “;” and should not
contain text qualifiers.

Place the CSV file on a location that is accessible by the IBIS service
account. After that:

-   Set the full path to the CSV file in the module configuration
    property

**Translation file for function codes**

-   Set the target property for the translated value in the module
    configuration property

**Target property for function code**. This property should exist in
Wish. For example: **Duty**

-   Add an export attribute mapping to destination property
    **\_param\_FunctionCode**. The value expression should result in the
    function code value set in column 1 of the CSV
