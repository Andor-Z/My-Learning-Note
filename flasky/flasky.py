from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask import request
from flask.ext.script import Manager  
from flask.ext.bootstrap import Bootstrap 
from flask.ext.moment import Moment
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import Required 
from datetime import datetime 

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


app.config['SECRET_KEY'] = 'flasky key'


class NameForm(Form):
    name = StringField('姓名', validators=[Required()])
    submit = SubmitField('提交')

@app.route('/' , methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('姓名已经更改！')
        session['name'] = form.name.data 
        return redirect(url_for('index'))
    return render_template('index.html', form = form,name = session.get('name'), current_time = datetime.utcnow())


@app.route('/user/<name>')
def use(name):
    return render_template('user.html', name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def inter_server_error(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    manager.run()

# python flasky.py runserver --host 0.0.0.0