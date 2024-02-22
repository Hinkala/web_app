from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index_get():
    return render_template('index.html')

@app.route('/one')
def one_get():
    return render_template('one.html')

@app.route('/two')
def two_get():
    return render_template('two.html')
