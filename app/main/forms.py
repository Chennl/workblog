from flask import request
from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets,StringField, PasswordField, BooleanField, SubmitField,SelectField,TextAreaField
from app.models import User

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
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    #category=[{"code":"文摘"},{}]
    post = TextAreaField(u'我要发表新微博',  
        validators = [
            validators.DataRequired(message=u'内容不能为空'),
            validators.Length(max=140, message=u'留意长度不能大于%(max)d')],
        render_kw={'placeholder': '写一些自己的心情或者自己遇到的一些事情...'}
        )
    host=StringField()
    category = SelectField(u'Programming Language', choices=[(u'文摘', u'文摘'), (u'感想', u'感想'), (u'琐事', u'琐事'), (u'其他', u'其他')])
    submit = SubmitField(u'发表微博', render_kw={'class':'btn btn-warning'})  