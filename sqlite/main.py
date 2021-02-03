''' database example '''

import sqlite3

if __name__ == '__main__':
    # connect database
    cnx = sqlite3.connect('./accounts.db')

    # create cursor object on connection
    crs = cnx.cursor()

    # open sql file
    sql_file = open('query.sql')

    # parse sql file into string
    sql_string = sql_file.read()

    # execute sql file on cursor
    crs.executescript(sql_string)

    # show db contents
    for records in crs.execute('select * from accounts'):
        print(records)
