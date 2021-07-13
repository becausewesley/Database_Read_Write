## Database Read and Write

> This program has been designed for use in a contacts database. If you 
> would like to use some of this code for use with other databases, you 
> will need to change up some of the logic, specifically lines 34 to 47, 
> and any other references to "Database-specific" variables.

This iterates over the rows in an excel spreadsheet, checks whether they already exist in the DB. If they do, they are
added to a 'duplicates' table in the DB, to retain any data.
<br />
<br />
This program also creates the databases mentioned above - however the file paths can be set to use any existing
database, but this will require some changes to the names of the tables and columns:

    db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT, phone INTEGER)")
    db.execute("CREATE TABLE IF NOT EXISTS duplicates (name TEXT, email TEXT, phone INTEGER)")

### Other important snippets to take note of:
- **Worksheet sheet number (line 27):** <br /><br />
`    sheet = wb.sheet_by_index(0)  # gets the sheet` <br /><br />
  If you have more than one sheet, or want to specify a sheet in the excel file, specify it here.<br />
  <br />
  

###Third party libraries:
This program uses the _[xlrd](https://xlrd.readthedocs.io/en/latest/)_ library.
<br />
Install using:
`pip install xlrd`



    