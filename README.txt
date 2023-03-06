Group Number - 79

Team member's CCID's: 
    - kmukherj (Kaustubh Mukherjee)
    - moeid (Moeid Khan)
    - sdutt1 (Shivansh Dutt)

Resources used: 
    - Modules used: 
        1. random
        2. csv
        3. sqlite3
        4. numpy
        5. matplotlib
        6. time

Collaboration status: 
    - "We declare that we did not collaborate with anyone outside our own
group in this assignment"

USER OPTIMIZED INDEX CHOICE REPORT: 
Query - 1:
    - We are creating an index with order_id from Orders and customer_id, customer_postal_code from Customers
    - The reason for choosing these 3 keys being that these specific columns seemed to 
       be used more in our queries therefore since these columns are queried frequently we decided 
       index them in order to retreive data more quickly from the database than otherwise

Query - 2:
    - We are creating an index with order_id, customer_id from Orders, order_id from Order_items and customer_id, customer_postal_code from Customers
    - The reason for choosing these 5 keys being that these specific columns seemed to 
       be used more in our queries therefore since these columns are queried frequently we decided 
       index them in order to retreive data more quickly from the database than otherwise

Query - 3:
    - We are creating an index with order_id, customer_id from Orders, order_id from Order_items and customer_id, customer_postal_code from Customers
    - The reason for choosing these 5 keys being that these specific columns seemed to 
       be used more in our queries therefore since these columns are queried frequently we decided 
       index them in order to retreive data more quickly from the database than otherwise

Query - 4:
    - We are creating an index with order_id, customer_id from Orders, seller_id from Sellers, order_id from Order_items, seller_postal_code from Sellers and customer_id from Customers
    - The reason for choosing these 6 keys being that these specific columns seemed to 
       be used more in our queries therefore since these columns are queried frequently we decided 
       index them in order to retreive data more quickly from the database than otherwise