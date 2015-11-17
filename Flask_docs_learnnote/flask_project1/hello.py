from flask import Flask, url_for 
app = Flask(__name__)

# route() 装饰器是用于把一个函数绑定到一个 URL 上。
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello Flask!'


#变量规则
#为了给 URL 增加变量的部分，你需要把一些特定的字段标记成 <variable_name>。这些特定的字段将作为参数传入到你的函数中。当然也可以指定一个可选的转换器通过规则 <converter:variable_name>。
@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id


#唯一 URLs / 重定向行为，基于 Apache 和早期的 HTTP 服务器定下先例确保优雅和唯一的 URL。
@app.route('/projects/')
def projects():
	return 'Projects page'
#规范的 URL 指向 projects 尾端有一个斜线。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范URL去。

@app.route('/about')
def about():
	return 'About page'
#结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。

#构建URL   使用url for()针对一个特定的函数构建一个URL。它能接受函数名作为第一参数，以及一些关键字参数，每一个关键字参数对应于URL规则的变量部分。
with app.test_request_context():
	print(url_for('index'))
	print(url_for('show_user_profile',username='Zhao'))
	print(url_for('about'))
	print(url_for('about', next = '/'))
	print(url_for('projects'))
	print(url_for('projects', next = '/'))

if __name__ == '__main__':
	app.run(debug = True)
	#app.debug = True
	#调试模式
