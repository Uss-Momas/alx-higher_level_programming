#!/usr/bin/python3
"""
5-filter_cities Module

Lists all cities acording to a filter provided by user
"""

import MySQLdb
from sys import argv


def print_row(table):
    """Function for printing tuple values in a normal way
    Args:
        -table: the query rows result
    """
    size = len(table)
    i = 0
    for row in table:
        if i != size - 1:
            print(row[0], end=", ")
        else:
            print(row[0])
        i += 1


if __name__ == "__main__":
    con = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3]
            )

    state_name = argv[4]
    cur = con.cursor()
    cur.execute(
            """SELECT cities.name FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC
            """, (state_name,)
            )
    query_rows = cur.fetchall()
    # print_row(query_rows)
    print(", ".join(city[0] for city in query_rows))
    cur.close()
    con.close()
