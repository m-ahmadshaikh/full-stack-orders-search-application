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


'''
  
  
cursor.execute(orders_sql)


order_items_sql = '''CREATE TABLE IF NOT EXISTS ORDER_ITEMS(id int NOT NULL,\
order_id int,\
price_per_unit varchar(30), quantity int, product varchar(30));'''


cursor.execute(order_items_sql)


deliveries_sql = '''CREATE TABLE DELIVERIES(id int NOT NULL,\
order_item_id int,\
delivered_quantity int);'''


cursor.execute(deliveries_sql)

  
sql2 = '''COPY orders(id,created_at,\
order_name,customer_id)
FROM '/Users/ahmad/Desktop/full-stack-projects/Order-Search/backend/orders.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)
  
sql3 = '''select * from orders;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()