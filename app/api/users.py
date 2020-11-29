from flask import jsonify, request, url_for, abort
from app import db
from app.models import User
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request,error_response
import traceback
import logging
from flask_login import login_user, logout_user


 
@bp.route('/users/login',methods=['POST'])
def login():
    try:
        data = request.get_json() or {}
        if 'username' not in data or 'password' not in data:
            return bad_request('请输入用户名和密码!')
        user = User.query.filter_by(username=data['username']).first()
        if user is None or not user.check_password(data['password']):
            return bad_request('用户名或密码错误。!')
        login_user(user)
        payload = {'status': 'success','message':'恭喜你，登录成功!'}
        payload['user'] = user.to_dict()
        payload['token'] = user.get_token()
        response = jsonify(payload)
        response.state_code =200
        return response
    except Exception as e:
        print(e)
        logging.debug(traceback.format_exc())
        abort(500)

@bp.route('/users/logout')
def logout():
    logout_user()
    payload = {'status': 'success','message':'登出成功!'}
    response = jsonify(payload)
    response.state_code =200
    return response

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/users',methods=['POST'])
def create_user():
    try:
        data = request.get_json() or {}
        
        if 'username' not in data or 'password' not in data or 'email' not in data:
            return bad_request('用户注册必须包含用户名，密码以及邮箱信息！')
        if User.query.filter_by(username = data['username']).first():
            return bad_request('请使用其它用户名注册！')
        if User.query.filter_by(email = data['email']).first():
            return bad_request('请使用其它邮箱注册！')

        if 'nickname' not in data:
            data['nickname'] = data['username']

        user = User()
        user.from_dict(data,new_user=True)
        db.session.add(user)
        db.session.commit()

        payload = {'status': 'success','message':'恭喜你，用户注册成功'}
        payload['user'] = user.to_dict()
        response = jsonify(payload)
        response.state_code =201
        return response
    except Exception as e:
        print(e)
        logging.debug(traceback.format_exc())
        payload = {'status': 'error','message':'服务器内部错误!'}
        response = jsonify(payload)
        response.state_code =500
        abort(response)