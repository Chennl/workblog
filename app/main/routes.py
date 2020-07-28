from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app import db,app
from app.main.forms import EmptyForm,PostForm
from app.models import User, Post
from app.main import bp



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data,author=current_user,language='')
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