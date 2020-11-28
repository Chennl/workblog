
from flask import request,session
import os,time
from flask import render_template, flash, redirect,url_for,request,current_app
from datetime import datetime
from app.models import User
from app import db

from flask import Blueprint

#bp = Blueprint('polls', __name__,template_folder='templates', static_folder=None, static_url_path="/static/backend/build/")
bp = Blueprint('polls', __name__)
@bp.route('/')
def home():
    #return render_template('polls/index.html')
    return render_template('polls/index.html')
 