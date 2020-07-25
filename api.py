import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import base64

import json
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kali'
app.config['MYSQL_DB'] = 'flaskapp1'

mysql = MySQL(app)



@app.route('/', methods=['POST', 'GET'])
def home():
    return "TEST"

@app.route('/register', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def register():
    jsonAcc = request.get_json()
    cur  = mysql.connection.cursor()
    insertcmd = "insert users values('{}', '{}','{}','{}','null')".format(jsonAcc['email'], jsonAcc['name'], jsonAcc['lname'], jsonAcc['password'])
    cur.execute(insertcmd)
    mysql.connection.commit()
    cur.close()
    return 'User Saved'

@app.route('/login', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def login():
    jsonAcc = request.get_json()
    cur = mysql.connection.cursor()
    selectcmd = "select * from users where email='{}' and password='{}'".format(jsonAcc['email'],jsonAcc['password'])
    cur.execute(selectcmd)
    data = cur.fetchall()
    if data:
        return 'Welcome '+ jsonAcc['email']
    else:
        return 'User Not found'

app.run(host=('192.168.1.4'))