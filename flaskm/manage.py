#! /usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role, Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from init_db import create_db


app = create_app(os.getenv('FLASK_CONFIG') or 'default') 
#? 对于这种参数使用 or 的，在实际使用时究竟是如何使用参数的，先第一个，没有再使用第二个？

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
# 为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以附加到Flask-Script的manager对象上
# 此例中MigrateCommand类使用db命令附加
# 创建迁移仓库 - 使用init 子命令
# python manage.py db init
# 这个命令会创建 migrations 文件夹

# 自动创建迁移脚本  - migrate 子命令
# python manage.py db migrate -m"initial migration 初始化迁移"

# 更新数据库 - db upgrade 
# python manage.py db upgrade 
# ?不太明白是将更改后的数据库迁移到migrations中，还是在migrations中写好脚本迁移到环境中

def make_shell_context():
    return dict(app=app , db = db , User = User, Role = Role)

manager.add_command('shell', Shell(make_context = make_shell_context))  #? add_command函数？


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