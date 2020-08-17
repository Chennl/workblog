import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'workblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #upload files
    UPLOAD_FOLDER='app\\static\\avatars'
    SONG_FOLDER=os.path.join(basedir,'app\\static\\media\\song')
    #照片上传设置
    AVATAR_UPLOAD_FOLDER=os.path.join(basedir,'app\\static\\avatars')
    MAX_CONTENT_LENGTH   = 1024 * 1024
    AVATAR_FILE_EXTENSIONS = ['.jpg', '.png', '.gif']
    #相册
    MAX_PHOTO_LENGTH   = 1024 * 1024
    PHOTO_FILE_EXTENSIONS = ['.jpg', '.png', '.gif']
    PHOTO_UPLOAD_FOLDER = os.path.join(basedir,'app\\album')

    # emiail
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.126.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'chennlhz@126.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'chennl1975a'
    
    ADMINS = ['chennlhz@126.com']


    #日志输出
    LOG_TO_STDOUT = True

    POSTS_PER_PAGE = 10


    #SESSION_COOKIE_SECURE = True
    #REMEMBER_COOKIE_SECURE = True
