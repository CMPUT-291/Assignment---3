import sqlite3

# Connecting to database and creating cursor
conn = sqlite3.connect('A3Small.db')
cur = conn.cursor()

# running test to check if population worked
cur.execute("SELECT * FROM Customers")
print(len(cur.fetchall()))

# running test to check if the randomization worked
cur.execute("SELECT * FROM Customers")
print(cur.fetchone())

# Commits the Command
conn.commit()

# Closes the connection 
conn.close()