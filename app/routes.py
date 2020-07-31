import os
from flask import render_template, flash, redirect,url_for,request,current_app,jsonify,make_response
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime,timedelta
from werkzeug import secure_filename
import math
import imghdr


from app import app,db
from app.forms import LoginForm,RegistrationForm,EditProfileForm,EmptyForm,CourseForm
from app.models import User, Post,Course,Schedule,Likes



@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()


def get_next_page_or(default):
    next_page = request.args.get('next')
    if next_page and url_parse(next_page).netloc == '':
        return next_page
    return url_for(default)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
   
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码错误。')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        next_page = get_next_page_or('index')
        resp =make_response(redirect(next_page))
        resp.set_cookie('name',current_user.username)
        resp.set_cookie('token',current_user.get_token())
        return resp

    return render_template('login.html', title=u'登录', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,gender=form.gender.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你, 注册会员成功!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/@<username>')
@login_required
def user(username):
    user =User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    form = EmptyForm()
    return render_template('user.html', title='Profile', form=form, user=user,posts=posts)

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        file = request.files['avatar_file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.avatar_file = filename
        db.session.commit()

        flash('资料更新成功!')
        return redirect(url_for('edit_profile'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.avatar_file.data  = current_user.avatar_file
        return render_template('edit_profile.html', title='修改个人资料',form=form)


@app.route('/explore/@<username>')
@login_required
def explore():
    pass

@app.route('/follow/@<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} is not found.'.format(username))
        redirect(url_for('index'))
    if user == current_user:
        flash('You can not follow yourself.')
        return redirect(url_for('user',username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}.'.format(username))
    return redirect(url_for('user',username=username))

@app.route('/unfollow/@<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.', username=username)
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))


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





@app.route('/new_task',methods=['GET','POST','PUT'])
def new_task():
    form =CourseForm()
    if form.validate_on_submit():
        startTime = datetime.strptime(form.startTime.data,'%H:%M')
        endTime = datetime.strptime(form.endTime.data,'%H:%M')
        grade = form.grade.data
        name =form.name.data
        startDate =  datetime.strptime(form.startDate.data,'%Y-%m-%d') 
        endDate = datetime.strptime(form.startDate.data,'%Y-%m-%d')
        course = Course(grade=grade,name=name,start_date=startDate,end_date=endDate,start_time=startTime,end_time=endTime)
        db.session.add(course)
        db.session.commit()
        flash('恭喜你, 注册课程成功!')
        return redirect(url_for('task_schedule'))
    return render_template('new_task.html',form=form)

@app.route('/task_schedule',methods=['GET','POST','PUT'])
@login_required
def task_schedule():
    startTime =  datetime.strptime('2020-07-03', "%Y-%m-%d")
    form = CourseForm()
    return render_template('task_schedule.html',title='任务计划',form=form)



@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH']),filename)
            return redirect(url_for('upload_file'))
    return render_template('upload_file.html',title='File Upload')