from flask import render_template
from app import app,db

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
@app.errorhandler(500)
def not_found(error):
    db.session.rollback()
    return render_template('500.html')