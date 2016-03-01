from config import config
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail 
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager



bootstrap = Bootstrap()
mail = Mail() 
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
# LoginManager 对象的 session_protection 属性可以设为 None、 'basic' 或 'strong'，以提供不同的安全等级防止用户会话遭篡改。
# 设为 'strong' 时， Flask-Login 会记录客户端 IP地址和浏览器的用户代理信息， 如果发现异动就登出用户。

login_manager.login_view = 'auth.login'
#?
# login_view 属性设置登录页面的端点。


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #? 不理解为何这些扩展函数会有init_app()方法
    # config[config_name].init_app(app)是自定义的静态方法，目前为空
    # 下面几个是Flask扩展带有的init_app方法
    # xxx.init_app(app) 和 xxx = XXX(app)的效果是一样的吗
    #  一般来说，XXX(app)会调用init_app方法，但不一定是都是这样
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 附加路由和自定义的错误界面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 
    # 注册蓝本

    from .auth import auth as auth_blueprint 
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')
    # url_prefix 是可选参数，如果使用了这个参数，注册后蓝本中定义的所有路由都会加上指定的前缀，如本例中，完整的 URL 就变成了 http://localhost:5000/auth/login。

    return app