#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    datab = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], datab=sys.argv[3])

    cursor = datab.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    datab.close()
