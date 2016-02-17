import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_guess_string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
    FLASK_MAIL_SUBJECT_PREFIX　= '[Flaskm]'
    