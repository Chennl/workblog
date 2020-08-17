from app import create_app, db
from app.models import User, Post,Course,Schedule,Likes,comments

import sched, time
 
app = create_app()
if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    s =sched.scheduler(time.time,time.sleep)
    print(time.time())
    s.enter(10, 1, job)
    return {'db': db, 'User': User, 'Post': Post,'Course':Course,'Schedule':Schedule,'Likes':Likes,'comments':comments}

@app.cli.command()
def scheduled():
    """Run scheduled job."""
    print('Importing feeds...')
    time.sleep(5)
    print('Users:', str(User.query.all()))
    print('Done!') 