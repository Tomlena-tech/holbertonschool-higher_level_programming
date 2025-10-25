#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query with JOIN to get cities with their state names
    cursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch and display all results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
