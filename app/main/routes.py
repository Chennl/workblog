from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.main.forms import EmptyForm,PostForm,EditProfileForm
from app.models import User, Post
from app.main import bp


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data,author=current_user,language='',host_id=form.host.data,category=form.category.data)
        db.session.add(post)
        db.session.commit()
        flash(u'微博发表成功!')
        return redirect(url_for('main.index'))
    
    page = request.args.get('page',1,type=int)
    pagination = current_user.followed_posts().paginate(page,current_app.config['POSTS_PER_PAGE'],False)

    next_url =url_for('main.index',page=pagination.next_num if pagination.has_next else None)
    prev_url =url_for('main.index',page=pagination.prev_num if pagination.has_prev else None)


    return render_template('index.html', title=u'首页', form=form,posts=pagination.items,pagination=pagination)
 
#https://fontawesome.com/icons?d=gallery&q=next&m=free  6
#https://fontawesome.com/v4.7.0/icons/ 4.7

@bp.route('/user/<username>')
@login_required
def user(username):
    user =User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    form = EmptyForm()
    return render_template('user.html', title='Profile', form=form, user=user,posts=posts)

@bp.route('/user/<username>/popup')
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)

@bp.route('/edit_profile',methods=['GET','POST'])
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

@bp.route('/follow/@<username>')
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

@bp.route('/unfollow/@<username>')
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
