from werkzeug.security import generate_password_hash, check_password_hash 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import db 
from . import login_manager
from datetime import datetime
from flask import current_app
from flask.ext.login import UserMixin, AnonymousUserMixin


class Role(db.Model):
    __tablename__ ='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    default = db.Column(db.Boolean, default = False, index = True)
    # 设置用户的默认角色，只有一个角色的default字段设置为True
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy = 'dynamic')
    # ? backref :在关系的另一模型中添加反向引用
    # ? lazy :指定如何加载相关记录。可选值有 select（首次访问时按需加载）、 immediate（源对象加载后就加载）、 joined（加载记录，但使用联结）、 subquery（立即加载，但使用子查询），noload（永不加载）和 dynamic（不加载记录，但提供加载记录的查询）

    @staticmethod
    def insert_roles():
        roles = {
        'User': (Permission.FOLLOW |
                 Permission.COMMENT|
                 Permission.WRITE_ARTICLES, True
            ),
        'Moderator': (Permission.FOLLOW|
                      Permission.COMMENT|
                      Permission.WRITE_ARTICLES|
                      Permission.MODERATE_COMMENTS, False),
        'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name = r).first()
            if role is None:
                '''
                若Role表中不包含roles中的角色，则自动为其创建
                '''
                role = Role(name = r)

            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name 
    # 在python解释器里直接输入类Role的实例a后，调用a.__repr__()方法

class Permission:
    FOLLOW = 0x01 # 关注其他用户
    COMMENT = 0x02 # 在其他人的文章中发布评论
    WRITE_ARTICLES = 0x04 # 写文章
    MODERATE_COMMENTS = 0x08 # 管理他人发表的评论
    ADMINISTER = 0x80 # 管理员权限



    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default = datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default = datetime.utcnow)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default = False)

    def __init__(self, **kwargs):
        '''
        定义默认的用户角色
        '''
        super(User, self).__init__(**kwargs) 
        if self.role is None:
            if self.email == current_app.config['FLASKM_ADMIN']:
                self.role = Role.query.filter_by(permissions = 0xff).first()
            if self.role is None:  # 这句可以直接使用 else: ?
                self.role = Role.query.filter_by(default = True).first()

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

    def ping(self):
        '''
        实现最后访问时间的函数，需要在每次收到用户请求的时候都要调用此函数，由于auth蓝本中的before_app_request 处理程序会在每次请求前运行
        '''
        self.last_seen = datetime.utcnow()
        db.session.add(self)

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

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions
        # ?没看懂啊，(self.role.permissions & permissions)在self.role.permissions不为False的前提下，都返回的是permissions，这样肯定相等了啊

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False 

    def is_adminstrator(self):
        return False 

login_manager.anonymous_user = AnonymousUser 
# AnonymousUser这个对象继承自 Flask-Login 中的 AnonymousUserMixin 类，并将其设为用户未登录时current_user 的值。这样程序不用先检查用户是否登录，就能自由调用 current_user.can() 和current_user.is_administrator()。

@login_manager.user_loader    #?
def load_user(user_id):
    # Flask-Login 要求程序实现一个回调函数，使用指定的标识符加载用户。
    return User.query.get(int(user_id))
    # 加载用户的回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象；否则应该返回 None。


    