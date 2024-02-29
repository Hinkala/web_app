from app import app,model
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index_get():
    cats = []
    cats.append(model.Cat(1, 'Naf', 'Red', 2, 'cat1.png'))
    cats.append(model.Cat(2, 'Bars', 'White', 6, 'cat2.png'))
    cats.append(model.Cat(3, 'Simba', 'Gold', 4, 'cat3.png'))
    cats.append(model.Cat(4, 'Mars', 'Black', 3, 'cat4.png'))
    return render_template('index.html',cat_list = cats)

@app.route('/one')
def one_get():
    return render_template('one.html')

@app.route('/two')
def two_get():
    return render_template('two.html')
