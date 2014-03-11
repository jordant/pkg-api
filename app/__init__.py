from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.login import current_user, login_user, LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
      return render_template('404.html'), 404

# import controllers/models before create_all
import package.controllers
import package.models
import repository.controllers
import repository.models
import repository_package.models
import repository_package.controllers

# Create all the db tables
db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
