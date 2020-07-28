from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,validators
from app.models import User
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
    
class PostForm(FlaskForm):
    post = TextAreaField(u'说点什么吧',  
        validators = [
            validators.DataRequired(message=u'内容不能为空'),
            validators.Length(max=140, message=u'留意长度不能大于%(max)d')]
        )
    submit = SubmitField(u'发表')  