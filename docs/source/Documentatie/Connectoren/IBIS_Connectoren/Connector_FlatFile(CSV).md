# Flat File (CSV)

The CSV connector is capable of reading from- and writing to character
separated text files. the module supports import and export operations.

The file should contain columns separated by the ***Column separator***
parameter. A ***Text qualifier*** can be set in order for IBIS to
recognize the text portion of a column.

If the data in a colum contains the text qualifier itself (for example,
the text qualifier is **‘**, en the data is **Dhr. A in 't Veld**), the
qualifier should be escaped by duplicating it (**Dhr. A in 't Veld**).

## Parameters

| Parameter                                   |     Required    |                                                                                                        Description                                                                              |
|:--------------------------------------------|:---------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File path                                   |                 | The full path name of the file which contains the objects to import                                                                                                                             |
| Export file path                            |                 | The full path name of the file in which exported objects will be written                                                                                                                        |
| File contains a header                      |        X        | If set, the first row in the file contains the column names                                                                                                                                     |
| File header                                 |                 | In case the file does not contain a header, specify the header here. Use the same format as the file contents (including the column separator and optional text-qualifier)                      |
| Column separator                            |        X        | The character(s) that is used to separate columns                                                                                                                                               |
| Text qualifier                              |                 | The character(s) that is used to specify text                                                                                                                                                   |
| Encoding                                    |        X        | The encoding of the file                                                                                                                                                                        |
| Primary key column                          |        X        | The name of the primary key column in the file. This is used to set the ExternalID property on the staging area entity                                                                          |
