#!/usr/bin/python3
"""
filter states Module
Lists all states that starts name with 'N'
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    hst = 'localhost'
    prt = 3306
    user = argv[1]
    passw = argv[2]
    db = argv[3]

    con = MySQLdb.connect(host=hst, port=prt, user=user, passwd=passw, db=db)
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
