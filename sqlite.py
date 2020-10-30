import sqlite3

db = sqlite3.connect(':memory:') # Using an in-memory database
cur = db.cursor()

# Create three tables, Customer: primary key and customers first n last name
# Items: Primary key, item name and price
# Items Bought: Order number, date and price connect to primary keys in the Items and
# Customer tables

cur.execute('''CREATE TABLE IF NOT EXISTS Customer ( id integer PRIMARY KEY, firstname
varchar(255), lastname varchar(255))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Item ( id integer PRIMARY KEY, title
varchar(255), price decimal )''')
cur.execute('''CREATE TABLE IF NOT EXISTS BoughtItem ( ordernumber integer PRIMARY KEY,
customerid integer, itemid integer, price decimal, CONSTRAINT customerid FOREIGN KEY
(customerid) REFERENCES Customer(id), CONSTRAINT itemid FOREIGN KEY (itemid) REFERENCES
Item(id) )''')

cur.execute('''INSERT INTO Customer(firstname, lastname)
               VALUES ('Bob', 'Adams'),
                      ('Amy', 'Smith'),
                      ('Rob', 'Bennet');''')
cur.execute('''INSERT INTO Item(title, price)
               VALUES ('USB', 10.2),
                      ('Mouse', 12.23),
                      ('Monitor', 199.99);''')
cur.execute('''INSERT INTO BoughtItem(customerid, itemid, price)
               VALUES (1, 1, 10.2),
                      (1, 2, 12.23),
                      (1, 3, 199.99),
                      (2, 3, 180.00),
                      (3, 2, 11.23);''') # Discounted price 



#cur.execute('''SELECT customer.firstname, SUM(boughtitem.price) FROM BoughtItem as boughtitem
#             INNER JOIN Customer as customer on (customer.id = boughtitem.customerid)
#             GROUP BY customer.firstname''')
#
#cur.execute('''SELECT item.title, AVG(boughtitem.price) FROM BoughtItem as boughtitem
#             INNER JOIN Item as item on (item.id = boughtitem.itemid)
#             GROUP BY boughtitem.itemid''')
#
#cur.execute('''SELECT itemid, AVG(price) FROM BoughtItem GROUP BY itemid''')
#
#cur.execute('''EXPLAIN QUERY PLAN SELECT customer.firstname, item.title, 
#                item.price, boughtitem.price FROM BoughtItem as boughtitem
#                INNER JOIN Customer as customer on (customer.id = boughtitem.customerid)
#                INNER JOIN Item as item on (item.id = boughtitem.itemid)''')

print(cur.fetchall())

