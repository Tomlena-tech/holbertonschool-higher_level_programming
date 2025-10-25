#!/usr/bin/python3

"""
Module qui permet de récupérer une liste de ville des
USA en utilisant un nom en argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
