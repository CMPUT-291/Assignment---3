import sqlite3
import random
import csv 

# parses the customers csv file and populates respective database's customer table
def customers_dataset(cur, size):
    with open('olist_customers_dataset.csv', 'r') as fh:
        customers_reader = csv.reader(fh)
        customers_data_complete = list(customers_reader)

    customers_data = []

    for rows in range (1, len(customers_data_complete)):
        temp_list = []
        temp_list.append(customers_data_complete[rows][0])
        temp_list.append(customers_data_complete[rows][2])
        customers_data.append(tuple(temp_list))

    # Creating the table
    cur.execute(""" CREATE TABLE Customers (
                customer_id TEXT, 
                customer_postal_code INTEGER, 
                PRIMARY KEY(customer_id)
    )""")

    # Inserting specified amount of data into the table
    customers_sample_size = size
    for row in random.sample(customers_data, customers_sample_size):
        cur.execute('INSERT INTO Customers VALUES (?,?)', row)
        
    print('worked - 1')

# parses the sellers csv file and populates respective database's sellers table
def sellers_dataset(cur, size):
    with open('olist_sellers_dataset.csv', 'r') as fh:
        sellers_reader = csv.reader(fh)
        sellers_data_complete = list(sellers_reader)

    sellers_data = []

    for rows in range (1, len(sellers_data_complete)):
        temp_list = []
        temp_list.append(sellers_data_complete[rows][0])
        temp_list.append(sellers_data_complete[rows][2])
        sellers_data.append(tuple(temp_list))

    # Creating the table
    cur.execute(""" CREATE TABLE Sellers (
                seller_id TEXT, 
                seller_postal_code INTEGER, 
                PRIMARY KEY(seller_id)
    )""")

    # Inserting specified amount of data into the table
    sellers_sample_size = size
    for row in random.sample(sellers_data, sellers_sample_size):
        cur.execute('INSERT INTO Sellers VALUES (?,?)', row)

    print('worked - 2')
    
# parses the orders csv file and populates respective database's orders table
def orders_dataset(cur, size):
    with open('olist_orders_dataset.csv', 'r') as fh:
        orders_reader = csv.reader(fh)
        orders_data_complete = list(orders_reader)

    orders_data = []

    for rows in range (1, len(orders_data_complete)):
        temp_list = []
        temp_list.append(orders_data_complete[rows][0])
        temp_list.append(orders_data_complete[rows][1])
        orders_data.append(tuple(temp_list))

    # Creating the table
    cur.execute(""" CREATE TABLE Orders (
                order_id TEXT, 
                customer_id TEXT, 
                PRIMARY KEY(order_id),
                FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
    )""")

    # Inserting specified amount of data into the table
    orders_sample_size = size
    for row in random.sample(orders_data, orders_sample_size):
        cur.execute('INSERT INTO Orders VALUES (?,?)', row)

    print("worked - 3")

# parses the order_items csv file and populates respective database's order_items table
def order_items_dataset(cur, size):
    with open('olist_order_items_dataset.csv', 'r') as fh:
        orders_items_reader = csv.reader(fh)
        orders_items_data_complete = list(orders_items_reader)

    orders_items_data = []

    for rows in range (1, len(orders_items_data_complete)):
        temp_list = []
        temp_list.append(orders_items_data_complete[rows][0])
        temp_list.append(orders_items_data_complete[rows][1])
        temp_list.append(orders_items_data_complete[rows][2])
        temp_list.append(orders_items_data_complete[rows][3])
        orders_items_data.append(tuple(temp_list))

    # Creating the table
    cur.execute(""" CREATE TABLE Order_items (
                order_id TEXT, 
                order_item_id INTEGER,
                product_id TEXT, 
                seller_id TEXT,
                PRIMARY KEY(order_id, order_item_id, product_id, seller_id),
                FOREIGN KEY(seller_id) REFERENCES Sellers(seller_id),
                FOREIGN KEY(order_id) REFERENCES Orders(order_id)
    )""")

    # Inserting specified amount of data into the table
    orders_sample_size = size
    for row in random.sample(orders_items_data, orders_sample_size):
        cur.execute('INSERT INTO Order_items VALUES (?,?,?,?)', row)

    print("worked - 4")
    
# creates the A3Small database and populates it with the mentioned tables
def A3Small_creation():
    # Connecting to database and creating cursor
    conn = sqlite3.connect('A3Small.db')
    cur = conn.cursor()

    # Calling the functions in order to fill in the respective database with values
    customers_dataset(cur, 10000)
    sellers_dataset(cur, 500)
    orders_dataset(cur, 10000)
    order_items_dataset(cur, 2000)

    # Commits the Command
    conn.commit()

    # Closes the connection 
    conn.close()

# creates the A3Medium database and populates it with the mentioned tables
def A3Medium_creation():
    # Connecting to database and creating cursor
    conn = sqlite3.connect('A3Medium.db')
    cur = conn.cursor()

    # Calling the functions in order to fill in the respective database with values
    customers_dataset(cur, 20000)
    sellers_dataset(cur, 750)
    orders_dataset(cur, 20000)
    order_items_dataset(cur, 4000)

    # Commits the Command
    conn.commit()

    # Closes the connection 
    conn.close()

# creates the A3Large database and populates it with the mentioned tables
def A3Large_creation():
    # Connecting to database and creating cursor
    conn = sqlite3.connect('A3Large.db')
    cur = conn.cursor()

    # Calling the functions in order to fill in the respective database with values
    customers_dataset(cur, 33000)
    sellers_dataset(cur, 1000)
    orders_dataset(cur, 33000)
    order_items_dataset(cur, 10000)

    # Commits the Command
    conn.commit()

    # Closes the connection 
    conn.close()

# created for test purposes
# def drop_values_small():
#     # Connecting to database and creating cursor
#     conn = sqlite3.connect('A3Small.db')
#     cur = conn.cursor()

#     cur.execute("DROP TABLE Customers")
#     cur.execute("DROP TABLE Sellers")
#     cur.execute("DROP TABLE Orders")
#     cur.execute("DROP TABLE Order_items")

#     # Commits the Command
#     conn.commit()

#     # Closes the connection 
#     conn.close()

# for test purposes
# drop_values_small()

# runs the function and populates the database
A3Small_creation()

# runs the function and populates the database
A3Medium_creation()

# runs the function and populates the database
A3Large_creation()