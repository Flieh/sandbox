'''
    utilities
'''
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    '''
        create a database connection to sqlite db
        specified by db_file
        :param dbfile: database file
        :return: Connection object or None
    '''
    if not db_file:
        db_file = ':memory:'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as err:
        print(err)
    finally:
        if conn:
            conn.close()
