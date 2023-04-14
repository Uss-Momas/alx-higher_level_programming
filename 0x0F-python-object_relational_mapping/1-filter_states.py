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
        # (5, 'Nevada') -> Nevada is string
        # row[1] => 'Nevada', 'Nevada'[0] => 'N'
        # making sure we a only printing the records
        # that starts with 'N'
        if row[1][0] == 'N':
            print(row)
    cur.close()
    con.close()
