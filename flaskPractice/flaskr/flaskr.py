import os 
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

@app.route('/')
def hello_world():
	return "hello_world"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# def init_db():
# 	sql = 'create table entries (id INT,title TEXT,text TEXT)'
# 	conn = sqlite3.connect('flaskr.db')
# 	cursor = conn.cursor()
# 	cursor.execute(sql)
# 	conn.commit()
# 	cursor.close()
# 	conn.close()

if __name__ == "__main__":
	app.run(debug=True)