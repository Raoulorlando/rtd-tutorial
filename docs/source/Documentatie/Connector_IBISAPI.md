# IBIS

The IBIS connector module supports import and export of data from and to
another IBIS instance through the ODATA API.

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
</thead>
<tbody>
<tr class="odd">
<td><p>OData URL</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The full URL of the IBIS instance to connect to (including
/OData). For example:</p>
<p> </p>
<p><a
href="https://ibis.domain.tld/OData">https://ibis.domain.tld/OData</a></p>
<p> </p></td>
</tr>
<tr class="even">
<td><p>Authentication method</p></td>
<td><p><strong> </strong></p></td>
<td><p><strong>Optional</strong> – the type of authentication to use for
connections to IBIS</p>
<p> </p></td>
</tr>
<tr class="odd">
<td><p>Username</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The username of the account to use when connecting to IBIS.
Required for NTLM, Kerberos and Azure authentication</p>
<p> </p></td>
</tr>
<tr class="even">
<td><p>Password</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The password of the useraccount used to connect to IBIS. Required
for NTLM, Kerberos and Azure authentication</p>
<p> </p></td>
</tr>
<tr class="odd">
<td><p>OAuth – Tenant ID</p></td>
<td><p><strong> </strong></p></td>
<td><p><strong>Optional</strong> – the Azure tenant ID when the
connected IBIS instance is running in an Azure App service</p>
<p> </p></td>
</tr>
<tr class="even">
<td><p>OAuth – Resource ID</p></td>
<td><p><strong> </strong></p></td>
<td><p><strong>Optional</strong> – the Azure resource ID when the
connected IBIS instance is running in an Azure App service</p>
<p> </p></td>
</tr>
<tr class="odd">
<td><p>OAuth – Application ID</p></td>
<td><p><strong> </strong></p></td>
<td><p><strong>Optional</strong> – the Azure application ID when the
connected IBIS instance is running in an Azure App service</p>
<p> </p></td>
</tr>
<tr class="even">
<td><p>OAuth – Application secret</p></td>
<td><p><strong> </strong></p></td>
<td><p><strong>Optional</strong> – the Azure application secret when the
connected IBIS instance is running in an Azure App service</p>
<p> </p></td>
</tr>
<tr class="odd">
<td><p>API object name</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The name of the message model the API supports. Supported values
are:</p>
<ul>
<li>AliasDossierApiModel</li>
<li>DynamicPropertyApiModel</li>
<li>EpicDossierApiModel</li>
<li>FmhDossierApiModel</li>
<li>IBISQueueApiModel</li>
<li>IdentityDossierApiModel</li>
<li>IDossierApiModel</li>
<li>IDossierFotoApiModel</li>
<li>OrganisatieApiModel</li>
<li>PbsDossierApiModel</li>
<li>RegisterApiModel</li>
<li>SysInputFieldApiModel</li>
<li>TgDossierApiModel</li>
<li>WidDossierApiModel</li>
</ul></td>
</tr>
<tr class="even">
<td><p>IBIS object name</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The name of the IBIS object to synchronize. Supported values
are:</p>
<ul>
<li>AliasDossier</li>
<li>EpicDossier</li>
<li>FmhDossier</li>
<li>IbisQueue</li>
<li>IdentityDossier</li>
<li>IdmNumber</li>
<li>IDossier</li>
<li>Organisatie</li>
<li>PbsDossier</li>
<li>Register</li>
<li>Supplier</li>
<li>SupplierOrganisation</li>
<li>SupplierStatus</li>
<li>TgDossier</li>
<li>WidDossier</li>
</ul></td>
</tr>
<tr class="odd">
<td><p>OData resource name</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The name of the IBIS object as known by the OData API. Supported
values are:</p>
<ul>
<li>AliasDossiers</li>
<li>DynamicProperties</li>
<li>EpicDossiers</li>
<li>FmhDossiers</li>
<li>IBISQueues</li>
<li>IDentityDossiers</li>
<li>IDossierFoto</li>
<li>IDossiers</li>
<li>PbsDossiers</li>
<li>Registers</li>
<li>Remarks</li>
<li>SysInputFields</li>
<li>TgDossiers</li>
<li>WidDossiers</li>
</ul></td>
</tr>
<tr class="even">
<td><p>OData filter (query)</p></td>
<td></td>
<td><p>Allows for filtering in the OData. For example:
_01_40_Dienstverband_DatumIngangGeldigheid ge 2018-10-01T00:00:00Z</p>
<p>For more examples, see "Filtering" section in the <a
href="javascript:void(0)" class="help-trigger"
data-helpkey="HelpPageODataApi">OData Api</a> documentation</p></td>
</tr>
<tr class="odd">
<td><p>Enable dynamic properties</p></td>
<td></td>
<td><p>Enables the use for dynamic properties. Turn this off when
connecting to IBIS versions older than 5.4.7</p></td>
</tr>
</tbody>
</table>
