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
