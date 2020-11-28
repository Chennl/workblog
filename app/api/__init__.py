from flask import Blueprint
bp = Blueprint('api',__name__)

from app.api import tokens,users,courses,blog,lbs,polls_api,authorize
