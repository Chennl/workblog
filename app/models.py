from datetime import datetime ,timedelta
from time import time
import os
import json
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, url_for
from flask_login import UserMixin
from hashlib import md5
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import text,and_
import jwt

 
from app import db,login_manager

followers = db.Table(
    'followers',
    db.Column('follower_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer,db.ForeignKey('user.id'))
)

comments = db.Table(
    'comments',
    db.Column('post_id',db.Integer),
    db.Column('host_id',db.Integer)
)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    def __repr__(self):
        return '<Message {}>'.format(self.body)
 

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    password_plain = db.Column(db.String(32))
    gender = db.Column(db.String(4))
    about_me = db.Column(db.String(140))
    avatar_file = db.Column(db.String(100),default="default.jpg")
    last_seen = db.Column(db.DateTime, default=datetime.now)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    token = db.Column(db.String(256))
    token_expiration = db.Column(db.DateTime)
    

    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

    notifications = db.relationship('Notification', backref='user',lazy='dynamic')

    followed = db.relationship('User',
                secondary=followers,
                primaryjoin=(followers.c.follower_id==id),
                secondaryjoin=(followers.c.followed_id==id),
                backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
                
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def to_dict(self, include_email=False,include_link=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            'follower_count': self.followers.count(),
            'followed_count': self.followed.count()
        }
        if include_email:
            data['email'] = self.email
        if include_link:
            data['_links'] =  {
                'self': url_for('api.get_user', id=self.id),
                'followers': url_for('api.get_followers', id=self.id),
                'followed': url_for('api.get_followed', id=self.id),
                'avatar': self.avatar(128)
            }
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me','nickname']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.password_plain=password

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        #digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        #return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
        return  '/static/avatars/{}'.format(self.avatar_file)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.followed_id == self.id)
        #own = Post.query.filter_by(user_id=self.id)
        own = Post.query.filter(text('user_id=:user_id and host_id=0')).params(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())
    
    def generate_token(self,expires_in=3600):
        s=Serializer('w84nA58bLnoLHhhaMTJklu',expires_in) 
        return s.dumps({'id':self.id}).decode('utf-8')

    def get_token(self,expires_in=3600):
        now = datetime.now()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        #self.token = self.generate_token(expires_in)
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.now() - timedelta(seconds=1)
        db.session.commit()
        
    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.now():
            return None
        return user

    def get_reset_password_token(self,expires_in=600):
        print({'reset_password':self.id,'exp':time() + expires_in})
        return jwt.encode({'reset_password':self.id,'exp':time() + expires_in},current_app.config['SECRET_KEY'],algorithm='HS256').decode('utf-8')
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],algorithms=['HS256'])['reset_password']
        except Exception as e:
            print(e)
            return
        return User.query.get(id)

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        print(last_read_time)
        return Message.query.filter_by(recipient=self).filter(Message.timestamp > last_read_time).count()
    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5)) 
    host_id = db.Column(db.Integer,default=0)
    category = db.Column(db.String(50),default='') 
    def get_comments(self):
        #return  Post.query.join(comments,(comments.c.post_id==Post.id)).filter(comments.c.host_id==self.id).order_by(Post.timestamp.desc())
        return  Post.query.filter(Post.host_id==self.id).order_by(Post.timestamp.asc())
 
    def likes_count(self):
        return Likes.query.filter(Likes.post_id==self.id).count()

    def is_liking(self,user):
        filter = {
            and_(
                Likes.post_id==self.id,
                Likes.user_id==user.id,
            )}
        count = Likes.query.filter(*filter).count()
        return count>0

    def __repr__(self):
        return '<Post:("id":%s,"body":%s)>'%(self.id,self.body)

# class Comments(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     language = db.Column(db.String(5))
    
 
#     def __repr__(self):
#         return '<Comments:("id":%s,"body":%s)>'%(self.id,self.body)
        
class Likes(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    post_id=db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
    def to_dict(self):
        return  {'post_id':self.post_id,'user_id':user_id} 

    def __repr__(self):
        return '<like: (id=%s,post_id=%s,user_id=%s)'%(self.id,self.post_id,self.user_id)

class Schedule(db.Model):
    id = db.Column(db.INTEGER,autoincrement=True,primary_key=True)
    course_id = db.Column(db.INTEGER,db.ForeignKey('course.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(10), default='')
    def __repr__(self):
        return '<Schedule:%s>' % (self.start_time)

class Course(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    grade = db.Column(db.String(30), default='')
    name = db.Column(db.String(30), default='')
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    schedule= db.relationship('Schedule',backref='course', lazy='dynamic')
    comment = db.Column(db.String(100), default='')

    def __repr__(self):
        return '<Course:%s>'%(self.name)
    def to_dict(self):
        data = {
            'id':self.id,
            'name':self.name,
            'grade':self.grade,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'start_time':self.start_time,
            'end_time':self.end_time,
            'comment':self.comment
        }
        return data
    def from_dict(self,data):
        for field in ['id','name','grade','start_date','end_date','start_time','end_time']:
            if field in data:
                setattr(self,field,data[field])

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))
 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    fs_start = db.Column(db.DateTime)
    fs_end = db.Column(db.DateTime)
    qa_start = db.Column(db.DateTime)
    qa_end = db.Column(db.DateTime)
    uat_start = db.Column(db.DateTime)
    uat_end = db.Column(db.DateTime)
    sign_off = db.Column(db.DateTime)
    target_release = db.Column(db.DateTime)
    current_status = db.Column(db.String(32))
    current_comment = db.Column(db.String(256))
    updated_date = db.Column(db.DateTime)
    updated_by = db.Column(db.String(32))

class WechatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_user= db.Column(db.String(128))
    message_type = db.Column(db.String(32))
    message_body = db.Column(db.String(512))
    created_date = db.Column(db.DateTime, default=datetime.now)
# class WxAccessToken(db.Model):
#     access_token =  db.Column(db.String(512),primary_key=True)
#     open_id = db.Column(db.String(64))
#     expires_in = db.Column(db.INTEGER)
#     refresh_token = db.Column(db.DateTime)
#     scope = db.Column(db.String(32))
#     updated_date = db.Column(db.DateTime)

#     def __repr__(self):
#         return access_token

class MallGoods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(128))
    privilegePrice = db.Column(db.Numeric(10,2))
    price = db.Column(db.Numeric(10,2))
    imgUrl = db.Column(db.String(256))
    details = db.Column(db.String(512))
    remark= db.Column(db.String(128))
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)
    clickRate= db.Column(db.Integer)
    buyRate= db.Column(db.Integer)
    stock= db.Column(db.Integer)
    isHot= db.Column(db.Integer)
    isNew= db.Column(db.Integer)
    classifyId= db.Column(db.Integer)
    discount = db.Column(db.Numeric(10,2))
    activityId= db.Column(db.Integer)
    desc= db.Column(db.String(128))
    shopGoodsImageList= db.Column(db.String(512))
    def from_dict(self,data):
        pass





from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
import uuid

# Base model that for other models to inherit from
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
 
 

# Model for poll topics
class Topics(Base):
    __tablename__ = 'poll_topics'
    title = db.Column(db.String(500))
    status = db.Column(db.Boolean, default=True)  # to mark poll as open or closed
    create_uid = db.Column(db.ForeignKey('user.id'))
    close_date = db.Column(db.DateTime)
    created_by = db.relationship('User', foreign_keys=[create_uid],
                                 backref=db.backref('user_topics',lazy='dynamic'))
   

    # user friendly way to display the object
    def __repr__(self):
        return self.title

    # returns dictionary that can easily be jsonified
    def to_json(self):
        return {
                'title': self.title,
                'options': [{'name': option.option.name,
                            'vote_count': option.vote_count,
                            'uuid':option.uuid}
                            for option in self.options.all()],
                'close_date': self.close_date,
                'status': self.status,
                'total_vote_count': self.total_vote_count
            }

    @hybrid_property
    def total_vote_count(self, total=0):
        for option in self.options.all():
            total += option.vote_count
        return total

    @total_vote_count.expression
    def total_vote_count(cls):
        return select([func.sum(Polls.vote_count)]).where(Polls.topic_id == cls.id)



# Model for poll options
class Options(Base):
    __tablename__ = 'poll_options'
    name = db.Column(db.String(128), unique=True)
    def __repr__(self):
        return self.name

    def to_json(self):
        return {
                'id': uuid.uuid4(),  # Generates a random uuid
                'name': self.name
        }

# Polls model to connect topics and options together
class Polls(Base):
    def gen_uuid():
        return uuid.uuid4().hex
    __tablename__ = 'poll_polls'
    topic_id = db.Column(db.Integer, db.ForeignKey('poll_topics.id'))
    option_id = db.Column(db.Integer, db.ForeignKey('poll_options.id'))
    vote_count = db.Column(db.Integer, default=0)
    uuid = db.Column(db.String(32),default=gen_uuid,index=True, unique=True)

    topic = db.relationship('Topics', foreign_keys=[topic_id],backref=db.backref('options', lazy='dynamic'))
    option = db.relationship('Options', foreign_keys=[option_id],backref=db.backref('options', lazy='dynamic'))

    def __repr__(self):
        return self.option.name


class UserPolls(Base):
    __tablename__ = 'poll_userpolls'
    topic_id = db.Column(db.Integer, db.ForeignKey('poll_topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    option_id = db.Column(db.Integer,default=0)
    topics = db.relationship('Topics', foreign_keys=[topic_id],
                             backref=db.backref('voted_on_by', lazy='dynamic'))

    users = db.relationship('User', foreign_keys=[user_id],
                            backref=db.backref('voted_on', lazy='dynamic'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))