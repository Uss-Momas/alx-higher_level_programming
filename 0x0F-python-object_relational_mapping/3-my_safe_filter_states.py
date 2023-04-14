#!/usr/bin/python3
"""
3-my_safe_filter_states Module
Filtering the states table in a safe way
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    state_name_searched = argv[4]
    cur = con.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (state_name_searched,)
            )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
