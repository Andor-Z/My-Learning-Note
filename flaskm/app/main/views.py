from flask import render_template, session, redirect,url_for, flash, request, current_app, abort
from flask.ext.login import login_required, login_user, current_user 
from .. import db 
from ..models import User ,Role, Permission, Post
from ..decorators import admin_required, permission_required
from . import main  #main = Blueprint('main', __name__)
from .forms import NameForm, EditProfileForm, EditProfileAdminForm, PostForm
from datetime import datetime 

@main.route('/', methods = ['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body = form.body.data, author = current_user._get_current_object() ) # User.query.filter_by(username = current_user).first()  
        db.session.add(post)
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    # 渲染的页数从请求的查询字符串（ request.args）中获取，如果没有明确指定，则默认渲染第一页。参数 type=int 保证参数无法转换成整数时，返回默认值。
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page= current_app.config['FLASK_POSTS_PER_PAGE'], error_out = False)
    # 为了显示某页中的记录， 要把 all() 换成 Flask-SQLAlchemy 提供的 paginate() 方法
    # 页数是 paginate() 方法的第一个参数，也是唯一必需的参数。
    # 可选参数 per_page 用来指定每页显示的记录数量； 如果没有指定，则默认显示 20 个记录。
    # 可选参数为 error_out，当其设为 True 时（默认值），如果请求的页数超出了范围，则会返回 404 错误；如果设为 False，页数超出范围时会返回一个空列表。
    posts = pagination.items
    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form = form, posts = posts, pagination = pagination, current_time = datetime.utcnow())

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    # 索引使用get函数
    return render_template('post.html', posts = [post])

@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if current_user.is_following(user):
        flash('You are already following this user.')
        return redirect(url_for('.user', username = username))
    current_user.follow(user)
    flash('You are now following %s.' % username)
    return redirect(url_for('.user', username = username))

@main.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if not current_user.is_following(user):
        flash('You are not following this user.')
        return redirect(url_for('.user', username = username))
    current_user.unfollow(user)
    flash('You are not following %s anymore.' % username)
    return redirect(url_for('.user', username = username))    

@main.route('/followers/<username>')
def followers(username):
    # 显示关注了这个用户的user
    user = User.query.filter_by(username = username).first()
    if user is None:
        flash('Invalid name.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type= int)
    # ?
    pagination = user.followers.paginate(page, per_page = current_app.config['FLASK_POSTS_PER_PAGE'],error_out = False)
    follows = [{'user': item.follower, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user = user, title = 'Followers of', endpoint = '.followers', pagination = pagination, follows = follows)

@main.route('/followed-by/<username>')
def followed_by(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid name.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type= int)
    # ?
    pagination = user.followed.paginate(page, per_page = current_app.config['FLASK_POSTS_PER_PAGE'],error_out = False)
    follows = [{'user': item.followed, 'timestamp': item.timestamp} for item in pagination.items]
    return render_template('followers.html', user = user, title = 'Followerd of', endpoint = '.followers', pagination = pagination, follows = follows)


@main.route('/edit/<int:id>', methods = ['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and not current_user.can(Permission.ADMINISTER):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data 
        db.session.add(post)
        flash('The post has been updated.')
        return redirect(url_for('.post', id = post.id))
    form.body.data = post.body
    return render_template('edit_post.html', form = form)

# @main.route('/', methods = ['GET', 'POST'])
# def index():
#     form = NameForm() # 视图函数创建一个NameForm
#     if form.validate_on_submit():
#         user = User.query.filter_by(username = form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             if current_app.config['FLASKY_ADMIN']:
#                 send_email(current_app.config['FLASKY_ADMIN'], 'New User',
#                            'mail/new_user', user=user)
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         return redirect(url_for('.index'))  # 重新定向
#         # Flask 会为蓝本中的全部端点加上一个命名空间，这样就可以在不同的蓝本中使用相同的端点名定义视图函数， 而不会产生冲突。命名空间就是蓝本的名字（ Blueprint 构造函数的第一个参数），所以视图函数 index() 注册的端点名是 main.index，其 URL 使用 url_for('main.index') 获取。
#     return render_template('index.html', form = form , name = session.get('name'), known = session.get('known', False), current_time = datetime.utcnow())



@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username = username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user = user, posts = posts)

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
    # User.query.get(  )   用主键查询用户
    form = EditProfileAdminForm(user =user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data 
        user.confirmed = form.confirmed.data 
        user.role = Role.query.get(form.role.data )
        user.name = form.name.data
        user.location = form.location.data 
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username = user.username))
    form.email.data = user.email 
    form.username.data = user.username 
    form.confirmed.data = user.confirmed 
    form.role.data = user.role 
    form.name.data = user.name 
    form.location.data = user.location 
    form.about_me.data = user.about_me 
    return render_template('edit_profile.html', form = form, user = user)
