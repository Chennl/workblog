from datetime import datetime ,timedelta
import time
import os
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 


from app import db,login_manager

followers = db.Table(
    'followers',
    db.Column('follower_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer,db.ForeignKey('user.id'))
)

comments = db.Table(
    'comments',
    db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
    db.Column('comment_id',db.Integer,db.ForeignKey('post.id'))
)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    password_plain = db.Column(db.String(32))
    gender = db.Column(db.String(4))
    about_me = db.Column(db.String(140))
    avatar_file = db.Column(db.String(100),default="default.jpg")
    last_seen = db.Column(db.DateTime, default=datetime.now)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    followed = db.relationship('User',
                secondary=followers,
                primaryjoin=(followers.c.follower_id==id),
                secondaryjoin=(followers.c.followed_id==id),
                backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
                
    def __repr__(self):
        return '<User {}>'.format(self.username)
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
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())
    
    def generate_token(self,expires_in=3600):
        s=Serializer('w84nA58bLnoLHhhaMTJklu',expires_in) 
        return s.dumps({'id':self.id}).decode('utf-8')

    def get_token(self,expires_in=3600):
        now = datetime.now()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        #self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token = self.generate_token(expires_in)
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.now() - timedelta(seconds=1)
        db.session.commit()
        
    @staticmethod
    def check_token(token):
        print(token)
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.now():
            return None
        return user

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))    
    thumb_up = db.Column(db.Integer, default=0)
    commented = db.relationship('Post',
            secondary=comments,
            primaryjoin=(comments.c.post_id==id),
            secondaryjoin=(comments.c.comment_id==id),
            backref=db.backref('comments', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.body)


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


 
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

