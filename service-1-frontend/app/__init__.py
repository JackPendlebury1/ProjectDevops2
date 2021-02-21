from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='../templates')
app.config["SQLALCHEMY_DATABASE_URI"] =  getenv("DATABASE_URI")
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from app import routes