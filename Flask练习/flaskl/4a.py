from flask import Flask, render_template,session,redirect,url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')



@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed your name!')
        session['name'] = form.name.data
        return(redirect(url_for('index')))
    return(render_template('index.html',form = form, name = session.get('name'), current_time = datetime.utcnow()))

@app.route('/user/<name>')
def user(name):
    return(render_template('user.html',name = name))


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

@app.errorhandler(500)
def internal_server(e):
    return render_template("500.html"), 500




if __name__ == '__main__':
    app.run(debug = True)


