##### <span id="index"></span>Data resolution and supported functions

-   [Data resolution](#Data%20resolution)
-   [Functions](#Functions)

# <span id="Data resolution"></span>Data resolution

Data resolution provides the ability to translate an expression to an
actual value.

<table class="table table-bordered">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Markup</th>
<th>Result</th>
<th>Example markup</th>
<th>Example result</th>
</tr>
<tr class="odd">
<th>{x}</th>
<th>The value of the property named <strong><em>x</em></strong> of the
incoming object</th>
<th>{DisplayName}</th>
<th>The value of the <strong><em>DisplayName</em></strong> property of
the incoming object</th>
</tr>
<tr class="header">
<th>{@x}</th>
<th>The value of argument <strong><em>x</em></strong></th>
<th>{@Argument1}</th>
<th>The value of argument <strong><em>Argument1</em></strong></th>
</tr>
<tr class="odd">
<th>{?{x},f()}</th>
<th>The result of function <strong><em>f</em></strong> performed on
property <strong><em>x</em></strong> of the incoming object</th>
<th>See section <strong><em>Functions</em></strong></th>
<th>See section <strong><em>Functions</em></strong></th>
</tr>
<tr class="header">
<th>{?{@x},f()}</th>
<th>The result of function <strong><em>f</em></strong> performed on
argument <strong><em>x</em></strong></th>
<th>See section <strong><em>Functions</em></strong></th>
<th>See section <strong><em>Functions</em></strong></th>
</tr>
<tr class="odd">
<th>["{x}"]</th>
<th>A collection (array) of objects</th>
<th>["{a}","{b}","{c}"]</th>
<th>An array of strings with the values of the properties a, b and
c.</th>
</tr>
<tr class="header">
<th>[\{"y":"{y}"\}]</th>
<th>A collection (array) of dictionaries</th>
<th>[\{"a":"{a}", "b":"{b}"\}, \{ "a":"1", "b":"2" \}]</th>
<th>An array of 2 dictionaries with the properties a and b<br />
It is important to escape the object holders (curly braces), otherwise
they will be parsed as a property and the array will not be created</th>
</tr>
</thead>
&#10;</table>

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

#### Linked objects

It is possible to reference linked objects using data resolution. A
linked object is specified using a dot (.) in the markup. For example,
{Tree.DisplayName} will return the DisplayName of the Tree for the
incoming node.

The following table describes the relations in the different products.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Product</th>
<th>Source</th>
<th>Target</th>
<th>Object markup</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TreeManager</td>
<td>Attribute</td>
<td>Attribute Type</td>
<td>Type</td>
</tr>
<tr class="even">
<td>TreeManager</td>
<td>Attribute Value</td>
<td>Attribute</td>
<td>Attribute</td>
</tr>
<tr class="odd">
<td>TreeManager</td>
<td>Attribute Value</td>
<td>Node</td>
<td>Node</td>
</tr>
<tr class="even">
<td>TreeManager</td>
<td>Node</td>
<td>Node Type</td>
<td>NodeType</td>
</tr>
<tr class="odd">
<td>TreeManager</td>
<td>Node</td>
<td>Parent Node</td>
<td>Parent</td>
</tr>
<tr class="even">
<td>TreeManager</td>
<td>Node</td>
<td>Childs (direct)</td>
<td>Childs</td>
</tr>
<tr class="odd">
<td>TreeManager</td>
<td>Node</td>
<td>Childs (recursive)</td>
<td>ChildsRecursive</td>
</tr>
<tr class="even">
<td>TreeManager</td>
<td>Node</td>
<td>Tree</td>
<td>Tree</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;ApplicationDossierProduct&gt;</td>
<td>Assets</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;string&gt;</td>
<td>EmailAddresses</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;string&gt;</td>
<td>EmailAddresses_IncludingPrimary</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>IdentityDossier</td>
<td>Identity</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>Manager IDossier</td>
<td>Manager</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;IDossier&gt; of Managers</td>
<td>Managers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>Organisatie</td>
<td>Organisation</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;SmtpAlias&gt;</td>
<td>SmtpAliasses</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>SysDossierStatus</td>
<td>Status</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>AliasDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>AliasDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>Requester e-mail</td>
<td>AanvragerEmail</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>List&lt;ApplicationDossierProduct&gt;</td>
<td>Assets</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>SysIbisUser</td>
<td>CreatedByUser</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>SysIbisUser</td>
<td>ModifiedByUser</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>Organisatie</td>
<td>Organisation</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>ApplicationDossier</td>
<td>List&lt;ApplicationDossierProduct&gt;</td>
<td>Products</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>EpicDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>EpicDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>FmhDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>FmhDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;ApplicationDossierProduct&gt;</td>
<td>Assets</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IdentityDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>Aliasdossier (Valid aliasdossier present? The first valid
aliasdossier with the earliest startdate. Otherwise the first invalid
aliasdossier with the latest enddate)</td>
<td>Alias</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;ApplicationDossierProduct&gt;</td>
<td>Assets</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>Contract</td>
<td>Contract</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>The description of the employment group</td>
<td>EmploymentGroupDescription</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>The description of the employment type</td>
<td>EmploymentTypeDescription</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>IdentityDossier</td>
<td>Identity</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>Lokatie</td>
<td>Lokatie</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>Manager iDossier</td>
<td>Manager</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>Manager e-mail</td>
<td>ManagerEmail</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;IDossier&gt; of Managers</td>
<td>Managers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>Employee e-mail</td>
<td>MedewerkerEmail</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>Organisation</td>
<td>Organisation</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>SysDossierStatus</td>
<td>Status</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>IDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>IDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>Organisatie</td>
<td>Parent Organisatie</td>
<td>Parent</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>Organisatie</td>
<td>Organisation</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>SysDossierStatus</td>
<td>Status</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>PbsDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>PbsDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>Organisatie</td>
<td>Organisation</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>TgDossier</td>
<td>WidDossier</td>
<td>WidDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>TgDossier</td>
<td>List&lt;WidDossier&gt;</td>
<td>WidDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>AliasDossier</td>
<td>AliasDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;AliasDossier&gt;</td>
<td>AliasDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>EpicDossier</td>
<td>EpicDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;EpicDossier&gt;</td>
<td>EpicDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>FmhDossier</td>
<td>FmhDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;FmhDossier&gt;</td>
<td>FmhDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>IdentityDossier</td>
<td>IdentityDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;IdentityDossier&gt;</td>
<td>IdentityDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>IDossier</td>
<td>IDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;IDossier&gt;</td>
<td>IDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>PbsDossier</td>
<td>PbsDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;PbsDossier&gt;</td>
<td>PbsDossiers</td>
</tr>
<tr class="odd">
<td>IBIS</td>
<td>WidDossier</td>
<td>TgDossier</td>
<td>TgDossier</td>
</tr>
<tr class="even">
<td>IBIS</td>
<td>WidDossier</td>
<td>List&lt;TgDossier&gt;</td>
<td>TgDossiers</td>
</tr>
</tbody>
</table>

[Top](#index)

# <span id="Functions"></span>Functions

Functions can be used to perform checks or transformations on data
present in a property of the incoming object or an argument.

Functions are specified using the following markup:

-   {? {propertyname/argument} function(params)}

<u>NOTE: Before 2018-03-23, functions were specified using the dollar
sign ($). This was causing UI errors, therefore it’s changed to a
questionmark.</u>

<u> </u>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Examples</th>
<th></th>
</tr>
<tr class="odd">
<th>{?{DisplayName},substring(10)}</th>
<th>returns the first 10 characters of the <em>DisplayName</em> property
of the object specified in the workflow content</th>
</tr>
<tr class="header">
<th>{?{@arg0},substring(10)}</th>
<th>returns the first 10 characters of the string contained in the
<em>arg0</em> argument</th>
</tr>
</thead>
&#10;</table>

### GetDate

This function can be used to Extract day|month|year|hour|minutes|seconds
according to specified format. If no format is specified, the format of
IBIS settings is used.

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Date / Datetime</th>
<th>Required</th>
<th>The date or datetime to extract the (formatted) date from</th>
</tr>
<tr class="header">
<th>Format</th>
<th>Optional</th>
<th><p>dd-MM-yyyy | d-M-yyyy | yyyy | MM | hh:mm:ss</p>
<p>Other types of format specifiers can be found in the <a
href="https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings">custom
date and time format strings</a> documentation.</p></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
<th><strong>IBIS setting</strong></th>
</tr>
<tr class="header">
<th>{?{EndDate}, GetDate()}</th>
<th>31-12-2021 12:00:01.000</th>
<th>31-12-2021 12:00:01.000</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
<tr class="odd">
<th>{?{EndDate}, GetDate(dd-MM-yyyy)}</th>
<th>31-12-2021 12:00:01.000</th>
<th>31-12-2021</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
<tr class="header">
<th>{?{EndDate}, GetDate(d-M-yyyy)}</th>
<th>01-01-2021 12:00:01.000</th>
<th>1-1-2021</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
<tr class="odd">
<th>{?{EndDate}, GetDate(yyyy)}</th>
<th>01-01-2021 12:00:01.000</th>
<th>2021</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
<tr class="header">
<th>{?{EndDate}, GetDate(MM)}</th>
<th>01-01-2021 12:00:01.000</th>
<th>01</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
<tr class="odd">
<th>{?{EndDate}, GetDate(HH:mm:ss)}</th>
<th>01-01-2021 12:00:01.000</th>
<th>12:00:01</th>
<th>dd-MM-yyyy HH:mm:ss.fff</th>
</tr>
</thead>
&#10;</table>

* *

### GetDay

This function can be used to extract the day from a date or datetime
field (2 numbers).

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Date / Datetime</th>
<th>Required</th>
<th>The date or datetime to extract the day from</th>
</tr>
<tr class="header">
<th>Format</th>
<th>Optional</th>
<th>d | dd</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{EndDate},GetDay()}</th>
<th>31-12-2021 12:10:00</th>
<th>31</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetDay()}</th>
<th>31-12-2021</th>
<th>31</th>
</tr>
<tr class="header">
<th>{?{EndDate},GetDay()}</th>
<th>01-01-2021</th>
<th>1</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetDay(dd)}</th>
<th>01-01-2021</th>
<th>01</th>
</tr>
</thead>
&#10;</table>

* *

### GetMonth

This function can be used to extract the month from a date or datetime
field (2 numbers).

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Date / Datetime</th>
<th>Required</th>
<th>The date or datetime to extract the month from</th>
</tr>
<tr class="header">
<th>Format</th>
<th>Optional</th>
<th>M | MM</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{EndDate},GetMonth()}</th>
<th>31-12-2021 12:10:00</th>
<th>12</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetMonth()}</th>
<th>31-12-2021</th>
<th>12</th>
</tr>
<tr class="header">
<th>{?{EndDate},GetMonth()}</th>
<th>31-01-2021</th>
<th>1</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetMonth(MM)}</th>
<th>31-01-2021</th>
<th>01</th>
</tr>
</thead>
&#10;</table>

* *

### GetYear

This function can be used to extract the year from a date or datetime
field (4 numbers).

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Date / Datetime</th>
<th>Required</th>
<th>The date or datetime to extract the year from</th>
</tr>
<tr class="header">
<th>Format</th>
<th>Optional</th>
<th>yy | yyyy</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{EndDate},GetYear()}</th>
<th>31-12-2021 12:10:00</th>
<th>2021</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetYear()}</th>
<th>31-12-2021</th>
<th>2021</th>
</tr>
<tr class="header">
<th>{?{EndDate},GetYear(yy)}</th>
<th>31-12-2021</th>
<th>21</th>
</tr>
<tr class="odd">
<th>{?{EndDate},GetYear(yyyy)}</th>
<th>31-12-2021</th>
<th>2021</th>
</tr>
</thead>
&#10;</table>

* *

### IsIndefiniteDate

This function checks if a date or datetime field has the year 9999.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Date / Datetime</th>
<th>Required</th>
<th>The date or datetime to check if it contains the year 9999</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{EndDate},IsIndefiniteDate()}</th>
<th>31-12-9999 12:10:00</th>
<th>True</th>
</tr>
<tr class="odd">
<th>{?{EndDate},IsIndefiniteDate()}</th>
<th>31-12-2021</th>
<th>False</th>
</tr>
</thead>
&#10;</table>

* *

### IsNull

This function can be used to replace a null (or empty) value with
another value.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Replacement value</th>
<th>Required</th>
<th>The value to replace the input with in case it is null or empty</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},isnull(Sample displayname)}</th>
<th>Test Displayname</th>
<th>Test DisplayName</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},isnull(Sample displayname)}</th>
<th>[null]</th>
<th>Sample DisplayName</th>
</tr>
<tr class="header">
<th>{?{DisplayName},isnull({Id})}</th>
<th>[null]</th>
<th>The value of the Id property</th>
</tr>
</thead>
&#10;</table>

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

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Start</th>
<th>Required</th>
<th>Specifies at which position to start. 0 is the first character of
the incoming string</th>
</tr>
<tr class="header">
<th>Length</th>
<th>Optional</th>
<th>Specifies the number of characters to read</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},substring(0)}</th>
<th>Test Displayname</th>
<th>Test DisplayName</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},substring(5)}</th>
<th>Test Displayname</th>
<th>DisplayName</th>
</tr>
<tr class="header">
<th>{?{DisplayName},substring(12)}</th>
<th>Test Displayname</th>
<th>name</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},substring(0,4)}</th>
<th>Test Displayname</th>
<th>Test</th>
</tr>
<tr class="header">
<th>{?{DisplayName},substring(5,7)}</th>
<th>Test Displayname</th>
<th>Display</th>
</tr>
</thead>
&#10;</table>

* *

### IIF

This function can be used to make a decision based on the value of the
incoming property.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>expression</th>
<th>Required</th>
<th>The value to compare the incoming property with</th>
</tr>
<tr class="header">
<th>truePart</th>
<th>Required</th>
<th>The return value in case the incoming property and
<em>expression</em> match</th>
</tr>
<tr class="odd">
<th>falsePart</th>
<th>Required</th>
<th>The return value in case the incoming property and
<em>expression</em> do not match</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},iif(Test Displayname,Waar,Onwaar)}</th>
<th>Test Displayname</th>
<th>Waar</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},iif(Test,Waar,Onwaar)}</th>
<th>Test Displayname</th>
<th>Onwaar</th>
</tr>
<tr class="header">
<th>{?{DisplayName},iif(Test Displayname,{Id},{DisplayName})}</th>
<th>Test Displayname</th>
<th>The value of property Id</th>
</tr>
</thead>
&#10;</table>

* *

### StartsWith

This function can be used to determine if the incoming string starts
with the specified value.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>expression</th>
<th>Required</th>
<th>The value which the incoming property has to start with</th>
</tr>
<tr class="header">
<th>caseSensitive</th>
<th>Optional</th>
<th><strong><em>false</em></strong> to turn off case sensitivity. In
case not specified, case sensitivity is on.</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},startswith(Test)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},startswith(Test,true)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="header">
<th>{?{DisplayName},startswith(Test,false)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},startswith(test)}</th>
<th>Test Displayname</th>
<th>false</th>
</tr>
<tr class="header">
<th>{?{DisplayName},startswith(test,true)}</th>
<th>Test Displayname</th>
<th>false</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},startswith(test,false)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
</thead>
&#10;</table>

* *

### EndsWith

This function can be used to determine if the incoming string ends with
the specified value.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>expression</th>
<th>Required</th>
<th>The value which the incoming property has to end with</th>
</tr>
<tr class="header">
<th>caseSensitive</th>
<th>Optional</th>
<th><strong><em>false</em></strong> to turn off case sensitivity. In
case not specified, case sensitivity is on.</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},endswith(name)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},endswith(name,true)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="header">
<th>{?{DisplayName},endswith(name,false)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},endswith(Name)}</th>
<th>Test Displayname</th>
<th>false</th>
</tr>
<tr class="header">
<th>{?{DisplayName},endswith(Name,true)}</th>
<th>Test Displayname</th>
<th>false</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},endswith(Name,false)}</th>
<th>Test Displayname</th>
<th>true</th>
</tr>
</thead>
&#10;</table>

* *

### Trim

This function can be used to trim spaces at the beginning and the end of
the incoming string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
</tr>
<tr class="odd">
<th><em>This function has no parameters</em></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value (quotes for readability)</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},trim()}</th>
<th>Test Displayname</th>
<th>Test Displayname</th>
</tr>
<tr class="odd">
<th>{?{DisplayName},trim()}</th>
<th>Test Displayname</th>
<th>Test Displayname</th>
</tr>
</thead>
&#10;</table>

* *

### DateFormat

This function can be used to convert the format of the incoming date to
another format.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>inputFormat</th>
<th>Required</th>
<th>The format of the incoming date</th>
</tr>
<tr class="header">
<th>outputFormat</th>
<th>Required</th>
<th>The desired output format</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{CreatedDate},dateformat(MM/dd/yyyy HH:mm:ss,dd-MM-yyyy)}</th>
<th>11/13/2017 00:00:00</th>
<th>13-11-2017</th>
</tr>
</thead>
&#10;</table>

* *

### AddTime

This function adds a timespan to an existing DateTime object

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Days</th>
<th>Required</th>
<th>The number of days to add to the DateTime</th>
</tr>
<tr class="header">
<th>Hours</th>
<th>Optional</th>
<th>The number of hours to add to the DateTime</th>
</tr>
<tr class="odd">
<th>Minutes</th>
<th>Optional</th>
<th>The number of minutes to add to the DateTime</th>
</tr>
<tr class="header">
<th>Seconds</th>
<th>Optional</th>
<th>The number of seconds to add to the DateTime</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value (in DateTime structure)</strong></th>
</tr>
<tr class="header">
<th>{?{?,code(System.DateTime,Today)},addTime(1)}</th>
<th></th>
<th>Tomorrow</th>
</tr>
<tr class="odd">
<th>{?{?,code(System.DateTime,Today)},addTime(-1)}</th>
<th></th>
<th>Yesterday</th>
</tr>
<tr class="header">
<th>{?{?,code(System.DateTime,Today)},addTime(1,1)}</th>
<th></th>
<th>Tomorrow, 01:00 AM</th>
</tr>
<tr class="odd">
<th>{?{?,code(System.DateTime,Today)},addTime(1,1,1)}</th>
<th></th>
<th>Tomorrow, 01:01 AM</th>
</tr>
<tr class="header">
<th>{?{?,code(System.DateTime,Today)},addTime(1,1,1,1)}</th>
<th></th>
<th>Tomorrow, 01:01:01 AM</th>
</tr>
<tr class="odd">
<th>{?{?,code(System.DateTime,Today)},addTime(-1,1,1,1)}</th>
<th></th>
<th>Yesterday, 01:01:01 AM</th>
</tr>
</thead>
&#10;</table>

* *

### Code

This function returns the value of a field, property or method in code
(using reflection).

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Class</th>
<th>Required</th>
<th>The name of the (static) class that contains the
field/property/method to call</th>
</tr>
<tr class="header">
<th>Field/Property/Method</th>
<th>Required</th>
<th>The name of the (static) field, property or method to call</th>
</tr>
<tr class="odd">
<th>Parameters</th>
<th>Optional</th>
<th>Parameters to pass to the method</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?,code(System.DateTime,Today)}</th>
<th>The current date and time in DateTime format</th>
</tr>
<tr class="odd">
<th>{?,code(System.Guid,NewGuid)}</th>
<th>A new random GUID</th>
</tr>
<tr class="header">
<th>{?,code(System.Int32,MaxValue)}</th>
<th>The maximum value of an Int32</th>
</tr>
<tr class="odd">
<th>{? (System.Int32,Parse,11)}</th>
<th>11 (as string)</th>
</tr>
</thead>
&#10;</table>

### ToLower

This function can be used to reformat the input string to lowercase.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},tolower()}</th>
<th>Test Displayname</th>
<th>test displayname</th>
</tr>
<tr class="odd">
<th>{?{_42_01_Persoon_IdmNummer},tolower()}</th>
<th>111-IN-111111</th>
<th>111-in-111111</th>
</tr>
</thead>
&#10;</table>

### ToUpper

This function can be used to reformat the input string to uppercase.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},toupper()}</th>
<th>Test Displayname</th>
<th>TEST DISPLAYNAME</th>
</tr>
</thead>
&#10;</table>

### UcFirst

This function can be used to reformat the input string to make the first
character uppercase.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},ucfirst()}</th>
<th>test Displayname</th>
<th>Test Displayname</th>
</tr>
</thead>
&#10;</table>

### RemoveDiacritics

This function can be used to remove diacritics from a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},removediacritics()}</th>
<th>String with diacritics</th>
<th>String without diacritics</th>
</tr>
</thead>
&#10;</table>

### Length

This function can be used to determine the length of a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},length()}</th>
<th>Test Displayname</th>
<th>16</th>
</tr>
</thead>
&#10;</table>

### RemoveWhitespaces

This function can be used to remove whitespaces from a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},removewhitespaces()}</th>
<th>Test Displayname</th>
<th>Testdisplayname</th>
</tr>
</thead>
&#10;</table>

### RemoveExcessiveWhitespaces

This function can be used to remove excessive whitespaces.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},removeexcessivewhitespaces()}</th>
<th>Test  Displayname  space</th>
<th>Test displayname space</th>
</tr>
</thead>
&#10;</table>

### Eval

This function returns the evaluated value of an expression which can be
contained in an argument

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Name</th>
<th>Availability</th>
<th>Version (or date)</th>
</tr>
<tr class="odd">
<th>IBIS</th>
<th>Available</th>
<th>2018-07-18</th>
</tr>
<tr class="header">
<th>TreeManager</th>
<th>Not available</th>
<th></th>
</tr>
<tr class="odd">
<th>ABAC</th>
<th>Not available</th>
<th></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Argument</th>
<th>Optional</th>
<th>The argument which contains the content to examine</th>
</tr>
</thead>
&#10;</table>

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

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Name</th>
<th>Availability</th>
<th>Version (or date)</th>
</tr>
<tr class="odd">
<th>IBIS</th>
<th>Available</th>
<th>2019-04-17</th>
</tr>
<tr class="header">
<th>TreeManager</th>
<th>Not available</th>
<th></th>
</tr>
<tr class="odd">
<th>ABAC</th>
<th>Not available</th>
<th></th>
</tr>
</thead>
&#10;</table>

<table>
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
</tr>
<tr class="odd">
<th>{?2019-04-17 00:00:00,dateistodayorfuture()}</th>
</tr>
<tr class="header">
<th>{?{_09_41_Alias_DatumEindeGeldigheid},dateistodayorfuture()}</th>
</tr>
</thead>
&#10;</table>

####  

### DateIsTodayOrPast

This function returns one of the following values:

-   true : The input date is today or in the past
-   false : The input date is in the future
-   null : The input is not a valid DateTime representation

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Name</th>
<th>Availability</th>
<th>Version (or date)</th>
</tr>
<tr class="odd">
<th>IBIS</th>
<th>Available</th>
<th>2019-04-17</th>
</tr>
<tr class="header">
<th>TreeManager</th>
<th>Not available</th>
<th></th>
</tr>
<tr class="odd">
<th>ABAC</th>
<th>Not available</th>
<th></th>
</tr>
</thead>
&#10;</table>

<table>
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
</tr>
<tr class="odd">
<th>{?2019-04-17 00:00:00,dateistodayorpast()}</th>
</tr>
<tr class="header">
<th>{?{_09_40_Alias_DatumIngangGeldigheid},dateistodayorpast()}</th>
</tr>
</thead>
&#10;</table>

####  

### GetLocaleName

This function returns the locale name of the matching locale name by
iso6391 code or name. First a match on iso code when not found a match
on name is given.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Name</th>
<th>Availability</th>
<th>Version (or date)</th>
</tr>
<tr class="odd">
<th>IBIS</th>
<th>Available</th>
<th>2019-04-18</th>
</tr>
<tr class="header">
<th>TreeManager</th>
<th>Not available</th>
<th></th>
</tr>
<tr class="odd">
<th>ABAC</th>
<th>Not available</th>
<th></th>
</tr>
</thead>
&#10;</table>

<table>
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
</tr>
<tr class="odd">
<th>{?nl,getlocalename()}</th>
</tr>
<tr class="header">
<th>{?{propertywithvalue},getlocalename()}</th>
</tr>
</thead>
&#10;</table>

### ParseJsonArrayValue

This function takes a JSON representation of an array as input, and
returns the value of the specified result property for the first item
that matches the specified search property value. The JSON array can
only be inputted as workflow argument value

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th>Name</th>
<th>Availability</th>
<th>Version (or date)</th>
</tr>
<tr class="odd">
<th>IBIS</th>
<th>Available</th>
<th>2019-04-25</th>
</tr>
<tr class="header">
<th>TreeManager</th>
<th>Not available</th>
<th></th>
</tr>
<tr class="odd">
<th>ABAC</th>
<th>Not available</th>
<th></th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>SearchProperty</th>
<th>Required</th>
<th>The property to search on</th>
</tr>
<tr class="header">
<th>SearchValue</th>
<th>Required</th>
<th>The value to search on</th>
</tr>
<tr class="odd">
<th>ReturnProperty</th>
<th>Required</th>
<th>The property of which to return the value</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?[{"type":"work", "value":"work@trusted-id.eu"},{"type":"home",
"value":"home@trusted-id.eu"}],<strong>parsejsonarrayvalue</strong>(type,work,value)}</th>
<th>work@trusted-id.eu</th>
</tr>
<tr class="odd">
<th>{?[{"type":"work", "value":"work@trusted-id.eu"},{"type":"home",
"value":"home@trusted-id.eu"}],<strong>parsejsonarrayvalue</strong>(type,home,value)}</th>
<th>home@trusted-id.eu</th>
</tr>
</thead>
&#10;</table>

### AddValue

This function adds a value to an existing object

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>Value</th>
<th>Required</th>
<th>The value to add to the object</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{RetryCounter},addvalue(2)}</th>
<th>1</th>
<th>3</th>
</tr>
<tr class="odd">
<th>{?{RetryCounter},addvalue(-1)}</th>
<th>10</th>
<th>9</th>
</tr>
</thead>
&#10;</table>

### Replace

This function can be used to replace characters in a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},replace(1,2)}</th>
<th>String1</th>
<th>String2</th>
</tr>
</thead>
&#10;</table>

### FirstWord

This function can be used to receive the first word of a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName},firstword()}</th>
<th>Multiple words</th>
<th>Multiple</th>
</tr>
</thead>
&#10;</table>

### Escapecharactersforldif

This function can be used to escape characters for ldif in a string.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{DisplayName}, escapecharactersforldif()}</th>
<th>String/,+&lt;&gt;</th>
<th>String \,\+\&lt;\&gt;</th>
</tr>
</thead>
&#10;</table>

* *

### Workflow

This function will call the DirectExecute workflow specified by
\[workflow ID\], and returns the value set in the **ReturnValue**
argument of the workflow. In case the workflow does not have a
**ReturnValue** argument, NULL is returned.

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Workflow content</strong></th>
</tr>
<tr class="header">
<th>{?workflow(4a31ce5f-a738-4930-a595-1dee42f3725f)}</th>
<th><ul>
<li>Connector import flow: Hologram
<ul>
<li>Use {Content.propertyName} to access hologram properties</li>
</ul></li>
<li>Connector export flow: IBIS entity
<ul>
<li>Use {propertyName} to access IBIS entity properties</li>
</ul></li>
<li>Other places: The entity that triggered the function
<ul>
<li>Use {propertyName} to access IBIS entity properties</li>
</ul></li>
</ul></th>
</tr>
<tr class="odd">
<th>%{?workflow(4a31ce5f-a738-4930-a595-1dee42f3725f)}</th>
<th><ul>
<li>Connector import flow: Staging area entity
<ul>
<li>Use {Content.propertyName} to access staging area entity
properties</li>
<li>Use {Content.Hologram.propertyName} to access hologram
properties</li>
</ul></li>
<li>Connector export flow: Staging area entity
<ul>
<li>Use {Content.propertyName} to access staging area entity
properties</li>
<li>Use {Content.Hologram.propertyName} to access hologram
properties</li>
</ul></li>
<li>Other places: <em>not implemented</em></li>
</ul></th>
</tr>
</thead>
&#10;</table>

### ToUniversalTime

This function can be used to convert the incoming date to Universal Time
format.

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>IncomingValue</th>
<th>Required</th>
<th>The incoming datetime to convert</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{IncomingValue},ToUniversalTime()}</th>
<th>12/16/2020 10:10:00</th>
<th>2020/12/16 10:10 AM</th>
</tr>
</thead>
&#10;</table>

* *

### ToFileTimeUtc

This function can be used to convert the incoming date to FileTime UTC
format.

The incoming value must be in either of the following formats:

-   yyyy-MM-dd
-   yyyy-MM-dd HH:mm:ss

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>IncomingValue</th>
<th>Required</th>
<th>The incoming datetime to convert</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?{IncomingValue},ToFileTimeUtc()}</th>
<th>2020-12-16 10:10:00</th>
<th>132525870000000000</th>
</tr>
</thead>
&#10;</table>

* *

### Join

This function can be used to convert an array of objects to a character
separated string. The array must contain simple types like string or
integer.

<table class="table table-bordered">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th><p>Parameters</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>propertyname</th>
<th>Required</th>
<th><p>The name of the property which contains the array</p>
<p>When used in a workflow, use @argumentName to resolve a workflow
argument</p></th>
</tr>
<tr class="header">
<th>separator</th>
<th>Optional</th>
<th>The separator to use. If no separator is specified, a semicolon will
be used</th>
</tr>
</thead>
&#10;</table>

<table class="table table-bordered">
<thead class="thead-light">
<tr class="header">
<th><p>Examples</p></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Markup</strong></th>
<th><strong>Incoming value</strong></th>
<th><strong>Result value</strong></th>
</tr>
<tr class="header">
<th>{?Join(Groups,;)}</th>
<th>["1","2","3"]</th>
<th>1;2;3</th>
</tr>
<tr class="odd">
<th>{?Join(Property,,)}</th>
<th>["1","2","3"]</th>
<th>1,2,3</th>
</tr>
<tr class="header">
<th><p>{?Join(@argument1,,)}</p></th>
<th><p>["1","2","3"]</p></th>
<th><p>1,2,3</p></th>
</tr>
</thead>
&#10;</table>

# Testing data resolution and functions

1.  Go to the workflow management screen:

-   IBIS &gt; Admin &gt; Workflow
-   ABAC &gt; Main menu &gt; Workflow
-   TreeManager &gt; TreeDesigner &gt; Workflow

1.  In the top-level menu, click on the icon with the bricks

<!-- -->

1.  Use the new screen to test your expressions

-   Contenttype (optional) : Select a type and press the magnifier to
    search for content to examine
-   Identification (optional) : Contains the Id of the selected content
-   Expression : The expression to evaluate
-   Result : After pressing Execute, the result will be displayed here

[Top](#index)
