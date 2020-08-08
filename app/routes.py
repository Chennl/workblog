import os
import requests 
from flask import render_template, flash, redirect,url_for,request,current_app,jsonify,make_response
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime,timedelta
from werkzeug import secure_filename
import math
import imghdr


from app import db
from app.forms import LoginForm,RegistrationForm,EditProfileForm,EmptyForm,CourseForm,SongForm
from app.models import User, Post,Course,Schedule,Likes


@app.route('/user/@<username>')
@login_required
def user(username):
    user =User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    form = EmptyForm()
    return render_template('user.html', title='Profile', form=form, user=user,posts=posts)



@app.route('/explore/@<username>')
@login_required
def explore():
    pass



def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route('/upload_avatar',methods=['GET','POST'])
def upload_avatar():
    if request.method =='GET':
        return render_template('upload_avatar.html')
    if request.method == 'POST':
        files = request.files.getlist('avatar[]')
        for file in files:
            filename = secure_filename(file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in current_app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
                    abort(400)
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))









@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH']),filename)
            return redirect(url_for('upload_file'))
    return render_template('upload_file.html',title='File Upload')


