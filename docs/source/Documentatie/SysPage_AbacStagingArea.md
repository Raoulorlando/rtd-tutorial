# ABAC Staging area

Each connector contains a staging area for intermediate storage of
objects.

A staging area object consists of 3 major parts:

|      Component      |                                          Description                                         |
|:-------------------:|:--------------------------------------------------------------------------------------------:|
| General information | Information about connection state, exclusion, external ID, etc.                             |
| Members             | The representation of the current members of the object as imported from the external system |
| Pending export      | A list of property/value combinations that needs to be exported to the external system       |
