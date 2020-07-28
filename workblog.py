from app import app, db
from app.models import User, Post,Course,Schedule

import sched
import time

def job():
    print("I'm working...")
 


@app.shell_context_processor
def make_shell_context():
    s =sched.scheduler(time.time,time.sleep)
    print(time.time())
    s.enter(10, 1, job)
    return {'db': db, 'User': User, 'Post': Post,'Course':Course,'Schedule':Schedule}