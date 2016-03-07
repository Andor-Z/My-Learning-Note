from flask import current_app, render_template
from flask.ext.mail import Message 
from . import mail 
from threading import Thread 


def send_async_email(app, msg):
    with app.app_context():
        #? 在不同线程中执行 mail.send() 函数时，程序上下文要使用 app.app_context() 人工创建。
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    # send_email 函数的参数分别为收件人地址、主题、渲染邮件正文的模板和关键字参数列表。
    app = current_app._get_current_object()
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + ' ' + subject, sender = app.config['FLASK_MAIL_SENDER'], recipients=[to])

    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target = send_async_email, args = [app, msg])
    thr.start()
    return thr