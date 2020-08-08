from flask import Blueprint

bp = Blueprint('foo', __name__)

from app.foo import routes
