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