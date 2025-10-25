#!/usr/bin/python3

"""
Module qui permet de récupérer une liste de ville des
USA ainsi que des les afficher à l'écran.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name "
                "FROM cities c JOIN states s ON c.state_id = s.id "
                "ORDER BY c.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
