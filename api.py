import flask
from flask import request, jsonify, request, session, make_response, render_template
from flask_cors import CORS, cross_origin
import jwt
from flask_mysqldb import MySQL
from functools import wraps
import base64
import datetime
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
app.config['SECRET_KEY'] = 'flaskit'

mysql = MySQL(app)

def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'MISSING TOKEN'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Invalid token'}), 403
        return func(*args, **kwargs)
    return wrapped

@app.route('/dashboard')
@check_for_token
def dashboard():
    return 'Only if has jwt'

@app.route('/', methods=['POST', 'GET'])
def index():
    if not session.get('logged_in'):
        return render_template('main.html')
    else:
        return 'Curently logged in'

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
        session['logged_in'] = True
        token = jwt.encode({
            'user': data[0][0],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
        }, app.config['SECRET_KEY'])
        #cur = mysql.connection.cursor()
        #update_token = "update users set token='{}' where email='{}'".format(token.decode('utf-8'), data[0][0])
        #cur.execute(update_token)
        #mysql.connection.commit()
        #cur.close()
        return jsonify(
            msg= 'Success',
            email= data[0][0],
            name= data[0][1],
            lname= data[0][2],
            password= data[0][3],
            token= token.decode('utf-8')
            )
    else:
        return make_response('Unable to verify', 403)


app.run(host=('192.168.1.4'))