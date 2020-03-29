#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 4:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    value = cur.fetchone()
    while value is not None:
        print (value)
        value = cur.fetchone()

    cur.close()
    db.close()
