from flask.ext.wtf import Form 
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import Required, Length, Email 

class LoginForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('Keep me login')
    submit = SubmitField('Log In 登录')