#!/usr/bin/python3
"""
cities_by_state module

listing all cities in hbtn_0e_0_usa database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3]
            )
    cur = con.cursor()
    cur.execute(
            """SELECT cities.id, cities.name, states.name FROM cities
            JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
            )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
