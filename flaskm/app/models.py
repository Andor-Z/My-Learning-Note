import hashlib
import bleach
from werkzeug.security import generate_password_hash, check_password_hash 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import db 
from . import login_manager
from datetime import datetime
from markdown import markdown
from flask import current_app, request 
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

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    # follower 关注者 
    # followed 被关注者
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)


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
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default = False)
    avatar_hash = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    followed = db.relationship('Follow', 
                                foreign_keys = [Follow.follower_id], 
                                backref = db.backref('follower', lazy = 'joined'),
                                lazy = 'dynamic',
                                cascade = 'all, delete-orphan')
    followers = db.relationship('Follow', 
                                foreign_keys = [Follow.followed_id], 
                                backref = db.backref('followed', lazy = 'joined'),
                                lazy = 'dynamic',
                                cascade = 'all, delete-orphan')
    # P134
    comments = db.relationship('Comment', backref = 'author', lazy = 'dynamic')


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
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        self.follow(self)



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
        # & 为位运算

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def gravatar(self, size =100, default = 'identicon', rating = 'g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url= url, hash = hash, size = size, default = default, rating = rating)

    def change_email(self, token):
        self.email = new_email
        self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True 
        # ? new_email是什么？这句话能真确应对改邮箱？

    def is_following(self, user):
        return self.followed.filter_by(followed_id = user.id).first() is not None 

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower = self, followed = user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id = user.id).first()
        if f:
            db.session.delete(f)

    def is_followed_by(self, user):
        return self.followers.filter_by(follower_id = user.id).first() is not None

    @staticmethod
    def generate_fake(count = 100):
        '''
        生成虚拟用户和博客文章
        '''
        from sqlalchemy.exc import IntegrityError
        from random import seed 
        import forgery_py

        seed() # 不加参数，默认时间
        for i in range(count):
            u = User(email = forgery_py.internet.email_address(),
                     username = forgery_py.internet.user_name(True),
                     password = forgery_py.lorem_ipsum.word(),
                     confirmed = True,
                     name = forgery_py.name.full_name(),
                     location = forgery_py.address.city(),
                     about_me = forgery_py.lorem_ipsum.sentence(),
                     member_since = forgery_py.date.date(True))
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    @staticmethod
    def add_self_follows():
        for user in User.query.all():
            if not user.is_following(user):
                user.follow(user)
                db.session.add(user)
                db.session.commit()

    @property
    def followed_posts(self):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id).filter(Follow.follower_id == self.id)
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    disabled = db.Column(db.Boolean)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i', 'strong']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format = 'html'),tags = allowed_tags, strip = True))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'post', lazy = 'dynamic')

    @staticmethod
    def generate_fake(count = 100):
        from random import seed, randint 
        import forgery_py

        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            # offset() 查询过滤器会跳过参数中指定的记录数量。 通过设定一个随机的偏移值，再调用 first()方法，就能每次都获得一个不同的随机用户。
            p = Post(body = forgery_py.lorem_ipsum.sentences(randint(1, 3)),
                     timestamp = forgery_py.date.date(True),
                     author = u)
            db.session.add(p)
            db.session.commit()

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        # ?不太明白后两个参数的作用？
        # 首先，markdown() 函数初步把 Markdown 文本转换成 HTML。
        # 然后，把得到的结果和允许使用的 HTML 标签列表传给 clean() 函数。 
        # clean() 函数删除所有不在白名单中的标签。
        # linkify() 这个函数由 Bleach 提供，把纯文本中的 URL 转换成适当的 <a> 链接。
        # 最后一步是很有必要的，因为 Markdown规范没有为自动生成链接提供官方支持。 
        # PageDown 以扩展的形式实现了这个功能，因此在服务器上要调用 linkify() 函数。
        allowed_tags = ['a', 'abbr', 'acronym', 'b','blockquote','code', 'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format = 'html'), tags = allowed_tags, strip = True))

class Permission:
    FOLLOW = 0x01 # 关注其他用户
    COMMENT = 0x02 # 在其他人的文章中发布评论
    WRITE_ARTICLES = 0x04 # 写文章
    MODERATE_COMMENTS = 0x08 # 管理他人发表的评论
    ADMINISTER = 0x80 # 管理员权限

db.event.listen(Post.body, 'set', Post.on_changed_body)
#设置事件监听
# event.listen(表单或表单字段, 触发事件, 回调函数, 是否改变插入值 retval=True)
# on_changed_body 函数注册在 body 字段上，是 SQLAlchemy“ set”事件的监听程序，这意味着只要这个类实例的 body 字段设了新值，函数就会自动被调用。 on_changed_body 函数把 body 字段中的文本渲染成 HTML 格式，结果保存在 body_html 中，自动且高效地完成Markdown 文本到 HTML 的转换。

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False 

    def is_administrator(self):
        return False 

login_manager.anonymous_user = AnonymousUser 
# AnonymousUser这个对象继承自 Flask-Login 中的 AnonymousUserMixin 类，并将其设为用户未登录时current_user 的值。这样程序不用先检查用户是否登录，就能自由调用 current_user.can() 和current_user.is_administrator()。

@login_manager.user_loader    #?
def load_user(user_id):
    # Flask-Login 要求程序实现一个回调函数，使用指定的标识符加载用户。
    return User.query.get(int(user_id))
    # 加载用户的回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象；否则应该返回 None。


    