#!/usr/bin/python3
"""
2-my_filter_state Module

Filtering the table states by user input
where the name matches this input
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3],
            )

    st_name = argv[4]
    cur = conection.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
            .format(st_name)
            )
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == st_name:
            print(row)
    cur.close()
    conection.close()
