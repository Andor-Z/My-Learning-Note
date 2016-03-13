#! /usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default') 

#? 对于这种参数使用 or 的，在实际使用时究竟是如何使用参数的，先第一个，没有再使用第二个？
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app , db = db , User = User, Role = Role)

manager.add_command('shell', Shell(make_context = make_shell_context))  #? add_command函数？
manager.add_command('db', MigrateCommand)

# manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名，函数的文档字符串会显示在帮助消息中。 
# python manage.py test   运行此函数
@manager.command
def test():
    '''
    启动单元测试的命令
    Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity = 2).run(tests)


if __name__ == '__main__':
    manager.run()