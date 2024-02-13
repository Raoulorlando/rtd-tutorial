<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_Connector">Connectors</a> / IBIS API

##### IBIS

The IBIS connector module supports import and export of data from and to
another IBIS instance through the ODATA API.

#### Parameters

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
<li>ActivityApiModel</li>
<li>AliasDossierApiModel</li>
<li>ApplicationDossierProductApiModel</li>
<li>ApplicationDossierApiModel</li>
<li>AssetApiModel</li>
<li>AssetRelationApiModel</li>
<li>BestelmethodeApiModel</li>
<li>ContractApiModel</li>
<li>DossierStateApiModel</li>
<li>DynamicPropertyApiModel</li>
<li>EpicDossierApiModel</li>
<li>FmhDossierApiModel</li>
<li>FormatieplaatsApiModel</li>
<li>IBISQueueApiModel</li>
<li>IdentityDossierApiModel</li>
<li>IDossierApiModel</li>
<li>IDossierFotoApiModel</li>
<li>LokatiegegevenApiModel</li>
<li>MailTemplateApiModel</li>
<li>OrganisatieApiModel</li>
<li>PbsDossierApiModel</li>
<li>ProductApiModel</li>
<li>ProductGroupApiModel</li>
<li>ProductGroupFilterApiModel</li>
<li>ProductGroupFilterOrganisationApiModel</li>
<li>ProductGroupFilterTypeApiModel</li>
<li>ProductGroupProductApiModel</li>
<li>ProductOrganisationApiModel</li>
<li>ProductStateApiModel</li>
<li>ProductSupplierApiModel</li>
<li>RegisterApiModel</li>
<li>RemarkApiModel</li>
<li>SysInputFieldApiModel</li>
<li>TgDossierApiModel</li>
<li>TransitionApiModel</li>
<li>WaitingActivityApiModel</li>
<li>WidDossierApiModel</li>
<li>WithdrawRelationApiModel</li>
<li>WorkflowApiModel</li>
</ul></td>
</tr>
<tr class="even">
<td><p>IBIS object name</p></td>
<td><p><strong>X</strong></p></td>
<td><p>The name of the IBIS object to synchronize. Supported values
are:</p>
<ul>
<li>AliasDossier</li>
<li>ApplicationDossier</li>
<li>ApplicationDossierProduct</li>
<li>Asset</li>
<li>Bestelmethode</li>
<li>Contract</li>
<li>EpicDossier</li>
<li>FmhDossier</li>
<li>Formatieplaats</li>
<li>Functie</li>
<li>Functieroepnaam</li>
<li>Group</li>
<li>IbisQueue</li>
<li>IdentityDossier</li>
<li>IdmNumber</li>
<li>IDossier</li>
<li>Land</li>
<li>Lokatiegegevens</li>
<li>MailTemplate</li>
<li>Notification</li>
<li>NotificationAttachment</li>
<li>NotificationAttribute</li>
<li>Organisatie</li>
<li>PbsDossier</li>
<li>Product</li>
<li>ProductGroup</li>
<li>ProductGroupFilter</li>
<li>ProductGroupFilterOrganisation</li>
<li>ProductGroupFilterType</li>
<li>ProductGroupFunction</li>
<li>ProductGroupOrganisation</li>
<li>ProductGroupProduct</li>
<li>ProductGroupProductGroupFilter</li>
<li>ProductGroupSupplier</li>
<li>ProductOrganisation</li>
<li>ProductStatus</li>
<li>ProductSupplier</li>
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
<li>ApplicationDossierProducts</li>
<li>ApplicationDossiers</li>
<li>Assets</li>
<li>Bestelmethodes</li>
<li>Contracts</li>
<li>DossierStates</li>
<li>DynamicProperties</li>
<li>EpicDossiers</li>
<li>FmhDossiers</li>
<li>Formatieplaatsen</li>
<li>IBISQueues</li>
<li>IDentityDossiers</li>
<li>IDossierFoto</li>
<li>IDossiers</li>
<li>Lokatiegegevens</li>
<li>MailTemplates</li>
<li>Organisaties</li>
<li>PbsDossiers</li>
<li>ProductGroupFilterOrganisations</li>
<li>ProductGroupFilters</li>
<li>ProductGroupFilterTypes</li>
<li>ProductGroupProducts</li>
<li>ProductGroups</li>
<li>ProductOrganisations</li>
<li>Products</li>
<li>ProductStates</li>
<li>ProductSuppliers</li>
<li>Registers</li>
<li>Remarks</li>
<li>SysInputFields</li>
<li>TgDossiers</li>
<li>WidDossiers</li>
<li>Workflows</li>
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
