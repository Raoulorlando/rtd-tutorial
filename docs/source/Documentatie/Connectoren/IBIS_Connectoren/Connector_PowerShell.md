# PowerShell

The PowerShell module is capable of importing the results of a
PowerShell command

## Parameters

|     Parameter    | Required |                                                      Description                                                      |
|:-----------------|:--------:|:----------------------------------------------------------------------------------------------------------------------|
|     Hostname     |          |                            Optional, the name of the Windows or Exchange host to connect to                           |
| PowerShell Agent |          |              Optional, the PowerShell agent to use. Cannot be used in conjunction with a connector agent              |
|       Mode       |     X    |                                    Used to determine the shell URI if a host is set                                   |
|     Username     |     X    |      The username of the account to use for authentication. This cannot be the same as the IBIS app pool account      |
|     Password     |     X    |                                           The password of above user account                                          |
|      Command     |     X    | The PowerShell command (one-liner) to execute. Dynamic expressions may be used. Either command or script are required |
|      Script      |     X    |        The PowerShell script to execute. Dynamic expressions may be used. Either command or script are required       |
|    Identifier    |     X    |                                     The name of the property to use as primary key                                    |