# PeopleInc

## PeopleIncModel

### Employee

Employee is mapped as following

|                                 Source (employee)                                 |       Target (PeopleIncModel)       |  Type  |
|:---------------------------------------------------------------------------------|:-----------------------------------|:------|
|                                 activity_fte.Value                                |         Employee_ActivityFte        | String |
|                               activity_status.Value                               |       Employee_ActivityStatus       | String |
|                               business_language.code                              |    Employee_BusinessLanguage_Code   | String |
| Resource name found by match between business_language.code and I18N.Iso6391Code. | Employee_BusinessLanguage_Code_Ibis | String |
|                                business_language.cs                               |     Employee_BusinessLanguage_Cs    | String |
|                                business_language.da                               |     Employee_BusinessLanguage_Da    | String |
|                                business_language.de                               |     Employee_BusinessLanguage_De    | String |
|                                business_language.en                               |     Employee_BusinessLanguage_En    | String |
|                                business_language.es                               |     Employee_BusinessLanguage_Es    | String |
|                                business_language.fr                               |     Employee_BusinessLanguage_Fr    | String |
|                                business_language.it                               |     Employee_BusinessLanguage_It    | String |
|                                business_language.nl                               |     Employee_BusinessLanguage_Nl    | String |
|                                business_language.pl                               |     Employee_BusinessLanguage_Pl    | String |
|                                business_language.pt                               |     Employee_BusinessLanguage_Pt    | String |
|                                 contract_status.cs                                |      Employee_ContractStatus_Cs     | String |
|                                 contract_status.da                                |      Employee_ContractStatus_Da     | String |
|                                 contract_status.de                                |      Employee_ContractStatus_De     | String |
|                                 contract_status.en                                |      Employee_ContractStatus_En     | String |
|                                 contract_status.es                                |      Employee_ContractStatus_Es     | String |
|                                 contract_status.fr                                |      Employee_ContractStatus_Fr     | String |
|                                 contract_status.it                                |      Employee_ContractStatus_It     | String |
|                                 contract_status.nl                                |      Employee_ContractStatus_Nl     | String |
|                                 contract_status.pl                                |      Employee_ContractStatus_Pl     | String |
|                                 contract_status.pt                                |      Employee_ContractStatus_Pt     | String |
|                                   cost_fte.Value                                  |           Employee_CostFte          | String |
|                                    email.Value                                    |            Employee_Email           | String |
|                                 employee_id.Value                                 |         Employee_EmployeeId         | String |
|                                     fax.Value                                     |             Employee_Fax            | String |
|                                  first_name.Value                                 |          Employee_FirstName         | String |
|                               individual_email.Value                              |       Employee_IndividualEmail      | String |
|                      individual_email.Value parsed as boolean                     |    Employee_IndividualEmail_Ibis    |  Bool  |
|                                  last_name.Value                                  |          Employee_LastName          | String |
|                              license_plate_car.Value                              |       Employee_LicensePlateCar      | String |
|                                 middle_names.Value                                |         Employee_MiddleNames        | String |
|                                    mobile.Value                                   |           Employee_Mobile           | String |
|                              participates_in_pm.Value                             |       Employee_ParticipateInPm      | String |
|                                    phone.Value                                    |            Employee_Phone           | String |
|                                     title.code                                    |         Employee_Title_Code         | String |
|                                      title.cs                                     |          Employee_Title_Cs          | String |
|                                      title.da                                     |          Employee_Title_Da          | String |
|                                      title.de                                     |          Employee_Title_De          | String |
|                                      title.en                                     |          Employee_Title_En          | String |
|                                      title.es                                     |          Employee_Title_Es          | String |
|                                      title.fr                                     |          Employee_Title_Fr          | String |
|                                      title.it                                     |          Employee_Title_It          | String |
|                                      title.nl                                     |          Employee_Title_Nl          | String |
|                                      title.pl                                     |          Employee_Title_Pl          | String |
|                                      title.pt                                     |          Employee_Title_Pt          | String |
|                                  user_name.Value                                  |          Employee_UserName          | String |
|                                    work_site.cs                                   |         Employee_WorkSite_Cs        | String |
|                                    work_site.da                                   |         Employee_WorkSite_Da        | String |
|                                    work_site.de                                   |         Employee_WorkSite_De        | String |
|                                    work_site.en                                   |         Employee_WorkSite_En        | String |
|                                    work_site.es                                   |         Employee_WorkSite_Es        | String |
|                                    work_site.fr                                   |         Employee_WorkSite_Fr        | String |
|                                    work_site.it                                   |         Employee_WorkSite_It        | String |
|                                    work_site.nl                                   |         Employee_WorkSite_Nl        | String |
|                                    work_site.pl                                   |         Employee_WorkSite_Pl        | String |
|                                    work_site.pt                                   |         Employee_WorkSite_Pt        | String |
## Contract

Contract is mapped as following

|                                                                                     Source (contract)                                                                                    |          Target (PeopleIncModel)         |    Type   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|:---------|
|                                                                    When no contract is available this property is true                                                                   |            Contract_NotPresent           |    bool   |
|                                                                             allocation_employment_entity.code                                                                            | Contract_AllocationEmploymentEntity_Code |   String  |
|                                                                              allocation_employment_entity.cs                                                                             |  Contract_AllocationEmploymentEntity_Cs  |   String  |
|                                                                              allocation_employment_entity.da                                                                             |  Contract_AllocationEmploymentEntity_Da  |   String  |
|                                                                              allocation_employment_entity.de                                                                             |  Contract_AllocationEmploymentEntity_De  |   String  |
|                                                                              allocation_employment_entity.en                                                                             |  Contract_AllocationEmploymentEntity_En  |   String  |
|                                                                              allocation_employment_entity.es                                                                             |  Contract_AllocationEmploymentEntity_Es  |   String  |
|                                                                              allocation_employment_entity.fr                                                                             |  Contract_AllocationEmploymentEntity_Fr  |   String  |
|                                                                              allocation_employment_entity.it                                                                             |  Contract_AllocationEmploymentEntity_It  |   String  |
|                                                                              allocation_employment_entity.nl                                                                             |  Contract_AllocationEmploymentEntity_Nl  |   String  |
|                                                                              allocation_employment_entity.pl                                                                             |  Contract_AllocationEmploymentEntity_Pl  |   String  |
|                                                                              allocation_employment_entity.pt                                                                             |  Contract_AllocationEmploymentEntity_Pt  |   String  |
|                                                                                   business_title.Value                                                                                   |          Contract_BusinessTitle          |   String  |
|                                                                                    contract_fte.Value                                                                                    |           Contract_ContractFte           |   String  |
|                                                                                contract_legal_entity.code                                                                                |     Contract_ContractLegalEntity_Code    |   String  |
|                                                                                 contract_legal_entity.cs                                                                                 |      Contract_ContractLegalEntity_Cs     |   String  |
|                                                                                 contract_legal_entity.da                                                                                 |      Contract_ContractLegalEntity_Da     |   String  |
|                                                                                 contract_legal_entity.de                                                                                 |      Contract_ContractLegalEntity_De     |   String  |
|                                                                                 contract_legal_entity.en                                                                                 |      Contract_ContractLegalEntity_En     |   String  |
|                                                                                 contract_legal_entity.es                                                                                 |      Contract_ContractLegalEntity_Es     |   String  |
|                                                                                 contract_legal_entity.fr                                                                                 |      Contract_ContractLegalEntity_Fr     |   String  |
|                                                                                 contract_legal_entity.it                                                                                 |      Contract_ContractLegalEntity_It     |   String  |
|                                                                                 contract_legal_entity.nl                                                                                 |      Contract_ContractLegalEntity_Nl     |   String  |
|                                                                                 contract_legal_entity.pl                                                                                 |      Contract_ContractLegalEntity_Pl     |   String  |
|                                                                                 contract_legal_entity.pt                                                                                 |      Contract_ContractLegalEntity_Pt     |   String  |
|                                                                                    contract_type.code                                                                                    |        Contract_ContractType_Code        |   String  |
|                                                                                     contract_type.cs                                                                                     |         Contract_ContractType_Cs         |   String  |
|                                                                                     contract_type.da                                                                                     |         Contract_ContractType_Da         |   String  |
|                                                                                     contract_type.de                                                                                     |         Contract_ContractType_De         |   String  |
|                                                                                     contract_type.en                                                                                     |         Contract_ContractType_En         |   String  |
|                                                                                     contract_type.es                                                                                     |         Contract_ContractType_Es         |   String  |
|                                                                                     contract_type.fr                                                                                     |         Contract_ContractType_Fr         |   String  |
|                                                                                     contract_type.it                                                                                     |         Contract_ContractType_It         |   String  |
|                                                                                     contract_type.nl                                                                                     |         Contract_ContractType_Nl         |   String  |
|                                                                                     contract_type.pl                                                                                     |         Contract_ContractType_Pl         |   String  |
|                                                                                     contract_type.pt                                                                                     |         Contract_ContractType_Pt         |   String  |
|                                                                                      end_date.Value                                                                                      |             Contract_EndDate             |   String  |
|                                                                             end_date.Value parsed as DateTime                                                                            |           Contract_EndDate_Ibis          | DateTime? |
|                                                                                   hr_responsible.Value                                                                                   |          Contract_HrResponsible          |   String  |
| Lookup of first name in hr_responsible.Value which result in IdmNumber from IDossier.<br> <br>Matching on:<br> <br>§   _42_11_Persoon_Geslachtsnaam<br> <br>§   _42_15_Persoon_Voornamen |        Contract_HrResponsible_Ibis       |   String  |
|                                                                                     is_manager.Value                                                                                     |            Contract_IsManager            |   String  |
|                                                                            is_manager.Value parsed as Boolean                                                                            |          Contract_IsManager_Ibis         |    Bool   |
|                                                  First item from job_description_family.name where en not empty and type == “translated”                                                 |       Contract_JobDescriptionFamily      |   String  |
|                                                                                job_description_level_2.cs                                                                                |     Contract_JobDescriptionLevel2_Cs     |   String  |
|                                                                                job_description_level_2.da                                                                                |     Contract_JobDescriptionLevel2_Da     |   String  |
|                                                                                job_description_level_2.de                                                                                |     Contract_JobDescriptionLevel2_De     |   String  |
|                                                                                job_description_level_2.en                                                                                |     Contract_JobDescriptionLevel2_En     |   String  |
|                                                                                job_description_level_2.es                                                                                |     Contract_JobDescriptionLevel2_Es     |   String  |
|                                                                                job_description_level_2.fr                                                                                |     Contract_JobDescriptionLevel2_Fr     |   String  |
|                                                                                job_description_level_2.it                                                                                |     Contract_JobDescriptionLevel2_It     |   String  |
|                                                                                job_description_level_2.nl                                                                                |     Contract_JobDescriptionLevel2_Nl     |   String  |
|                                                                                job_description_level_2.pl                                                                                |     Contract_JobDescriptionLevel2_Pl     |   String  |
|                                                                                job_description_level_2.pt                                                                                |     Contract_JobDescriptionLevel2_Pt     |   String  |
|                                                                                        level_2.cs                                                                                        |            Contract_Level2_Cs            |   String  |
|                                                                                        level_2.da                                                                                        |            Contract_Level2_Da            |   String  |
|                                                                                        level_2.de                                                                                        |            Contract_Level2_De            |   String  |
|                                                                                        level_2.en                                                                                        |            Contract_Level2_En            |   String  |
|                                                                                        level_2.es                                                                                        |            Contract_Level2_Es            |   String  |
|                                                                                        level_2.fr                                                                                        |            Contract_Level2_Fr            |   String  |
|                                                                                        level_2.it                                                                                        |            Contract_Level2_It            |   String  |
|                                                                                        level_2.nl                                                                                        |            Contract_Level2_Nl            |   String  |
|                                                                                        level_2.pl                                                                                        |            Contract_Level2_Pl            |   String  |
|                                                                                        level_2.pt                                                                                        |            Contract_Level2_Pt            |   String  |
|                                                                                        level_3.cs                                                                                        |            Contract_Level3_Cs            |   String  |
|                                                                                        level_3.da                                                                                        |            Contract_Level3_Da            |   String  |
|                                                                                        level_3.de                                                                                        |            Contract_Level3_De            |   String  |
|                                                                                        level_3.en                                                                                        |            Contract_Level3_En            |   String  |
|                                                                                        level_3.es                                                                                        |            Contract_Level3_Es            |   String  |
|                                                                                        level_3.fr                                                                                        |            Contract_Level3_Fr            |   String  |
|                                                                                        level_3.it                                                                                        |            Contract_Level3_It            |   String  |
|                                                                                        level_3.nl                                                                                        |            Contract_Level3_Nl            |   String  |
|                                                                                        level_3.pl                                                                                        |            Contract_Level3_Pl            |   String  |
|                                                                                        level_3.pt                                                                                        |            Contract_Level3_Pt            |   String  |
|                                                                                        manager.urn                                                                                       |           Contract_Manager_Urn           |   String  |
|                                       Lookup IdmNumber in IDossier for manager by match on _42_08_Persoon_IdentificatieBronsysteem with manager.urn                                      |           Contract_Manager_Ibis          |   String  |
|                                                                                     start_date.Value                                                                                     |            Contract_StartDate            |   String  |
|                                                                            start_date.Value parsed as DateTime                                                                           |          Contract_StartDate_Ibis         | DateTime? |