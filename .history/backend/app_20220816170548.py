import psycopg2
  
conn = psycopg2.connect(database="order-search",
                        user='postgres', password='4897', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
  
sql = '''CREATE TABLE ORDERS(id int NOT NULL,\
order_name char(20),\
customer_id varchar(30), employee_salary float);'''
  
  
cursor.execute(sql)
  
sql2 = '''COPY details(employee_id,employee_name,\
employee_email,employee_salary)
FROM '/private/tmp/details.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)
  
sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()