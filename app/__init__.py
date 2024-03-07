from flask import Flask
app = Flask(__name__)
from app import controller
app.config.from_object('config')
from app import model
