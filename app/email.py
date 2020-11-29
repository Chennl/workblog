from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()

from smtplib  import SMTP
from email.header import Header
from email.mime.text import MIMEText

def send_email_python(subject,sender, recipients, text_body):
    message = MIMEText(text_body,'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From']=sender
    message['To']=recipients
    smtpter = SMTP('smtp.126.com',25)
    smtpter.set_debuglevel(1)
    smtpter.login('chennlhz@126.com','chennl1975a')
    smtpter.sendmail(sender,recipients,message.as_string())
    #smtpter.sendmail(sender,recipients,message.as_string())
    smtpter.quit()
    print('邮件发送完成')