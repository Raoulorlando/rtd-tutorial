# <span id="index"></span>ABAC Connectors


-   [Introduction](#introduction)
-   [Staging area](#stagingarea)
-   [Settings](#GeneralSettings)
-   [Thresholds](#thresholds)
-   [Operations](#operations)
-   [Modules](#modules)

(introduction)=
::rubric:: ## <span id="Introductie"></span>Introduction

The ABAC connector framework enables membership enforcement in external
systems. The connector uses vendor-specific modules for communication
with external systems. A number of modules are available out-of-the-box.
In case an external system cannot be connected using an existing module,
a custom module can be developed.

The connector framework works with staging area objects, targets and
roles. For readability we will refer to them as groups, users and roles.

::rubric:: ## <span id="StagingArea"></span>Staging area

Each connector contains a staging area for intermediate storage of
objects.  
For more information how to use the staging area, see the
<a href="javascript:void(0)" class="help-trigger"
data-helpkey="SysPage_AbacStagingArea">Staging Area</a> documentation

::rubric::## <span id="GeneralSettings"></span>Settings

**Orientation**  
Determines which type of objects are managed by this connector:

-   Resource: one or more resources are linked to an external object.
    Members of the resource will be added as a member of the external
    object
-   Target: a single target is mapped to an external object. Role
    memberships of the target will be added as a memberOf on the
    external object

**Name**  
The name of the connector. This name will be used to identify the
connector in system logs and run history.  
Changing the name has no impact on operations.

**Role property which contains the group identifiers managed by this
connector (resource oriented)**  
This setting is used to locate the roles responsible for each group in
this connector.

During a synchronization, the connector searches for roles which have
the specified property set to the External ID of the group.  
The members of the resulting roles will be added to the group, and
removed when they are no longer a member of a role which assigns the
group

A single role can manage multiple groups, and multiple roles can manage
a single group.

**Role property which contains the value that must be set in the
external system (target oriented)**  
This setting is used to determine the value(s) that must be set on the
external object

**Target property which contains the primary key for targets in this
connector**  
This setting is used to determine the External ID of targets in the
connected system (for example, a UPN).  
In case a target should be added to a group but the External ID cannot
be determined, the target will be skipped.

::rubric:: ## <span id="Thresholds"></span>Thresholds

Thresholds can be used to abort processing when certain limits are
reached. To configure thresholds, open the Thresholds tab of the
connector:

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Use object count instead of percentage</p></td>
<td><p>Enabled: the number specified will be used as object count
threshold</p>
<p>Disabled: the number specified will be used as percentage</p></td>
</tr>
<tr class="even">
<td><p>Create</p></td>
<td><p>The total percentage (or count) of members that will be
added</p></td>
</tr>
<tr class="odd">
<td><p>Delete</p></td>
<td><p>The total percentage (or count) of members that will be
removed</p></td>
</tr>
</tbody>
</table>

When a threshold violation occurs, processing is aborted immediately
and:

-   A log entry is written to the system log
-   And error will be shown in the connector overview page

[Top](#index)

::rubric:: ## <span id="Operations"></span>Operations

**Sync**  
Calculates members for groups, and stages the necessary export changes
on the staging area object.

**Full Import**  
Reads all object from the external system and updates the staging area.

**Delta Import**  
Reads all object from the external system which are changed since the
last import, and updates the staging area.

**Export**  
Processes all pending exports in the connected system.

(modules)=
## <span id="Modules"></span>Modules

Below table displays the modules are available in a standard
installation.

| Module                          | Full Import | Delta Import |
|---------------------------------|-------------|--------------|
| Microsoft Active Directory      | X           | X            |
| [Microsoft Entra Id](./AbacConnector_MicrosoftEntraId.md)              | X           | X            |
| [Google Groups](./AbacConnector_GoogleGroup.md)                 | X           |              |
| [Google Calendar](./AbacConnector_GoogleCalendar.md)                 | X           |              |
| [Google Mailbox](./AbacConnector_GoogleMailbox.md)                 | X           |              |

  

[Top](#index)
