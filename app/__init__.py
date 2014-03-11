from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
      return render_template('404.html'), 404

# import controllers/models before create_all
import package.controllers
import package.models

# Create all the db tables
db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
