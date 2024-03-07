from app import app,model
import pickle
from flask import render_template, url_for, redirect, request, flash

@app.route('/')
@app.route('/index')
def index_get():

    with open('cats.txt','rb') as f:
        cats = pickle.load(f)
    return render_template('index.html',cat_list = cats)

@app.route('/one')
def one_get():
    return render_template('one.html')

@app.route('/two', methods=['GET'])
def two_get():
    return render_template('two.html')

@app.route('/two', methods=['POST'])
def two_post():
    cats = []

    age = request.form.get('age')
    name = request.form.get('name')
    fur = request.form.get('fur')
    cats.append(model.Cat(1,name,fur,age,''))
    with open('cats.txt','wb') as f:
        pickle.dump(cats,f)



    return redirect('/two')
