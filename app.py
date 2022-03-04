from flask import Flask, render_template, url_for, request, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
import queries
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
db = SQLAlchemy(app)

class customers(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Age = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.ID

result = {}

def get_by_Name(Name):
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()
    statement = "SELECT * FROM customers WHERE Name = ?"
    cur.execute(statement, [Name])
    cust_details = cur.fetchall()
    return cust_details

@app.route("/")
def index():
    tasks = customers.query.limit(5).all()
    return render_template('index.html', tasks=tasks)

@app.route("/Name", methods = ["GET"])
def get_cust():
    body = request.args.get('Name')
    sent = get_by_Name(body)
    print(sent)
    return render_template('update.html', sent=sent)

if __name__ == "__main__":
    app.run(host='127.0.0.13', port=8080, debug=True)
