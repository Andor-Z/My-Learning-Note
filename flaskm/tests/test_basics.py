import unittest  
from flask import current_app 
from app import create_app, db 

class BasicsTestCase(unittest.TestCase):
    '''
这个测试使用 Python 标准库中的 unittest 包编写。测试函数以 test_ 开头；这使得 unittest 能够自动识别要运行的测试方法。setUp() 和 tearDown() 方法分别在每个单独的测试函数运行前后运行，并且测试函数都作为测试执行。
    '''
    def setUp(self):
        # 创建一个测试环境，类似于运行中的程序
        self.app = create_app('testing')
        # 使用测试配置创建程序
        self.app_context = self.app.app_context()
        # 在程序实例上调用 app.app_context() 可获得一个程序上下文。激活上下文
        self.app_context.push()
        #? 这一步的作用是确保能在测试中使用 current_app
        db.create_all()

    def tearDown(self):
        '''
        数据库和程序上下文在 tearDown() 方法中删除。
        '''
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        # 确保程序实例存在
        self.assertFalse(current_app is None)

    def test_app_exists_2(self):
        # 确保程序实例存在
        self.assertTrue(current_app)

    def test_app_testing(self):
        # 确保程序在测试配置中运行。
        self.assertTrue(current_app.config['TESTING'])