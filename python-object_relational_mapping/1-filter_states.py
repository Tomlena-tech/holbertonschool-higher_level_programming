#!/usr/bin/python3

"""
Module qui permet de récupérer une liste de ville des
USA commencant par la lettre N.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
