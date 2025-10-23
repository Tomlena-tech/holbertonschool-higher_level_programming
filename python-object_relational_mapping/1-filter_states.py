#!/usr/bin/python3
"""Create a script who's listing cities starting by 'N'"""

import MySQLdb
import sys


def filter_list_states(user: str, password: str, db_name: str):
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    