from flask.ext.wtf import Form 
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError 
from ..models import User 


class LoginForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('Keep me login')
    submit = SubmitField('Log In 登录')

class ChangePasswordForm(Form):
    old_password = PasswordField('old password 旧密码', validators = [Required()])
    password = PasswordField('New password 新密码', validators = [Required(), EqualTo('password2', message = 'Passwords must match.两次密码输入不一致')])
    password2 = PasswordField('Confirm new password 确认新密码', validators = [Required()])
    submit = SubmitField('Submit 提交')

class RegistrationForm(Form):
    email = StringField('邮箱', validators = [Required(), Length(1, 64), Email()])
    username = StringField('用户名', validators = [Required(), Length(1, 64), Regexp('^[A-Za-z][A-za-z0-9_.]*$', 0, 'Username must have only letters, numbers, dots or underscores')])
    # 使用 WTForms 提供的 Regexp 验证函数，确保 username 字段只包含字母、数字、下划线和点号。 这个验证函数中正则表达式后面的两个参数分别是正则表达式的旗标和验证失败时显示的错误消息。
    password = PasswordField('密码', validators=[Required(), EqualTo('password2', message = 'Passwords must match.')])
    #  EqualTo。这个验证函数要附属到两个密码字段中的一个上，另一个字段则作为参数传入。
    password2 = PasswordField('密码确认', validators=[Required()])
    submit = SubmitField('Register 注册')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use.')
    # 如果表单类中定义了以validate_ 开头且后面跟着字段名的方法，这个方法就和常规的验证函数一起调用。


    