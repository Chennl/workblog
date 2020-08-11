
from app.foo import bp
from flask import request
import os,time
import requests 
from flask import render_template, flash, redirect,url_for,request,current_app
from flask_login import login_required
from app.foo.forms import SongForm,EmailForm

from app.email import send_email_python,send_email
from app import mail


from flask_mail import Mail, Message


@bp.route('/song/download', methods=['GET','POST'])
def download_song():

 
    clientip=request.remote_addr
    print(clientip)
    form = SongForm()
    song_base_path=current_app.config['SONG_FOLDER']
    print(song_base_path)
    #begin Study 获取当前目录绝对路径
    dir_path = os.path.dirname(os.path.abspath(__file__))
    print('当前目录绝对路径:',dir_path)
    print('当前flask current_app.root_path目录绝对路径:',current_app.root_path)
    print('当前flask instance_path目录绝对路径:',current_app.instance_path)
    #end Study
    filelist=[]
    files = os.listdir(song_base_path)
    for file in files:
        if not os.path.isdir(file):
            filepath=os.path.join(song_base_path,file)
            filesize = os.path.getsize(filepath)
            filesize = filesize/float(1024*1024*1.0000)
            filesize = round(filesize,2)
            filelist.append({'name':file,'size':'%s MB'%(filesize)})
    if request.method == 'POST':
        song_id=request.form['song_id']
        song_name = request.form['song_name']
        song_file_name =  os.path.join(song_base_path,'%s.mp3'%(song_name))
        song_url='http://music.163.com/song/media/outer/url?id=%s'%(song_id)
        print(song_url)
        try:
            req_music = requests.get(song_url, timeout = 5000)
            with open( song_file_name,'wb' ) as f:
                f.write ( req_music.content )
            flash('音乐下载成功!')
            form.play_url.data=song_file_name
        except Exception as e:
            flash('音乐下载失败!')
            print(e)
        return redirect(url_for('download_song'))
    return render_template('download_song.html',form=form,files=filelist,clientip=clientip)

@bp.route('/email', methods=['GET','POST'])
def html_email():
    form = EmailForm()
    if form.validate_on_submit():
        subject = form.subject.data
        recipients = form.recipients.data.split(';')
        text_body =form.text_body.data
        html_body ='<h1>HTML body</h1>'
        #recipients = ['chennlhz@126.com']
        msg = Message(subject, sender = current_app.config['MAIL_USERNAME'], recipients = recipients)
        msg.body =  text_body
        mail.send(msg)
        #send_email(subject,sender,recipients)
        flash('邮件发送成功!')
        return redirect(url_for('foo.html_email'))
    return render_template('html_email.html',form=form)

@bp.route('/new_task',methods=['GET','POST','PUT'])
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

@bp.route('/task_schedule',methods=['GET','POST','PUT'])
@login_required
def task_schedule():
    startTime =  datetime.strptime('2020-07-03', "%Y-%m-%d")
    form = CourseForm()
    return render_template('task_schedule.html',title='任务计划',form=form)