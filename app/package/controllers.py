from app import db
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from app.package.models import Package

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Package, methods=['GET', 'POST', 'DELETE'], results_per_page=-1)
