from flask import Flask
app = Flask(__name__)


# 处理 URL 和函数之间关系的程序称为路由。
# 在 Flask 程序中定义路由的最简便方式，是使用程序实例提供的 app.route 修饰器，把修饰的函数注册为路由。
@app.route('/')
def index():
    return('<h1>Hello zhao</h1> '
        )
# 修饰器 惯常用法是使用修饰器把函数注册为事件的处理程序
# 本句是把 index()函数注册为程序根地址的处理程序
# index()称为视图函数 (view function)


# 尖括号中的是动态部分
#路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由 /user/<int:id>只会匹配动态片段 id 为整数的 URL。 Flask 支持在路由中使用 int、 float 和 path 类型。path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。
@app.route('/user/<name>')
def user(name):
    return('<h1>Hello, %s!</h>' % name)




from flask import request 
@app.route('/agentf')
def agentf():
    user_agent = request.headers.get('User-Agent')
    return('<p> Your browser is %s.</p>' %user_agent)


from flask import make_response

@app.route('/responsef')
def responsef():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return(response)


# 重新定向
from flask import redirect 
@app.route('/redirectf')
def redirectf():
    return redirect('http://www.baidu.com')

 
# Flask-Script 支持命令行选项   
from flask.ext.script import Manager 
manager = Manager(app)

# 启动服务器 
# debug = True 启动调试模式。调试模式中有 激活调试器和重载程序
if __name__ == '__main__':
    manager.run()



