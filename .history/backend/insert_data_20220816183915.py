import psycopg2
from itertools import zip_longest
import json
conn = psycopg2.connect(database="db56ir97s1v38l",
                        user='vhovanfzobpdbh', password='08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6', 
                        host='ec2-3-224-184-9.compute-1.amazonaws.com', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
  
orders_sql = '''CREATE TABLE IF NOT EXISTS ORDERS(id int NOT NULL,\
created_at TIMESTAMP,\
order_name varchar(30), customer_id varchar(30));

CREATE TABLE IF NOT EXISTS order_items(id int NOT NULL,\
order_id int,\
price_per_unit varchar(30), quantity int, product varchar(30));


CREATE TABLE IF NOT EXISTS DELIVERIES(id int NOT NULL,\
order_item_id int,\
delivered_quantity int);

CREATE TABLE IF NOT EXISTS CUSTOMERS(user_id varchar(30) NOT NULL,\
login varchar(30),\
password varchar(30), name varchar(30), company_id int,credit_cards varchar(50));

CREATE TABLE IF NOT EXISTS CUSTOMER_COMPANIES(company_id int NOT NULL,\
company_name varchar(30));

'''
  
  
cursor.execute(orders_sql)



  
sql2 = '''
COPY orders(id,created_at,\
order_name,customer_id)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/orders.csv'
DELIMITER ','
CSV HEADER;

COPY order_items(id,order_id,\
price_per_unit,quantity, product)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/order_items.csv'
DELIMITER ','
CSV HEADER;

COPY deliveries(id,order_item_id,\
delivered_quantity)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/deliveries.csv'
DELIMITER ','
CSV HEADER;

COPY customers(user_id,login,\
password,name,company_id,credit_cards)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/customers.csv'
DELIMITER ','
CSV HEADER;

COPY customer_companies(company_id,company_name)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/customer_companies.csv'
DELIMITER ','
CSV HEADER;





'''
  
# cursor.execute(sql2)
def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip_longest([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]
  
sql3 = '''select * from customer_companies;'''
cursor.execute(sql3)
results = dictfetchall(cursor)
json_results = json.dumps(results)
# for i in cursor.fetchall():
#     print(i)
print(json_results)
conn.commit()
conn.close()