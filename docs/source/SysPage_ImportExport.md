##### <span id="index"></span>IBIS Configuration Import/Export

It's possible to export an IBIS configuration and import it in another
environment. This may prove useful for keeping an OTAP environment in
sync or just to have a backup of your configuration.

-   When importing a configuration the current configuration will be
    wiped and only the configuration present in the import file will be
    left.
-   Import and export can be started from the Import/Export page at
    ~/ImportExport

Only object present in the ConfigurationExportTypes key in
AppSettings.config will be exported. The value of this setting is a
comma separated list of objects to export. Possible objects are:

-   AclForImportExport
-   AuthorizationObjectForImportExport
-   AuthorizationPropertyForImportExport
-   DataSetForImportExport
-   I18NResourceOverrideForImportExport
-   MailTemplateForImportExport
-   PasswordModuleForImportExport
-   SysAccordionForImportExport
-   SysButtonForImportExport
-   SysCategoryForImportExport
-   SysDossierStatusForImportExport
-   SysGeneralForImportExport
-   SysGridResultFieldForImportExport
-   SysInputFieldForImportExport
-   SysLicenseForImportExport
-   SysListItemForImportExport
-   SysListItemCategoryForImportExport
-   SysMenuItemForImportExport
-   SysPageForImportExport
-   SysRoleForImportExport
-   SysRoleAutorisationAttributeForImportExport
-   SysRoleAutorisationAttributeTypeForImportExport
-   SysRoleDossierStatusForImportExport
-   SysRoleRelationForImportExport
-   SysSearchControlForImportExport
-   SysSearchFieldForImportExport
-   TaskForImportExport
-   TaskParameterForImportExport
-   TypeDienstverbandHoofdgroepForImportExport
-   TypeDienstverbandSubgroepForImportExport
-   WorkflowForImportExport
-   WorkflowActivityForImportExport
-   WorkflowTransitionForImportExport

*NOTE: After changing AppSettings.config the IBIS application pool needs
to be recycled to load the changes*

[Top](#index)

  
