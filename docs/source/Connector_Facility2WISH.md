<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / Facility<sup>2</sup>
Wish

# Facility<sup>2</sup> Wish

The Wish connector is capable of reading from- and writing to the Wish
API.

## Parameters

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Parameter</th>
<th class="text-center">Required</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><p>API URL</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The URL of the Wish system, without /API.<br />
<br />
For example: https://wish3-api-test.facility2.nl</p></th>
</tr>
<tr class="header">
<th><p>Username</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The username of the account to use when accessing the
API</p></th>
</tr>
<tr class="odd">
<th><p>Password</p></th>
<th><p><strong>X</strong></p></th>
<th><p>The password of above username</p></th>
</tr>
<tr class="header">
<th><p>Translation file for function codes</p></th>
<th><p><strong> </strong></p></th>
<th><p>Optional, the full path of a semicolon separated textfile (CSV)
which contains function code translations. See chapter 9.8.1 for
details.</p></th>
</tr>
<tr class="odd">
<th><p>Target property for function code</p></th>
<th><p><strong> </strong></p></th>
<th><p>Optional, the target property to apply the function code
translation to</p></th>
</tr>
</thead>
&#10;</table>

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
