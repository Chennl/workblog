<<<<<<< HEAD
from flask import Flask,request
from app import create_app


app = create_app()
#app = Flask(__name__)

@app.before_request
def before():
	print('Request.path: '+request.path)

@app.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    print('workblog start...')
    app.run()
=======
from app import create_app, db
from app.models import User, Post,Course,Schedule,Likes,comments,Polls,Options,Topics

import sched, time
 
app = create_app()
if __name__ == '__main__':
    app.run()
from flask import request
@app.before_request
def print_request_info():
    print("请求地址：" + str(request.path))
    # print("请求方法：" + str(request.method))
    # print("---请求headers--start--")
    # print(str(request.headers).rstrip())
    # print("---请求headers--end----")
    #print("GET参数：" + str(request.args))
    #print("POST参数：" + str(request.form))

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,'Polls': Polls,'Options':Options,'Topics':Topics}

@app.cli.command()
def scheduled():
    """Run scheduled job."""
    print('Importing feeds...')
    time.sleep(5)
    print('Users:', str(User.query.all()))
    print('Done!') 
>>>>>>> fc6ef113da6905feeb85d8d5b96d69ee319eb637
