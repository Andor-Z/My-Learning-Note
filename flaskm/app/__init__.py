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
    app = (__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # ?不理解为何这些扩展函数会有init_app()方法
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 附加路由和自定义的错误界面

    return app