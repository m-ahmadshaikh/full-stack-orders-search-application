from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import psycopg2
  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost/order-search'

db = SQLAlchemy(app)


conn = psycopg2.connect(database="order-search",
                        user='postgres', password='4897', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()

sql3 = '''select * from customer_companies;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)



conn.commit()
conn.close()

@app.route('/')
def hello():
    return 'Hey'

if __name__ == '__main__':
    app.run()