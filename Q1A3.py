# importing all the necessary modules needed 
import sqlite3 
import time
import matplotlib.pyplot as plt
import numpy as np

# for creating and running test on uninformed and returns list of run times to calc avg from
def create_uninf_db(cur, conn):
    # creates a replica of the tables which doesn't have primary and foreign keys assigned to them
    cur.execute("PRAGMA foreign_keys = OFF")
    cur.execute("PRAGMA automatic_index = FALSE")
    cur.executescript('''DROP TABLE IF EXISTS Customers_new;
                        DROP TABLE IF EXISTS Orders_new;
                        DROP TABLE IF EXISTS Sellers_new;
                        DROP TABLE IF EXISTS Order_items_new;''')
    cur.executescript('''CREATE TABLE Customers_new(customer_id, customer_postal_code); 
                        CREATE TABLE Sellers_new (seller_id, seller_postal_code); 
                        CREATE TABLE Orders_new (order_id, customer_id); 
                        CREATE TABLE Order_items_new (order_id, order_item_id, product_id, seller_id);''' )
    cur.executescript('''INSERT INTO Customers_new SELECT * FROM Customers; 
                        INSERT INTO Sellers_new SELECT * FROM Sellers; 
                        INSERT INTO Orders_new SELECT * FROM Orders; 
                        INSERT INTO Order_items_new SELECT * FROM Order_items; ''')
    conn.commit()
    exec_times = []
    for i in range(50):
        start = time.time()
        cur.execute("""SELECT COUNT(*) as ANSWER
                    FROM (SELECT nos.order_id
                        FROM (SELECT o.order_id
                            FROM Orders_new o, Customers_new c
                            WHERE c.customer_id = o.customer_id AND (c.customer_postal_code = (SELECT c.customer_postal_code FROM Customers_new c ORDER BY random() LIMIT 1))) nos
                        WHERE (SELECT COUNT(*) FROM Order_items i WHERE i.order_id = nos.order_id) > 1)""")
        end = time.time()
        exec_times.append((end - start) * 1000)
    return exec_times

# for creating and running test on self-optimized and returns list of run times to calc avg from
def create_self_db(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("PRAGMA automatic_index = TRUE")
    conn.commit()

    exec_times = []
    for i in range(50):
        start = time.time()
        cur.execute("""SELECT COUNT(*) as ANSWER
                    FROM (SELECT nos.order_id
                        FROM (SELECT o.order_id
                            FROM Orders o, Customers c
                            WHERE c.customer_id = o.customer_id AND (c.customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1))) nos
                        WHERE (SELECT COUNT(*) FROM Order_items i WHERE i.order_id = nos.order_id) > 1)""")
        end = time.time()
        exec_times.append((end - start) * 1000)
    return exec_times

# for creating and running test on user-optimized and returns list of run times to calc avg from
def create_user_db(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("PRAGMA automatic_index = FALSE")
    cur.executescript(""" DROP INDEX IF EXISTS idx_order_id;
                            DROP INDEX IF EXISTS idx_customer_id;
                            DROP INDEX IF EXISTS idx_cust_postal_code;""")
    cur.executescript("""CREATE INDEX idx_order_id ON Orders(order_id);
                            CREATE INDEX idx_customer_id ON Customers(customer_id);
                            CREATE INDEX idx_cust_postal_code ON Customers(customer_postal_code);""")
    conn.commit()

    exec_times = []
    for i in range(50):
        start = time.time()
        cur.execute("""SELECT COUNT(*) as ANSWER
                    FROM (SELECT nos.order_id
                        FROM (SELECT o.order_id
                            FROM Orders o, Customers c
                            WHERE c.customer_id = o.customer_id AND (c.customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1))) nos
                        WHERE (SELECT COUNT(*) FROM Order_items i WHERE i.order_id = nos.order_id) > 1)""")
        end = time.time()
        exec_times.append((end - start) * 1000)
    return exec_times

# calculates the average of all the data present in a list 
def average(runtimes):
    avg = sum(runtimes)/len(runtimes)
    return avg

# Connecting to database, creating cursor, running the test and procuring the average run time for small db first query 
conn = sqlite3.connect('A3Small.db')
cur = conn.cursor()

run_times = create_uninf_db(cur, conn)
average_undef_run_times_small = average(run_times)
print(average_undef_run_times_small)

run_times = create_self_db(cur, conn)
average_self_run_times_small = average(run_times)
print(average_self_run_times_small)

run_times = create_user_db(cur,conn)
average_user_run_times_small = average(run_times)
print(average_user_run_times_small)

# Connecting to database, creating cursor, running the test and procuring the average run time for medium db first query 
conn = sqlite3.connect('A3Medium.db')
cur = conn.cursor()

run_times = create_uninf_db(cur, conn)
average_undef_run_times_medium = average(run_times)
print(average_undef_run_times_medium)

run_times = create_self_db(cur, conn)
average_self_run_times_medium = average(run_times)
print(average_self_run_times_medium)

run_times = create_user_db(cur,conn)
average_user_run_times_medium = average(run_times)
print(average_user_run_times_medium)

# Connecting to database, creating cursor, running the test and procuring the average run time for large db first query 
conn = sqlite3.connect('A3Large.db')
cur = conn.cursor()

run_times = create_uninf_db(cur, conn)
average_undef_run_times_large = average(run_times)
print(average_undef_run_times_large)

run_times = create_self_db(cur, conn)
average_self_run_times_large = average(run_times)
print(average_self_run_times_large)

run_times = create_user_db(cur,conn)
average_user_run_times_large = average(run_times)
print(average_user_run_times_large)

# Taking in all the necessary data caculated from above and making a stacked box plot of the run times
uninformed = np.array([average_undef_run_times_small, average_undef_run_times_medium, average_undef_run_times_large])
self_optimized = ([average_self_run_times_small,average_self_run_times_medium,average_self_run_times_large])
user_optimized = ([average_user_run_times_small, average_user_run_times_medium, average_user_run_times_large])

x = ['SmallDB', 'MediumDB', 'LargeDB']
###xpos = np.arange(len(x))
barwidth = 0.4
plt.figure(figsize=(10,7))
plt.bar(x, uninformed, color='royalblue', width=barwidth, label='Uninformed')
plt.bar(x, self_optimized, bottom= uninformed , color='red', width=barwidth, label='Self Optimized')
plt.bar(x, user_optimized, bottom=uninformed+self_optimized, color='yellow', width=barwidth, label='User Optimized')
plt.title("Query 1 runtime in ms")
plt.legend()

plt.show()