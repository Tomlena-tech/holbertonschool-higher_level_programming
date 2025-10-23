#!/usr/bin/env python3


"""Listing all states from USA database """
import MySQLdb
import sys


def list_states(user: str, password: str, db_name: str)
    """Se connecte et affiche les états."""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

# Protection « pas d'exécution à l'import »
if __name__ == "__main__":
    # Récupération des 3 arguments tels quels
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(user, password, db_name)
