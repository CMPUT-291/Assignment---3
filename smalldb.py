import csv 
import random 
import sqlite3

with open('olist_customers_dataset.csv', 'r') as fh:
    customers_reader = csv.reader(fh)
    customers_data = list(customers_reader)

customers_sample_size = 10000
customers_ignored_columns = ["customer_unique_id", "customer_city", "customer_state"]
customers_sample_data = []
for row in random.sample(customers_data, customers_sample_size):
    new_row = {k: v for k, v in row.items() if k not in customers_ignored_columns}
    customers_sample_data.append(new_row)

# create a database and table to store data in
conn = sqlite3.connect('A3Small.db')
cur = conn.cursor()

# delete this statement before submitting
cur.execute('DROP TABLE Customers')

# creating the table
cur.execute('CREATE TABLE Customers (customer_id TEXT, customer_postal_code INTEGER, PRIMARY KEY(customer_id))')

# populating the table
for row in customers_sample_data:
    cur.execute('INSERT INTO Customers (customer_id, customer_postal_code) VALUES (?, ?)', (row['customer_id', 'customer_postal_code']))

conn.commit()
conn.close()