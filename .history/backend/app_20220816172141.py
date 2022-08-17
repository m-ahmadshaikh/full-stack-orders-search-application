import psycopg2
  
conn = psycopg2.connect(database="order-search",
                        user='postgres', password='4897', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
  
orders_sql = '''CREATE TABLE IF NOT EXISTS ORDERS(id int NOT NULL,\
created_at TIMESTAMP,\
order_name varchar(30), customer_id varchar(30));

CREATE TABLE IF NOT EXISTS ORDER_ITEMS(id int NOT NULL,\
order_id int,\
price_per_unit varchar(30), quantity int, product varchar(30));


CREATE TABLE IF NOT EXISTS DELIVERIES(id int NOT NULL,\
order_item_id int,\
delivered_quantity int);

CREATE TABLE IF NOT EXISTS CUSTOMERS(user_id int NOT NULL,\
login varchar(30),\
password varchar(30), name varchar(30), company_id int);

CREATE TABLE IF NOT EXISTS CUSTOMERS_COMPANIES(company_id int NOT NULL,\
company_name varchar(30));

'''
  
  
cursor.execute(orders_sql)



  
sql2 = '''
COPY orders(id,created_at,\
order_name,customer_id)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/orders.csv'
DELIMITER ','
CSV HEADER;

COPY orders_item(id,created_at,\
order_name,customer_id)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/orders.csv'
DELIMITER ','
CSV HEADER;

COPY orders(id,created_at,\
order_name,customer_id)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/orders.csv'
DELIMITER ','
CSV HEADER;




'''
  
cursor.execute(sql2)
  
sql3 = '''select * from orders;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()