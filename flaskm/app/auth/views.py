from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required, current_user
from . import auth 
from .. import db
from ..models import User 
from ..email import send_email
from .forms import LoginForm, RegistrationForm,ChangePasswordForm


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            #  login_user() 函数在用户会话中把用户标记为已登录。
            #  login_user() 函数的参数是要登录的用户，以及可选的“记住我”布尔值，“记住我”也在表单中填写。如果值为 False，那么关闭浏览器后用户会话就过期了，所以下次用户访问时要重新登录。 如果值为 True，那么会在用户浏览器中写入一个长期有效的 cookie，使用这个 cookie 可以复现用户会话。
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名或密码')
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # logout_user() 函数，删除并重设用户会话。
    flash('You have been logged out.您已经登出')
    return redirect(url_for('main.index'))
'''
from flask.ext.login import login_required
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


为了保护路由只让认证用户访问， Flask-Login 提供了一个 login_required 修饰器。
如果未认证的用户访问这个路由， Flask-Login 会拦截请求，把用户发往登录页面。
'''


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user = user , token = token)
        flash('A confirmation email has been sent to you by email.')
        flash(url_for('auth.confirm', token = token, _external=True))
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form = form)


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    # send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user = current_user , token = token)  # NameError: name 'user' is not defined
    flash('A new confirmation email has been sent to you by email.')
    flash(url_for('auth.confirm', token = token, _external=True))
    # <a href ="{{ url_for('auth.confirm', token = token, _external=True) }}">验证链接</a>
    return redirect(url_for('main.index'))

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        #? 为何使用if 而不是 elif
        #? 似乎user.confirm()只是add添加到回话，并未提交到数据库
        flash('You have confirmed your account.')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    # 为何使用 before_request 钩子名作为函数名
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.' and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))
        # request.endpoint 获取请求的端点

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/change-password', methods = ['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data 
            db.session.add(current_user)
            flash('Your password has been updated')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password 无效的密码')
    return render_template('auth/change_password.html', form = form)


@auth.before_app_request 
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))