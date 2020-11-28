from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app,abort,send_from_directory
from app.main import bp

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return "<h1 style='color:blue'>Hello Blueprint!</h1>"

