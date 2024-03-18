# <span id="index"></span>Run profile settings

###### General settings

|              Setting             |                  Description                 |
|:---------------------------------|:---------------------------------------------|
| Name                             | The name of run profile                      |
| Schedule (CRON)                  | The schedule                                 |
| Temporarily turn off run profile | If set, the run profile will not be executed |

###### Steps

|      Setting     |                                                                                                                                                     Description                                                                                                                                                     |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type             | The type of operation. Choose from:<br> <br> <br>- ABAC: execute a background task in ABAC<br> <br>- Connector: execute a connector profile<br> <br>- BackgroundTask: execute a configured background task<br> <br>- PowerShellScript: execute a PowerShell script<br> <br>- Workflow: execute a configured workflow          |
| ABAC             |  <br>- Task: the task to execute<br> <br>- Timeout: the time in minutes IBIS will wait for ABAC to finish                                                                                                                                                                                                               |
| Connector        |  <br>- Connector: the connector to execute<br> <br>- Operation: the operation to execute on the connector                                                                                                                                                                                                               |
| BackgroundTask   |  <br>- Background task: the task to execute. This task must be configured on the [background tasks]() page in order to be selectable                                                                                                                                                                                      |
| Workflow         |  <br>- Workflow: The workflow to execute                                                                                                                                                                                                                                                                              |
| PowerShellScript |  <br>- Agent: optional, the agent the script must be executed on<br> <br>- Hostname: optional, the machine the script must be executed on<br> <br>- Username: the username of the account that must be used to execute the script<br> <br>- Password: the password of above username<br> <br>- Script: the script to execute  |
| Disabled         | If set, the run profile will not be executed                                                                                                                                                                                                                                                                        |
| Abort on error   | If set, subsequent steps will not be executed in case an error occurs                                                                                                                                                                                                                                               |
