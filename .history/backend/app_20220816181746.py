from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from itertools import zip_longest
import json
  

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:4897@localhost/order-search'

# db = SQLAlchemy(app)

conn = psycopg2.connect(database="order-search",
                        user='postgres', password='4897', 
                        host='127.0.0.1', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip_longest([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]

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
def orders(): 
    sql3 = '''select * from customers;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

@app.route('/customer_companies')
def orders(): 
    sql3 = '''select * from customers;'''
    cursor.execute(sql3)
    results = dictfetchall(cursor)
    json_results = json.dumps(results, indent=4, sort_keys=True, default=str)
    return json_results

if __name__ == '__main__':
    app.run()

    conn.commit()
    conn.close()