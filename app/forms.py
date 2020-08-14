from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
#https://www.cnblogs.com/haiyan123/p/8254228.html
class LoginForm(FlaskForm):
    username = StringField(
        label =u'用户名',
        validators = [
        validators.DataRequired(message='用户名不能为空'),
        validators.length(min=4, max=16, message='用户名长度必须大于%(min)d且小于%(max)d')]
        )
    password = PasswordField(
        label=u'Password',
        validators=[
        validators.DataRequired(message='密码不能为空'),
        validators.length(min=6, message='密码必须大于%(min)d位')
        ],
        widget=widgets.PasswordInput())
    remember_me = BooleanField(label=u'记住密码')
    submit = SubmitField('登录')




 
class EmptyForm(FlaskForm):
    submit = fields.SubmitField(u'提交')  

class FileUploadForm(FlaskForm):
    pass


