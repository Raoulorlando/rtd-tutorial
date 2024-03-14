# <span id="index"></span>Data resolution and supported functions

<!-- -   [Data resolution](#Data%20resolution)
-   [Functions](#Functions) -->

```{eval-rst}.. contents:: Table of Contents
```

## <span id="Data resolution"></span>Data resolution

Data resolution provides the ability to translate an expression to an
actual value.

|      Markup     |                                  Result                                 |                   Example markup                   |                                                                                             Example result                                                                                            |
|:---------------|:-----------------------------------------------------------------------|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       {x}       |         The value of the property named x of the incoming object        |                    {DisplayName}                   |                                                                      The value of the DisplayName property of the incoming object                                                                     |
|       {@x}      |                         The value of argument x                         |                    {@Argument1}                    |                                                                                    The value of argument Argument1                                                                                    |
|    {?{x},f()}   | The result of function f performed on property x of the incoming object |                See section Functions               |                                                                                         See section Functions                                                                                         |
|   {?{@x},f()}   |             The result of function f performed on argument x            |                See section Functions               |                                                                                         See section Functions                                                                                         |
|     ["{x}"]     |                     A collection (array) of objects                     |                 ["{a}","{b}","{c}"]                |                                                                   An array of strings with the values of the properties a, b and c.                                                                   |
| [\{"y":"{y}"\}] |                   A collection (array) of dictionaries                  | [\{"a":"{a}", "b":"{b}"\}, \{ "a":"1", "b":"2" \}] | An array of 2 dictionaries with the properties a and b<br> It is important to escape the object holders (curly braces), otherwise they will be parsed as a property and the array will not be created |

In case the value between the curly braces cannot be translated to a
property, the name as specified will be returned. For example, in case
***{DisplayName1}*** is specified and this property does not exist on
the incoming object, ***DisplayName1*** *will be returned.*

* *

In case you want a curly brace in the return value, it has to be
prefixed with a backslash.

For example:

-   *This is an example using \\DisplayName\\*

will return

-   *This is an example using {DisplayName}*

## Linked objects

It is possible to reference linked objects using data resolution. A
linked object is specified using a dot (.) in the markup. For example,
{Tree.DisplayName} will return the DisplayName of the Tree for the
incoming node.

The following table describes the relations in the different products.

|   Product   |       Source       |                                                                                 Target                                                                                |          Object markup          |
|:-----------:|:------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------:|
| TreeManager | Attribute          | Attribute Type                                                                                                                                                        | Type                            |
| TreeManager | Attribute Value    | Attribute                                                                                                                                                             | Attribute                       |
| TreeManager | Attribute Value    | Node                                                                                                                                                                  | Node                            |
| TreeManager | Node               | Node Type                                                                                                                                                             | NodeType                        |
| TreeManager | Node               | Parent Node                                                                                                                                                           | Parent                          |
| TreeManager | Node               | Childs (direct)                                                                                                                                                       | Childs                          |
| TreeManager | Node               | Childs (recursive)                                                                                                                                                    | ChildsRecursive                 |
| TreeManager | Node               | Tree                                                                                                                                                                  | Tree                            |
| IBIS        | AliasDossier       | List<ApplicationDossierProduct>                                                                                                                                       | Assets                          |
| IBIS        | AliasDossier       | List<string>                                                                                                                                                          | EmailAddresses                  |
| IBIS        | AliasDossier       | List<string>                                                                                                                                                          | EmailAddresses_IncludingPrimary |
| IBIS        | AliasDossier       | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | AliasDossier       | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | AliasDossier       | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | AliasDossier       | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | AliasDossier       | IdentityDossier                                                                                                                                                       | Identity                        |
| IBIS        | AliasDossier       | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | AliasDossier       | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | AliasDossier       | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | AliasDossier       | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | AliasDossier       | Manager IDossier                                                                                                                                                      | Manager                         |
| IBIS        | AliasDossier       | List<IDossier> of Managers                                                                                                                                            | Managers                        |
| IBIS        | AliasDossier       | Organisatie                                                                                                                                                           | Organisation                    |
| IBIS        | AliasDossier       | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | AliasDossier       | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | AliasDossier       | List<SmtpAlias>                                                                                                                                                       | SmtpAliasses                    |
| IBIS        | AliasDossier       | SysDossierStatus                                                                                                                                                      | Status                          |
| IBIS        | AliasDossier       | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | AliasDossier       | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | AliasDossier       | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | AliasDossier       | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | ApplicationDossier | Requester e-mail                                                                                                                                                      | AanvragerEmail                  |
| IBIS        | ApplicationDossier | List<ApplicationDossierProduct>                                                                                                                                       | Assets                          |
| IBIS        | ApplicationDossier | SysIbisUser                                                                                                                                                           | CreatedByUser                   |
| IBIS        | ApplicationDossier | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | ApplicationDossier | SysIbisUser                                                                                                                                                           | ModifiedByUser                  |
| IBIS        | ApplicationDossier | Organisatie                                                                                                                                                           | Organisation                    |
| IBIS        | ApplicationDossier | List<ApplicationDossierProduct>                                                                                                                                       | Products                        |
| IBIS        | EpicDossier        | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | EpicDossier        | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | EpicDossier        | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | EpicDossier        | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | EpicDossier        | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | EpicDossier        | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | EpicDossier        | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | EpicDossier        | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | EpicDossier        | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | EpicDossier        | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | EpicDossier        | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | EpicDossier        | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | EpicDossier        | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | EpicDossier        | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | FmhDossier         | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | FmhDossier         | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | FmhDossier         | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | FmhDossier         | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | FmhDossier         | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | FmhDossier         | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | FmhDossier         | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | FmhDossier         | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | FmhDossier         | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | FmhDossier         | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | FmhDossier         | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | FmhDossier         | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | FmhDossier         | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | FmhDossier         | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | IdentityDossier    | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | IdentityDossier    | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | IdentityDossier    | List<ApplicationDossierProduct>                                                                                                                                       | Assets                          |
| IBIS        | IdentityDossier    | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | IdentityDossier    | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | IdentityDossier    | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | IdentityDossier    | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | IdentityDossier    | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | IdentityDossier    | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | IdentityDossier    | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | IdentityDossier    | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | IdentityDossier    | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | IdentityDossier    | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | IdentityDossier    | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | IdentityDossier    | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | IDossier           | Aliasdossier (Valid aliasdossier present? The first valid aliasdossier with the earliest startdate. Otherwise the first invalid aliasdossier with the latest enddate) | Alias                           |
| IBIS        | IDossier           | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | IDossier           | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | IDossier           | List<ApplicationDossierProduct>                                                                                                                                       | Assets                          |
| IBIS        | IDossier           | Contract                                                                                                                                                              | Contract                        |
| IBIS        | IDossier           | The description of the employment group                                                                                                                               | EmploymentGroupDescription      |
| IBIS        | IDossier           | The description of the employment type                                                                                                                                | EmploymentTypeDescription       |
| IBIS        | IDossier           | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | IDossier           | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | IDossier           | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | IDossier           | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | IDossier           | IdentityDossier                                                                                                                                                       | Identity                        |
| IBIS        | IDossier           | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | IDossier           | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | IDossier           | Lokatie                                                                                                                                                               | Lokatie                         |
| IBIS        | IDossier           | Manager iDossier                                                                                                                                                      | Manager                         |
| IBIS        | IDossier           | Manager e-mail                                                                                                                                                        | ManagerEmail                    |
| IBIS        | IDossier           | List<IDossier> of Managers                                                                                                                                            | Managers                        |
| IBIS        | IDossier           | Employee e-mail                                                                                                                                                       | MedewerkerEmail                 |
| IBIS        | IDossier           | Organisation                                                                                                                                                          | Organisation                    |
| IBIS        | IDossier           | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | IDossier           | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | IDossier           | SysDossierStatus                                                                                                                                                      | Status                          |
| IBIS        | IDossier           | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | IDossier           | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | IDossier           | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | IDossier           | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | Organisatie        | Parent Organisatie                                                                                                                                                    | Parent                          |
| IBIS        | PbsDossier         | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | PbsDossier         | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | PbsDossier         | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | PbsDossier         | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | PbsDossier         | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | PbsDossier         | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | PbsDossier         | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | PbsDossier         | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | PbsDossier         | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | PbsDossier         | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | PbsDossier         | Organisatie                                                                                                                                                           | Organisation                    |
| IBIS        | PbsDossier         | SysDossierStatus                                                                                                                                                      | Status                          |
| IBIS        | PbsDossier         | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | PbsDossier         | List<TgDossier>                                                                                                                                                       | TgDossiers                      |
| IBIS        | PbsDossier         | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | PbsDossier         | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | TgDossier          | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | TgDossier          | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | TgDossier          | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | TgDossier          | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | TgDossier          | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | TgDossier          | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | TgDossier          | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | TgDossier          | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | TgDossier          | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | TgDossier          | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | TgDossier          | Organisatie                                                                                                                                                           | Organisation                    |
| IBIS        | TgDossier          | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | TgDossier          | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | TgDossier          | WidDossier                                                                                                                                                            | WidDossier                      |
| IBIS        | TgDossier          | List<WidDossier>                                                                                                                                                      | WidDossiers                     |
| IBIS        | WidDossier         | AliasDossier                                                                                                                                                          | AliasDossier                    |
| IBIS        | WidDossier         | List<AliasDossier>                                                                                                                                                    | AliasDossiers                   |
| IBIS        | WidDossier         | EpicDossier                                                                                                                                                           | EpicDossier                     |
| IBIS        | WidDossier         | List<EpicDossier>                                                                                                                                                     | EpicDossiers                    |
| IBIS        | WidDossier         | FmhDossier                                                                                                                                                            | FmhDossier                      |
| IBIS        | WidDossier         | List<FmhDossier>                                                                                                                                                      | FmhDossiers                     |
| IBIS        | WidDossier         | IdentityDossier                                                                                                                                                       | IdentityDossier                 |
| IBIS        | WidDossier         | List<IdentityDossier>                                                                                                                                                 | IdentityDossiers                |
| IBIS        | WidDossier         | IDossier                                                                                                                                                              | IDossier                        |
| IBIS        | WidDossier         | List<IDossier>                                                                                                                                                        | IDossiers                       |
| IBIS        | WidDossier         | PbsDossier                                                                                                                                                            | PbsDossier                      |
| IBIS        | WidDossier         | List<PbsDossier>                                                                                                                                                      | PbsDossiers                     |
| IBIS        | WidDossier         | TgDossier                                                                                                                                                             | TgDossier                       |
| IBIS        | WidDossier         | List<TgDossier>                                                                                                                                                       | TgDossiers                      |


## <span id="Functions"></span>Functions

Functions can be used to perform checks or transformations on data
present in a property of the incoming object or an argument.

Functions are specified using the following markup:

-   {? {propertyname/argument} function(params)}

<u>NOTE: Before 2018-03-23, functions were specified using the dollar
sign ($). This was causing UI errors, therefore it’s changed to a
questionmark.</u>

<u> </u>

|            Examples            |                                                                                                            |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------|
| {?{DisplayName},substring(10)} | returns the first 10 characters of the DisplayName property of the object specified in the workflow content| 
|    {?{@arg0},substring(10)}    |                 returns the first 10 characters of the string contained in the arg0 argument               | 

### GetDate

This function can be used to Extract day|month|year|hour|minutes|seconds
according to specified format. If no format is specified, the format of
IBIS settings is used.

|    Parameters   |          |                                                                                                                                                                  |
|:----------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Date / Datetime | Required |                                                     The date or datetime to extract the (formatted) date from                                                    |
|      Format     | Optional | dd-MM-yyyy \| d-M-yyyy \| yyyy \| MM \| hh:mm:ss<br> <br>Other types of format specifiers can be found in the custom date and time format strings documentation. |

|              Examples             |                         |                         |                         |
|:----------------------------------|:------------------------|:------------------------|:------------------------|
|             **Markup**            |    **Incoming value**   |     **Result value**    |     **IBIS setting**    |
|      {?{EndDate}, GetDate()}      | 31-12-2021 12:00:01.000 | 31-12-2021 12:00:01.000 | dd-MM-yyyy HH:mm:ss.fff |
| {?{EndDate}, GetDate(dd-MM-yyyy)} | 31-12-2021 12:00:01.000 |        31-12-2021       | dd-MM-yyyy HH:mm:ss.fff |
|  {?{EndDate}, GetDate(d-M-yyyy)}  | 01-01-2021 12:00:01.000 |         1-1-2021        | dd-MM-yyyy HH:mm:ss.fff |
|    {?{EndDate}, GetDate(yyyy)}    | 01-01-2021 12:00:01.000 |           2021          | dd-MM-yyyy HH:mm:ss.fff |
|     {?{EndDate}, GetDate(MM)}     | 01-01-2021 12:00:01.000 |            01           | dd-MM-yyyy HH:mm:ss.fff |
|  {?{EndDate}, GetDate(HH:mm:ss)}  | 01-01-2021 12:00:01.000 |         12:00:01        | dd-MM-yyyy HH:mm:ss.fff |

* *

### GetDay

This function can be used to extract the day from a date or datetime
field (2 numbers).

|    Parameters   |          |                                              |
|:----------------|:---------|:---------------------------------------------|
| Date / Datetime | Required | The date or datetime to extract the day from |
|      Format     | Optional |                    d \| dd                   |

|         Examples        |                     |                  |
|:------------------------|:--------------------|:-----------------|
|        **Markup**       |  **Incoming value** | **Result value** |
|  {?{EndDate},GetDay()}  | 31-12-2021 12:10:00 |        31        |
|  {?{EndDate},GetDay()}  |      31-12-2021     |        31        |
|  {?{EndDate},GetDay()}  |      01-01-2021     |         1        |
| {?{EndDate},GetDay(dd)} |      01-01-2021     |        01        |

* *

### GetMonth

This function can be used to extract the month from a date or datetime
field (2 numbers).

|        Parameters       |            |                                                |
|:------------------------|:-----------|:-----------------------------------------------|
|     Date / Datetime     |  Required  | The date or datetime to extract the month from |
|          Format         |  Optional  |                     M \| MM                    |
|  {?{EndDate},GetDay()}  | 31-12-2021 |                       31                       |
|  {?{EndDate},GetDay()}  | 01-01-2021 |                        1                       |
| {?{EndDate},GetDay(dd)} | 01-01-2021 |                       01                       |

|          Examples         |                     |              |
|:-------------------------:|:-------------------:|:------------:|
|         **Markup**        |  **Incoming value** | **Result value** |
|  {?{EndDate},GetMonth()}  | 31-12-2021 12:10:00 |        12        |
|  {?{EndDate},GetMonth()}  |      31-12-2021     |        12        |
|  {?{EndDate},GetMonth()}  |      31-01-2021     |         1        |
| {?{EndDate},GetMonth(MM)} |      31-01-2021     |        01        |

* *

### GetYear

This function can be used to extract the year from a date or datetime
field (4 numbers).

|    Parameters   |          |                                               |
|:----------------|:---------|:----------------------------------------------|
| Date / Datetime | Required | The date or datetime to extract the year from |
|      Format     | Optional |                   yy \| yyyy                  |

|          Examples          |                     |              |
|:---------------------------|:--------------------|:-------------|
|           Markup           |    Incoming value   | Result value |
|   {?{EndDate},GetYear()}   | 31-12-2021 12:10:00 |     2021     |
|   {?{EndDate},GetYear()}   |      31-12-2021     |     2021     |
|  {?{EndDate},GetYear(yy)}  |      31-12-2021     |      21      |
| {?{EndDate},GetYear(yyyy)} |      31-12-2021     |     2021     |

* *

### IsIndefiniteDate

This function checks if a date or datetime field has the year 9999.

|    Parameters   |          |                                                            |
|:----------------|:---------|:-----------------------------------------------------------|
| Date / Datetime | Required | The date or datetime to check if it contains the year 9999 |

|             Examples            |                     |                     |
|:--------------------------------|:--------------------|:--------------------|
|            **Markup**           |  **Incoming value** |   **Result value**  |
| {?{EndDate},IsIndefiniteDate()} | 31-12-9999 12:10:00 |         True        |
| {?{EndDate},IsIndefiniteDate()} |      31-12-2021     |        False        |

* *

### IsNull

This function can be used to replace a null (or empty) value with
another value.

|     Parameters    |          |                                                                 |
|:-----------------:|:--------:|:---------------------------------------------------------------:|
| Replacement value | Required | The value to replace the input with in case it is null or empty |

* *

### Substring

This function can be used to select a part of the incoming string.

-   The index of the first character of the incoming string is always 0

<!-- -->

-   In case *length* is greater then the difference between *start* and
    the length of the incoming string, everything between start and the
    end of the string will be returned

<!-- -->

-   In case length is not specified, everything between start and the
    end of the string will be returned

| Parameters |          |                                                                                       |
|:----------:|:--------:|:-------------------------------------------------------------------------------------:|
|    Start   | Required | Specifies at which position to start. 0 is the first character of the incoming string |
|   Length   | Optional |                       Specifies the number of characters to read                      |

|             Examples            |                    |                  |
|:--------------------------------|:-------------------|:-----------------|
|            **Markup**           | **Incoming value** |   **Result value**   |
|  {?{DisplayName},substring(0)}  |  Test Displayname  |    Test DisplayName  |
|  {?{DisplayName},substring(5)}  |  Test Displayname  |      DisplayName     |
|  {?{DisplayName},substring(12)} |  Test Displayname  |         name         |
| {?{DisplayName},substring(0,4)} |  Test Displayname  |         Test         |
| {?{DisplayName},substring(5,7)} |  Test Displayname  |        Display       |

* *

### IIF

This function can be used to make a decision based on the value of the
incoming property.

| Parameters |          |                                                                            |
|:-----------|:---------|:---------------------------------------------------------------------------|
| expression | Required |               The value to compare the incoming property with              |
|  truePart  | Required |     The return value in case the incoming property and expression match    |
|  falsePart | Required | The return value in case the incoming property and expression do not match |

|                          Examples                         |                    |                          |
|:----------------------------------------------------------|:-------------------|:-------------------------|
|                         **Markup**                        | **Incoming value** |     **Result value**     |
|     {?{DisplayName},iif(Test Displayname,Waar,Onwaar)}    |  Test Displayname  |           Waar           |
|           {?{DisplayName},iif(Test,Waar,Onwaar)}          |  Test Displayname  |          Onwaar          |
| {?{DisplayName},iif(Test Displayname,{Id},{DisplayName})} |  Test Displayname  | The value of property Id |

* *

### StartsWith

This function can be used to determine if the incoming string starts
with the specified value.

|                         Parameters                        |                  |                                                                                    |
|:----------------------------------------------------------|:-----------------|:-----------------------------------------------------------------------------------|
|                         expression                        |     Required     |               The value which the incoming property has to start with              |
|                       caseSensitive                       |     Optional     | false to turn off case sensitivity. In case not specified, case sensitivity is on. |
|           {?{DisplayName},iif(Test,Waar,Onwaar)}          | Test Displayname |                                       Onwaar                                       |
| {?{DisplayName},iif(Test Displayname,{Id},{DisplayName})} | Test Displayname |                              The value of property Id                              |

|                 Examples                |                  |              |
|:----------------------------------------|:-----------------|:-------------|
|                  Markup                 |  Incoming value  | Result value |
|    {?{DisplayName},startswith(Test)}    | Test Displayname |     true     |
|  {?{DisplayName},startswith(Test,true)} | Test Displayname |     true     |
| {?{DisplayName},startswith(Test,false)} | Test Displayname |     true     |
|    {?{DisplayName},startswith(test)}    | Test Displayname |     false    |
|  {?{DisplayName},startswith(test,true)} | Test Displayname |     false    |
| {?{DisplayName},startswith(test,false)} | Test Displayname |     true     |

* *

### EndsWith

This function can be used to determine if the incoming string ends with
the specified value.

|   Parameters  |          |                                                                                    |
|:--------------|:---------|:-----------------------------------------------------------------------------------|
|   expression  | Required |                The value which the incoming property has to end with               |
| caseSensitive | Optional | false to turn off case sensitivity. In case not specified, case sensitivity is on. |

|                Examples               |                    |                  |
|:--------------------------------------|:-------------------|:-----------------|
|                **Markup**             | **Incoming value** | **Result value** |
|    {?{DisplayName},endswith(name)}    |  Test Displayname  |       true       |
|  {?{DisplayName},endswith(name,true)} |  Test Displayname  |       true       |
| {?{DisplayName},endswith(name,false)} |  Test Displayname  |       true       |
|    {?{DisplayName},endswith(Name)}    |  Test Displayname  |       false      |
|  {?{DisplayName},endswith(Name,true)} |  Test Displayname  |       false      |
| {?{DisplayName},endswith(Name,false)} |  Test Displayname  |       true       |

* *

### Trim

This function can be used to trim spaces at the beginning and the end of
the incoming string.

|            Parameters           |
|:-------------------------------:|
| This function has no parameters |

|         Examples        |                                             |                  |
|:------------------------|:--------------------------------------------|:-----------------|
|        **Markup**       | **Incoming value (quotes for readability)** | **Result value** |
| {?{DisplayName},trim()} |               Test Displayname              | Test Displayname |
| {?{DisplayName},trim()} |               Test Displayname              | Test Displayname |

* *

### DateFormat

This function can be used to convert the format of the incoming date to
another format.

|  Parameters  |          |                                 |
|:-------------|:---------|:--------------------------------|
|  inputFormat | Required | The format of the incoming date |
| outputFormat | Required |    The desired output format    |

|                           Examples                          |                     |                  |
|:------------------------------------------------------------|:--------------------|:-----------------|
|                          **Markup**                         |  **Incoming value** | **Result value** |
| {?{CreatedDate},dateformat(MM/dd/yyyy HH:mm:ss,dd-MM-yyyy)} | 11/13/2017 00:00:00 |    13-11-2017    |

* *

### AddTime

This function adds a timespan to an existing DateTime object

| Parameters |          |                                              |
|:-----------|:---------|:---------------------------------------------|
|    Days    | Required |   The number of days to add to the DateTime  |
|    Hours   | Optional |  The number of hours to add to the DateTime  |
|   Minutes  | Optional | The number of minutes to add to the DateTime |
|   Seconds  | Optional | The number of seconds to add to the DateTime |

|                       Examples                       |                    |                                          |
|:-----------------------------------------------------|:-------------------|:-----------------------------------------|
|                      **Markup**                      | **Incoming value** | **Result value (in DateTime structure)** |
|     {?{?,code(System.DateTime,Today)},addTime(1)}    |                    |                 Tomorrow                 |
|    {?{?,code(System.DateTime,Today)},addTime(-1)}    |                    |                 Yesterday                |
|    {?{?,code(System.DateTime,Today)},addTime(1,1)}   |                    |            Tomorrow, 01:00 AM            |
|   {?{?,code(System.DateTime,Today)},addTime(1,1,1)}  |                    |            Tomorrow, 01:01 AM            |
|  {?{?,code(System.DateTime,Today)},addTime(1,1,1,1)} |                    |           Tomorrow, 01:01:01 AM          |
| {?{?,code(System.DateTime,Today)},addTime(-1,1,1,1)} |                    |          Yesterday, 01:01:01 AM          |

* *

### Code

This function returns the value of a field, property or method in code
(using reflection).

|       Parameters      |          |                                                                                |
|:----------------------|:---------|:-------------------------------------------------------------------------------|
|         Class         | Required | The name of the (static) class that contains the field/property/method to call |
| Field/Property/Method | Required |           The name of the (static) field, property or method to call           |
|       Parameters      | Optional |                        Parameters to pass to the method                        |

|             Examples            |                                              |
|:-------------------------------:|:--------------------------------------------:|
|            **Markup**           |               **Result value**               |
| {?,code(System.DateTime,Today)} | The current date and time in DateTime format |
|  {?,code(System.Guid,NewGuid)}  |               A new random GUID              |
| {?,code(System.Int32,MaxValue)} |         The maximum value of an Int32        |
|   {? (System.Int32,Parse,11)}   |                11 (as string)                |

### ToLower

This function can be used to reformat the input string to lowercase.

|                 Examples                |                               |                  |
|:----------------------------------------|:------------------------------|:-----------------|
|                **Markup**               |       **Incoming value**      | **Result value** |
|        {?{DisplayName},tolower()}       |        Test Displayname       | test displayname |
| {?{_42_01_Persoon_IdmNummer},tolower()} |         111-IN-111111         |   111-in-111111  |
|     {?,code(System.Int32,MaxValue)}     | The maximum value of an Int32 |                  |
|       {? (System.Int32,Parse,11)}       |         11 (as string)        |                  |

### ToUpper

This function can be used to reformat the input string to uppercase.

|          Examples          |                    |                  |
|:---------------------------|:-------------------|:-----------------|
|         **Markup**         | **Incoming value** | **Result value** |
| {?{DisplayName},toupper()} |  Test Displayname  | TEST DISPLAYNAME |

### UcFirst

This function can be used to reformat the input string to make the first
character uppercase.

|          Examples          |                    |                  |
|:---------------------------|:-------------------|:-----------------|
|         **Markup**         | **Incoming value** |   Result value   |
| {?{DisplayName},ucfirst()} |  test Displayname  | Test Displayname |

### RemoveDiacritics

This function can be used to remove diacritics from a string.

|               Examples              |                        |                           |
|:------------------------------------|:-----------------------|:--------------------------|
|              **Markup**             |   **Incoming value**   |      **Result value**     |
| {?{DisplayName},removediacritics()} | String with diacritics | String without diacritics |

### Length

This function can be used to determine the length of a string.

|          Examples         |                      |                  |
|:--------------------------|:---------------------|:-----------------|
|         **Markup**        |  **Incoming value**  | **Result value** |
| {?{DisplayName},length()} |   Test Displayname   |        16        |
### RemoveWhitespaces

This function can be used to remove whitespaces from a string.

|               Examples               |                    |                  |
|:-------------------------------------|:-------------------|:-----------------|
|              **Markup**              | **Incoming value** | **Result value** |
| {?{DisplayName},removewhitespaces()} |  Test Displayname  |  Testdisplayname |

### RemoveExcessiveWhitespaces

This function can be used to remove excessive whitespaces.

|                    Examples                   |                          |                        |
|:----------------------------------------------|:-------------------------|:-----------------------|
|                   **Markup**                  |    **Incoming value**    |    **Result value**    |
| {?{DisplayName},removeexcessivewhitespaces()} | Test  Displayname  space | Test displayname space |

### Eval

This function returns the evaluated value of an expression which can be
contained in an argument

|     Name    |  Availability | Version (or date) |
|:------------|:--------------|:------------------|
|     IBIS    |   Available   |     2018-07-18    |
| TreeManager | Not available |                   |
|     ABAC    | Not available |                   |

Examples

**Markup**

**Result value**

{?{@ArgumentWithExpression},eval(ArgumentWithContent)}

Returns the evaluated value of @ArgumentwithExpression from the workflow
argument ArgumentWithContent

@ArgumentWithExpression contains a string with the value:
{\_42\_01\_Persoon\_IdmNummer} - {\_42\_11\_Persoon\_Geslachtsnaam}

@ArgumentWithContent contains an iDossier with:

\- \_42\_01\_Persoon\_IdmNummer = 12345

\- \_42\_11\_Persoon\_Geslachtsnaam = Lankreijer

The result will be 12345 - Lankreijer

{?{@ArgumentWithExpression},eval()}

Returns the evaluated value of @ArgumentwithExpression from the workflow
content (because no argument name is specified after eval)

@ArgumentWithExpression contains a string with the value:
{\_42\_01\_Persoon\_IdmNummer} - {\_42\_11\_Persoon\_Geslachtsnaam}

Workflow content contains an iDossier with:

\- \_42\_01\_Persoon\_IdmNummer = 12345

\- \_42\_11\_Persoon\_Geslachtsnaam = Lankreijer

The result will be 12345 - Lankreijer

{?{\_42\_01\_Persoon\_IdmNummer},eval()}

Returns the evaluated value of {\_42\_01\_Persoon\_IdmNummer} from the
workflow content (because no argument name is specified after eval)

Workflow content contains an iDossier with:

\- \_42\_01\_Persoon\_IdmNummer = 12345

\- \_42\_11\_Persoon\_Geslachtsnaam = Lankreijer

The result will be 12345

{?{\_42\_01\_Persoon\_IdmNummer},eval(ArgumentWithContent)}

Returns the evaluated value of {\_42\_01\_Persoon\_IdmNummer} from the
workflow argument ArgumentWithContent

@ArgumentWithContent contains an iDossier with:

\- \_42\_01\_Persoon\_IdmNummer = 12345

\- \_42\_11\_Persoon\_Geslachtsnaam = Lankreijer

The result will be 12345

### DateIsTodayOrFuture

This function returns one of the following values:

-   true : The input date is today or in the future
-   false : The input date is in the past
-   null : The input is not a valid DateTime representation

|     Name    |  Availability | Version (or date) |
|:-----------:|:-------------:|:-----------------:|
|     IBIS    |   Available   |     2019-04-17    |
| TreeManager | Not available |                   |
|     ABAC    | Not available |                   |

|                           Examples                           |
|:-------------------------------------------------------------|
|         {?2019-04-17 00:00:00,dateistodayorfuture()}         |
| {?{_09_41_Alias_DatumEindeGeldigheid},dateistodayorfuture()} |



### DateIsTodayOrPast

This function returns one of the following values:

-   true : The input date is today or in the past
-   false : The input date is in the future
-   null : The input is not a valid DateTime representation

|     Name    |  Availability | Version (or date) |
|:-----------:|:-------------:|:-----------------:|
|     IBIS    |   Available   |     2019-04-17    |
| TreeManager | Not available |                   |
|     ABAC    | Not available |                   |

|                           Examples                          |  Availability | Version (or date) |
|:------------------------------------------------------------|:--------------|:------------------|
|          {?2019-04-17 00:00:00,dateistodayorpast()}         |   Available   |     2019-04-17    |
| {?{_09_40_Alias_DatumIngangGeldigheid},dateistodayorpast()} | Not available |                   |
|                             ABAC                            | Not available |                   |



### GetLocaleName

This function returns the locale name of the matching locale name by
iso6391 code or name. First a match on iso code when not found a match
on name is given.

|     Name    |  Availability | Version (or date) |
|:------------|:--------------|:------------------|
|     IBIS    |   Available   |     2019-04-18    |
| TreeManager | Not available |                   |
|     ABAC    | Not available |                   |

|                Examples                |
|:--------------------------------------:|
|          {?nl,getlocalename()}         |
| {?{propertywithvalue},getlocalename()} |

### ParseJsonArrayValue

This function takes a JSON representation of an array as input, and
returns the value of the specified result property for the first item
that matches the specified search property value. The JSON array can
only be inputted as workflow argument value

|     Name    |  Availability | Version (or date) |
|:------------|:--------------|:------------------|
|     IBIS    |   Available   |     2019-04-25    |
| TreeManager | Not available |                   |
|     ABAC    | Not available |                   |

|   Parameters   |          |                                           |
|:---------------|:---------|:------------------------------------------|
| SearchProperty | Required |         The property to search on         |
|   SearchValue  | Required |           The value to search on          |
| ReturnProperty | Required | The property of which to return the value |

|                                                                Examples                                                               |                    |                                           |
|:--------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:------------------------------------------|
|                                                               **Markup**                                                              |  **Result value**  |       **The property to search on**       |
| {?[{"type":"work", "value":"work@trusted-id.eu"},{"type":"home", "value":"home@trusted-id.eu"}],parsejsonarrayvalue(type,work,value)} | work@trusted-id.eu |           The value to search on          |
| {?[{"type":"work", "value":"work@trusted-id.eu"},{"type":"home", "value":"home@trusted-id.eu"}],parsejsonarrayvalue(type,home,value)} | home@trusted-id.eu | The property of which to return the value |

### AddValue

This function adds a value to an existing object

| Parameters |          |                                |
|:-----------|:---------|:-------------------------------|
|    Value   | Required | The value to add to the object |

|            Examples            |                    |                  |
|:-------------------------------|:-------------------|:-----------------|
|           **Markup**           | **Incoming value** | **Result value** |
|  {?{RetryCounter},addvalue(2)} |          1         |         3        |
| {?{RetryCounter},addvalue(-1)} |         10         |         9        |

### Replace

This function can be used to replace characters in a string.

|            Examples           |                    |                  |
|:------------------------------|:-------------------|:-----------------|
|           **Markup**          | **Incoming value** | **Result value** |
| {?{DisplayName},replace(1,2)} |       String1      |      String2     |

### FirstWord

This function can be used to receive the first word of a string.

|           Examples           |                    |                  |
|:-----------------------------|:-------------------|:-----------------|
|          **Markup**          | **Incoming value** | **Result value** |
| {?{DisplayName},firstword()} |   Multiple words   |     Multiple     |

### Escapecharactersforldif

This function can be used to escape characters for ldif in a string.

|                   Examples                  |                    |                     |
|:--------------------------------------------|:-------------------|:--------------------|
|                  **Markup**                 | **Incoming value** |  ** Result value**  |
| {?{DisplayName}, escapecharactersforldif()} |     String/,+<>    |   String \,\+\<\>   |

* *

### Workflow

This function will call the DirectExecute workflow specified by
\[workflow ID\], and returns the value set in the **ReturnValue**
argument of the workflow. In case the workflow does not have a
**ReturnValue** argument, NULL is returned.


|                      Examples                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                 |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|                       **Markup**                       |                                                                                                                                                                                                                      **Workflow content**                                                                                                                                                                                                                     |   **Result value**  |
|  {?workflow(4a31ce5f-a738-4930-a595-1dee42f3725f)} |                                                         <br>-Connector import flow: Hologram <br> <br>&emsp; - Use {Content.propertyName} to access hologram properties <br> <br>- Connector export flow: IBIS entity <br> <br>&emsp; - Use {propertyName} to access IBIS entity properties <br> <br>- Other places: The entity that triggered the function <br> <br>&emsp; - Use {propertyName} to access IBIS entity properties                                                         | String \,\+\<\> |
| %{?workflow(4a31ce5f-a738-4930-a595-1dee42f3725f)} |  <br>- Connector import flow: Staging area entity <br> <br>&emsp; - Use {Content.propertyName} to access staging area entity properties<br> <br>&emsp; - Use {Content.Hologram.propertyName} to access hologram properties <br> <br>- Connector export flow: Staging area entity <br> <br>&emsp; - Use {Content.propertyName} to access staging area entity properties<br> <br>&emsp; - Use {Content.Hologram.propertyName} to access hologram properties <br> <br>- Other places: not implemented  |                 |

### ToUniversalTime

This function can be used to convert the incoming date to Universal Time
format.

|   Parameters  |          |                                  |
|:--------------|:---------|:---------------------------------|
| IncomingValue | Required | The incoming datetime to convert |

|               Examples               |                     |                     |
|:-------------------------------------|:--------------------|:--------------------|
|              **Markup**              |  **Incoming value** |   **Result value**  |
| {?{IncomingValue},ToUniversalTime()} | 12/16/2020 10:10:00 | 2020/12/16 10:10 AM |

* *

### ToFileTimeUtc

This function can be used to convert the incoming date to FileTime UTC
format.

The incoming value must be in either of the following formats:

-   yyyy-MM-dd
-   yyyy-MM-dd HH:mm:ss

|   Parameters  |          |                                  |
|:--------------|:---------|:---------------------------------|
| IncomingValue | Required | The incoming datetime to convert |

|              Examples              |                     |                    |
|:-----------------------------------|:--------------------|:-------------------|
|             **Markup**             |  **Incoming value** |  **Result value**  |
| {?{IncomingValue},ToFileTimeUtc()} | 2020-12-16 10:10:00 | 132525870000000000 |

* *

### Join

This function can be used to convert an array of objects to a character
separated string. The array must contain simple types like string or
integer.

|  Parameters  |          |                                                                                                                                     |
|:-------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------|
| propertyname | Required | The name of the property which contains the array<br> <br>When used in a workflow, use @argumentName to resolve a workflow argument |
|   separator  | Optional |                             The separator to use. If no separator is specified, a semicolon will be used                            |

|        Examples       |                    |                  |
|:----------------------|:-------------------|:-----------------|
|       **Markup**      | **Incoming value** | **Result value** |
|   {?Join(Groups,;)}   |    ["1","2","3"]   |       1;2;3      |
|  {?Join(Property,,)}  |    ["1","2","3"]   |       1,2,3      |
| {?Join(@argument1,,)} |    ["1","2","3"]   |       1,2,3      |

## Testing data resolution and functions

1.  Go to the workflow management screen:

    -   IBIS &gt; Admin &gt; Workflow
    -   ABAC &gt; Main menu &gt; Workflow
    -   TreeManager &gt; TreeDesigner &gt; Workflow

2.  In the top-level menu, click on the icon with the bricks

<!-- -->

3.  Use the new screen to test your expressions

    -   Contenttype (optional) : Select a type and press the magnifier to
    search for content to examine
    -   Identification (optional) : Contains the Id of the selected content
    -   Expression : The expression to evaluate
    -   Result : After pressing Execute, the result will be displayed here


