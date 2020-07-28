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

class RegistrationForm(FlaskForm):
    username = StringField(
        label =u'用户名',
        validators = [
        validators.DataRequired(message='用户名不能为空'),
        validators.length(min=4, max=16, message='用户名长度必须大于%(min)d且小于%(max)d')]
    )

    email = StringField(label='电子邮箱', 
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
         ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    password = PasswordField(
        label=u'密码',
        validators=[
        validators.DataRequired(message=u'密码不能为空'),
        validators.length(min=6, message=u'密码必须大于%(min)d位')
        ],
        widget=widgets.PasswordInput())

    password2 = PasswordField(
        label=u'重复密码',
        validators=[
            validators.DataRequired(message=u'重复密码不能为空.'),
            validators.EqualTo('password',message=u'两次密码不一致')
        ]
        )
   
    gender = fields.RadioField(
        label=u'性别',
        choices=(
            (1,u'男'),
            (0,u'女'),
        ),
        coerce=int,  #限制是int类型的
        render_kw={'class': 'form-control'}
    )

    submit = SubmitField(u'注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('该用户名已经被注册！')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('该邮箱已经被注册.')

class EditProfileForm(FlaskForm):
    username = StringField(
        label =u'用户名',
        validators = [
        validators.DataRequired(message='用户名不能为空'),
        validators.length(min=4, max=16, message='用户名长度必须大于%(min)d且小于%(max)d')]
        )
    avatar_file = fields.FileField(u'Avatar')
    about_me = fields.TextAreaField('关于我', validators=[validators.Length(min=0, max=140,message='自我介绍不能超过%(max)d')])
    submit = SubmitField('提交')


 
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