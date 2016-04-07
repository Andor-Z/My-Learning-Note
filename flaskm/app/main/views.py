from flask import render_template, session, redirect,url_for, flash
from flask.ext.login import login_required, login_user, current_user 
from .. import db 
from ..models import User 
from ..decorators import admin_required, permission_required
from . import main  #main = Blueprint('main', __name__)
from .forms import NameForm, EditProfileForm




from datetime import datetime 

@main.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm() # 视图函数创建一个NameForm
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))  # 重新定向
        # Flask 会为蓝本中的全部端点加上一个命名空间，这样就可以在不同的蓝本中使用相同的端点名定义视图函数， 而不会产生冲突。命名空间就是蓝本的名字（ Blueprint 构造函数的第一个参数），所以视图函数 index() 注册的端点名是 main.index，其 URL 使用 url_for('main.index') 获取。
    return render_template('index.html', form = form , name = session.get('name'), known = session.get('known', False), current_time = datetime.utcnow())

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)
        return render_template('user.html', user = user)

@main.route('/edit-profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data 
        current_user.about_me = form.about_me.data 
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('main.user',username = current_user.username))
    form.name.data = current_user.name 
    form.location.data = current_user.location 
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form = form)


@main.route('/edit-profile/<int:id>', methods = ['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    
