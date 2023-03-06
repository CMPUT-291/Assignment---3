import sqlite3 
import time

# for creating and running test on uninformed and returns list of run times to calc avg from
def create_uninf_db(cur, conn):
    # creates a replica of the tables which doesn't have primary and foreign keys assigned to them
    cur.execute("PRAGMA foreign_keys = OFF;")
    cur.execute("PRAGMA automatic_index = FALSE;")
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
        cur.execute("""SELECT COUNT(*)
                        FROM (SELECT DISTINCT s.seller_postal_code
                            FROM (SELECT i.seller_id
                                    FROM (SELECT order_id
                                        FROM Orders_new
                                        WHERE customer_id = (SELECT cust
                                                            FROM (SELECT c.customer_id as cust
                                                                    FROM Orders_new o,
                                                                        Customers_new c
                                                                    WHERE o.customer_id = c.customer_id
                                                                    GROUP by c.customer_id
                                                                    HAVING COUNT(order_id) > 1)
                                                            ORDER BY random()
                                                            LIMIT 1)) nest_2,
                                        Order_items_new i
                                    WHERE nest_2.order_id = i.order_id) nest_3,
                                Sellers_new s
                            WHERE nest_3.seller_id = s.seller_id);""")
        end = time.time()
        exec_times.append((end - start) * 1000)
    return exec_times

# for creating and running test on self-optimized and returns list of run times to calc avg from
def create_self_db(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("PRAGMA automatic_index = TRUE;")
    conn.commit()

    exec_times = []
    for i in range(50):
        start = time.time()
        cur.execute("""SELECT COUNT(*)
                        FROM (SELECT DISTINCT s.seller_postal_code
                            FROM (SELECT i.seller_id
                                    FROM (SELECT order_id
                                        FROM Orders
                                        WHERE customer_id = (SELECT cust
                                                            FROM (SELECT c.customer_id as cust
                                                                    FROM Orders o,
                                                                        Customers c
                                                                    WHERE o.customer_id = c.customer_id
                                                                    GROUP by c.customer_id
                                                                    HAVING COUNT(order_id) > 1)
                                                            ORDER BY random()
                                                            LIMIT 1)) nest_2,
                                        Order_items i
                                    WHERE nest_2.order_id = i.order_id) nest_3,
                                Sellers s
                            WHERE nest_3.seller_id = s.seller_id);""")
        end = time.time()
        exec_times.append((end - start) * 1000)
    return exec_times

# for creating and running test on user-optimized and returns list of run times to calc avg from
def create_user_db(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("PRAGMA automatic_index = FALSE")
    cur.executescript(""" DROP INDEX IF EXISTS idx_order_id;
                            DROP INDEX IF EXISTS idx_customer_id;
                            DROP INDEX IF EXISTS idx_seller_id;
                            DROP INDEX IF EXISTS idx_order_id_items;
    """)
    cur.executescript("""CREATE INDEX idx_order_id ON Orders(order_id);
                            CREATE INDEX idx_customer_id ON Customers(customer_id);
                            CREATE INDEX idx_seller_id ON Sellers(seller_id);
                            CREATE INDEX idx_order_id_items ON Order_items(order_id);""")
    conn.commit()

    exec_times = []
    for i in range(50):
        start = time.time()
        cur.execute("""SELECT COUNT(*)
                        FROM (SELECT DISTINCT s.seller_postal_code
                            FROM (SELECT i.seller_id
                                    FROM (SELECT order_id
                                        FROM Orders
                                        WHERE customer_id = (SELECT cust
                                                            FROM (SELECT c.customer_id as cust
                                                                    FROM Orders o,
                                                                        Customers c
                                                                    WHERE o.customer_id = c.customer_id
                                                                    GROUP by c.customer_id
                                                                    HAVING COUNT(order_id) > 1)
                                                            ORDER BY random()
                                                            LIMIT 1)) nest_2,
                                        Order_items i
                                    WHERE nest_2.order_id = i.order_id) nest_3,
                                Sellers s
                            WHERE nest_3.seller_id = s.seller_id);""")
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