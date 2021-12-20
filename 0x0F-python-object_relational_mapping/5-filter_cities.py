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
    cursor.execute('''SELECT cities.name FROM cities JOIN states ON states.id
                    = cities.state_id WHERE states.name=%s ORDER BY cities.id''',
                    (sys.argv[4]))
    for i in cursor.fetchall():
        print(", ".join(["{}".format(i[0])]))

    cursor.close()
    datab.close()
