from werkzeug.security import generate_password_hash, check_password_hash 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import db 
from . import login_manager
from flask import current_app
from flask.ext.login import UserMixin


class Role(db.Model):
    __tablename__ ='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role', lazy = 'dynamic')
    #? backref :在关系的另一模型中添加反向引用
    #? lazy :指定如何加载相关记录。可选值有 select（首次访问时按需加载）、 immediate（源对象加载后就加载）、 joined（加载记录，但使用联结）、 subquery（立即加载，但使用子查询），noload（永不加载）和 dynamic（不加载记录，但提供加载记录的查询）

    def __repr__(self):
        return '<Role %r>' % self.name 
    # 在python解释器里直接输入类Role的实例a后，调用a.__repr__()方法

    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    comfirmed = db.Column(db.Boolean, default = False)

    def generate_confirmation_token(self, expiration = 3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        # TimedJSONWebSignatureSerializer 类生成具有过期时间的 JSON Web 签名（ JSON Web Signatures， JWS）。这个类的构造函数接收的参数是一个密钥，可使用 SECRET_KEY 设置。expires_in 参数设置令牌的过期时间，单位为秒。
        return s.dumps({'confirm':self.id})
        # dumps() 方法为指定的数据生成一个加密签名，然后再对数据和签名进行序列化，生成令牌字符串

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False 
        self.confirmed = True 
        db.session.add(self)
        return True



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


@login_manager.user_loader    #?
def load_user(user_id):
    # Flask-Login 要求程序实现一个回调函数，使用指定的标识符加载用户。
    return User.query.get(int(user_id))
    # 加载用户的回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象；否则应该返回 None。


    