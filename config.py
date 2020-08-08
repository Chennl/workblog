import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'workblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #upload files
    UPLOAD_FOLDER='app\\static\\avatars'
    SONG_FOLDER='app\\static\\media\\song'
    #照片上传设置
    MAX_CONTENT_LENGTH   = 1024 * 1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']

    # emiail
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'outlook.office365.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 993)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'chennl@live.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'live1975'
    ADMINS = ['chennl@live.com']

    #日志输出
    LOG_TO_STDOUT = True

    POSTS_PER_PAGE = 10



