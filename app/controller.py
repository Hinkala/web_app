from app import app
from flask import render_template


@app.route('/')
def index_get():
    return render_template('index.html',a1 = 'Hello',g1 = 'Hello')

@app.route('/one')
def one_get():
    return render_template('one.html')
