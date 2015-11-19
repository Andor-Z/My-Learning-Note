#flaskr.py
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, falsh
from contextlib import closing #添加一个函数来对初始化数据库

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
#secret_key 为了保持客户端的会话安全。明智地选择该键，使得它难以猜测，尽可能复杂。 调试标志启用或禁用交互式调试。决不让调试模式在生产系统中启动，因为它将允许用户在服务器上执行代码！
USERNAME = 'admin'
PASSWORD = 'default'

# creat our little application  :)
app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) #YOURAPPLICATION_SETTINGS

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
	app.run()








