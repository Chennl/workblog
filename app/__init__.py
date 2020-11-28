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
    

