<<<<<<< HEAD
from flask import Flask
import os

def create_app():
    print('create app...')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    app = Flask(__name__)
    # app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
    # 将app交由blue管理
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    app.logger.info('Workblog startup...')
    return app
    

=======
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler,RotatingFileHandler
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
mail = Mail()
moment = Moment()


def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from app.errors import bp as err_bp
    app.register_blueprint(err_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api')

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.foo import bp as foo_bp
    app.register_blueprint(foo_bp, url_prefix='/foo')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    from app.polls import bp as polls_bp
    app.register_blueprint(polls_bp, url_prefix='/polls')

     
    #微信公众号接入蓝图
    from app.wx import bp as wx_bp
    app.register_blueprint(wx_bp,url_prefix='/wx')


    #微信小程序
    from app.wxmp import bp as mp_bp
    app.register_blueprint(mp_bp,url_prefix='/minimall')

    log_path = os.path.join(os.path.dirname(__file__),'logs')
    logname = os.path.join(log_path ,'out.log') #指定输出的日志文件名

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    print('You will find log file under path:',logname)
    # if app.config['LOG_TO_STDOUT'] :
    #     stream_handler = logging.StreamHandler()
    #     stream_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(stream_handler)
    # else:
    file_handler = RotatingFileHandler(logname, maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # if app.config['MAIL_SERVER']:
    #         auth = None
    #         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
    #             auth = (app.config['MAIL_USERNAME'],
    #                     app.config['MAIL_PASSWORD'])
    #         secure = None
    #         if app.config['MAIL_USE_TLS']:
    #             secure = ()
    #         mail_handler = SMTPHandler(
    #             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    #             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    #             toaddrs=app.config['ADMINS'], subject='Microblog Failure',
    #             credentials=auth, secure=secure)
    #         mail_handler.setLevel(logging.INFO)


    app.logger.setLevel(logging.INFO)
    app.logger.info('Workblog startup...')
    
    return app
""" if app.config['MAIL_SERVER']:
    auth = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject='Microblog Failure',
        credentials=auth, secure=secure)
    mail_handler.setLevel(logging.INFO)
    app.logger.addHandler(mail_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup') """


from app import   models,errors
>>>>>>> fc6ef113da6905feeb85d8d5b96d69ee319eb637
