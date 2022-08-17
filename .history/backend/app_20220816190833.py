from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from itertools import zip_longest
import json
  

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:4897@localhost/order-search'

# db = SQLAlchemy(app)

conn = psycopg2.connect(database="db56ir97s1v38l",
                        user='vhovanfzobpdbh', password='08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6', 
                        host='ec2-3-224-184-9.compute-1.amazonaws.com', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip_longest([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]

@app.route('/')
def orders(): 
    
    return json_results

@app.route('/orders')
def orders(): 
    sql3 = '''select * from orders;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

@app.route('/order_items')
def order_items(): 
    sql3 = '''select * from order_items;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

@app.route('/deliveries')
def deliveries(): 
    sql3 = '''select * from deliveries;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

@app.route('/customers')
def customers(): 
    sql3 = '''select * from customers;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

@app.route('/customer_companies')
def customer_companies(): 
    sql3 = '''select * from customers;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

if __name__ == '__main__':
    app.run()

    conn.commit()
    conn.close()