from flask import jsonify,request,url_for,abort,Response
from app import db
from app.api import bp
from app.models import Course
from app.api.errors import bad_request,error_response
import time
import datetime
from app.api.auth import token_auth

@bp.route('/courses',methods=['GET'])
@token_auth.login_required
def get_courses():
    #courseName = request.args['name'] or ''
    #rows = Course.query.filter(Course.name.like('%{}%'.format(courseName)))
    rows = Course.query.all()
    data={'rows': [row.to_dict() for row in rows],'total':10}
    return jsonify(data)


@bp.route('/courses',methods=['POST','PUT'])
@token_auth.login_required
def create_course():
    data = request.get_json() or {}
    try:
        if 'name' not in data or 'id' not in data or 'oid' not in data:
            return bad_request('科目名称或编号不能为空!')
        else:
            data['name']=(data['name']).strip()
            data['id']=(data['id']).strip()
            if len(data['name'])==0:
                return bad_request('科目名称不能为空!')
            if len(data['id'])==0:
                return bad_request('班级编号不能为空!')
        if request.method == 'POST':
            if Course.query.filter_by(id=data['id']).first():
                return bad_request('该班级编号已经存在!')
            course = Course()
        elif request.method == 'PUT':
            course =Course.query.filter_by(id=data['oid']).first()
    
        course.name = data['name']
        course.id = data['id']
        course.grade = data['grade']
        timestamp = data['start_date']
        course.start_date =datetime.datetime.fromtimestamp(timestamp)
        timestamp = data['end_date']
        course.end_date =datetime.datetime.fromtimestamp(timestamp)
        course.start_time =datetime.datetime.fromtimestamp(data['start_time'])
        course.end_time =datetime.datetime.fromtimestamp( data['end_time'])
        course.comment = data['comment']

        if request.method == 'POST':
            db.session.add(course)
        db.session.commit()
        response = jsonify(course.to_dict())
        if request.method == 'POST':
            response.status_code = 201
        elif request.method == 'PUT':
            response.status_code = 202
        response.headers['Location'] = url_for('api.get_courses', id=course.id)
        return response
    except:
        return error_response(500)

 

@bp.route('/courses/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_course(id):
    course =Course.query.filter_by(id=id).first()
    db.session.delete(course)
    db.session.commit()
    response = jsonify(course.to_dict())
    response.status_code = 202
    return response