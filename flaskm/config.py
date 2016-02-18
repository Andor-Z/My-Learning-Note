import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_guess_string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次request自动提交db.session.commit()
    FLASKM_MAIL_SUBJECT_PREFIX　= '[Flaskm]' # 邮件前缀
    FLASKM_MAIL_SENDER = 'Flaskm admin <zyfsta@163.com>'
    FLASKM_ADMIN = os.environ.get('FLASKM_ADMIN')

    @staticmethod
    def init_app(app):
        '''
        参数为程序实例。在这个方法中，可以执行对当前环境的配置初始化。
        '''
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465 
    MAIL_USE_TLS = True  # 启用传输层安全（ Transport Layer Security， TLS）协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
