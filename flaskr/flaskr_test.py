import os
import flaskr
import unittest
import tempfile  # 临时文件夹

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        '''
        setUp() 函数在每个单独的测试函数运行前被调用
        '''
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()    #? mkstemp() 函数返回一个低级别的文件句柄和一个随机文件名 ​​，我们使用后者作为数据库名。
        flaskr.app.config['TESTING'] = True 
        self.app = flaskr.app.test_client()   # 创建了一个新的测试客户端
        flaskr.init_db()    # 初始化新的数据库


    def tearDown(self):
        os.close(self.db_fd)   # 关闭数据库文件
        os.unlink(flaskr.app.config['DATABASE'])   # 删除数据库文件 

    def test_empty_db(self):   # 测试函数以 test 开头；这使得 unittest 能够自动识别要运行的测试方法。
        rv = self.app.get('/')   # 返回的值将会是一个 response_class 对象
        s = 'No entries here so far'
        s_u = s.encode('utf8')
        assert s_u in rv.data 


    def login(self, username, password):
        return self.app.post('/login', data = dict(username = username, password = password), follow_redirects = True)


    def logout(self):
        return self.app.get('/logout', follow_redirects = True)


    def test_login_logout(self):
        
        rv = self.login('admin', 'default')
        s = 'You were logged in'
        s_u = s.encode('utf8')
        assert s_u in rv.data 
        
        rv = self.logout()
        s = 'You were logged out'
        s_u = s.encode('utf8')
        assert s_u in rv.data 
        rv = self.login('adminx', 'default')
        s = 'Invalid username'
        s_u = s.encode('utf8')
        assert s_u in rv.data 
        rv = self.login('admin', 'defaultx')
        s = 'Invalid password'
        s_u = s.encode('utf8')
        assert s_u in rv.data 







if __name__ == '__main__':
    unittest.main()