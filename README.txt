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
The indices that were created for the user optimized scenario for this query is an index on the customer_postal_code,customer_id columns of the Customers table. Both were used in the where clause that essentially filtered down the data so they would be searched within when there was a large amount of data. An index on the order_id column of Order_items and an index on the customer_id column of Orders as these were used in a where clause so these will be searched within.


Query - 2:
The indices that were created for the user optimized scenario for this query is an index on the customer_postal_code,customer_id columns of the Customers table for the same reason as the first query. An index on the order_id column of the Order_items table and an index on customer_id and order_id columns of the Orders table as they were used in a where clause so these will be searched within.


Query - 3:
Same as Query 2.

Query - 4:
The indices that were created for the user optimized scenario for this query is an index on the customer_id and order_id columns of the Orders table, an index on the customer_id and customer_postal_code columns of the Customers table, an index on the seller_postal_code and seller_id columns of the Sellers table, and lastly an index on the seller_id and order_id columns of the Order_items table. These were chosen as they participated in one or more where clauses and thus would have to be searched within, so by indexing them we will make the search faster, thus allowing our query to be faster.
