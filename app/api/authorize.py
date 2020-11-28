
import traceback
import logging
import datetime
from flask import Flask,request,make_response,jsonify,abort
import jwt
from app import db
from app.models import User
from app.api import bp as api
from app.api.errors import bad_request,error_response

 
def token_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get('Authorization')
        _,token = header.split()
        try:
            decoded = jwt.decode(token,'SECRET_KEY',algorithms='HS256')
            username=decoded['name']
        except jwt.DecodeError:
            abort(400,message='Token is not valid.')
        except jwt.ExpiredSignatureError:
            abort(400,message='Token is expired.')
        return f(username,*args, **kwargs)
    return wrapper


SECRET_KEY = 'GodBlessMyFamily2020'
@api.route('/authorize',methods=['POST'])
def authorize():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return bad_request('需要用户名和密码!')
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
            return bad_request('用户名或密码错误。!')
    expires_in = int( datetime.datetime.utcnow().timestamp()) + 3600
    token = jwt.encode({'reset_password': username,'expire_in': expires_in}, SECRET_KEY, algorithm='HS256').decode('utf-8')
    response = {'expires_in':3600,'token':token}
    return make_response(jsonify(response),200)




 


