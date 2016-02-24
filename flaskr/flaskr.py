
#flaskr.py
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.bootstrap import Bootstrap
from contextlib import closing  
#添加一个函数来对初始化数据库

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
#secret_key 为了保持客户端的会话安全。明智地选择该键，使得它难以猜测，尽可能复杂。 调试标志启用或禁用交互式调试。决不让调试模式在生产系统中启动，因为它将允许用户在服务器上执行代码！
USERNAME = 'admin'
PASSWORD = 'default'

# creat our little application  
app = Flask(__name__)
app.config.from_object(__name__)
# from_object() 将会寻找给定的对象(如果它是一个字符串，则会导入它)， 搜寻给定对象里的全部大写的变量。在我们的这种情况中，配置文件就是我们上面写的几行代码。 你也可以将他们分别存储到多个文件。

#app.config.from_envvar('FLASKR_SETTINGS', silent = True) #YOURAPPLICATION_SETTINGS

bootstrap = Bootstrap(app)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()
#init_db()

#每个函数中都会用到数据库连接，因此需要在请求之前初始化连接，并在请求后关闭
#使用 before_request() 装饰的函数会在请求之前调用，且不传递 参数。
@app.before_request
def before_request():
	g.db = connect_db()

#装饰器下 的函数在响应对象构建后被调用。它们不允许修改请求，并且它们的返回值被忽略。如果 请求过程中出错，那么这个错误会传递给每个函数；否则传递 None 。
@app.teardown_request
def teardown_request(exception):                       #? 
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()
	g.db.close()


#视图函数
#显示条目
@app.route('/')
def show_entries():
	cur = g.db.execute('select title, text from entries order by id desc')
	entries = [dict(title = row[0], text = row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries = entries)

#添加一个新条目
@app.route('/add', methods = ['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
	g.db.commit()
	flash('New entry was succeddfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None 
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True                                    #? session
			flash('You were logged in')                                   #? flash
			return redirect(url_for('show_entries'))       #redirect 重新定向
	return render_template('login.html', error = error)                    #? 为何要有error 这个参数



@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))




if __name__ == '__main__':
	app.run()








