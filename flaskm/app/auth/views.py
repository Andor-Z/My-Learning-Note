from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required
from . import auth 
from .. import db
from ..models import User 
from .forms import LoginForm, RegistrationForm


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
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form = form)
