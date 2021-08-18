import sys
import sqlite3

FILE_PATH = "DATA/wombats.txt"

try:
    with open(FILE_PATH) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except FileNotFoundError as err:
    print(err)
print()

try:
    values = [5, 8, 10, 3, 2]
    x = values[10]
except IndexError as err:
    print(err)
    x = 0
    # log error here...

values = [0, 8, 4, 0, "5", 6, 3, "8", 1]
m = 22
for value in values:
    try:
        result = m / value
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    else:
        print(result)

conn = None
try:
    conn = sqlite3.connect('BLARG/FLUFF/foo.db')
except sqlite3.OperationalError as err:
    print(err)
    sys.exit()
else:
    cur = conn.cursor()
    cur.execute("select * from customers")
    print(cur.fetchall())
finally:
    if conn is not None:
        conn.close()





print("ALL DONE.")
