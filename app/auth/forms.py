from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
 

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
    remember_me = BooleanField(label=u'记住我')
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


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Request Password Reset')
