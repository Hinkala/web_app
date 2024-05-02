from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

from app import controller, model, utils, forms, repository

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return repository.get_credentials_by_id(user_id)
