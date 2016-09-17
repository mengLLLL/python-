from flask_script import Manager
from app import app
import sqlite3
from models import User
manager = Manager(app)

#python3 manmage.py hello 来执行
@manager.command
def hello():
	print('hello manager')



#python manage.py hello_world
@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_world(msg_val):
	print ('hello'+msg_val)

@manager.command
def init_db():
	sql = 'create table user (id INT,name TEXT)'
	conn = sqlite3.connect('meng.db')
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()

@manager.command
def save():
	user = User(2,'liang')
	user.save()
@manager.command
def query_all():
	users = User.query()
	for user in users:
		print(user)


if __name__ == '__main__':
	manager.run()