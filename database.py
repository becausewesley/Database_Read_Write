import sqlite3
import xlrd


def main():
    database_file_path = ''
    excel_file_path = ''

    db = sqlite3.connect(database_file_path)
    db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT, phone INTEGER)")
    db.execute("CREATE TABLE IF NOT EXISTS duplicates (name TEXT, email TEXT, phone INTEGER)")

    read_contacts(excel_file_path, db)

    db.close()


def read_contacts(filename: str, database) -> None:
    """
    Reads the contacts from the excel sheet, and then calls the add_contact
    function to add the contact to the DB.

    :param filename: The excel file
    :param database: The SQL DB
    """
    wb = xlrd.open_workbook(filename)  # opens the excel workbook
    sheet = wb.sheet_by_index(0)  # gets the sheet

    number_of_rows = sheet.nrows  # total number of rows in the sheet

    blank_counter = 0  # Will count the number of blank phone numbers

    # Loops through each row in the excel sheet
    for row in range(0, number_of_rows):
        name, email, phone = sheet.row_values(row)  # assigns variables for the row contents
        # print(name, email, phone)  # for debugging

        # If no email or phone, skip the contact
        if email == '' and phone == '':
            continue
        elif phone == '':
            # Here we pass the counter number so that there is a unique
            # number added to the blank phone number column
            add_contact(database, name, email, blank_counter)
            blank_counter += 1  # Increment the counter
        else:
            add_contact(database, name, email, phone)

        # print(sheet.row_values(row))  # for debugging


def add_contact(database, name: str, email: str, phone: int) -> None:
    """
    Checks if the current contact already exists in the database, and adds
    it if it does not exist. Otherwise, the contact is added to the "duplicates"
    table.

    :param database: The database to add the contacts to
    :param name: The contact name
    :param email: The contact email
    :param phone: The contact phone number
    """
    cursor = database.execute("SELECT DISTINCT name, email, phone FROM contacts "
                              "WHERE name = ? AND email =? OR phone = ?", (name, email, phone))

    row = cursor.fetchone()
    print(row)  # For debugging

    # This checks if the contact already exists in the database or not
    if row:
        print("\n{}, {}, {} is already in the database.".format(name, email, phone))
        database.execute("INSERT INTO duplicates VALUES (?, ?, ?)", (name, email, phone))
    else:
        cursor.execute("INSERT INTO contacts VALUES (?, ?, ?)", (name, email, phone))
        cursor.connection.commit()
        # print("{}, {}, {} added to database.".format(name, email, phone))     # For debugging


if __name__ == '__main__':
    main()
