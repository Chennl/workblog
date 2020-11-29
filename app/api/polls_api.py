
from app.api import bp as api
from app.api.errors import error_response,bad_request
from app import db
from flask import jsonify,request
import  uuid
from app.models import Options ,Polls,Topics,User,UserPolls
from datetime import datetime
import traceback
import logging 

def msg(success,status,message,extra = []):
    return {'success':success,'status' :status,'message' :message,'extra':extra}


@api.route('/polls', methods=['GET', 'POST'])
# retrieves/adds polls from/to the database
def api_polls():
    if request.method == 'POST':
        # get the poll and save it in the database
        poll = request.get_json()

        # simple validation to check if all values are properly set
        for key, value in poll.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)})

        title = poll['title']

        user_id =poll['user_id'] if 'user_id' in poll.items() else 1
       
        topic = Topics.query.filter_by(title=title).first()
        if topic:
            return bad_request('Sorry! The topic title is already in use, please try another!')
         
        options_query = lambda option: Options.query.filter(Options.name.like(option))

        options = [Polls(option=Options(name=option)) 
                   if options_query(option).count() == 0
                   else Polls(option=options_query(option).first()) for option in poll['options']
                   ]
        close_date = datetime.utcfromtimestamp(poll['close_date'])
        new_topic = Topics(title=title, options=options, close_date=close_date,create_uid=user_id)
        new_topic.options =  options
        db.session.add(new_topic)
        db.session.commit()
        
        # # run the task
        # from tasks import close_poll

        # close_poll.apply_async((new_topic.id, SQLALCHEMY_DATABASE_URI), eta=eta)

        return jsonify({'message': 'Poll was created succesfully'})

    else:
        # it's a GET request, return dict representations of the API
        #polls = Topics.query.filter_by(status=True).join(Polls).order_by(Topics.id.desc()).all()
        #polls = Topics.query.filter_by(status=True).order_by(Topics.id.desc()).all()

        polls = Topics.query.filter_by(status=True).join(Polls).order_by(Topics.id.desc()).all()
        all_polls = {'Polls':  [poll.to_json() for poll in polls]}
        return jsonify(all_polls)


@api.route('/polls/options',methods=['GET','POST'])
def api_polls_options():
   all_options = [option.to_json() for option in Options.query.all()]
   return jsonify(all_options)
 
@api.route('/polls/<poll_name>')
def api_poll(poll_name):
    #poll = Topics.query.first()
    poll = Topics.query.filter(Topics.title.ilike('%'+poll_name+'%')).first()
    return jsonify({'Polls': [poll.to_json()]}) if poll else jsonify({'message': 'poll not found'})


@api.route('/poll/vote', methods=['PATCH'])
def api_poll_vote():
    try:
            poll = request.get_json()

            poll_title, option,username = (poll['poll_title'], poll['option'],poll['username'])
            
            # Get topic and username from the database
            topic = Topics.query.filter_by(title=poll_title, status=True).first()
            user = User.query.filter_by(username=username).first()
            
            # if poll was closed in the background before user voted
            if not topic:
                #return jsonify({'message': 'Sorry! this poll has been closed'})
                return bad_request('Sorry! this poll has been closed')

            # filter options
            #join_tables = Polls.query.join(Topics).join(Options)
            #qy = join_tables.filter(Topics.title.like(poll_title), Topics.status == True).filter(Options.name.like(option))
       
            option= Polls.query.filter_by(uuid=option).first()
            # check if the user has voted on this poll
            poll_count = UserPolls.query.filter_by(topic_id=topic.id).filter_by(user_id=user.id).count()
            if poll_count > 0:
                #return jsonify({'message': 'Sorry! multiple votes are not allowed'})
                return bad_request('Sorry! multiple votes are not allowed')

            if option:
                # record user and poll
                user_poll = UserPolls(topic_id=topic.id, user_id=user.id,option_id=option.id)
                db.session.add(user_poll)

                # increment vote_count by 1 if the option was found
                option.vote_count += 1
                db.session.commit()

                return jsonify({'message': 'Thank you for voting'})

            return bad_request('option or poll was not found please try again')
            #return jsonify({'message': 'option or poll was not found please try again'})
    except Exception as e:
        print(e)
        logging.debug(traceback.format_exc())
        return error_response(500,' Interal error whiling processing a vote')


