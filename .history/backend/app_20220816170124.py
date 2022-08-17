import psycopg2
  
conn = psycopg2.connect(database="EMPLOYEE_DATABASE",
                        user='postgres', password='pass', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
  
sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
employee_name char(20),\
employee_email varchar(30), employee_salary float);'''
  
  
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