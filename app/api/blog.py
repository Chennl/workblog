from flask import jsonify,request,url_for,abort,Response
from flask_login import current_user, login_user,logout_user,login_required
import time,datetime
from app.api.auth import token_auth
from sqlalchemy import text
from app import db
from app.api import bp
from app.models import Likes
from app.api.errors import bad_request,error_response

@bp.route('/likes/<postid>',methods=['POST'])
def likes(postid):
    if request.method=='POST':
        like = Likes.query.filter(text("user_id=:uid and post_id=:pid")).params(uid=current_user.id, pid=postid).first()
        if like:
            db.session.delete(like)
            db.session.commit()
            return jsonify({'message':'已取消点赞!','user_id':current_user.id,'post_id':postid,'action':'dislike'})
        likes = Likes(user_id=current_user.id,post_id=postid)
        db.session.add(likes)
        db.session.commit()
        data = request.get_json() or {}
        print(data)
        return jsonify({'message':'点赞成功!','user_id':current_user.id,'post_id':postid,'action':'like'})
    else:
        return jsonify({'message':'~~'})
