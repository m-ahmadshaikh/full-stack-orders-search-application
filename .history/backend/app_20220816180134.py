from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import psycopg2
  

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:4897@localhost/order-search'

# db = SQLAlchemy(app)

conn = psycopg2.connect(database="order-search",
                        user='postgres', password='4897', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()


@app.route('/')
def index(): 
    sql3 = '''select * from customer_companies;'''
    cursor.execute(sql3)
    lst = []
    for i in cursor.fetchall():
        lst.append()
    return jsonify({'in':'progress'})

if __name__ == '__main__':
    app.run()