from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class SongForm(FlaskForm):
    song_id = fields.StringField(DataRequired(message='歌曲ID不能为空'))
    song_name = fields.StringField(DataRequired(message='歌曲名称不能为空'))
    play_url=fields.StringField()
    submit = fields.SubmitField(u'下载')  