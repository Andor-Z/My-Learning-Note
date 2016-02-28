# 使用Werkzeug实现密码散列
使用Werkzeug.security 模块中的`generate_password_hash`(注册用户),`check_password_hash`(验证用户) 两个函数能够很方便地实现密码散列值的计算。  
  
- `generate_password_hash(password, method=pbkdf2:sha1, salt_length=8)`：这个函数将
原始密码作为输入，以字符串形式输出密码的散列值， 输出的值可保存在用户数据库中。
method 和 salt_length 的默认值就能满足大多数需求。

- `check_password_hash(hash, password)`：这个函数的参数是从数据库中取回的密码散列
值和用户输入的密码。返回值为 True 表明密码正确。


《Flask Web Development》中的例子：

```python
from werkzeug.security import generate_password_hash, check_password_hash 
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ ='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role', lazy = 'dynamic')
    #? backref :在关系的另一模型中添加反向引用
   

    def __repr__(self):
        return '<Role %r>' % self.name 
    # 在python解释器里直接输入类Role的实例a后，调用a.__repr__()方法


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute/ password 不是一个可读属性。')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' %self.username
```  

# @property 用法理解

@property装饰器用于将一个方法变成属性。
 1.上例中，先加上@property将`password`方法变成属性
 

2.此时，@property本身又创建了另一个装饰器@password.setter，负责把一个setter方法变成属性赋值。可以通过`User.password = `进行赋值，同时，调用`@password.setter   
    def password(self, password):`函数，对`self.password_hash`赋值。


3.当调用`User.password`时，返回`password is not a readable attribute/ password 不是一个可读属性。`
