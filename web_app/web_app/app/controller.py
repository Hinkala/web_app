from app import app, model, utils, forms, repository
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, current_user
import pickle
import uuid
import os

@app.route('/login')
def login_get():
    form = forms.LoginForm()
    return render_template('login.html', form = form)


@app.route('/login', methods=['POST'])
def login_post():
    form = forms.LoginForm()
    if form.validate_on_submit():
        login = form.loginField.data
        password = form.passwordField.data
        user = repository.authorize_user(login, password)
        if user != None:
            login_user(user)
            return redirect('two')
        else:
            flash('Неправильный лог.пар')
            return redirect('/login')
    else:
        return redirect('/login')

@app.route('/')
@app.route('/index')
def index_get():
    cats = []
    with open("cats", 'rb') as f:
        cats = pickle.load(f)
    return render_template('index.html', a1 = "HELLO FROM A1", cat_list = cats)


@app.route('/one')
def one_get():
    return render_template('one.html')

@app.route('/registration')
def registration_get():
    form = forms.RegistrationForm()
    return render_template('registration.html', form = form)


@app.route("/registration", methods=['POST'])
def registration_post():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        if repository.check_login(form.loginField.data):
            credential = model.Credentials(None, form.loginField.data, form.passwordField.data, None)
            repository.create_credentials(credential)
            return render_template("one.html")
        else:
            flash("Пользователь с таким логином уже существует")
            return redirect('/registration')
    return redirect('/registration')


@app.route('/two', methods=['GET'])
def two_get():
    form = forms.catForm()
    print("atTWO")
    return render_template('two.html', form = form)


@app.route("/two", methods=['POST'])
def two_post():
    cats = []
    with open("cats", 'rb') as f:
        cats = pickle.load(f)
    form = forms.catForm()
    cat = form.nameField.data
    cats.append(model.Cat(utils.generate_unique_id(cats), cat, cat, cat, ""))
    with open("cats", 'wb') as f:
        pickle.dump(cats, f)
    return redirect('/two')


@app.route("/delete-cat/<int:cat_id>", methods=['GET'])
def cat_delete(cat_id):
    cats = []
    with open("cats", 'rb') as f:
        cats = pickle.load(f)
    utils.cat_delete(cats, cat_id)
    with open("cats", 'wb') as f:
        pickle.dump(cats, f)
    return index_get()

@app.route("/cat-pic-upload", methods=['POST'])
def cat_pic_upload():
    if 'cat-pic' in request.files:
        file = request.files['cat-pic']
        if file:
            unique_fn = str(uuid.uuid4())
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_fn))
            with open("cats", 'rb') as f:
                cats = pickle.load(f)
            cat_id = request.args['cat_id']
            flash(cat_id)
            for i in cats:
                flash(i.cat_id)
            utils.add_pic(cats, int(cat_id), unique_fn)

            with open("cats", 'wb') as f:
                pickle.dump(cats, f)
    return index_get()


