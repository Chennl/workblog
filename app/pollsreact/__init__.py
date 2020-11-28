from flask import render_template
from flask import Blueprint
from flask import url_for

bp = Blueprint('pollsreact', __name__, template_folder='templates', static_folder='static', static_url_path="/static/pollsreact")

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def index(path):
  return render_template('index.html')


