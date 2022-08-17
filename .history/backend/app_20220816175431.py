from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import psycopg2
  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:4897@localhost/order-search'

db = SQLAlchemy(app)



@app.route('/')
def index():
    return jsonify({'in',progress})

if __name__ == '__main__':
    app.run()