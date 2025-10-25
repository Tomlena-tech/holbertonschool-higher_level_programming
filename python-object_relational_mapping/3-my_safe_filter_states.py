#!/usr/bin/python3
"""
Script that displays all values in the states table
where name matches the argument (safe from SQL injection)
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
    
    # CHANGEMENT ICI : Paramètres préparés au lieu de .format()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()
