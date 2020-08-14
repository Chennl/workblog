from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class SongForm(FlaskForm):
    song_id = fields.StringField(DataRequired(message='歌曲ID不能为空'))
    song_name = fields.StringField(DataRequired(message='歌曲名称不能为空'))
    play_url=fields.StringField()
    submit = fields.SubmitField(u'下载')  

class EmailForm(FlaskForm):
    subject = StringField(DataRequired(message='主题不能为空'))
    sender = StringField()
    recipients = StringField(DataRequired(message='收件人不能为空'))
    text_body = StringField(DataRequired(message='邮件内容不能为空'))
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