from config import config
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail 
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy



bootstrap = Bootstrap()
mail = Mail() 
moment = Moment()
db = SQLAlchemy()

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

    # 附加路由和自定义的错误界面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 
    # 注册蓝本

    return app