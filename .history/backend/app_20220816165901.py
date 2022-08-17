from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:48@localhost/order-search'

db = SQLAlchemy(app)

class Event(db.Model):

@app.route('/')
def hello():
    return 'Hey'

if __name__ == '__main__':
    app.run()