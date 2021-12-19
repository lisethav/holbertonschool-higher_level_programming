#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. 
"""
import MySQLdb
import sys

if __name__ == "__main__":

    datab = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], datab=sys.argv[3])

    cursor = datab.cursor()
    cursor.execute('SELECT * FROM states WHERE name=%s ORDER BY id')
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    datab.close()
