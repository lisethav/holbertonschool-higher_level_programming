#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    datab = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3])

    cursor = datab.cursor()
    cursor.execute('''SELECT cities.id, cities.name, states.name FROM states 
                    INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id''')
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    datab.close()
