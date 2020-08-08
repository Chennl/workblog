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
class CourseForm(FlaskForm):
    course_name = fields.SelectField(
        label =u'科目',
        choices=(
            ('',u'请选择'),
            ('数学',u'数学'),
            ('科学',u'科学'),
            ('物理',u'物理'),
            ('化学',u'化学'),
        ),
        validators = [validators.DataRequired('科目不能为空')],
        render_kw={'class': 'form-control'}
        )
    grade = fields.SelectField(
        label=u'年级',
        choices=(
            ('',u'请选择'),
            (u'初一',u'初一'),
            (u'初二',u'初二'),
            (u'初三',u'初三'),
        ),
        #coerce=int,  #限制是int类型的
        render_kw={'class': 'form-control'}
    )
    start_date = StringField(
        label =u'开始日期',
        validators = [
        validators.DataRequired(message='日期不能为空')],
        render_kw={'class': 'form-control'}
        )
    end_date = StringField(
        label =u'结束日期',
        validators = [
        validators.DataRequired(message='日期不能为空')]
        )
    start_time = StringField(
        label =u'开始时间',
        validators = [
        validators.DataRequired(message='时间不能为空')]
        )
    end_time = StringField(
        label =u'结束时间',
        validators = [
        validators.DataRequired(message='时间不能为空')]
        )

    submit = SubmitField('添加')

